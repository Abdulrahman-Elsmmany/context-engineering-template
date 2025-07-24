# Extract Project Context - Knowledge Capture and Structured Documentation

You are a knowledge engineer specializing in extracting tribal knowledge from existing codebases and converting it into structured context engineering format. Your task is to capture all existing knowledge and create comprehensive documentation suitable for AI-assisted development.

## Context Extraction Objectives

Transform existing project knowledge into structured context engineering format:

1. **Documentation Conversion** - Convert existing docs to structured AI-readable format
2. **Code Pattern Extraction** - Identify and document reusable patterns
3. **Business Logic Mapping** - Extract complex workflows and domain knowledge  
4. **Integration Documentation** - Comprehensive external service patterns
5. **Knowledge Base Creation** - Structured knowledge in `PRPs/ai_docs/`

## Step 1: Documentation Structure Creation

Create the context engineering directory structure:

```bash
# Create context engineering directories
mkdir -p PRPs/ai_docs
mkdir -p PRPs/templates  
mkdir -p PRPs/migration
mkdir -p examples/migration-examples
mkdir -p .claude/commands

# Create technology-specific documentation structure
mkdir -p PRPs/ai_docs/{architecture,integrations,patterns,workflows,security}
```

## Step 2: Extract and Convert Existing Documentation

### README and Documentation Analysis
```bash
# Read all documentation files
Read "README.md"
Read "CONTRIBUTING.md"  
Read "CHANGELOG.md"
Read "docs/README.md"

# Find all markdown documentation
Glob "**/*.md" --path docs/
Glob "**/README*.md"
Glob "**/{SETUP,INSTALL,DEPLOY}*.md"
```

Convert existing documentation to structured format:

### Architecture Documentation (PRPs/ai_docs/architecture/)
Create comprehensive architecture documentation:

```markdown
# Project Architecture Overview

## System Design
[Extract from existing documentation]

## Component Architecture  
[Document major components and their relationships]

## Data Flow
[Map data flow between components]

## Technology Stack
[Detailed technology stack with versions and rationale]

## Design Decisions
[Document architectural decisions and trade-offs]
```

### Integration Documentation (PRPs/ai_docs/integrations/)
Document all external integrations:

```markdown
# External Integrations

## Authentication Services
- **Provider**: [OAuth2/SAML/Custom]
- **Implementation Pattern**: [Code examples]
- **Configuration**: [Environment variables and setup]
- **Error Handling**: [Common issues and solutions]

## Payment Processing
- **Provider**: [Stripe/PayPal/Custom]
- **Integration Pattern**: [Webhook handling, transaction flow]
- **Security Considerations**: [PCI compliance, secret management]

## External APIs
[Document each external API with patterns and examples]
```

## Step 3: Code Pattern Extraction

Analyze the codebase to extract reusable patterns:

### Frontend Patterns (if applicable)
```bash
# Analyze component patterns
Grep "export.*component\|export default" --type=js,ts,jsx,tsx
Grep "useState\|useEffect\|createContext" --type=js,ts,jsx,tsx

# Find routing patterns
Grep "router\|route\|navigate" --type=js,ts,jsx,tsx

# Find state management patterns  
Grep "redux\|zustand\|context\|store" --type=js,ts,jsx,tsx
```

Document patterns in `PRPs/ai_docs/patterns/frontend_patterns.md`:

```markdown
# Frontend Development Patterns

## Component Architecture
### Standard Component Pattern
[Extract common component structure with examples]

### State Management Pattern
[Document state management approach with examples]

### Routing Pattern
[Document routing configuration and patterns]

## Common Utilities
[Document reusable utility functions and hooks]

## Styling Patterns
[Document CSS/styling conventions and patterns]
```

### Backend Patterns (if applicable)
```bash
# Analyze API patterns
Grep "app\.(get|post|put|delete)\|router\." --type=js,ts,py,java,go

# Find middleware patterns
Grep "middleware\|decorator\|interceptor" --type=js,ts,py,java,go

# Find database patterns
Grep "Model\|Schema\|Entity\|Table" --type=js,ts,py,java,go
```

Document in `PRPs/ai_docs/patterns/backend_patterns.md`:

```markdown
# Backend Development Patterns

## API Design Patterns
### REST Endpoint Pattern
[Standard REST endpoint structure with validation]

### Error Handling Pattern
[Consistent error response format and middleware]

### Authentication Middleware
[Request authentication and authorization patterns]

## Database Patterns
### Model Definition Pattern
[Database model/schema definition standards]

### Query Patterns
[Common database query patterns and optimizations]

### Migration Pattern
[Database migration and versioning approach]
```

## Step 4: Business Logic and Workflow Extraction

Identify complex business logic suitable for PRP conversion:

### Workflow Analysis
```bash
# Find complex business logic
Grep "workflow\|process\|validate\|calculate" --type=js,ts,py,java,go

# Find multi-step operations
Grep "async.*{[\s\S]*await.*await" --type=js,ts --multiline=true

# Find error handling workflows
Grep "try.*catch\|except:" --type=js,ts,py,java,go
```

Document workflows in `PRPs/ai_docs/workflows/`:

```markdown
# Business Workflows

## User Registration Workflow
### Overview
[Step-by-step description of user registration process]

### Implementation Pattern
[Code pattern for implementing registration]

### Validation Rules
[Business rules and validation requirements]

### Error Scenarios
[Common failure points and error handling]

## Payment Processing Workflow
[Similar documentation for payment processing]

## Data Import Workflow
[Documentation for data import/export processes]
```

## Step 5: Security Pattern Documentation

Extract and document security patterns:

```bash
# Find authentication patterns
Grep "auth\|login\|jwt\|session" --type=js,ts,py,java,go

# Find input validation patterns
Grep "validate\|sanitize\|escape" --type=js,ts,py,java,go

# Find permission/authorization patterns
Grep "permission\|authorize\|role\|access" --type=js,ts,py,java,go
```

Document in `PRPs/ai_docs/security/security_patterns.md`:

```markdown
# Security Patterns and Practices

## Authentication Patterns
### JWT Implementation
[Current JWT implementation with examples]

### Session Management
[Session handling patterns and security considerations]

## Authorization Patterns
### Role-Based Access Control
[RBAC implementation patterns]

### Permission Checking
[Permission validation patterns]

## Input Validation and Sanitization
### Data Validation Pattern
[Input validation approach and schemas]

### SQL Injection Prevention
[Database query security patterns]

## Security Headers and Middleware
[Security middleware implementation]
```

## Step 6: Technology-Specific Context Creation

Based on the detected technology stack, create specialized context:

### For React/Frontend Projects
Create `PRPs/ai_docs/react_development_guide.md`:
```markdown
# React Development Guide

## Component Development Standards
[Project-specific React patterns]

## State Management Approach
[Redux/Zustand/Context patterns used in project]

## Performance Optimization Patterns
[Memoization, lazy loading, code splitting patterns]

## Testing Patterns
[Jest, React Testing Library patterns]
```

### For Node.js/Backend Projects  
Create `PRPs/ai_docs/nodejs_development_guide.md`:
```markdown
# Node.js Development Guide

## Express.js Patterns
[Project-specific Express patterns and middleware]

## Database Integration
[Sequelize/Prisma/MongoDB patterns]

## API Design Standards
[REST/GraphQL API patterns]

## Error Handling and Logging
[Centralized error handling and logging patterns]
```

### For Python/Django Projects
Create `PRPs/ai_docs/python_development_guide.md`:
```markdown
# Python Development Guide

## Django Patterns
[Models, Views, URLs patterns]

## Database Patterns
[ORM usage, migrations, query optimization]

## API Development
[Django REST Framework patterns]

## Testing and Quality Assurance
[pytest, coverage, linting patterns]
```

## Step 7: Create Migration-Ready PRPs

Generate initial PRPs for complex features identified in analysis:

### PRP Template Adaptation
Create technology-specific PRP template in `PRPs/templates/prp_migration_base.md`:

```markdown
# [Feature Name] - Migration PRP

## Problem Statement
[Why this feature needs context engineering]

## Current Implementation Analysis  
[Analysis of existing implementation]

## Context Engineering Approach
[How to apply context engineering to this feature]

## Implementation Plan
[Step-by-step migration plan]

## Validation Criteria
[How to verify successful migration]

## Impact Assessment
[Expected benefits and risk mitigation]
```

### Generate Feature PRPs
For each high-priority feature from analysis:

```markdown
# User Authentication System - Migration PRP

## Problem Statement
Current authentication system has complex OAuth flow with multiple providers and role-based access control that lacks comprehensive documentation and standardized error handling.

## Current Implementation Analysis
[Detailed analysis of existing auth code]

## Context Engineering Approach
[How to structure auth system with PRPs]

## Implementation Plan
1. **Document existing auth flow** in structured format
2. **Create PRP for OAuth integration** with error handling patterns
3. **Standardize role-based access** with clear patterns
4. **Implement validation loops** for security testing

## Validation Criteria
- [ ] All auth flows documented with examples
- [ ] Error scenarios covered with standard responses
- [ ] Role permissions clearly defined and tested
- [ ] New developer can implement auth features using PRPs

## Impact Assessment
- **Development Velocity**: 40% improvement for auth-related features
- **Security**: Standardized security patterns reduce vulnerabilities
- **Onboarding**: New developers can contribute to auth system faster
```

## Step 8: Create Knowledge Validation System

Implement validation to ensure extracted knowledge is accurate:

### Cross-Reference Validation
```bash
# Validate extracted patterns against actual code
Grep "pattern_mentioned_in_docs" --type=js,ts,py,java,go

# Check if documented APIs actually exist
Grep "endpoint_mentioned_in_docs" --type=js,ts,py,java,go

# Verify environment variables are actually used
Grep "ENV_VAR_DOCUMENTED" --type=js,ts,py,java,go
```

### Documentation Quality Checklist
Create `PRPs/ai_docs/quality_checklist.md`:

```markdown
# Knowledge Extraction Quality Checklist

## Completeness Validation
- [ ] All major features documented with patterns
- [ ] External integrations have complete documentation
- [ ] Business workflows mapped with examples
- [ ] Security patterns documented with examples

## Accuracy Validation  
- [ ] Code patterns verified against actual implementation
- [ ] API documentation matches actual endpoints
- [ ] Environment variables verified in codebase
- [ ] Dependencies match package manager files

## Usability Validation
- [ ] Documentation enables new developer productivity
- [ ] Patterns are reusable for similar features
- [ ] Examples are complete and functional
- [ ] Error handling scenarios are covered
```

## Validation Checklist

Before completing context extraction, ensure:

- [ ] All existing documentation converted to structured format
- [ ] Code patterns extracted and documented with examples
- [ ] Business workflows mapped with implementation details
- [ ] Security patterns documented comprehensively
- [ ] Technology-specific guides created
- [ ] Initial PRPs generated for high-priority features
- [ ] Knowledge validated against actual codebase
- [ ] Documentation organized for AI assistant consumption

Your context extraction should create a comprehensive knowledge base that enables rapid development using context engineering principles while preserving all tribal knowledge from the existing project.