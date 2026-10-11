# AI Engineering Journal

## Experiment
AI-Augmented Software Development Environment

## Project
Student CGPA Performance Management System

## Development Environment
- IDE: Visual Studio Code
- Programming Language: Python 3.14.3
- AI Coding Assistant: GitHub Copilot Chat
- Version Control: Git and GitHub
- Code Quality Tool: Ruff
- Automated Testing Tool: Pytest

## AI Interaction 1: Code Explanation
**Prompt:** Explain the purpose of the existing Student CGPA Performance Management System and how the `calculate_cgpa()` function works without modifying files.

**AI Assistance:** Copilot reviewed the project code and tests and explained the application's purpose and CGPA calculation logic.

**Human Validation:** Reviewed the explanation against the existing code.

## AI Interaction 2: Code Quality
**Prompt:** Explain the Ruff configuration and the coding standards it enforces.

**AI Assistance:** Copilot explained the configured linting rules, line-length setting, Python target version, and formatting preferences.

**Human Validation:** Ran Ruff checks in the terminal.

**Result:** All Ruff checks passed before the AI-assisted code changes.

## AI Interaction 3: Debugging
**Prompt:** Review the application and tests for potential input-validation and edge-case issues without modifying files.

**AI Assistance:** Copilot identified possible edge cases, including empty input and unexpected input-stream termination.

**Human Validation:** Treated suggestions as potential concerns until verified.

## AI Interaction 4: Code Generation, Testing, and Refactoring
**Prompt:** Propose and implement small improvements to the existing application and tests while preserving the project structure.

**AI Assistance:** Copilot updated the existing application and test files and added edge-case coverage for invalid grade inputs.

**Human Validation:** Reviewed the proposed changes and ran the project's automated tests.

**Reported Result:** Eight tests passed. Final Ruff and formatting check results were checked separately in the terminal.

## Engineering Decisions
- Retained the existing project structure.
- Used Ruff to check code quality and formatting.
- Used Pytest to validate program behavior.
- Reviewed AI suggestions rather than accepting them as automatically correct.
- Kept the changes focused on input validation and testing.

## Conclusion
AI assistance supported code explanation, debugging, code improvement, and test generation. Automated checks and human review were used to validate the work. Git provides a way to track and trace the resulting changes.