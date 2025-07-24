#!/usr/bin/env python3
"""
Project Migration Template Copy Script

This script copies the project migration template to an existing project directory,
preserving the existing codebase while adding context engineering capabilities.

Usage:
    python copy_template.py /path/to/existing/project
"""

import os
import sys
import shutil
import argparse
import re
from pathlib import Path

def load_gitignore_patterns():
    """Load .gitignore patterns to avoid copying build artifacts and dependencies."""
    gitignore_patterns = [
        'node_modules/',
        '__pycache__/',
        '*.pyc',
        '.env',
        '.env.local',
        '.env.*.local',
        'dist/',
        'build/',
        '.next/',
        '.nuxt/',
        'target/',
        'bin/',
        'obj/',
        '*.log',
        '.DS_Store',
        'Thumbs.db',
        '.vscode/',
        '.idea/',
        '*.swp',
        '*.swo',
        '*.tmp',
        '.git/',
        '.svn/',
        '.hg/',
        'coverage/',
        '.coverage',
        '.nyc_output/',
        'npm-debug.log*',
        'yarn-debug.log*',
        'yarn-error.log*',
    ]
    return gitignore_patterns

def should_ignore(path, ignore_patterns):
    """Check if a path should be ignored based on gitignore patterns."""
    path_str = str(path)
    for pattern in ignore_patterns:
        if pattern.endswith('/'):
            # Directory pattern
            if f"/{pattern}" in f"/{path_str}/" or path_str.endswith(pattern[:-1]):
                return True
        else:
            # File pattern
            if path_str.endswith(pattern) or pattern in path_str:
                return True
    return False

def copy_template_files(source_dir, target_dir, ignore_patterns):
    """Copy template files to target directory, respecting ignore patterns."""
    source_path = Path(source_dir)
    target_path = Path(target_dir)
    
    # Ensure target directory exists
    target_path.mkdir(parents=True, exist_ok=True)
    
    copied_files = []
    skipped_files = []
    
    for item in source_path.rglob('*'):
        if item.is_file():
            # Calculate relative path from source
            relative_path = item.relative_to(source_path)
            
            # Check if should be ignored
            if should_ignore(relative_path, ignore_patterns):
                skipped_files.append(str(relative_path))
                continue
            
            # Calculate target path
            target_file = target_path / relative_path
            
            # Special handling for README.md - rename to README_TEMPLATE.md
            if relative_path.name == 'README.md':
                target_file = target_file.parent / 'README_TEMPLATE.md'
            
            # Create target directory if it doesn't exist
            target_file.parent.mkdir(parents=True, exist_ok=True)
            
            # Copy file
            try:
                shutil.copy2(item, target_file)
                copied_files.append(str(relative_path))
                print(f"[OK] Copied: {relative_path}")
            except Exception as e:
                print(f"[ERR] Error copying {relative_path}: {e}")
                skipped_files.append(str(relative_path))
    
    return copied_files, skipped_files

def find_files_by_content_patterns(directory):
    """Find migration-related files by content patterns instead of hardcoded names."""
    directory_path = Path(directory)
    migration_files = {
        'strategy_files': [],
        'progress_files': [],
        'analysis_files': [],
        'planning_files': [],
        'task_files': []
    }
    
    # Define content patterns to identify file types
    patterns = {
        'strategy': [
            r'migration.*strategy',
            r'context.*engineering.*migration',
            r'migration.*plan',
            r'implementation.*roadmap'
        ],
        'progress': [
            r'migration.*progress',
            r'validation.*report',
            r'phase.*completion',
            r'migration.*status'
        ],
        'analysis': [
            r'migration.*analysis',
            r'project.*analysis',
            r'codebase.*analysis',
            r'technology.*stack'
        ],
        'planning': [
            r'planning',
            r'project.*goals',
            r'architecture.*overview',
            r'design.*decisions'
        ],
        'task': [
            r'task',
            r'todo',
            r'backlog',
            r'work.*items'
        ]
    }
    
    # Search through all markdown files
    for md_file in directory_path.rglob('*.md'):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read().lower()
                filename = md_file.name.lower()
                
                # Check against patterns
                for category, pattern_list in patterns.items():
                    for pattern in pattern_list:
                        if re.search(pattern, content) or re.search(pattern, filename):
                            migration_files[f'{category}_files'].append(str(md_file))
                            break
        except Exception:
            continue
    
    return migration_files

def create_project_specific_docs(target_dir):
    """Create project-specific documentation files."""
    target_path = Path(target_dir)
    
    # Create MIGRATION_ANALYSIS.md placeholder
    migration_analysis = target_path / 'MIGRATION_ANALYSIS.md'
    if not migration_analysis.exists():
        with open(migration_analysis, 'w', encoding='utf-8') as f:
            f.write("""# Migration Analysis Report

*This file will be generated when you run `/analyze-existing-project`*

## Quick Start

1. Run the project analysis:
   ```
   /analyze-existing-project
   ```

2. Extract existing project context:
   ```
   /extract-project-context
   ```

3. Generate migration strategy:
   ```
   /generate-migration-strategy MIGRATION_ANALYSIS.md
   ```

4. Execute migration phases:
   ```
   /execute-migration-phase PRPs/migration-strategy.md --phase=1
   ```

5. Validate progress:
   ```
   /validate-migration-progress
   ```

## Context Engineering Migration Commands

The following Claude Code commands are now available in your project:

- `/analyze-existing-project` - Comprehensive codebase analysis
- `/extract-project-context` - Knowledge extraction and documentation
- `/generate-migration-strategy` - Strategic migration planning
- `/execute-migration-phase` - Incremental implementation
- `/validate-migration-progress` - Quality validation and metrics

## Directory Structure Added

```
.claude/commands/        # Migration-specific commands
PRPs/                   # Problem-Reasoning-Plan documents
├── ai_docs/           # Extracted knowledge base
├── templates/         # PRP templates
└── migration/         # Migration-specific PRPs
examples/              # Migration examples and patterns
CLAUDE.md              # Global context engineering rules
```

## Next Steps

1. **Read the migration README**: `README_TEMPLATE.md` contains comprehensive migration guidance
2. **Run project analysis**: Start with `/analyze-existing-project` to understand your codebase
3. **Review extracted context**: Examine the generated documentation in `PRPs/ai_docs/`
4. **Plan migration strategy**: Use the analysis to create a phased migration plan
5. **Execute incrementally**: Implement context engineering practices gradually

For detailed guidance, see `README_TEMPLATE.md`.
""")
        print(f"[OK] Created: MIGRATION_ANALYSIS.md")

def main():
    parser = argparse.ArgumentParser(
        description="Copy project migration template to existing project directory"
    )
    parser.add_argument(
        "target_directory",
        help="Path to existing project directory where migration template will be copied"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing files without prompting"
    )
    
    args = parser.parse_args()
    
    # Get source directory (where this script is located)
    source_dir = Path(__file__).parent
    target_dir = Path(args.target_directory)
    
    # Validate target directory
    if not target_dir.exists():
        print(f"Error: Target directory '{target_dir}' does not exist.")
        print("Please provide the path to your existing project directory.")
        return 1
    
    if not target_dir.is_dir():
        print(f"Error: '{target_dir}' is not a directory.")
        return 1
    
    # Check if target directory has some project files
    common_project_files = [
        'package.json', 'requirements.txt', 'Cargo.toml', 'go.mod',
        'pom.xml', 'build.gradle', '.git', 'src', 'lib', 'app'
    ]
    
    has_project_files = any((target_dir / f).exists() for f in common_project_files)
    if not has_project_files:
        response = input(
            f"Warning: '{target_dir}' doesn't appear to contain a project. Continue? (y/N): "
        )
        if response.lower() not in ['y', 'yes']:
            print("Migration cancelled.")
            return 0
    
    # Check for existing context engineering files
    existing_ce_files = [
        '.claude', 'PRPs', 'CLAUDE.md', 'MIGRATION_ANALYSIS.md'
    ]
    
    existing_files = [f for f in existing_ce_files if (target_dir / f).exists()]
    if existing_files and not args.force:
        print(f"Warning: The following context engineering files already exist:")
        for f in existing_files:
            print(f"  - {f}")
        response = input("Overwrite existing files? (y/N): ")
        if response.lower() not in ['y', 'yes']:
            print("Migration cancelled.")
            return 0
    
    print(f"Copying project migration template to: {target_dir}")
    print(f"Source template: {source_dir}")
    print()
    
    # Load ignore patterns
    ignore_patterns = load_gitignore_patterns()
    
    # Additional patterns to ignore when copying template
    template_ignore_patterns = [
        'copy_template.py',  # Don't copy this script
        '__pycache__/',
        '*.pyc',
        '.git/',
    ]
    
    all_ignore_patterns = ignore_patterns + template_ignore_patterns
    
    # Copy template files
    try:
        copied_files, skipped_files = copy_template_files(
            source_dir, target_dir, all_ignore_patterns
        )
        
        # Create project-specific documentation
        create_project_specific_docs(target_dir)
        
        print()
        print("=" * 60)
        print("Migration Template Copy Complete!")
        print("=" * 60)
        print(f"[OK] Copied {len(copied_files)} files")
        print(f"[SKIP] Skipped {len(skipped_files)} files (build artifacts, dependencies, etc.)")
        print()
        print("Context Engineering migration tools have been added to your project!")
        print()
        print("Next Steps:")
        print("1. Read the comprehensive guide: README_TEMPLATE.md")
        print("2. Run project analysis: /analyze-existing-project")
        print("3. Extract project context: /extract-project-context")
        print("4. Generate migration strategy: /generate-migration-strategy")
        print("5. Execute migration phases incrementally")
        print()
        print("Your existing codebase has been preserved completely.")
        print("Context engineering tools are now available alongside your current development workflow.")
        
        return 0
        
    except Exception as e:
        print(f"Error during migration: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())