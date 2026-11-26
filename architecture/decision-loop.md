# The decision loop

A human-in-the-loop pattern for AI recommendations. Each control exists because a specific stakeholder asked for it in `personas/`.

```mermaid
flowchart LR
    A[Source data] --> B{Data-quality gate}
    B -- pass --> C[Recommendation engine]
    B -- fail --> H[Hold + alert owner]
    C --> D[Explain: reasons, math, confidence]
    D --> E{Confidence high?}
    E -- yes --> F[Human approval]
    E -- no --> G[Route to analyst]
    G --> F
    F --> I[Action released]
    I --> J[Outcome measured]
    J --> K[(Outcome write-back)]
    K --> C
```

| Control | Why it exists | Who asked |
|---|---|---|
| Data-quality gate | Bad inputs produce confident wrong answers | VP RevOps, Chief AI Officer |
| Explain step | Unexplained recommendations get ignored | CRO, Chief AI Officer |
| Confidence routing | Low confidence goes to a person, not to production | Chief AI Officer |
| Human approval | Accountability stays with a named person | CRO, CEO |
| Outcome write-back | Results are measured, not assumed | CFO |
