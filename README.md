# Elasticsearch CI/CD Practice Project

[![CI/CD Pipeline](https://github.com/AboofazlNajmaddini/elseticSearch/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/AboofazlNajmaddini/elseticSearch/actions/workflows/ci-cd.yml)

This is a hands-on practice project to learn **Continuous Integration (CI)** and basics of **Continuous Delivery (CD)** using modern DevOps tools.

The goal was to build a simple Python application that interacts with Elasticsearch, write automated tests, containerize everything with Docker, and set up a full CI/CD pipeline with GitHub Actions.




### Project Overview

- **Application**: A simple Python script that connects to Elasticsearch, creates an index, indexes documents, and performs searches.
- **Testing**: Comprehensive unit/integration tests using `pytest` to verify connection, indexing, and search functionality.
- **Containerization**:
  - Multi-container setup with Docker Compose (one container for Elasticsearch, one for the Python app).
  - Custom bridge network for inter-container communication (app connects to `elasticsearch:9200`).




### Key Features Implemented

- **Docker & Docker Compose**: Full multi-container environment with health checks and automatic networking.
- **Automated Testing**: Tests run inside the app container, ensuring everything works end-to-end.
- **GitHub Actions CI/CD**:
  - On every push to `main`: Runs tests inside Docker containers.
  - If tests pass: Triggers deployment (webhook to Render.com for automatic deploy).








### How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/[your-username]/elasticsearch-ci-practice.git
   cd elasticsearch-ci-practice
   ```

2. Start the application with Docker Compose:
   ```bash
   docker compose up --build
   ```

   - Elasticsearch will start first.
   - The Python app will run tests automatically.
   - You should see all tests **PASS** if everything is working.

3. To run tests only:
   ```bash
   docker compose up --build --abort-on-container-exit
   ```

### Technologies Used

- Python 3.11
- Elasticsearch 8.x
- pytest for testing
- Docker & Docker Compose
- GitHub Actions for CI/CD
- Render.com for deployment attempts (CD webhook trigger)

### What I Learned

- Writing clean, testable code.
- Advanced pytest features (fixtures, cleanup).
- Multi-container Docker setups with custom networking.
- Building robust GitHub Actions workflows (test → deploy chain).
- Common production issues (like dependency resolution in cloud environments).

This project is a complete beginner-to-intermediate DevOps portfolio piece. Feel free to fork and improve it!

**Note**: The final deployment to Render triggers successfully, but the app requires a managed Elasticsearch instance in production (learned a real-world lesson about environment differences!).
