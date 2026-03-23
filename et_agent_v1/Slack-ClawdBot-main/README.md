
#  ET Gen AI Hackathon 2026 – Autonomous Workflow Agent

>  **Team: HealthStack103**
> Building an **Agentic AI System for Autonomous Enterprise Workflows** that can execute multi-step tasks, self-correct errors, and maintain a full audit trail.

---

## 👥 Team Details

* **Yakshith K D** - Team  Lead  and ML developer
* **Nithesh**      - Embedded Ai developer
* **Sagar K**      - Flutter Developer

---

##  Problem Statement

### **Agentic AI for Autonomous Enterprise Workflows**

Design a **multi-agent system** that:

* Owns complex enterprise workflows end-to-end
* Detects failures and self-recovers
* Minimizes human intervention
* Maintains **auditable decision trails**

---

##  Project Overview

This project extends a **Slack-based AI Assistant** into a **fully autonomous workflow orchestration system**.

Instead of just responding to queries, the system:

-  Executes multi-step enterprise workflows
-  Coordinates multiple specialized AI agents
-  Detects failures and self-corrects
-  Logs every decision for auditability

---

##  Use Case (Demo Workflow)

###  Example: Meeting → Task → Execution Pipeline

1. User shares meeting discussion in Slack
2. AI extracts:

   * Decisions
   * Tasks
   * Owners
3. Assigns tasks automatically
4. Tracks progress
5. Detects delays
6. Escalates or reassigns

👉 All without manual follow-up

---

## 🧠 Core Idea: Multi-Agent System

```
User → Orchestrator Agent → Specialized Agents → Execution → Monitoring → Self-Healing
```

---

## ⚙️ Key Features

### 🤖 1. Multi-Agent Orchestration

* Orchestrator agent manages full workflow
* Specialized agents:

  * Task Extraction Agent
  * Decision Agent
  * Execution Agent
  * Monitoring Agent
  * Audit Agent

---

### 🔄 2. Autonomous Workflow Execution

* End-to-end task handling
* Minimal human input required
* Automatic task assignment & tracking

---

### 🛠 3. Self-Healing System

* Detects:

  * Delays
  * Failures
  * Missing actions
* Automatically:

  * Retries
  * Reassigns
  * Escalates

---

###  4. Audit Trail (Hackathon Key Requirement)

Every step is logged:

```
[Time] → Agent → Action → Reason → Outcome
```

Example:

```
10:02 → Task Agent → Created task → Based on meeting notes
10:10 → Monitor → Delay detected → No update from owner
10:11 → Orchestrator → Reassigned → Backup user assigned
```

---

### 5. Tool Integration (via MCP)

* GitHub → Issues, PRs
* Notion → Docs, tasks
* Slack → Communication

---

###  6. RAG + Memory System

* Retrieves past conversations
* Remembers user preferences
* Uses context for smarter decisions

---

## 🏗 Architecture

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

##  Workflow Lifecycle

1. Input received (Slack / API)
2. Context built (RAG + Memory)
3. Orchestrator decides workflow
4. Agents execute tasks
5. Monitor tracks progress
6. Errors handled automatically
7. Audit logs stored

---

##  Impact Model (IMPORTANT FOR HACKATHON)

### ⏱ Time Savings

| Task            | Manual | AI System |
| --------------- | ------ | --------- |
| Task extraction | 30 min | 2 min     |
| Assignment      | 10 min | Instant   |
| Follow-ups      | Daily  | Automated |

 **~70% reduction in workflow time**

---

###  Cost Reduction

Assumption:

* Manager hourly cost: ₹1000
* 2 hrs saved/day

```
Savings = ₹1000 × 2 × 22 days = ₹44,000/month per team
```

---

###  Efficiency Gains

* 0 missed tasks
* Faster execution
* Real-time monitoring

---

##  Example Scenario

**User Input:**

```
"We need to fix login bug, update docs, and deploy by Friday"
```

**AI System Output:**

* Creates 3 tasks
* Assigns owners
* Tracks deadlines
* Sends reminders
* Escalates if delayed

---

##  Tech Stack

* **LLM:** GPT-4o
* **Backend:** Node.js
* **Slack API:** Bolt.js
* **RAG:** ChromaDB
* **Memory:** mem0
* **Tool Integration:** MCP (GitHub + Notion)

---

##  Installation

```bash
git clone https://github.com/your-repo
cd project
npm install
npm run dev
```

---

##  Project Structure

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

##  Demo (To be added)

 3-minute walkthrough showing:

* Input → Workflow execution
* Agent coordination
* Auto error recovery

---

##  Submission Checklist

-  GitHub Repo
-  README (this file)
-  Pitch Video
-  Architecture Diagram
- Impact Model (included above)

---

##  Future Improvements

* Add real enterprise workflows (HR, Finance)
* Add predictive failure detection
* Improve agent collaboration logic
* Dashboard for workflow visibility

---

##  Conclusion

This project transforms a **chatbot into an autonomous enterprise worker**:
