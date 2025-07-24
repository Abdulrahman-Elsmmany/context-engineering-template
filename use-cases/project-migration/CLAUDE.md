# Project Migration - Global Rules for Context Engineering Migration

This file contains the global rules and principles that apply to ALL project migration work. These rules are specialized for analyzing existing codebases and implementing context engineering practices without disrupting current development.

## 🔄 Migration Core Principles

**IMPORTANT: These principles apply to ALL project migration work:**

### Migration Development Workflow
- **Always start with comprehensive analysis** - Understand the existing project completely before making changes
- **Preserve existing functionality** - Never modify existing code during initial migration phases
- **Use incremental adoption** - Implement context engineering gradually alongside existing practices
- **Follow validation loops** - Each migration phase must include quality validation
- **Document everything** - Capture all analysis findings and migration decisions

### Analysis Methodology for Existing Projects
- **Technology stack detection** - Automatically identify frameworks, languages, and dependencies
- **Architectural pattern extraction** - Document existing design patterns and conventions
- **Knowledge capture** - Extract tribal knowledge from documentation and code comments
- **Dependency mapping** - Map all external services, APIs, and integrations
- **Complexity assessment** - Identify technical debt and migration priorities

## 📚 Project Awareness & Migration Context

- **Respect existing project structure** - Work within current organizational patterns
- **Identify existing documentation** - Catalog README files, docs/, wiki content, and code comments
- **Map current development workflow** - Understand existing git practices, CI/CD, and deployment patterns
- **Preserve team conventions** - Maintain existing naming conventions and coding standards
- **Document integration points** - Identify all external dependencies and service connections

## 🧱 Migration Structure & Modularity

- **Create parallel context structure** - Add context engineering alongside existing code
- **Organize migration artifacts** in clearly separated directories:
  - `MIGRATION_ANALYSIS.md` - Complete project assessment and roadmap
  - `.claude/commands/` - Migration-specific analysis and implementation commands
  - `PRPs/migration/` - Migration-specific Problem-Reasoning-Plan documents
  - `PRPs/ai_docs/` - Extracted knowledge base from existing project
  - `examples/migration-examples/` - Real-world migration patterns and success stories
- **Use non-invasive integration** - Add context engineering without modifying existing files
- **Follow incremental adoption** - Implement context engineering features gradually

## 🔍 Migration Analysis Standards

### Technology Detection Patterns
- **Package manager analysis** - Scan package.json, requirements.txt, Cargo.toml, go.mod
- **Framework identification** - Detect React, Vue, Angular, Django, Rails, Spring, etc.
- **Database integration** - Identify SQL/NoSQL databases, ORMs, and connection patterns
- **API patterns** - Map REST APIs, GraphQL, WebSocket, and RPC integrations
- **Testing frameworks** - Document existing test patterns and coverage

### Knowledge Extraction Standards
- **Documentation scanning** - Parse README, docs/, wiki, and inline documentation
- **Code pattern analysis** - Identify reusable architectural patterns and conventions
- **Business logic mapping** - Extract complex workflows and domain logic
- **Integration documentation** - Capture external service integration patterns
- **Configuration management** - Document environment variables, config files, and secrets

### Dependency Mapping Standards
- **External services** - Map APIs, databases, message queues, caching layers
- **Authentication systems** - Document OAuth, SAML, JWT, and session management
- **Deployment infrastructure** - Identify CI/CD, containers, cloud services, CDNs
- **Monitoring and logging** - Map existing observability and error tracking
- **Security patterns** - Document existing security practices and compliance requirements

## 🚀 Migration Implementation Standards

### Analysis Phase
```python
# Comprehensive project analysis following established patterns
from migration.analyzers import (
    TechnologyStackAnalyzer,
    DependencyMapper,
    DocumentationExtractor,
    ArchitectureAnalyzer
)

# Analyze technology stack
tech_analyzer = TechnologyStackAnalyzer(project_path)
tech_stack = tech_analyzer.analyze()

# Map dependencies and integrations
dep_mapper = DependencyMapper(project_path)
dependencies = dep_mapper.map_dependencies()

# Extract existing documentation
doc_extractor = DocumentationExtractor(project_path)
knowledge_base = doc_extractor.extract_knowledge()

# Generate migration strategy
migration_strategy = generate_migration_roadmap(
    tech_stack, dependencies, knowledge_base
)
```

### Context Generation Standards
- **PRP generation from features** - Convert existing features into Problem-Reasoning-Plan format
- **Knowledge base creation** - Structured documentation in `PRPs/ai_docs/`
- **Template specialization** - Technology-specific PRP templates based on detected stack
- **Integration documentation** - Comprehensive external service integration patterns

### Validation Standards for Migration
- **Functionality preservation** - Ensure existing features remain unchanged
- **Context accuracy** - Validate extracted knowledge against actual codebase behavior
- **Team adoption metrics** - Measure development velocity improvements
- **Quality gates** - Comprehensive validation at each migration phase

## 📎 Migration Development Standards

### Project Analysis Workflow
```bash
# Step 1: Comprehensive analysis
/analyze-existing-project

# Step 2: Knowledge extraction
/extract-project-context

# Step 3: Migration strategy (creates PRPs/migration-strategy.md)
/generate-migration-strategy MIGRATION_ANALYSIS.md

# Step 4: Incremental implementation (4 phases)
/execute-migration-phase PRPs/migration-strategy.md --phase=1
/execute-migration-phase PRPs/migration-strategy.md --phase=2
/execute-migration-phase PRPs/migration-strategy.md --phase=3
/execute-migration-phase PRPs/migration-strategy.md --phase=4

# Step 5: Validation after each phase
/validate-migration-progress

# Step 6: Create project-specific CLAUDE.md (after all phases)
/finalize-project-context

# Step 7: Clean up temporary migration files (final step)
/cleanup-migration-artifacts
```

### Technology-Specific Migration Patterns
- **Web Frontend**: Component analysis, state management patterns, routing documentation
- **Backend Services**: API documentation, database schema mapping, middleware patterns
- **Microservices**: Service mesh documentation, communication patterns, deployment strategies
- **Mobile Apps**: Platform-specific patterns, native integration documentation
- **Desktop Apps**: Cross-platform patterns, native system integration

### Migration Security Standards
- **Preserve existing security** - Never modify existing authentication or authorization
- **Document security patterns** - Capture existing security practices comprehensively
- **Secret management** - Document existing environment variable and secret patterns
- **Compliance mapping** - Identify existing compliance requirements and patterns

## ✅ Migration Task Management

- **Break migration into phases** with clear validation criteria for each phase
- **Mark analysis tasks complete** after thorough project assessment
- **Update migration progress** in real-time as context engineering is implemented
- **Validate each phase** before proceeding to ensure quality and team adoption

## 🔧 Migration Tool Usage Standards

### Available Migration Commands
- **`/analyze-existing-project`** - Comprehensive codebase analysis and technology detection
- **`/extract-project-context`** - Knowledge extraction from existing docs and code
- **`/generate-migration-strategy`** - Strategic planning (creates PRPs/migration-strategy.md)
- **`/execute-migration-phase`** - Incremental implementation by phase
- **`/validate-migration-progress`** - Quality validation and adoption assessment
- **`/finalize-project-context`** - Create project-specific CLAUDE.md (post-migration)
- **`/cleanup-migration-artifacts`** - Remove temporary files after completion

### File Creation Standards
- **Migration analysis**: Creates `MIGRATION_ANALYSIS.md` in root directory
- **Migration strategy**: Creates `PRPs/migration-strategy.md` (NOT in root)
- **Validation reports**: Creates in `PRPs/migration/validation-reports/`
- **Phase reports**: Creates in `PRPs/migration/phase-X-completion-report.md`
- **Final CLAUDE.md**: Replaces generic template with project-specific version

### Command Usage Patterns
- **Use extensive analysis commands** for project discovery and knowledge extraction
- **Follow migration-specific workflows** for gradual context engineering adoption
- **Use validation loops** to ensure migration quality and team satisfaction
- **Document migration patterns** for future project migrations

## 🧪 Migration Testing & Validation

- **Functionality regression testing** - Ensure existing features work unchanged
- **Context accuracy validation** - Verify extracted knowledge matches actual behavior
- **Team adoption testing** - Validate context engineering improves development velocity
- **Integration testing** - Ensure new context engineering integrates with existing workflows

## 🚫 Migration Anti-Patterns to Always Avoid

- ❌ Don't modify existing code during initial migration - preserve functionality completely
- ❌ Don't skip comprehensive analysis - understand the project fully before implementation
- ❌ Don't rush migration phases - allow time for team adoption and refinement
- ❌ Don't ignore existing patterns - respect and document current conventions
- ❌ Don't create generic migration - specialize for detected technology stack
- ❌ Don't skip validation - every migration phase must include quality gates
- ❌ Don't forget team adoption - migration success depends on developer experience

## 🎯 Migration Success Criteria

### Immediate Success (Week 1)
- Complete project analysis with technology stack identification
- Extracted knowledge base in structured format
- Strategic migration roadmap with phased implementation plan

### Short-term Success (Month 1)
- Context engineering applied to highest-impact features
- Team members using context engineering for new feature development
- Measurable improvement in development velocity for migrated components

### Long-term Success (Quarter 1)
- Significant portion of development using context engineering practices
- Documented improvement in team productivity and code quality
- Established patterns for ongoing context engineering adoption

These global rules ensure successful migration of existing projects to context engineering practices while preserving functionality and enabling gradual team adoption.