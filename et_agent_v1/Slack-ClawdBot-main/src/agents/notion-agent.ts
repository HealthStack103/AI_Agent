import { processMessage } from './agent';
import { AgentContext } from './agent';

export async function notionAgent(
  message: string,
  context: AgentContext
) {
  return processMessage(message, context, {
    name: "Notion Agent",
    description: `
You ONLY handle Notion-related tasks.

STRICT RULES:
- Always use notion_* tools
- Search pages, docs, workspace
`,
  });
}