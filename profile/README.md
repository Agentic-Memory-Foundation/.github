# AGENTIC MEMORY FOUNDATION

```text
      _                       _   _        __  __                                
     / \   __ _  ___ _ __ | |_(_) ___  |  \/  | ___ _ __ ___   ___  _ __ _   _ 
    / _ \ / _` |/ _ \ '_ \| __| |/ __| | |\/| |/ _ \ '_ ` _ \ / _ \| '__| | | |
   / ___ \ (_| |  __/ | | | |_| | (__  | |  | |  __/ | | | | | (_) | |  | |_| |
  /_/   \_\__, |\___|_| |_|\__|_|\___| |_|  |_|\___|_| |_| |_|\___/|_|   \__, |
          |___/                                                          |___/ 
             _____                      _       _   _             
            |  ___|__  _   _ _ __   __| | __ _| |_(_) ___  _ __  
            | |_ / _ \| | | | '_ \ / _` |/ _` | __| |/ _ \| '_ \ 
            |  _| (_) | |_| | | | | (_| | (_| | |_| | (_) | | | |
            |_|  \___/ \__,_|_| |_|\__,_|\__,_|\__|_|\___/|_| |_|
```

```text
=====================================================================================
» ESTABLISHED: 2026.11 · PROTOCOL: SECURE · LEVEL: ACADEMIC · COGNITIVE NODE: ACTIVE «
=====================================================================================
+-----------------------------------------------------------------------------------+
|  [SYSTEM STATUS]  ...................................................... ONLINE  |
|  [ARCHIVAL CODE]  ......................................... AMF-SUBSTRATE-2026-v2  |
|  [ENCRYPTION KEY] .................................. GHO_REF_MEM_UNBIND_ACTIVE  |
|  [ACTIVE SECTORS] .......................... PLANE-B, HMR-SYNTH, K-FLAT, ATLAS  |
+-----------------------------------------------------------------------------------+
```

---

## ⚡ The Manifesto

The prevailing paradigm of agentic intelligence relies heavily on the ephemeral context window of autoregressive models. **This is insufficient.** A collective intelligence requires more than context stuffing—it demands structured, database-resident, and holographically-reduced associative memory layers. 

The **Agentic Memory Foundation (AMF)** is an open scientific collective researching, developing, and standardizing the mathematical formalisms, database engines, and software substrates that will power the next era of permanent agentic state and secure tool governance. 

We do not merely build tools; we establish the foundational protocols for how machines remember, reason, and respect guardrails.

---

## 🔬 Core Research Quadrants & Substrates

Our work spans four critical domains of agentic systems architecture. Each domain is backed by empirical preprints, reference implementations, and active development.

### I. Database-Resident Agent Governance (Plane-B Guardrails)
*Unified policy, drift reduction, and secure agent-to-database interfaces.*

* **Primary Repository:** [`pg-policy`](https://github.com/Agentic-Memory-Foundation/pg-policy)
* **Working Paper:** [`agentic-policy`](https://github.com/Agentic-Memory-Foundation/agentic-policy)
* **The Scientific Thesis:** Deterministic agent authorization cannot exist solely as snowflake middleware inside volatile API gateways. It must reside inside the database's trust boundary. We introduce `pg_agent_policy` (and the Agent Policy Language - APL) to provide a non-bypassable, PostgreSQL-resident C-level policy referee that governs both data rows (Plane-A RLS) and tool/session actions (Plane-B) under a unified, fail-closed paradigm.
* **Mathematical Formalism:**
  The combined authorization space $\mathcal{E}$ is evaluated across three decoupled planes:
  $$\mathcal{E} = \mathcal{P}_A \land \mathcal{P}_B \land \mathcal{P}_C$$
  Where Plane-B policy enforcement matches tool invocation actions over sliding temporal intervals:
  $$\text{Decision}(t) = \text{Match}(\text{APL}) \cap \{ \text{Count}(\text{Action}) \le \theta \}_{\Delta t}$$

---

### II. Holographic Compositional Memory Retrieval (HMRBench)
*High-dimensional vector binding and robust role-reversal discrimination.*

* **Primary Repository:** [`hrr-basic-one`](https://github.com/Agentic-Memory-Foundation/hrr-basic-one)
* **The Scientific Thesis:** Standard dense RAG collapses on structurally-confusable queries (textually near-identical facts with reversed role-filler bindings). We design **HMRBench**, a self-contained, hyper-optimized C++ benchmark combining semantic routing with Holographic Reduced Representations (HRR). Using circular convolution for binding and circular correlation for unbinding, we achieve perfect role-reversal discrimination with up to 16× compression using Kashin 1-bit sign quantization.
* **Mathematical Formalism:**
  We consolidate $N$ distinct relations into a unified associative memory node $M$ by bundling bound role–value vectors:
  $$M = \sum_{i=1}^N (s_i \circledast r_i) \circledast f_i$$
  Unbinding is performed with circular correlation $\odot$, isolating the target filler vector:
  $$f_j \approx M \odot (s_j \circledast r_j)$$

---

### III. Local Principal Directions for Dense Retrieval (Manifold Routing)
*Affine k-flat projection for partitioned vector spaces.*

* **Primary Repository:** [`camman` / `grassmanian`](https://github.com/Agentic-Memory-Foundation/grassmanian)
* **The Scientific Thesis:** Approximate Nearest Neighbor (ANN) index structures typically route queries by comparing them to static cluster centroids. We propose that local cluster shape—represented as an affine $k$-flat—provides a much stronger routing signal. By projecting residual distances along local principal directions (local-PCA), we significantly improve recall and nDCG metrics under tight scan budgets compared to traditional cosine-to-centroid IVF methods.
* **Mathematical Formalism:**
  The distance metric for query routing to an affine $k$-flat is defined by:
  $$d_{\text{k-flat}}(q) = \left\| \tilde{q} - \sum_{j=1}^k \langle \tilde{q}, v_j \rangle v_j \right\|_2$$
  Where $\tilde{q} = q - \mu$ represents the centroid-centered query, and $\{v_j\}_{j=1}^k$ are the orthogonal local principal directions of the partition.

---

### IV. Virtual Directory Indexing for Coding Agents (System Mapping)
*The physical file-system path as a retrieval index.*

* **Primary Repositories:** [`directory-is-the-index`](https://github.com/Agentic-Memory-Foundation/directory-is-the-index) · [`repo-atlas`](https://github.com/Agentic-Memory-Foundation/repo-atlas) · [`shared-blindness`](https://github.com/Agentic-Memory-Foundation/shared-blindness)
* **The Scientific Thesis:** File and directory naming structures act as the physical index for coding agents, restricting searches to paths that match the agent's vocabulary. We evaluate physical renaming via `repo-atlas` versus virtual remapping (using `AGENTS.md` files). Empirically, virtual renaming yields far superior bug-fix localization (+4.9 points hit@5) with zero regression in existing test suites, establishing the necessity of virtual cognitive maps over structural refactoring.

---

## 🛰️ Join the Movement (Onboarding Protocol)

We are building a decentralized, serious, and academically-minded movement. If you are obsessed with the low-level systems and high-dimensional mathematics behind cognitive storage, database-level guardrails, or vector manifolds, your node belongs in our network.

```text
=====================================================================================
»                     INITIATING ONBOARDING PROTOCOL SEQUENCE                       «
=====================================================================================
  [STEP 1] : Inspect our core repositories and read the preprints.
  [STEP 2] : Open our structured Telemetry Application Form via the link below.
  [STEP 3] : Submit your node telemetry (GitHub handle, area of expertise, proposal).
  [STEP 4] : Your credentials will be queued for evaluation by our core steering peers.
=====================================================================================
```

### 🛰️ [ ► CLICK HERE TO SUBMIT YOUR ONBOARDING TELEMETRY ◄ ](https://github.com/Agentic-Memory-Foundation/.github/issues/new?template=apply_to_movement.yml)

Let's build the cognitive substrate of the future—together.

---

## ✉️ Contact & Steering
For formal inquiries, academic collaborations, or to establish joint research vectors:
* **Parag Paul:** [parag@rigai.co](mailto:parag@rigai.co) (Founder & Systems Architect)
* **Saurabh Sarkar:** [sarkar@chicory.ai](mailto:sarkar@chicory.ai) (Core Math Peer)
* **Avinash Anand:** [avinash@rigai.co](mailto:avinash@rigai.co) (Database & Security Peer)
