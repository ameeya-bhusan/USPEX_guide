Below is a flowchart illustrating the process of USPEX.

```mermaid
graph TD;
    A[Start] --> B[Initialization];
    B --> C{Create New Generation};
    C --> D[Best Individuals];
    C --> E[Mutation];
    C --> F[Heredity];
    D --> G[New Generation];
    E --> G[New Generation];
    F --> G[New Generation];
    G --> H[Criteria Achieved?];
    H -->|Yes| I[Finish];
    H -->|No| C[Create New Generation];
