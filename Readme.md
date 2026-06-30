# ET Gen AI Hackathon 2026 – Autonomous Workflow Agent

> **Team: HealthStack103**
> Building an **Agentic AI System for Autonomous Enterprise Workflows** that executes multi-step tasks, self-heals failures, and maintains full auditability.

---

## Team Details

* **Yakshith K D** – Team Lead & ML Developer
* **Nithesh** – Embedded AI Developer
* **Sagar K** – Flutter Developer

---

## Problem Statement

### Agentic AI for Autonomous Enterprise Workflows

Design a **multi-agent system** that:

* Owns complex enterprise workflows end-to-end
* Detects failures and self-recovers
* Minimizes human intervention
* Maintains auditable decision trails

---

## Project Overview

This project evolves a **Slack-based AI assistant** into a **fully autonomous workflow orchestration system**.

Instead of just responding to messages, the system:

* Executes multi-step enterprise workflows
* Coordinates multiple specialized AI agents
* Detects failures and self-recovers automatically
* Logs every decision for auditability

---

## Use Case (Demo Workflow)

### Example: Meeting → Task → Execution Pipeline

1. User shares meeting discussion in Slack
2. AI extracts:

   * Key decisions
   * Tasks
   * Responsible owners
3. Automatically assigns tasks
4. Tracks progress continuously
5. Detects delays or inactivity
6. Escalates or reassigns tasks

All without manual follow-up.

---

## Core Idea: Multi-Agent System

```
User → Orchestrator Agent → Specialized Agents → Execution → Monitoring → Self-Healing
```

---

## Key Features

### 1. Multi-Agent Orchestration

* Central **Orchestrator Agent** manages workflows
* Specialized agents:

  * Task Extraction Agent
  * Decision Agent
  * Execution Agent
  * Monitoring Agent
  * Audit Agent

---

### 2. Autonomous Workflow Execution

* End-to-end task lifecycle management
* Minimal human input required
* Automatic task assignment and tracking

---

### 3. Self-Healing System

System detects:

* Delays
* Failures
* Missing actions

Automatically performs:

* Retries
* Reassignments
* Escalations

---

### 4. Audit Trail (Hackathon Key Requirement)

Every step is logged in a structured format:

```
[Time] → Agent → Action → Reason → Outcome
```

#### Example:

```
10:02 → Task Agent → Created task → Based on meeting notes
10:10 → Monitor → Delay detected → No update from owner
10:11 → Orchestrator → Reassigned → Backup user assigned
```

---

### 5. Tool Integration (via MCP)

* GitHub → Issues, PRs
* Notion → Docs, databases
* Slack → Communication

---

### 6. RAG + Memory System

* Retrieves past Slack conversations (RAG)
* Stores long-term user preferences (mem0)
* Uses context to make smarter decisions

---

## Architecture

### High-Level Architecture

```
┌──────────────┐
│   USER       │
└──────┬───────┘
       ▼
┌──────────────┐
│ Slack Layer  │
└──────┬───────┘
       ▼
┌────────────────────────────┐
│  ORCHESTRATOR AGENT        │
└──────┬────────────┬────────┘
       ▼            ▼
┌────────────┐  ┌────────────┐
│ Task Agent │  │ Decision   │
└────────────┘  └────────────┘
       ▼            ▼
┌────────────┐  ┌────────────┐
│ Execution  │  │ Monitoring │
└────────────┘  └────────────┘
       ▼            ▼
     Tools       Audit Logs
```

---

## Workflow Lifecycle

1. Input received (Slack / API)
2. Context built using RAG + Memory
3. Orchestrator decides workflow plan
4. Specialized agents execute tasks
5. Monitoring agent tracks progress
6. Errors handled automatically
7. Audit logs stored

---

## Impact Model

### Time Savings

| Task            | Manual | AI System |
| --------------- | ------ | --------- |
| Task extraction | 30 min | 2 min     |
| Assignment      | 10 min | Instant   |
| Follow-ups      | Daily  | Automated |

Approximately **70% reduction in workflow time**.

---

### Cost Reduction

Assumption:

* Manager hourly cost: ₹1000
* 2 hours saved per day

```
Savings = ₹1000 × 2 × 22 days = ₹44,000/month per team
```

---

### Efficiency Gains

* No missed tasks
* Faster execution
* Real-time monitoring
* Automatic recovery

---

## Example Scenario

### User Input:

```
"We need to fix login bug, update docs, and deploy by Friday"
```

### AI System Output:

* Creates structured tasks
* Assigns owners automatically
* Tracks deadlines
* Sends reminders
* Escalates if delayed

---

## Tech Stack

* LLM: GPT-4o
* Backend: Node.js
* Slack API: Bolt.js
* RAG: ChromaDB
* Memory: mem0
* Tool Integration: MCP (GitHub + Notion)

---

## Installation

```bash
git clone https://github.com/your-repo
cd project
npm install
npm run dev
```

---

## Project Structure

```
src/
├── agents/          # Multi-agent logic
├── orchestrator/    # Workflow controller
├── rag/             # Context retrieval
├── memory/          # Long-term memory
├── mcp/             # Tool integrations
├── slack/           # Slack interface
```

---

## Demo

3-minute walkthrough should include:

* Input to workflow execution
* Agent coordination
* Automatic error recovery
* Audit logging

---

## Submission Checklist

* GitHub Repository
* README
* Pitch Video
* Architecture Diagram
* Impact Model

---

## Future Improvements

* Add enterprise workflows (HR, Finance, Operations)
* Predictive failure detection
* Improved agent collaboration logic
* Workflow visualization dashboard

---

## Conclusion

This project transforms a chatbot into an autonomous enterprise worker:

* From reactive to proactive systems
* From single-agent to multi-agent architecture
* From manual workflows to autonomous execution

