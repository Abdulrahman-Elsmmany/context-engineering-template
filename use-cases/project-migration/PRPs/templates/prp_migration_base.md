# [Feature Name] - Migration PRP Template

*Use this template for migrating existing project features to context engineering practices*

## Problem Statement

### Current State Analysis
**What exists today:**
- [Describe the current implementation of this feature]
- [Current pain points and challenges]
- [Technical debt or maintenance issues]
- [Developer experience problems]

**Why Context Engineering is Needed:**
- [Specific problems context engineering will solve]
- [Expected improvements in development velocity]
- [Knowledge gaps that need to be filled]
- [Pattern standardization opportunities]

### Target State Vision
**What we want to achieve:**
- [Clear, standardized patterns for this feature type]
- [Comprehensive documentation enabling rapid development]
- [Reduced onboarding time for new developers]
- [Measurable improvement in development efficiency]

## Current Implementation Analysis

### Technology Stack Assessment
**Framework/Technology:** [React/Vue/Django/Spring/etc.]
**Dependencies:** [List major dependencies and versions]
**Architecture Pattern:** [MVC/Component-based/Microservices/etc.]

### Code Structure Analysis
```
[Current directory structure]
src/
├── [feature-directory]/
│   ├── [component-files]
│   ├── [business-logic]
│   └── [configuration]
```

### Existing Patterns and Conventions
**Development Patterns:**
- [Current coding patterns and conventions]
- [State management approach]
- [Error handling patterns]
- [Testing approaches]

**Integration Patterns:**
- [External API integration methods]
- [Database interaction patterns]
- [Authentication/authorization approaches]
- [Configuration management]

### Knowledge Gaps and Pain Points
**Documentation Gaps:**
- [Areas lacking documentation]
- [Tribal knowledge not captured]
- [Complex logic without explanation]

**Development Friction:**
- [Time-consuming development tasks]
- [Frequent bugs or issues]
- [Inconsistent implementation approaches]
- [Onboarding difficulties]

## Context Engineering Strategy

### PRP Structure Design
**Primary PRP:** [Main feature PRP name and scope]
**Supporting PRPs:** [Related PRPs that may be needed]
**Integration PRPs:** [PRPs for external service integration]

### Knowledge Documentation Plan
**Architecture Documentation:**
- [System design and component relationships]
- [Data flow and state management]
- [Security and performance considerations]

**Pattern Documentation:**
- [Reusable development patterns]
- [Code templates and examples]
- [Testing and validation approaches]

**Integration Documentation:**
- [External service integration patterns]
- [Configuration and environment setup]
- [Error handling and recovery patterns]

### Success Criteria for Context Engineering
**Developer Experience:**
- [ ] New developer can implement feature enhancement in [X] days vs [Y] days
- [ ] 90%+ of implementation questions answered by documentation
- [ ] Consistent patterns across all instances of this feature type

**Development Velocity:**
- [ ] [X]% reduction in development time for similar features
- [ ] [X]% reduction in code review cycles
- [ ] [X]% reduction in bug rate for new implementations

## Implementation Plan

### Phase 1: Analysis and Documentation (Week 1)
**Step 1.1: Deep Code Analysis**
- [ ] Map all components and their responsibilities
- [ ] Document data flow and state management
- [ ] Identify all external dependencies and integrations
- [ ] Catalog existing tests and coverage

**Step 1.2: Pattern Extraction**
- [ ] Identify reusable patterns in current implementation
- [ ] Document business logic and validation rules
- [ ] Extract configuration and environment patterns
- [ ] Map error scenarios and handling approaches

**Step 1.3: Knowledge Capture**
- [ ] Interview developers familiar with this feature
- [ ] Document architectural decisions and trade-offs
- [ ] Capture troubleshooting knowledge and common issues
- [ ] Identify areas needing standardization

### Phase 2: PRP Creation (Week 1-2)
**Step 2.1: Primary PRP Development**
```markdown
# [Feature Name] Implementation PRP

## Problem Statement
[Specific implementation problem this PRP solves]

## Technical Context
[Technology stack, dependencies, constraints]

## Implementation Approach
[Step-by-step implementation guide]

### Step 1: [Foundation Setup]
[Detailed implementation steps with code examples]

### Step 2: [Core Logic Implementation]
[Business logic implementation with patterns]

### Step 3: [Integration and Configuration]
[External service integration and setup]

### Step 4: [Testing and Validation]
[Comprehensive testing approach]

## Validation Loops
- [ ] [Specific validation criteria]
- [ ] [Quality checkpoints]
- [ ] [Integration testing requirements]

## Common Pitfalls and Solutions
[Known issues and how to avoid them]
```

**Step 2.2: Supporting Documentation**
- [ ] Create `PRPs/ai_docs/[feature-category]/` documentation
- [ ] Document integration patterns in `PRPs/ai_docs/integrations/`
- [ ] Add patterns to `PRPs/ai_docs/patterns/`
- [ ] Include security considerations in `PRPs/ai_docs/security/`

**Step 2.3: Template and Example Creation**
- [ ] Create reusable code templates
- [ ] Develop working examples for common scenarios
- [ ] Document configuration templates
- [ ] Create testing templates and fixtures

### Phase 3: Validation and Refinement (Week 2)
**Step 3.1: Implementation Testing**
- [ ] Use PRP to implement feature enhancement or bug fix
- [ ] Track development time and developer experience
- [ ] Identify gaps or unclear areas in documentation
- [ ] Validate all code examples and templates

**Step 3.2: Peer Review and Feedback**
- [ ] Technical review by senior developers
- [ ] Usability review by team members unfamiliar with feature
- [ ] Accuracy validation against actual codebase
- [ ] Feedback integration and documentation updates

**Step 3.3: Quality Assurance**
- [ ] Comprehensive validation against quality checklist
- [ ] Cross-reference validation with existing implementation
- [ ] Performance impact assessment
- [ ] Security review for documented patterns

### Phase 4: Team Adoption and Integration (Week 2-3)
**Step 4.1: Team Training**
- [ ] Present PRP to development team
- [ ] Conduct hands-on training session
- [ ] Address questions and concerns
- [ ] Gather adoption feedback

**Step 4.2: Process Integration**
- [ ] Integrate PRP usage into development workflow
- [ ] Update code review checklist to include PRP compliance
- [ ] Add PRP creation guidelines to team documentation
- [ ] Establish maintenance and update procedures

**Step 4.3: Success Measurement**
- [ ] Implement metrics tracking for development velocity
- [ ] Monitor actual usage of PRP by team members
- [ ] Track developer satisfaction and feedback
- [ ] Measure impact on code quality and consistency

## Validation Loops and Quality Gates

### Technical Validation
- [ ] **Code Examples Functional**: All code snippets compile and run correctly
- [ ] **Pattern Accuracy**: Documented patterns match actual implementation
- [ ] **Dependency Correctness**: All imports and dependencies are accurate
- [ ] **Configuration Validity**: Environment and configuration examples work
- [ ] **Security Compliance**: Security patterns follow best practices

### Usability Validation
- [ ] **Developer Experience**: New team member can follow PRP successfully
- [ ] **Completeness**: All necessary information included for implementation
- [ ] **Clarity**: Instructions are clear and unambiguous
- [ ] **Efficiency**: PRP demonstrably reduces development time
- [ ] **Maintainability**: Documentation can be easily updated as code evolves

### Adoption Validation
- [ ] **Team Acceptance**: Positive feedback from development team
- [ ] **Usage Metrics**: PRP actively used for feature development
- [ ] **Quality Improvement**: Measurable improvement in code quality
- [ ] **Velocity Improvement**: Demonstrable increase in development speed
- [ ] **Knowledge Transfer**: Effective knowledge transfer to new team members

## Expected Impact and Benefits

### Development Velocity Improvements
**Time Savings:**
- **Research Time**: [X]% reduction in time spent understanding existing code
- **Implementation Time**: [X]% reduction in actual coding time
- **Testing Time**: [X]% reduction in testing and validation time
- **Review Time**: [X]% reduction in code review cycles

**Quality Improvements:**
- **Bug Reduction**: [X]% fewer bugs in new implementations
- **Consistency**: Standardized patterns across all implementations
- **Documentation**: Comprehensive documentation for all aspects
- **Maintainability**: Easier maintenance and updates

### Knowledge and Team Benefits
**Knowledge Capture:**
- **Tribal Knowledge**: Critical knowledge documented and accessible
- **Best Practices**: Established patterns prevent common mistakes
- **Decision Documentation**: Architectural decisions and rationale captured
- **Troubleshooting**: Common issues and solutions documented

**Team Development:**
- **Onboarding**: Faster onboarding for new team members
- **Cross-Training**: Easier knowledge transfer between team members
- **Consistency**: Standardized approaches across the team
- **Confidence**: Higher confidence in implementing similar features

## Risk Assessment and Mitigation

### Implementation Risks
**Technical Risks:**
- **Risk**: [Potential technical challenge]
  **Probability**: [High/Medium/Low]
  **Impact**: [High/Medium/Low]
  **Mitigation**: [Specific mitigation strategy]

**Adoption Risks:**
- **Risk**: Team resistance to new documentation processes
  **Probability**: Medium
  **Impact**: High
  **Mitigation**: Demonstrate clear benefits early, involve team in creation process

**Quality Risks:**
- **Risk**: Documentation becomes outdated as code evolves
  **Probability**: High
  **Impact**: Medium
  **Mitigation**: Establish update procedures, integrate with development workflow

### Success Monitoring
**Key Performance Indicators:**
- Development time for similar features
- Code review feedback quality
- Bug rate for new implementations
- Team satisfaction scores
- Documentation usage metrics

**Review Schedule:**
- **Weekly**: During initial implementation (first month)
- **Monthly**: During first quarter after implementation
- **Quarterly**: Long-term maintenance and updates

## Next Steps and Maintenance

### Immediate Actions
1. **[Action Item]**: [Specific next step with owner and timeline]
2. **[Action Item]**: [Specific next step with owner and timeline]
3. **[Action Item]**: [Specific next step with owner and timeline]

### Long-term Maintenance
**Documentation Updates:**
- Regular review and update schedule
- Process for incorporating new patterns and learnings
- Version control and change tracking

**Continuous Improvement:**
- Regular feedback collection from team members
- Metrics analysis and optimization
- Pattern evolution and refinement

**Knowledge Expansion:**
- Application to similar features and use cases
- Creation of related PRPs and documentation
- Knowledge sharing with other teams or projects

---

**Migration Success Definition**: This feature migration is successful when team members can independently implement enhancements or similar features using the PRP with demonstrably improved velocity, quality, and confidence compared to the pre-migration approach.