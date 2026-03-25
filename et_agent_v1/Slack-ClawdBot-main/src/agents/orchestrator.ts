// these one for multiple agent
import OpenAI from 'openai';
import { config } from '../config/index.js';
import { AgentContext, AgentResponse } from './agent';

import { githubAgent } from './github-agent';
import { notionAgent } from './notion-agent';
import { slackAgent } from './slack-agent';

const openaiClient = new OpenAI({ apiKey: config.ai.openaiApiKey });

/**
 * Decide which agent should handle the request
 */
async function decideAgent(message: string): Promise<string> {
  try {
    const response = await openaiClient.chat.completions.create({
      model: 'gpt-4o',
      messages: [
        {
          role: 'system',
          content: `
You are an AI router.

Decide which agent should handle the user request.

Available agents:
- github → repos, PRs, issues, code
- notion → docs, pages, notes
- slack → messages, reminders, scheduling, general

Reply ONLY with one word:
github / notion / slack
          `,
        },
        { role: 'user', content: message },
      ],
      max_tokens: 10,
    });

    return response.choices[0]?.message?.content?.trim().toLowerCase() || 'slack';
  } catch (err) {
    return 'slack'; // fallback
  }
}

/**
 * Main orchestrator function
 */
export async function orchestrate(
  message: string,
  context: AgentContext
): Promise<AgentResponse> {
  const agentType = await decideAgent(message);

  switch (agentType) {
    case 'github':
      return githubAgent(message, context);

    case 'notion':
      return notionAgent(message, context);

    default:
      return slackAgent(message, context);
  }
}