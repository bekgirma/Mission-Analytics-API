# Mission Analytics API
A hardened, production-ready ML inference service built with FastAPI and Docker.

## Key Engineering Features:

   Data Governance: Uses Pydantic v2 to enforce strict data contracts; rejects malformed inputs with 422 errors to protect model integrity.

   Hardened Containerization: Implements a multi-stage Docker build and runs as a non-root user to minimize the attack surface.

   Observability: Includes health check endpoints for cloud-native orchestration (e.g., K8s/ECS).

   Reliability: Built with a clean separation of concerns between model logic and API infrastructure.

