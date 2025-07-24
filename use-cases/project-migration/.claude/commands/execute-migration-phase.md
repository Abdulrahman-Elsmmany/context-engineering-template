# Execute Migration Phase - Implement Context Engineering Incrementally

You are a senior implementation engineer specializing in context engineering adoption and team transformation. Your task is to execute a specific phase of the migration strategy, implementing context engineering practices while preserving existing functionality and team productivity.

## Phase Execution Objectives

Implement the specified migration phase with precision and quality:

1. **Phase Implementation** - Execute phase activities according to migration strategy
2. **Quality Assurance** - Ensure all deliverables meet context engineering standards
3. **Team Support** - Provide guidance and support for team adoption
4. **Progress Tracking** - Monitor phase progress and adjust as needed
5. **Validation and Feedback** - Validate results and capture lessons learned

## Prerequisites

Before executing any migration phase, ensure:
- Migration strategy has been generated and reviewed
- Previous phases (if any) have been completed successfully
- Team has been briefed on phase objectives and activities
- Required resources and time allocations are confirmed

## Step 1: Phase Identification and Planning

Identify which phase to execute and prepare for implementation:

```bash
# Read the migration strategy
Read "PRPs/migration-strategy.md"

# Check current phase status
LS "PRPs/migration/"
Read "PRPs/migration/phase-status.md" || echo "No previous phase status found"

# Review team capacity and readiness
Read "MIGRATION_ANALYSIS.md"
```

## Step 2: Phase 1 Implementation - Foundation and Proof of Concept

### If executing Phase 1:

**Objective**: Establish context engineering infrastructure and prove value

#### Activity 1.1: Setup Infrastructure
```bash
# Ensure directory structure exists
mkdir -p .claude/commands
mkdir -p PRPs/{ai_docs,templates,migration}
mkdir -p examples/migration-examples

# Create technology-specific templates based on analysis
Read "MIGRATION_ANALYSIS.md" | grep "Primary Technology"
```

Create project-specific PRP template based on detected technology:

```markdown
# Technology-Specific PRP Template

Based on analysis showing [React/Vue/Django/Spring/etc.], create appropriate base template:

## For React/Frontend Projects:
```markdown
# [Feature Name] - React PRP

## Problem Statement
[What specific React feature/component needs to be built]

## Context and Requirements
### Component Requirements
[Detailed component specifications]

### State Management
[State requirements and patterns]

### Integration Points
[API integrations, routing, styling]

## Implementation Plan
### Step 1: Component Structure
[Component architecture and file organization]

### Step 2: State Implementation
[State management implementation]

### Step 3: Integration
[API integration and data flow]

### Step 4: Styling and UX
[CSS/styling implementation]

### Step 5: Testing
[Component testing approach]

## Validation Loops
- [ ] Component renders correctly with mock data
- [ ] State management works as expected
- [ ] API integration handles all scenarios
- [ ] Styling matches design requirements
- [ ] Tests cover all use cases
```

## For Backend/API Projects:
```markdown
# [Feature Name] - Backend PRP

## Problem Statement
[What specific API/service functionality needs to be built]

## Context and Requirements
### API Specifications
[Endpoint definitions, request/response formats]

### Business Logic
[Core business rules and processing]

### Data Requirements
[Database schema, validation rules]

## Implementation Plan
### Step 1: Data Layer
[Database models, migrations, repositories]

### Step 2: Business Logic
[Service layer implementation]

### Step 3: API Layer
[Controller/route implementation]

### Step 4: Validation and Security
[Input validation, authentication, authorization]

### Step 5: Testing
[Unit tests, integration tests, API tests]

## Validation Loops
- [ ] Database operations work correctly
- [ ] Business logic handles all scenarios
- [ ] API endpoints return correct responses
- [ ] Security measures are properly implemented
- [ ] Tests achieve adequate coverage
```

#### Activity 1.2: Select and Convert Pilot Features

Identify pilot features from analysis:
```bash
# Review high-priority features from analysis
Read "MIGRATION_ANALYSIS.md" | grep -A 10 "High Priority"

# Check existing documentation for pilot features
Grep "authentication\|user.*management\|payment\|api.*integration" --type=js,ts,py,java,go --output_mode=files_with_matches
```

Convert 1-2 pilot features to PRP format:

**Example: User Authentication PRP**
```markdown
# User Authentication System - Migration PRP

## Problem Statement
The current user authentication system includes OAuth2 integration with GitHub and JWT token management, but lacks comprehensive documentation and standardized error handling patterns. New developers struggle to understand the auth flow and extend authentication features.

## Current Implementation Analysis
[After analyzing existing auth code]

### Existing Components
- OAuth2 GitHub integration in `src/auth/github-oauth.js`
- JWT token generation and validation in `src/auth/jwt-utils.js`
- Authentication middleware in `src/middleware/auth.js`
- User session management in `src/auth/session.js`

### Identified Patterns
- OAuth callback handling with error recovery
- JWT token refresh mechanism
- Role-based authorization checks
- Session persistence and cleanup

### Pain Points
- Inconsistent error handling across auth components
- Missing documentation for adding new OAuth providers
- Complex token refresh logic without clear patterns
- No standardized testing approach for auth flows

## Context Engineering Approach

### PRP Structure for Authentication
1. **OAuth Provider Integration PRP** - Standardized pattern for adding OAuth providers
2. **JWT Token Management PRP** - Token generation, validation, and refresh patterns
3. **Authorization Middleware PRP** - Role-based access control implementation
4. **Session Management PRP** - User session lifecycle management

### Documentation Requirements
- Complete OAuth flow documentation with error scenarios
- JWT security best practices and implementation patterns
- Authorization patterns for different user roles
- Testing patterns for authentication workflows

## Implementation Plan

### Step 1: Document Current Auth Flow (Week 1)
1. **Map OAuth2 GitHub Integration**
   - Document authorization request flow
   - Map callback handling and error scenarios
   - Document token exchange and user data retrieval

2. **Document JWT Token Management**
   - Token generation with user claims
   - Token validation and expiration handling
   - Refresh token implementation and security

3. **Document Authorization Patterns**
   - Role-based access control implementation
   - Permission checking middleware
   - Route protection patterns

### Step 2: Create Authentication PRPs (Week 1-2)
1. **OAuth Provider Integration PRP**
   ```markdown
   # OAuth Provider Integration - PRP
   
   ## Problem Statement
   Add new OAuth2 provider (Google/Microsoft/etc.) to existing authentication system
   
   ## Implementation Pattern
   [Detailed step-by-step implementation using GitHub OAuth as template]
   
   ## Validation Loops
   [Testing approach for OAuth integration]
   ```

2. **JWT Token Management PRP**
   ```markdown
   # JWT Token Management - PRP
   
   ## Problem Statement
   Implement secure JWT token generation, validation, and refresh
   
   ## Security Patterns
   [JWT security best practices and implementation]
   
   ## Error Handling
   [Standardized error responses and recovery]
   ```

### Step 3: Implement Validation Loops (Week 2)
1. **Authentication Flow Testing**
   - Unit tests for OAuth callback handling
   - Integration tests for complete auth flows
   - Security testing for token validation

2. **Error Scenario Testing**
   - OAuth provider failures
   - Token expiration and refresh scenarios
   - Invalid authentication attempts

### Step 4: Team Validation and Feedback (Week 2)
1. **Developer Experience Testing**
   - Have team member implement auth feature using PRPs
   - Measure implementation time vs. previous approach
   - Gather feedback on PRP clarity and completeness

2. **Documentation Review**
   - Technical review of PRP accuracy
   - Usability review for new team members
   - Updates based on feedback

## Validation Criteria
- [ ] Complete OAuth flow documented with all error scenarios
- [ ] JWT patterns enable secure token management
- [ ] Authorization patterns support role-based access control
- [ ] New team member can implement auth features using PRPs
- [ ] 30%+ improvement in auth feature development time
- [ ] Comprehensive test coverage for all auth scenarios

## Impact Assessment
### Development Velocity
- **Estimated Improvement**: 40% faster for authentication-related features
- **Reduced Debugging**: Standardized error handling reduces investigation time
- **Faster Onboarding**: New developers productive on auth features in days vs. weeks

### Security Benefits
- **Standardized Security**: Consistent security patterns across all auth features
- **Error Handling**: Proper error handling reduces information leakage
- **Testing Coverage**: Comprehensive testing reduces security vulnerabilities

### Knowledge Capture
- **Tribal Knowledge**: Document authentication decisions and patterns
- **Best Practices**: Establish security best practices for team
- **Future Features**: Template for adding new authentication methods
```

#### Activity 1.3: Validate Pilot Implementation

Use the created PRPs to implement feature enhancements:

1. **Select Enhancement Opportunity**
   - Choose auth feature enhancement (e.g., add Google OAuth, improve error handling)
   - Use created PRP to guide implementation
   - Measure development time and developer experience

2. **Track Development Metrics**
   ```markdown
   # Pilot Validation Results
   
   ## Feature: [Enhancement Description]
   ## Developer: [Team Member Name]
   ## Timeline: [Start Date] to [End Date]
   
   ### Before Context Engineering
   - **Estimated Time**: [Previous estimate for similar work]
   - **Research Time**: [Time spent understanding existing code]
   - **Implementation Time**: [Actual coding time]
   - **Testing Time**: [Time spent on testing and validation]
   
   ### With Context Engineering PRPs
   - **Research Time**: [Reduced time due to PRP documentation]
   - **Implementation Time**: [Coding time with PRP guidance]
   - **Testing Time**: [Testing with PRP validation loops]
   - **Total Time**: [Overall implementation time]
   
   ### Developer Feedback
   - **Clarity**: [How clear were the PRPs?]
   - **Completeness**: [Were there gaps in documentation?]
   - **Efficiency**: [Did PRPs improve development speed?]
   - **Suggestions**: [Improvements for future PRPs]
   ```

## Step 3: Phase 2 Implementation - Core Feature Migration

### If executing Phase 2:

**Objective**: Scale successful patterns to additional high-priority features

#### Activity 2.1: Expand Feature Coverage

Based on Phase 1 success, migrate 3-5 additional features:

```bash
# Review Phase 1 results
Read "PRPs/migration/phase-1-results.md"

# Identify next features from analysis
Read "MIGRATION_ANALYSIS.md" | grep -A 15 "Migration Opportunities"
```

Create PRPs for additional high-priority features:
- Payment processing workflows
- Data import/export pipelines
- API rate limiting and caching
- Email template and notification systems
- Report generation workflows

#### Activity 2.2: Pattern Standardization

Document successful patterns from Phase 1:

```markdown
# PRP Quality Standards - [Project Name]

## Standard PRP Structure
[Based on successful Phase 1 PRPs]

## Required Components
1. **Problem Statement** - Clear problem definition
2. **Context Analysis** - Current implementation review
3. **Implementation Plan** - Step-by-step development guide
4. **Validation Loops** - Testing and quality criteria
5. **Impact Assessment** - Expected benefits and metrics

## Technology-Specific Patterns
### [React/Vue/Django/etc.] Components
[Standardized patterns for detected technology stack]

### Integration Patterns
[External service integration standards]

### Testing Patterns
[Standardized testing approaches]

## Quality Checklist
- [ ] Problem statement is clear and specific
- [ ] Implementation plan is actionable
- [ ] Validation criteria are measurable
- [ ] Code examples are complete and functional
- [ ] Error scenarios are documented
```

#### Activity 2.3: Team Training and Documentation

Create comprehensive training materials:

```markdown
# Context Engineering Training - [Project Name]

## Getting Started
### Understanding PRPs
[Introduction to Problem-Reasoning-Plan methodology]

### Using Project PRPs
[How to use existing PRPs for development]

### Creating New PRPs
[Guidelines for creating project-specific PRPs]

## Hands-On Exercises
### Exercise 1: Use Existing PRP
[Guided exercise using existing auth PRP]

### Exercise 2: Create Simple PRP
[Create PRP for simple feature enhancement]

### Exercise 3: Complex Feature PRP
[Create PRP for more complex functionality]

## Best Practices
[Project-specific best practices from Phase 1 experience]

## Common Pitfalls and Solutions
[Issues encountered in Phase 1 and their solutions]
```

## Step 4: Progress Tracking and Validation

For any phase execution, track progress and validate results:

### Progress Tracking Template
```markdown
# Migration Phase [X] Progress Report

## Week [X] Progress
### Completed Activities
- [x] Activity 1: [Description and completion date]
- [x] Activity 2: [Description and completion date]
- [ ] Activity 3: [In progress, expected completion]

### Metrics This Week
- **PRPs Created**: [Number] 
- **Features Migrated**: [Number]
- **Team Members Trained**: [Number]
- **Development Velocity**: [Improvement percentage]

### Challenges and Solutions
- **Challenge**: [Description]
  **Solution**: [How it was addressed]

### Next Week Plan
- [ ] Planned Activity 1
- [ ] Planned Activity 2
- [ ] Planned Activity 3

## Team Feedback
### What's Working Well
[Positive feedback from team members]

### Areas for Improvement  
[Constructive feedback and suggestions]

### Support Needs
[Additional support or resources needed]
```

### Validation Activities

1. **Quality Review**
   - Review all PRPs created in the phase
   - Validate accuracy against actual implementation
   - Ensure completeness and usability

2. **Team Adoption Assessment**
   - Survey team satisfaction with context engineering
   - Measure actual usage of PRPs and tools
   - Identify adoption barriers and solutions

3. **Metrics Collection**
   - Development velocity measurements
   - Code quality improvements
   - Developer onboarding time reductions

## Step 5: Phase Completion and Handoff

Complete the phase with proper documentation and preparation for next phase:

### Phase Completion Checklist
- [ ] All phase activities completed successfully
- [ ] Quality validation passed for all deliverables
- [ ] Team feedback collected and addressed
- [ ] Metrics documented and analyzed
- [ ] Lessons learned captured
- [ ] Next phase prepared and planned

### Phase Results Documentation

Create phase completion report in the proper location:

**IMPORTANT: Phase reports must be saved in PRPs/migration/ directory**

```bash
# Create migration directory if it doesn't exist
mkdir -p "PRPs/migration"

# Determine current phase number (extract from command or ask user)
phase_number="[X]"  # This should be determined from the --phase parameter or context

# Create the phase completion report
Write "PRPs/migration/phase-${phase_number}-completion-report.md" """
# Migration Phase ${phase_number} - Completion Report

## Phase Objectives Achievement
[Assessment of whether phase objectives were met]

## Deliverables Completed
[List of all deliverables with quality status]

## Metrics Achieved
[Actual metrics vs. target metrics]

## Team Adoption Status
[Current level of team adoption and engagement]

## Lessons Learned
[Key insights and learnings from the phase]

## Recommendations for Next Phase
[Adjustments and improvements for subsequent phases]

## Risks and Mitigation for Next Phase
[Identified risks and proposed mitigation strategies]
"""
```

**Expected Output**: Phase completion report created at `PRPs/migration/phase-[X]-completion-report.md`

## Validation Checklist

Before completing any migration phase, ensure:

- [ ] All planned activities completed with quality validation
- [ ] Team adoption is progressing according to expectations
- [ ] Metrics demonstrate improvement in development processes
- [ ] Documentation is complete and accurate
- [ ] Lessons learned are captured for future phases
- [ ] Next phase is prepared with necessary resources
- [ ] Risk mitigation strategies are in place
- [ ] Team satisfaction remains high throughout the process

Your phase execution should maintain high quality while ensuring team adoption and measurable improvement in development velocity and code quality.