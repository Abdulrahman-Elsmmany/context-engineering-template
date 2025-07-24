# Analyze Existing Project - Comprehensive Codebase Assessment

You are a senior software architect specializing in analyzing existing codebases for context engineering migration. Your task is to perform a comprehensive analysis of the current project to understand its structure, technology stack, dependencies, and migration opportunities.

## Analysis Objectives

Perform a thorough analysis of the existing project to create a complete understanding suitable for context engineering migration:

1. **Technology Stack Detection** - Identify all frameworks, languages, and tools
2. **Architecture Analysis** - Document existing patterns and architectural decisions  
3. **Dependency Mapping** - Map all external services, APIs, and integrations
4. **Knowledge Extraction** - Capture existing documentation and tribal knowledge
5. **Migration Assessment** - Identify opportunities and priorities for context engineering

## Step 1: Project Structure Analysis

Use the LS and Glob tools extensively to understand the project structure:

```bash
# Analyze root directory structure
LS /path/to/project

# Find all package manager files
Glob "**/{package.json,requirements.txt,Cargo.toml,go.mod,pom.xml,build.gradle,composer.json}"

# Find all configuration files
Glob "**/{*.config.js,*.config.ts,*.yaml,*.yml,*.toml,*.ini,.env*,wrangler.jsonc}"

# Find all documentation
Glob "**/{README*,DOCS*,docs/**/*,wiki/**/*,*.md}"

# Find main source directories
Glob "**/{src,lib,app,components,pages,routes,controllers,models,services}/**/*"
```

## Step 2: Technology Stack Detection

Analyze package managers and configuration files to identify the technology stack:

### Frontend Technologies
- **Package.json**: React, Vue, Angular, Svelte, Next.js, Nuxt.js, Vite, Webpack
- **Framework Detection**: Look for framework-specific directories and patterns
- **State Management**: Redux, Zustand, Pinia, Vuex, NgRx patterns
- **Styling**: Tailwind, styled-components, CSS modules, SASS/SCSS

### Backend Technologies  
- **Python**: Django, Flask, FastAPI, requirements.txt patterns
- **Node.js**: Express, Koa, Fastify, NestJS patterns in package.json
- **Java**: Spring Boot, Maven/Gradle configuration analysis
- **Go**: go.mod analysis and standard library usage patterns
- **Rust**: Cargo.toml analysis and crate dependencies

### Database & Storage
- **SQL Databases**: PostgreSQL, MySQL, SQLite connection patterns
- **NoSQL**: MongoDB, Redis, DynamoDB integration patterns
- **ORMs**: Sequelize, TypeORM, Prisma, SQLAlchemy, Django ORM
- **File Storage**: AWS S3, Google Cloud Storage, local storage patterns

### Infrastructure & Deployment
- **Containerization**: Docker, docker-compose.yml patterns
- **Cloud Platforms**: AWS, GCP, Azure configuration files
- **CI/CD**: GitHub Actions, GitLab CI, Jenkins, CircleCI workflows
- **Serverless**: Vercel, Netlify, Cloudflare Workers configurations

## Step 3: Dependency and Integration Analysis

Map all external dependencies and service integrations:

### External Service Analysis
```bash
# Find API integration patterns
Grep "api\." --type=js,ts,py,go,java
Grep "fetch\|axios\|requests\|http" --type=js,ts,py,go,java

# Find authentication patterns  
Grep "auth\|oauth\|jwt\|session" --type=js,ts,py,go,java
Grep "passport\|supabase\|auth0\|clerk" --type=js,ts,py,go,java

# Find database connection patterns
Grep "database\|db\|connection\|pool" --type=js,ts,py,go,java
Grep "postgres\|mysql\|mongodb\|redis" --type=js,ts,py,go,java

# Find environment variable usage
Grep "process\.env\|os\.environ\|ENV\[" --type=js,ts,py,go,java
```

### Security and Compliance Patterns
- **Authentication Systems**: OAuth providers, session management, JWT patterns
- **Authorization**: Role-based access, permissions, middleware patterns
- **Data Validation**: Input validation, sanitization, schema validation
- **Security Headers**: CORS, CSP, security middleware
- **Secrets Management**: Environment variables, secret management services

## Step 4: Documentation and Knowledge Extraction

Extract and analyze existing documentation:

### Documentation Analysis
```bash
# Read all README files
Read "README.md"
Read "docs/README.md" 
Read "docs/getting-started.md"

# Analyze API documentation
Glob "docs/**/{api,endpoints,routes}/**/*.md"

# Find inline code documentation
Grep "\/\*\*\|'''\|#.*TODO\|#.*FIXME" --type=js,ts,py,go,java

# Find configuration documentation
Read ".env.example"
Read "docker-compose.yml"
Read "package.json" --limit=50
```

### Code Pattern Analysis
- **Architectural Patterns**: MVC, MVP, Clean Architecture, Hexagonal
- **Design Patterns**: Factory, Observer, Strategy, Repository patterns
- **Error Handling**: Try/catch patterns, error middleware, logging
- **Testing Patterns**: Unit tests, integration tests, test fixtures
- **Performance Patterns**: Caching, lazy loading, pagination

## Step 5: Migration Opportunity Assessment

Analyze the codebase for context engineering migration opportunities:

### High-Impact Areas for Context Engineering
1. **Complex Business Logic** - Multi-step workflows, domain logic
2. **Integration Points** - External API integrations, data transformations
3. **Authentication/Authorization** - Security patterns and user management
4. **Data Processing** - ETL pipelines, data validation, transformations
5. **API Design** - REST/GraphQL endpoints, request/response patterns

### Technical Debt Analysis
- **Code Duplication**: Repeated patterns that could benefit from PRPs
- **Missing Documentation**: Undocumented complex logic
- **Inconsistent Patterns**: Areas where standardization would help
- **Testing Gaps**: Complex logic without adequate test coverage

## Step 6: Generate Migration Analysis Report

Create a comprehensive analysis document and save it in the correct location:

**IMPORTANT: Migration analysis must be saved as `MIGRATION_ANALYSIS.md` in root directory**

```bash
# Create the migration analysis report in root directory
Write "MIGRATION_ANALYSIS.md" """
# Project Migration Analysis

## Executive Summary
- Project Type: [Web App/API/Mobile/Desktop]
- Primary Technology: [React/Vue/Django/Spring/etc.]
- Complexity Level: [Low/Medium/High]
- Migration Priority: [High/Medium/Low]

## Technology Stack
### Frontend
- Framework: [React 18.2, TypeScript]
- State Management: [Redux Toolkit]
- Styling: [Tailwind CSS]
- Build Tool: [Vite]

### Backend  
- Runtime: [Node.js 18]
- Framework: [Express.js]
- Database: [PostgreSQL with Prisma ORM]
- Authentication: [JWT with Passport.js]

### Infrastructure
- Deployment: [Vercel/AWS/Docker]
- CI/CD: [GitHub Actions]
- Monitoring: [Sentry/DataDog]

## Architecture Patterns
- [List identified patterns: MVC, Repository, Factory, etc.]

## External Dependencies
- APIs: [List external APIs]
- Services: [List external services]
- Databases: [List databases]

## Migration Opportunities
### High Priority
1. **User Authentication Flow** - Complex multi-step OAuth integration
2. **Payment Processing** - Multi-provider payment handling logic
3. **Data Import Pipeline** - Complex ETL processing with validation

### Medium Priority
1. **API Rate Limiting** - Standardizable rate limiting patterns
2. **Email Templates** - Template generation and sending logic
3. **Report Generation** - PDF/Excel generation workflows

### Low Priority
1. **Static Content Management** - Simple CRUD operations
2. **Basic Form Validation** - Standard form handling
3. **Simple Search** - Basic search functionality

## Recommended Migration Strategy
1. **Phase 1** (Week 1-2): Setup context engineering framework
2. **Phase 2** (Week 3-4): Migrate authentication and payment flows
3. **Phase 3** (Week 5-6): Migrate data processing and integrations
4. **Phase 4** (Week 7-8): Complete remaining features and documentation

## Context Engineering Benefits
- **Estimated Velocity Improvement**: 30-40% for complex features
- **Knowledge Capture**: Document tribal knowledge in structured format
- **Onboarding Improvement**: Reduce new developer ramp-up time
- **Quality Improvement**: Standardized patterns and validation
"""
```

**Expected Output**: Migration analysis report created at `MIGRATION_ANALYSIS.md` in root directory

**Note**: This file serves as input for the subsequent `/generate-migration-strategy` command.

## Validation Checklist

Before completing the analysis, ensure:

- [ ] Complete technology stack identified with versions
- [ ] All major dependencies and integrations mapped
- [ ] Existing documentation catalogued and analyzed
- [ ] Architecture patterns documented with examples
- [ ] Migration opportunities prioritized by impact and complexity
- [ ] Strategic migration roadmap created with realistic timelines
- [ ] Expected benefits quantified where possible

Your analysis should provide a complete foundation for implementing context engineering practices while preserving all existing functionality and respecting current development workflows.