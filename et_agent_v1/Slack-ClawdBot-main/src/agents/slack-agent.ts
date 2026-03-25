import { processMessage } from './agent';
import { AgentContext } from './agent';

export async function slackAgent(
  message: string,
  context: AgentContext
) {
  return processMessage(message, context, {
    name: "Slack Agent",
    description: `
You handle:
- Slack messaging
- RAG history
- reminders
- scheduling
`,
  });
}