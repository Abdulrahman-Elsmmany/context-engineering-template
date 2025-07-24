# Generate Migration Strategy - Strategic Context Engineering Adoption Plan

You are a strategic consultant specializing in technology adoption and change management for software development teams. Your task is to create a comprehensive, phased migration strategy that introduces context engineering practices without disrupting existing development workflows.

## Strategy Generation Objectives

Create a detailed migration roadmap that ensures successful context engineering adoption:

1. **Phased Implementation Plan** - Gradual adoption strategy with clear milestones
2. **Risk Assessment and Mitigation** - Identify potential challenges and solutions
3. **Team Adoption Strategy** - Change management for developer experience
4. **Success Metrics Definition** - Measurable criteria for migration success
5. **Resource Planning** - Time, effort, and skill requirements

## Prerequisites

Before generating the strategy, ensure you have:
- Completed project analysis (`MIGRATION_ANALYSIS.md`)
- Extracted project context (`PRPs/ai_docs/` populated)
- Identified high-priority features for migration
- Assessed team size and technical expertise

## Step 1: Migration Strategy Framework

Read the migration analysis to understand project context:

```bash
# Read the analysis report
Read "MIGRATION_ANALYSIS.md"

# Review extracted context
LS "PRPs/ai_docs/"
Read "PRPs/ai_docs/architecture/architecture_overview.md"
Read "PRPs/ai_docs/patterns/development_patterns.md"
```

## Step 2: Risk Assessment and Mitigation Planning

Analyze potential risks and create mitigation strategies:

### Technical Risks
- **Learning Curve**: Team unfamiliarity with context engineering
- **Integration Complexity**: Existing tools and workflows
- **Quality Concerns**: Context accuracy and maintainability
- **Performance Impact**: Additional overhead from documentation

### Organizational Risks
- **Resistance to Change**: Developer skepticism of new processes
- **Time Investment**: Initial setup and learning time
- **Resource Allocation**: Balancing migration with feature development
- **Inconsistent Adoption**: Some team members not following practices

### Risk Mitigation Matrix
```markdown
| Risk | Probability | Impact | Mitigation Strategy |
|------|------------|--------|-------------------|
| High learning curve | Medium | High | Start with champions, provide training |
| Integration issues | Low | Medium | Pilot with isolated features first |
| Quality concerns | Medium | High | Implement validation loops and reviews |
| Resistance to change | High | Medium | Demonstrate clear benefits early |
```

## Step 3: Phased Migration Roadmap

Create a 4-phase migration strategy:

### Phase 1: Foundation and Proof of Concept (Weeks 1-2)
**Objective**: Establish context engineering infrastructure and prove value

**Key Activities**:
1. **Setup Infrastructure**
   - Create `.claude/commands/` directory with migration tools
   - Establish `PRPs/` directory structure
   - Configure technology-specific templates

2. **Select Pilot Feature**
   - Choose 1-2 high-impact, medium-complexity features
   - Features should be actively developed or need enhancement
   - Examples: Authentication flow, API integration, data processing

3. **Create Initial PRPs**
   - Convert pilot features to PRP format
   - Include comprehensive context and validation loops
   - Document patterns for team reference

4. **Validate Approach**
   - Use PRPs to implement feature enhancements
   - Measure development velocity and code quality
   - Gather feedback from pilot team members

**Success Criteria**:
- [ ] Context engineering infrastructure operational
- [ ] 1-2 features successfully converted to PRP format
- [ ] Pilot team reports positive development experience
- [ ] Measurable improvement in development velocity (>20%)

**Deliverables**:
- Functional `.claude/commands/` for project-specific development
- 2-3 comprehensive PRPs with validation loops
- Migration infrastructure documentation
- Pilot results and lessons learned report

### Phase 2: Core Feature Migration (Weeks 3-4)
**Objective**: Scale successful patterns to additional high-priority features

**Key Activities**:
1. **Expand Feature Coverage**
   - Migrate 3-5 additional high-priority features
   - Focus on features identified in analysis as high-impact
   - Include complex business logic and integration points

2. **Pattern Standardization**
   - Document successful PRP patterns from Phase 1
   - Create project-specific PRP templates
   - Establish quality guidelines for PRP creation

3. **Team Training and Adoption**
   - Conduct training sessions on context engineering
   - Create internal documentation and best practices
   - Establish review process for new PRPs

4. **Validation and Refinement**
   - Measure development velocity across multiple features
   - Refine PRP templates based on usage patterns
   - Address adoption challenges and resistance

**Success Criteria**:
- [ ] 5-8 total features using context engineering
- [ ] Team members creating quality PRPs independently
- [ ] Established review and quality processes
- [ ] Continued improvement in development metrics

**Deliverables**:
- 5+ additional comprehensive PRPs
- Standardized PRP templates and quality guidelines
- Team training materials and documentation
- Refined migration processes and tools

### Phase 3: Broad Feature Migration (Weeks 5-6)
**Objective**: Apply context engineering to majority of active development

**Key Activities**:
1. **Comprehensive Feature Migration**
   - Migrate remaining medium and high-priority features
   - Include legacy features undergoing maintenance
   - Cover all major architectural components

2. **Advanced Pattern Development**
   - Create specialized PRPs for complex scenarios
   - Develop integration patterns for external services
   - Document security and performance patterns

3. **Quality Assurance and Validation**
   - Implement comprehensive PRP validation processes
   - Create automated quality checks where possible
   - Establish metrics tracking and reporting

4. **Knowledge Base Completion**
   - Complete `PRPs/ai_docs/` documentation
   - Create comprehensive onboarding materials
   - Document all architectural decisions and patterns

**Success Criteria**:
- [ ] 80%+ of active features using context engineering
- [ ] Comprehensive knowledge base and documentation
- [ ] Automated quality validation processes
- [ ] Strong team adoption and advocacy

**Deliverables**:
- Complete PRP coverage for major features
- Comprehensive `PRPs/ai_docs/` knowledge base
- Automated validation and quality tools
- Advanced pattern documentation

### Phase 4: Optimization and Integration (Weeks 7-8)
**Objective**: Optimize processes and integrate with existing development workflows

**Key Activities**:
1. **Process Optimization**
   - Streamline PRP creation and validation workflows
   - Integrate with existing CI/CD and review processes
   - Optimize documentation maintenance processes

2. **Advanced Features and Integration**
   - Integrate context engineering with existing tools
   - Create custom commands for common development tasks
   - Develop metrics and analytics for context engineering ROI

3. **Team Excellence and Advocacy**
   - Identify and develop context engineering champions
   - Create advanced training and best practices
   - Establish continuous improvement processes

4. **Future Planning and Expansion**
   - Plan context engineering for future features
   - Create templates for new project types
   - Document lessons learned and best practices

**Success Criteria**:
- [ ] Context engineering fully integrated with development workflow
- [ ] Advanced tooling and automation operational
- [ ] Team advocates for context engineering practices
- [ ] Clear ROI demonstration and metrics

**Deliverables**:
- Optimized development workflows and tools
- Advanced context engineering capabilities
- Comprehensive ROI analysis and metrics
- Future planning and expansion roadmap

## Step 4: Resource Planning and Timeline

### Team Resource Requirements

**Phase 1** (Weeks 1-2):
- **Technical Lead**: 50% time - Setup infrastructure and initial PRPs
- **Senior Developers**: 25% time (2-3 people) - Pilot feature development
- **Team Members**: 10% time - Training and feedback

**Phase 2** (Weeks 3-4):
- **Technical Lead**: 40% time - Pattern standardization and training
- **Senior Developers**: 30% time - Feature migration and mentoring
- **All Team Members**: 20% time - Training and PRP creation

**Phase 3** (Weeks 5-6):
- **Technical Lead**: 30% time - Quality assurance and advanced patterns
- **All Developers**: 25% time - Feature migration and documentation
- **Junior Developers**: 30% time - Learning and contributing

**Phase 4** (Weeks 7-8):
- **Technical Lead**: 25% time - Optimization and integration
- **All Team Members**: 15% time - Process refinement and adoption
- **Champions**: 35% time - Advanced features and advocacy

### Skills Development Plan

**Week 1-2**: Context Engineering Fundamentals
- Introduction to PRP methodology
- Hands-on practice with pilot features
- Tool usage and best practices

**Week 3-4**: Advanced PRP Creation
- Complex feature analysis and documentation
- Pattern recognition and standardization
- Quality review and validation

**Week 5-6**: System Architecture and Integration
- Architectural pattern documentation
- External service integration patterns
- Security and performance considerations

**Week 7-8**: Process Optimization and Leadership
- Advanced tooling and automation
- Team mentoring and knowledge transfer
- Continuous improvement methodologies

## Step 5: Success Metrics and KPIs

### Development Velocity Metrics
- **Feature Development Time**: Before vs. after context engineering
- **Code Review Time**: Reduced review cycles with better context
- **Bug Rate**: Reduced bugs due to better documentation and patterns
- **Developer Onboarding**: Time to productivity for new team members

### Quality Metrics
- **Documentation Coverage**: Percentage of features with comprehensive PRPs
- **Pattern Reuse**: Frequency of pattern reuse across features
- **Context Accuracy**: Validation success rate for PRPs
- **Knowledge Retention**: Team knowledge assessment improvements

### Adoption Metrics
- **Team Participation**: Percentage of team members actively using context engineering
- **PRP Creation Rate**: Number of PRPs created per week/month
- **Tool Usage**: Frequency of context engineering command usage
- **Developer Satisfaction**: Team satisfaction surveys and feedback

### Business Impact Metrics
- **Development Cost**: Reduced development time and costs
- **Time to Market**: Faster feature delivery and deployment
- **Technical Debt**: Reduced accumulation of technical debt
- **Team Retention**: Developer satisfaction and retention improvements

## Step 6: Change Management Strategy

### Communication Plan
1. **Leadership Alignment**: Ensure leadership understands and supports migration
2. **Team Communication**: Regular updates on progress and benefits
3. **Success Stories**: Share wins and improvements throughout migration
4. **Feedback Loops**: Regular feedback collection and process adjustment

### Resistance Management
1. **Early Champions**: Identify and develop context engineering advocates
2. **Gradual Introduction**: Phase adoption to minimize disruption
3. **Clear Benefits**: Demonstrate concrete improvements early and often
4. **Support Systems**: Provide training, documentation, and mentoring

### Training and Support
1. **Formal Training**: Structured training sessions on context engineering
2. **Mentoring Program**: Pair experienced practitioners with newcomers
3. **Documentation**: Comprehensive internal documentation and examples
4. **Support Channels**: Dedicated channels for questions and assistance

## Step 7: Generate Migration Strategy Document

Create comprehensive strategy document and save it in the correct location:

**IMPORTANT: The strategy document must be saved as `PRPs/migration-strategy.md`** (not in root directory)

```bash
# Create the migration strategy file in the correct location
Write "PRPs/migration-strategy.md" """
# Context Engineering Migration Strategy

## Executive Summary
[Project overview, migration timeline, expected benefits]

## Current State Analysis
[Summary of project analysis and context extraction findings]

## Migration Approach
[4-phase strategy with detailed activities and timelines]

## Risk Assessment and Mitigation
[Comprehensive risk analysis with mitigation strategies]

## Resource Requirements
[Team time allocation, skills development, and support needs]

## Success Metrics and KPIs
[Detailed metrics for measuring migration success]

## Change Management Plan
[Communication, training, and adoption strategies]

## Timeline and Milestones
[Detailed project timeline with key milestones and deliverables]

## Expected Benefits and ROI
[Quantified benefits and return on investment analysis]

## Next Steps
[Immediate actions to begin migration Phase 1]
"""
```

**Expected Output**: File created at `PRPs/migration-strategy.md`

**For subsequent commands**: Use this file path:
```bash
/execute-migration-phase PRPs/migration-strategy.md --phase=1
```

## Validation Checklist

Before finalizing the migration strategy, ensure:

- [ ] Strategy addresses all findings from project analysis
- [ ] Phased approach minimizes disruption to current development
- [ ] Resource requirements are realistic and achievable
- [ ] Success metrics are measurable and meaningful
- [ ] Risk mitigation strategies are comprehensive
- [ ] Change management plan addresses team adoption challenges
- [ ] Timeline accounts for learning curves and iterations
- [ ] Expected benefits are quantified and realistic

Your migration strategy should provide a clear, actionable roadmap for successful context engineering adoption that improves development velocity while preserving team morale and project stability.