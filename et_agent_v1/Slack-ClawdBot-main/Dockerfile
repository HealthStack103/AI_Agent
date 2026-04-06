# ---------------------------
# Stage 1: Build Stage
# ---------------------------
FROM node:22-alpine AS builder

WORKDIR /app

# Copy package files
COPY package*.json ./
COPY tsconfig.json ./

# Install dependencies (including devDependencies for building)
# NOTE:
# - Use `npm ci` in production when package-lock.json exists
# - Use `npm install` for development/testing
RUN npm install

# Copy source code
COPY src ./src

# Build TypeScript → outputs to /app/dist
RUN npm run build


# ---------------------------
# Stage 2: Production Stage
# ---------------------------
FROM node:22-alpine AS production

WORKDIR /app

# Install dumb-init for proper signal handling (recommended for containers)
RUN apk add --no-cache dumb-init

# Create non-root user for security
RUN addgroup -g 1001 -S nodejs && \
    adduser -S assistant -u 1001

# Copy package files
COPY package*.json ./

# Install ONLY production dependencies
RUN npm install --omit=dev && npm cache clean --force

# Copy built files from builder stage
COPY --from=builder /app/dist ./dist

# Create data and logs directories
RUN mkdir -p /app/data /app/logs && \
    chown -R assistant:nodejs /app

# Switch to non-root user
USER assistant

# Environment variables
ENV NODE_ENV=production
ENV DATABASE_PATH=/app/data/assistant.db
ENV LOG_LEVEL=info

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD node -e "console.log('healthy')" || exit 1

# Use dumb-init to handle signals properly
ENTRYPOINT ["dumb-init", "--"]

# Start the application
CMD ["node", "dist/index.js"]