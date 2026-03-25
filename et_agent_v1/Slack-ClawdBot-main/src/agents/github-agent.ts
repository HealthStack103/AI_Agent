import { processMessage } from './agent';
import { AgentContext } from './agent';

export async function githubAgent(
  message: string,
  context: AgentContext
) {
  return processMessage(message, context, {
    name: "GitHub Agent",
    description: `
You ONLY handle GitHub-related tasks.

STRICT RULES:
- Always use github_* tools
- Never answer from memory
- If GitHub info needed → MUST call tool
`,
  });
}