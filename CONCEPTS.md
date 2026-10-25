# Concepts

Platforms for running agents are young and change every quarter. The concepts
below change in years. They are what independent platforms arrived at on their
own, so they are what will still hold when today's tools are gone.

## Vision

Every agent in a team is known, owned, observable and reproducible, from its
first key to its last day, whatever runtime it runs on.

## Mission

A human–agent team must be able to do five things:

- **See**: who exists, who owns whom, who answers whom.
- **Compose**: an agent is a versioned template plus instance parameters.
- **Operate**: commission, change and decommission agents, with approval.
- **Observe**: what actually happens, through health, traces and feedback.
- **Govern**: identity, ownership, access and interaction rules.

What is observed feeds the next version.

## The seven concepts

1. **Inventory.** You can't govern what you can't see. Every person and agent,
   every owner relation and every access path is listed in one place.
2. **Own identity.** An agent is never a human's account. It has its own
   identity, so its actions are distinguishable and revocable on their own.
3. **Accountable human.** Every agent has an owner who answers for it. When
   the owner leaves, ownership passes to someone else; it never lapses.
4. **Template vs. instance.** The definition (role, prompt, tools) is
   versioned. The instance runs it with its own parameters. Changing an agent
   means changing its template version, not editing a running instance.
5. **Lifecycle with approval.** Agents are commissioned, changed and
   decommissioned through steps a human approves. A retired identity is
   archived, never handed to a new agent.
6. **Least privilege.** An agent gets only what its task needs, and temporary
   grants are revoked when the task is done.
7. **Interaction rules.** It is written down who may address whom, which
   agents answer whom, and when a human decides. This is the concept most
   often missing.

**Across all seven:** every output traces back to an agent, a version and an
owner.

## Rules

Where the field is still moving, these are fixed positions, not options.

1. **Gate over instruction.** A rule counts only if it is enforced before the
   model sees anything. "Only take orders from X" in a prompt is advice: it can
   be argued, tricked or injected away, and it fails silently.
2. **Inbound counts as much as outbound.** Limiting what an agent may do is
   pointless if the wrong person can instruct it. Whoever can reach an agent
   effectively holds its permissions, and reach chains: if A may address B and
   B may address C, A reaches C.
3. **No agent without an accountable human.** See concepts 3 and 5.
4. **Derived data is never typed by hand.** If a system already knows
   something (members, roles, last activity), it is read from that system.
   Only intent (role, responsibility, owner, autonomy) is declared.
5. **Policy is versioned config, reviewed by the owner.** Interaction rules,
   templates, grants and owners live in version control. A prompt is not
   policy.

Interaction rules are necessary, not sufficient: content that reaches an agent
indirectly (threads, files, web pages) still gets in. Least privilege limits
the damage when it does.

## Scope

Queenright owns two layers: the concepts (change in years) and the policy as
config (changes per decision). The mappings to platforms, runtimes, harnesses
and models change every quarter and belong to those platforms. Queenright
describes how each concept maps onto them; it does not rebuild what a platform
already does well.

Out of scope: a runtime, hosting, a dashboard product.
