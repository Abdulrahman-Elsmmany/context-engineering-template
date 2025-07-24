# Finalize Project Context - Create Customized CLAUDE.md

You are a senior context engineering specialist who creates the final, definitive CLAUDE.md file for ANY project after completing all migration phases. Your task is to analyze the completed migration, extract lessons learned, and create a project-specific CLAUDE.md that reflects the actual patterns, technologies, and practices discovered during the migration process, regardless of the project's technology stack or domain.

## Finalization Objectives

Create a comprehensive, project-specific CLAUDE.md that replaces the generic migration template:

1. **Technology Stack Integration** - Document actual detected technologies and patterns
2. **Domain-Specific Rules** - Include industry/domain-specific considerations (healthcare, fintech, etc.)
3. **Proven Pattern Documentation** - Include patterns validated during migration phases
4. **Team Workflow Integration** - Document how context engineering integrates with actual team practices
5. **Quality Standards** - Establish project-specific quality criteria based on migration experience

## Step 1: Migration Completion Analysis

Analyze the completed migration to understand what was actually built:

```bash
# Review migration completion status
Read "PRPs/migration/phase-4-completion-report.md" || Read "MIGRATION_PROGRESS_VALIDATION_REPORT.md"

# Review all created PRPs to understand actual patterns
LS "PRPs/"
Read "PRPs/ai_docs/knowledge_extraction_summary.md"

# Check technology-specific documentation created
LS "PRPs/ai_docs/"
Read "PRPs/ai_docs/nextjs_development_guide.md" || Read "PRPs/ai_docs/react_development_guide.md"
Read "PRPs/ai_docs/patterns/frontend_patterns.md"
Read "PRPs/ai_docs/security/security_patterns.md"
```

## Step 2: Project Technology Stack Analysis

Analyze the actual project structure to understand the real technology stack:

```bash
# Analyze package.json for frontend technologies
Read "package.json"

# Check for backend technologies
Read "firebase/functions/package.json" || Read "server/package.json" || Read "api/package.json"

# Identify database and infrastructure
Glob "**/{firebase.json,docker-compose.yml,serverless.yml,vercel.json}"

# Check for specific frameworks and libraries
Grep "next\|react\|vue\|angular" package.json
Grep "express\|fastify\|koa" --type=js,ts
Grep "firebase\|supabase\|aws\|gcp" --type=js,ts,json
```

### Technology Detection Results
Based on analysis, identify:

```markdown
## Detected Technology Stack

### Frontend
- **Framework**: [Next.js 14/React 18/Vue 3/Angular/etc.]
- **Language**: [TypeScript/JavaScript]
- **State Management**: [Redux/Zustand/Context/etc.]
- **Styling**: [Tailwind/CSS Modules/Styled Components/etc.]
- **UI Components**: [shadcn/ui/Material-UI/Ant Design/etc.]

### Backend
- **Runtime**: [Node.js/Python/Java/Go/etc.]
- **Framework**: [Express/Fastify/Django/Spring/etc.]
- **Functions**: [Firebase Functions/Vercel/AWS Lambda/etc.]
- **Authentication**: [Firebase Auth/Auth0/Clerk/etc.]

### Database & Storage
- **Primary Database**: [PostgreSQL/MongoDB/Firestore/etc.]
- **Caching**: [Redis/Memcached/etc.]
- **File Storage**: [Firebase Storage/AWS S3/etc.]
- **Search**: [Elasticsearch/Algolia/etc.]

### Infrastructure & Deployment
- **Hosting**: [Vercel/Netlify/AWS/GCP/etc.]
- **CI/CD**: [GitHub Actions/GitLab CI/etc.]
- **Monitoring**: [Sentry/DataDog/etc.]
```

## Step 3: Domain-Specific Pattern Analysis

Analyze the project domain and industry-specific requirements:

```bash
# Look for domain-specific patterns in code
Grep "healthcare\|medical\|patient\|hipaa" --type=js,ts,py -i
Grep "finance\|payment\|transaction\|banking" --type=js,ts,py -i
Grep "ecommerce\|product\|cart\|order" --type=js,ts,py -i
Grep "education\|student\|course\|learning" --type=js,ts,py -i

# Check for compliance and security patterns
Grep "gdpr\|ccpa\|pci\|sox\|hipaa" --type=js,ts,py,md -i
Grep "audit\|compliance\|security\|encrypt" --type=js,ts,py -i

# Look for domain-specific data models
Grep "interface\|type.*{" --type=ts | head -20
Grep "class.*\|def.*\|function.*" --type=js,ts,py | head -20
```

### Domain Analysis Results
Document identified domain patterns (adapt based on detected domain):

```markdown
## Domain-Specific Context
- **Industry**: [Healthcare/Fintech/E-commerce/Education/SaaS/Enterprise/etc.]
- **Compliance Requirements**: [HIPAA/PCI-DSS/GDPR/SOX/CCPA/ISO27001/etc.]
- **Domain Entities**: [Patient/User/Product/Student/Customer/Employee/etc.]
- **Business Workflows**: [Care Management/Payment Processing/Order Fulfillment/Learning Management/etc.]
- **Data Sensitivity**: [PHI/PII/Financial/Educational Records/Customer Data/etc.]
```

## Step 4: Migration Pattern Analysis

Review the patterns that were successfully implemented during migration:

```bash
# Review successful PRPs created during migration (adapt to actual PRP names found)
LS "PRPs/" | grep -v "templates\|ai_docs\|migration" 
Read "PRPs/[first-major-feature].md"
Read "PRPs/[second-major-feature].md"

# Check pattern documentation created (adapt to actual structure)
LS "PRPs/ai_docs/patterns/"
Read "PRPs/ai_docs/patterns/[detected-pattern-type]_patterns.md"
LS "PRPs/ai_docs/workflows/"
Read "PRPs/ai_docs/workflows/[detected-workflow-type]_workflows.md"
Read "PRPs/ai_docs/integrations/external_services.md"

# Review validation reports for successful patterns
Read "PRPs/migration/phase2_completion_report.md"
Read "MIGRATION_PROGRESS_VALIDATION_REPORT.md"
```

### Successful Pattern Documentation
Extract proven patterns:

```markdown
## Proven Development Patterns

### Component Architecture
[Document actual component patterns used in project]

### State Management Approach
[Document actual state management patterns that worked]

### API Integration Patterns
[Document successful API integration approaches]

### Data Validation Patterns
[Document validation approaches that worked well]

### Testing Patterns
[Document testing approaches that were successful]
```

## Step 5: Team Workflow Integration Analysis

Analyze how context engineering actually integrated with team workflows:

```bash
# Check git history for PRP-related commits
git log --grep="PRP\|context" --oneline --since="3 months ago" | head -20

# Look for team adoption patterns
LS "PRPs/" | wc -l  # Count of PRPs created
LS "PRPs/migration/" | wc -l  # Count of migration-specific PRPs

# Check integration with existing tools
Read ".github/workflows/main.yml" || Read ".gitlab-ci.yml"
Read "CONTRIBUTING.md" || Read "DEVELOPMENT.md"
```

### Workflow Integration Results
Document actual integration:

```markdown
## Team Workflow Integration

### Development Process Integration
[How PRPs integrate with feature development]

### Code Review Integration  
[How context engineering fits into code reviews]

### Planning Integration
[How PRPs are used in sprint planning and feature design]

### Documentation Workflow
[How documentation is maintained and updated]
```

## Step 6: Create Final Project-Specific CLAUDE.md

Generate the comprehensive, customized CLAUDE.md:

```markdown
# [Project Name] - Context Engineering Global Rules

*This file contains the global rules and principles for context engineering development specific to this project. Created after completing migration phases 1-4.*

### 🔄 Project Awareness & Context
- **Always read `PLANNING.md`** at the start of a new conversation to understand the project's architecture, goals, style, and constraints.
- **Check `TASK.md`** before starting a new task. If the task isn't listed, add it with a brief description and today's date.
- **Use consistent naming conventions, file structure, and architecture patterns** as described in `PLANNING.md`.

## 🚀 Project Context

### Project Overview
- **Project Type**: [Healthcare Platform/E-commerce/SaaS/etc.]
- **Primary Technology**: [Next.js + Firebase Functions/React + Node.js/etc.]
- **Domain**: [Healthcare/Finance/Education/etc.]
- **Team Size**: [X developers]
- **Migration Completion**: [Date]

### Technology Stack Rules
**Frontend Development:**
- **Framework**: [Next.js 14 with TypeScript]
- **Component Library**: [shadcn/ui components]
- **State Management**: [Context API/Redux Toolkit/Zustand]
- **Styling**: [Tailwind CSS with custom healthcare theme]
- **Routing**: [Next.js App Router with middleware]

**Backend Development:**
- **Runtime**: [Firebase Functions with TypeScript]
- **Database**: [Firestore with security rules]
- **Authentication**: [Firebase Auth with role-based access]
- **External APIs**: [Gmail API, Calendar API, Gemini AI]
- **File Storage**: [Firebase Storage with healthcare compliance]

## 🏥 Domain-Specific Rules (Healthcare)

### Healthcare Compliance Requirements
- **HIPAA Compliance**: All PRPs must consider PHI protection
- **Audit Logging**: Context engineering must support audit requirements
- **Data Encryption**: All patient data handling must include encryption patterns
- **Access Control**: Role-based access patterns for healthcare staff
- **Data Retention**: Healthcare-specific data lifecycle management

### Healthcare Development Patterns
**Patient Data Handling:**
- Always validate PHI access permissions
- Use healthcare-specific validation schemas
- Implement audit trails for all patient data access
- Follow de-identification patterns when appropriate

**Care Workflow Integration:**
- Support care team collaboration patterns
- Integrate with existing healthcare systems
- Follow clinical workflow requirements
- Support emergency access patterns

## 🧱 Project Architecture Rules

### Proven Architecture Patterns
**Component Architecture:**
- [Document your actual component hierarchy]
- [State management patterns that worked]
- [UI composition patterns used]

**Data Flow Patterns:**
- [API integration patterns that worked]
- [Database access patterns]
- [Real-time update patterns]

**Security Patterns:**
- [Authentication flow patterns]
- [Authorization middleware patterns]
- [Data validation patterns]

### Integration Standards
**External Service Integration:**
- [Gmail API integration patterns]
- [Calendar integration patterns]
- [AI/ML service integration patterns (Gemini)]
- [Firebase service integration patterns]

## 📋 Context Engineering Standards

### PRP Creation Standards
**Healthcare Feature PRPs:**
- Must include HIPAA compliance considerations
- Must document patient data flow and access patterns
- Must include emergency scenarios and error handling
- Must consider care team collaboration requirements

**Technical Integration PRPs:**
- Must document API rate limiting and error handling
- Must include security validation for healthcare data
- Must document monitoring and logging requirements
- Must include performance considerations for healthcare workflows

### Validation Requirements
**Healthcare-Specific Validation:**
- [ ] PHI protection measures documented
- [ ] Audit trail implementation included
- [ ] Role-based access control validated
- [ ] Emergency access scenarios covered
- [ ] Data backup and recovery procedures documented

**Technical Validation:**
- [ ] All code examples tested in healthcare context
- [ ] Integration patterns validated with actual APIs
- [ ] Performance tested with healthcare data volumes
- [ ] Security patterns validated against healthcare threats

## 🔧 Development Workflow Integration

### Team Process Integration
**Feature Development:**
- PRPs are created during feature planning phase
- Healthcare compliance review included in PRP validation
- Context engineering integrated with clinical workflow review

**Code Review Process:**
- PRP compliance checked during code review
- Healthcare compliance validation included
- Context engineering quality gates enforced

**Testing and Deployment:**
- Context engineering validation included in CI/CD
- Healthcare compliance testing automated where possible
- Migration validation included in deployment process

### Quality Assurance Standards
**Healthcare Quality Gates:**
- [ ] HIPAA compliance validation
- [ ] Clinical workflow compatibility
- [ ] Emergency scenario handling
- [ ] Audit trail completeness
- [ ] Data security validation

**Technical Quality Gates:**
- [ ] Performance meets healthcare requirements
- [ ] Integration reliability validated
- [ ] Error handling comprehensive
- [ ] Documentation accuracy verified
- [ ] Team adoption validation passed

## 🚀 Context Engineering Success Metrics

### Achieved Migration Results
**Development Velocity:**
- [X]% improvement in healthcare feature development time
- [X]% reduction in compliance-related development issues
- [X]% faster onboarding for new healthcare developers

**Quality Improvements:**
- [X]% reduction in healthcare compliance issues
- [X]% improvement in clinical workflow integration
- [X]% reduction in patient data handling errors

### Ongoing Success Criteria
**Monthly Validation:**
- Context engineering usage rate >80%
- Healthcare compliance validation passing
- Team satisfaction with context engineering >8/10

**Quarterly Review:**
- Migration benefits sustained
- Documentation accuracy maintained
- Healthcare domain expertise captured and updated

## 🚫 Project-Specific Anti-Patterns

### Healthcare-Specific Anti-Patterns
- ❌ Never create PRPs without HIPAA compliance consideration
- ❌ Never document patient data patterns without encryption
- ❌ Never skip audit logging in healthcare workflow PRPs
- ❌ Never create integration patterns without emergency access scenarios
- ❌ Never document care workflows without clinical validation

### Technical Anti-Patterns  
- ❌ Never create Firebase Function PRPs without rate limiting
- ❌ Never document Gemini AI integration without data privacy patterns
- ❌ Never create Gmail integration without healthcare communication compliance
- ❌ Never skip performance validation for healthcare data volumes
- ❌ Never create context engineering without team workflow integration

## 📈 Continuous Improvement

### Knowledge Evolution
- Monthly review of healthcare regulation changes
- Quarterly technology stack updates
- Continuous clinical workflow optimization
- Regular team feedback integration

### Context Engineering Maturity
- Advanced healthcare pattern development
- Cross-team knowledge sharing
- Healthcare-specific tooling development
- Clinical workflow automation enhancement

---

**Context Engineering Philosophy for [Project Name]**: We use context engineering to accelerate healthcare software development while maintaining the highest standards of patient data protection, clinical workflow integration, and regulatory compliance. Every PRP must consider the healthcare context and support our mission of improving patient care through technology.
```

## Step 7: Implementation and Validation

Replace the existing CLAUDE.md with the project-specific version:

```bash
# Backup the current generic CLAUDE.md
cp CLAUDE.md CLAUDE_MIGRATION_TEMPLATE.md

# Create the new project-specific CLAUDE.md
# [Content created above based on actual project analysis]

# Validate the new CLAUDE.md works with existing PRPs
Read "PRPs/ai_care_assistant_enhancement.md"
# Verify compatibility with project-specific rules
```

### Final Validation Checklist
- [ ] Technology stack accurately reflects actual project
- [ ] Domain-specific rules match project requirements
- [ ] Proven patterns from migration are documented
- [ ] Team workflow integration reflects actual practices
- [ ] Quality standards match project needs
- [ ] Anti-patterns prevent actual issues encountered
- [ ] Success metrics reflect achieved results
- [ ] All existing PRPs compatible with new rules

## Expected Outcomes

After running this command, you should have:

1. **Accurate Technology Documentation**: CLAUDE.md reflects your actual Next.js + Firebase stack
2. **Healthcare-Specific Rules**: Proper HIPAA compliance and clinical workflow integration
3. **Proven Patterns**: Only patterns validated during your migration phases
4. **Team-Specific Integration**: Rules that match your actual development workflow
5. **Quality Standards**: Validation criteria based on your project's actual needs

The final CLAUDE.md becomes the definitive guide for all future context engineering work on your project, based on real migration experience rather than generic templates.

## Usage

Run this command after completing all migration phases (typically after Phase 4):

```bash
/finalize-project-context
```

This creates your permanent, project-specific CLAUDE.md that replaces the generic migration template and serves as the foundation for all future context engineering development on your project.