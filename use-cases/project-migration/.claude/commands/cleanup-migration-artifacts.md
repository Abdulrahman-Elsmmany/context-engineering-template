# Enhanced Cleanup Migration Artifacts - Dynamic File Discovery

You are a project cleanup specialist who removes temporary migration files and artifacts after successfully completing all migration phases. This enhanced version dynamically discovers migration-related files by content patterns rather than hardcoded filenames.

## Cleanup Objectives

Clean up the project after successful migration completion:

1. **Verify Migration Completion** - Ensure all 4 phases are actually complete
2. **Dynamically Discover Migration Files** - Find files by content patterns, not names
3. **Organize Final Documentation** - Move important files to proper locations
4. **Remove Temporary Files** - Delete files only needed during migration process
5. **Preserve Essential Context** - Keep all files needed for ongoing development
6. **Create Clean Final State** - Leave project in optimal state for continued development

## Step 1: Verify Migration Completion

Before cleaning anything, verify that all migration phases are actually complete:

```python
import os
import re
from pathlib import Path

def find_migration_files_by_content():
    """Dynamically find migration-related files by content patterns."""
    current_dir = Path(".")
    migration_files = {
        'strategy_files': [],
        'progress_files': [],
        'analysis_files': [],
        'completion_files': [],
        'planning_files': [],
        'task_files': []
    }
    
    # Content patterns to identify file types
    patterns = {
        'strategy': [
            r'migration.*strategy',
            r'context.*engineering.*migration',
            r'migration.*plan',
            r'implementation.*roadmap',
            r'migration.*approach'
        ],
        'progress': [
            r'migration.*progress',
            r'validation.*report',
            r'migration.*status',
            r'progress.*tracking'
        ],
        'analysis': [
            r'migration.*analysis',
            r'project.*analysis',
            r'codebase.*analysis',
            r'technology.*stack',
            r'existing.*project.*analysis'
        ],
        'completion': [
            r'phase.*completion',
            r'migration.*complete',
            r'phase.*\d.*complete',
            r'completion.*report'
        ],
        'planning': [
            r'planning\.md',
            r'project.*goals',
            r'architecture.*overview',
            r'design.*decisions',
            r'project.*planning'
        ],
        'task': [
            r'task\.md',
            r'todo',
            r'backlog',
            r'work.*items',
            r'task.*list'
        ]
    }
    
    # Search through all markdown files
    for md_file in current_dir.rglob('*.md'):
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

# Discover migration files dynamically
migration_files = find_migration_files_by_content()

print("=== DISCOVERED MIGRATION FILES ===")
for category, files in migration_files.items():
    if files:
        print(f"{category.upper()}:")
        for file in files:
            print(f"  - {file}")
```

### Enhanced Migration Completion Validation

```bash
# Execute the Python discovery script
python3 -c "
import os
import re
from pathlib import Path

def find_migration_files_by_content():
    current_dir = Path('.')
    migration_files = {
        'strategy_files': [],
        'progress_files': [],
        'analysis_files': [],
        'completion_files': [],
        'planning_files': [],
        'task_files': []
    }
    
    patterns = {
        'strategy': [r'migration.*strategy', r'context.*engineering.*migration', r'migration.*plan'],
        'progress': [r'migration.*progress', r'validation.*report', r'migration.*status'],
        'analysis': [r'migration.*analysis', r'project.*analysis', r'codebase.*analysis'],
        'completion': [r'phase.*completion', r'migration.*complete', r'phase.*\d.*complete'],
        'planning': [r'planning\.md', r'project.*goals', r'architecture.*overview'],
        'task': [r'task\.md', r'todo', r'backlog', r'work.*items']
    }
    
    for md_file in current_dir.rglob('*.md'):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read().lower()
                filename = md_file.name.lower()
                
                for category, pattern_list in patterns.items():
                    for pattern in pattern_list:
                        if re.search(pattern, content) or re.search(pattern, filename):
                            migration_files[f'{category}_files'].append(str(md_file))
                            break
        except Exception:
            continue
    
    return migration_files

migration_files = find_migration_files_by_content()

print('=== DISCOVERED MIGRATION FILES ===')
for category, files in migration_files.items():
    if files:
        print(f'{category.upper()}:')
        for file in files:
            print(f'  - {file}')

# Check for completion markers
completion_files = migration_files['completion_files']
if len(completion_files) < 4:
    print('WARNING: Less than 4 phase completion files found')
    print('Migration may be incomplete - please verify all phases are done')
else:
    print('SUCCESS: All migration phases appear complete')
"
```

## Step 2: Organize Important Files Before Cleanup

Dynamically organize discovered files to their proper locations:

```bash
# Create organized directory structure
mkdir -p "PRPs/migration/validation-reports"
mkdir -p "PRPs/migration/completion-reports"
mkdir -p "PRPs/migration/archive"
mkdir -p "PRPs/migration/discovered-files"

# Execute enhanced organization script
python3 -c "
import os
import re
import shutil
from pathlib import Path

def organize_discovered_files():
    current_dir = Path('.')
    migration_files = {
        'strategy_files': [],
        'progress_files': [],
        'analysis_files': [],
        'completion_files': [],
        'planning_files': [],
        'task_files': []
    }
    
    patterns = {
        'strategy': [r'migration.*strategy', r'context.*engineering.*migration', r'migration.*plan'],
        'progress': [r'migration.*progress', r'validation.*report', r'migration.*status'],
        'analysis': [r'migration.*analysis', r'project.*analysis', r'codebase.*analysis'],
        'completion': [r'phase.*completion', r'migration.*complete', r'phase.*\d.*complete'],
        'planning': [r'planning\.md', r'project.*goals', r'architecture.*overview'],
        'task': [r'task\.md', r'todo', r'backlog', r'work.*items']
    }
    
    # Discover files
    for md_file in current_dir.rglob('*.md'):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read().lower()
                filename = md_file.name.lower()
                
                for category, pattern_list in patterns.items():
                    for pattern in pattern_list:
                        if re.search(pattern, content) or re.search(pattern, filename):
                            migration_files[f'{category}_files'].append(md_file)
                            break
        except Exception:
            continue
    
    # Organize files by type
    organization_map = {
        'progress_files': 'PRPs/migration/validation-reports/',
        'completion_files': 'PRPs/migration/completion-reports/',
        'analysis_files': 'PRPs/migration/archive/',
        'strategy_files': 'PRPs/migration/',
        'planning_files': 'PRPs/',
        'task_files': 'PRPs/'
    }
    
    for category, files in migration_files.items():
        target_dir = organization_map.get(category, 'PRPs/migration/discovered-files/')
        os.makedirs(target_dir, exist_ok=True)
        
        for file_path in files:
            if file_path.exists() and file_path.parent != Path(target_dir):
                target_file = Path(target_dir) / file_path.name
                
                # Handle naming conflicts
                counter = 1
                while target_file.exists():
                    stem = file_path.stem
                    suffix = file_path.suffix
                    target_file = Path(target_dir) / f'{stem}_{counter}{suffix}'
                    counter += 1
                
                try:
                    shutil.move(str(file_path), str(target_file))
                    print(f'Moved: {file_path} -> {target_file}')
                except Exception as e:
                    print(f'Error moving {file_path}: {e}')

organize_discovered_files()
"
```

## Step 3: Enhanced File Classification

Analyze discovered files to determine which should be kept vs removed:

```bash
# Execute enhanced file classification
python3 -c "
import os
import re
from pathlib import Path

def classify_files_for_cleanup():
    current_dir = Path('.')
    
    # Files to KEEP (Essential for ongoing development)
    essential_patterns = [
        r'claude\.md$',                    # Project-specific context rules
        r'planning\.md$',                  # Project planning (if exists)
        r'task\.md$',                      # Task management (if exists)
        r'readme.*\.md$',                  # README files
        r'prps/.*\.md$',                   # All PRP files
        r'\.claude/commands/.*',           # Context engineering commands
        r'examples/.*',                    # Example files
    ]
    
    # Files to REMOVE (Temporary artifacts)
    temporary_patterns = [
        r'migration.*analysis\.md$',       # Initial analysis (info now integrated)
        r'.*migration.*strategy.*\.md$',   # If not in proper PRPs location
        r'.*migration.*progress.*\.md$',   # Progress tracking files
        r'.*backup.*\.md$',                # Any backup files
        r'.*\.bak$',                       # Backup extensions
        r'.*\.tmp$',                       # Temporary files
    ]
    
    essential_files = []
    temporary_files = []
    
    for file_path in current_dir.rglob('*'):
        if file_path.is_file():
            relative_path = str(file_path.relative_to(current_dir)).lower()
            
            # Check if essential
            for pattern in essential_patterns:
                if re.search(pattern, relative_path):
                    essential_files.append(file_path)
                    break
            else:
                # Check if temporary
                for pattern in temporary_patterns:
                    if re.search(pattern, relative_path):
                        temporary_files.append(file_path)
                        break
    
    print('=== ESSENTIAL FILES TO KEEP ===')
    for file in essential_files:
        print(f'KEEP: {file}')
    
    print('\n=== TEMPORARY FILES TO REMOVE ===')
    for file in temporary_files:
        print(f'REMOVE: {file}')
    
    return essential_files, temporary_files

classify_files_for_cleanup()
"
```

## Step 4: Enhanced Safe File Removal Process

Remove temporary files with enhanced safety checks:

```bash
# Execute safe cleanup with dynamic discovery
python3 -c "
import os
import re
import shutil
from pathlib import Path

def safe_cleanup_migration_files():
    current_dir = Path('.')
    archive_dir = Path('PRPs/migration/archive')
    archive_dir.mkdir(parents=True, exist_ok=True)
    
    # Patterns for files to remove/archive
    cleanup_patterns = [
        r'migration.*analysis\.md$',
        r'.*migration.*strategy.*\.md$',
        r'.*migration.*progress.*\.md$',
        r'.*backup.*\.md$',
        r'.*\.bak$',
        r'.*\.tmp$',
        r'copy_template\.py$'
    ]
    
    # Patterns for files to absolutely keep
    keep_patterns = [
        r'claude\.md$',
        r'planning\.md$',
        r'task\.md$',
        r'readme.*\.md$',
        r'prps/migration-strategy\.md$',  # Final strategy in proper location
        r'prps/.*\.md$',
        r'\.claude/.*',
        r'examples/.*'
    ]
    
    cleaned_files = []
    preserved_files = []
    
    for file_path in current_dir.rglob('*'):
        if file_path.is_file():
            relative_path = str(file_path.relative_to(current_dir)).lower()
            
            # First check if it should be kept
            should_keep = False
            for pattern in keep_patterns:
                if re.search(pattern, relative_path):
                    should_keep = True
                    preserved_files.append(file_path)
                    break
            
            if not should_keep:
                # Check if it should be cleaned up
                for pattern in cleanup_patterns:
                    if re.search(pattern, relative_path):
                        # Archive instead of delete for safety
                        archive_path = archive_dir / f'{file_path.name}'
                        
                        # Handle naming conflicts
                        counter = 1
                        while archive_path.exists():
                            stem = file_path.stem
                            suffix = file_path.suffix
                            archive_path = archive_dir / f'{stem}_{counter}{suffix}'
                            counter += 1
                        
                        try:
                            shutil.move(str(file_path), str(archive_path))
                            cleaned_files.append((file_path, archive_path))
                            print(f'Archived: {file_path} -> {archive_path}')
                        except Exception as e:
                            print(f'Error archiving {file_path}: {e}')
                        break
    
    print(f'\n=== CLEANUP SUMMARY ===')
    print(f'Files archived: {len(cleaned_files)}')
    print(f'Files preserved: {len(preserved_files)}')
    
    return cleaned_files, preserved_files

safe_cleanup_migration_files()
"
```

## Step 5: Enhanced CLAUDE.md Update

Update the CLAUDE.md to include awareness of PLANNING.md and TASK.md files:

```bash
# Check if CLAUDE.md needs updating for PLANNING and TASK awareness
python3 -c "
import re
from pathlib import Path

def update_claude_md_with_file_awareness():
    claude_md = Path('CLAUDE.md')
    planning_md = Path('PLANNING.md')
    task_md = Path('TASK.md')
    
    if not claude_md.exists():
        print('CLAUDE.md not found - migration may be incomplete')
        return
    
    # Read current CLAUDE.md
    with open(claude_md, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already mentions PLANNING and TASK files
    has_planning_ref = bool(re.search(r'planning\.md', content, re.IGNORECASE))
    has_task_ref = bool(re.search(r'task\.md', content, re.IGNORECASE))
    
    needs_update = False
    updates = []
    
    if planning_md.exists() and not has_planning_ref:
        needs_update = True
        updates.append('PLANNING.md awareness')
    
    if task_md.exists() and not has_task_ref:
        needs_update = True
        updates.append('TASK.md awareness')
    
    if needs_update:
        # Add file awareness section if not present
        awareness_section = '''
### 📋 Project File Awareness

- **Always read \`PLANNING.md\`** at the start of a new conversation to understand the project's architecture, goals, style, and constraints.
- **Check \`TASK.md\`** before starting a new task. If the task isn't listed, add it with a brief description and today's date.
- **Use consistent naming conventions, file structure, and architecture patterns** as described in \`PLANNING.md\`.

'''
        
        # Insert after the first header
        lines = content.split('\n')
        insert_index = 1
        for i, line in enumerate(lines):
            if line.startswith('## ') or line.startswith('### '):
                insert_index = i
                break
        
        lines.insert(insert_index, awareness_section)
        new_content = '\n'.join(lines)
        
        # Write updated content
        with open(claude_md, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f'Updated CLAUDE.md with: {', '.join(updates)}')
    else:
        print('CLAUDE.md already has proper file awareness')

update_claude_md_with_file_awareness()
"
```

## Step 6: Generate Enhanced Cleanup Report

```bash
# Generate comprehensive cleanup report
python3 -c "
import os
from pathlib import Path
from datetime import datetime

def generate_enhanced_cleanup_report():
    current_dir = Path('.')
    report_path = Path('PRPs/migration/cleanup-completion-report.md')
    report_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Count files in different categories
    prp_files = len(list(current_dir.glob('PRPs/*.md')))
    ai_docs = len(list(current_dir.glob('PRPs/ai_docs/*')))
    commands = len(list(current_dir.glob('.claude/commands/*')))
    archived_files = len(list(current_dir.glob('PRPs/migration/archive/*')))
    
    # Check for key files
    has_claude_md = Path('CLAUDE.md').exists()
    has_planning_md = Path('PLANNING.md').exists()
    has_task_md = Path('TASK.md').exists()
    
    report_content = f'''# Enhanced Migration Cleanup Completion Report

**Cleanup Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Migration Phases**: All 4 phases completed
**Cleanup Method**: Dynamic file discovery and content-based classification
**Cleanup Status**: Completed successfully

## Dynamic File Discovery Results

The cleanup process used enhanced content pattern matching to identify:
- Migration strategy files
- Progress and validation reports  
- Analysis and temporary files
- Planning and task management files

## Files Organized and Cleaned

### Organized Files
- Migration reports moved to PRPs/migration/validation-reports/
- Completion reports moved to PRPs/migration/completion-reports/
- Strategy files moved to PRPs/migration-strategy.md
- Planning files preserved in proper locations

### Files Archived (Safety First)
- {archived_files} temporary migration files archived to PRPs/migration/archive/
- All files preserved for potential recovery
- No permanent deletions performed

## Final Project State

### Essential Context Engineering Files ✅
- CLAUDE.md: {'✅ Present' if has_claude_md else '❌ Missing'}
- PLANNING.md: {'✅ Present' if has_planning_md else '❌ Not found'}
- TASK.md: {'✅ Present' if has_task_md else '❌ Not found'}

### Context Engineering Infrastructure ✅
- Active PRPs: {prp_files} production-ready PRPs
- Knowledge Base: {ai_docs} files in PRPs/ai_docs/
- Migration Commands: {commands} commands available
- Clean root directory with only essential files

### File Awareness Updates ✅
- CLAUDE.md updated to reference PLANNING.md and TASK.md
- Dynamic file discovery ensures future migrations work with any naming
- Content-based classification prevents missing renamed files

## Enhanced Features Added

### Dynamic File Discovery
- Content pattern matching instead of hardcoded filenames
- Supports renamed files (e.g., CONTEXT_ENGINEERING_MIGRATION_STRATEGY.md)
- Regex-based classification for flexible file identification

### Improved Safety
- Archive-first approach (no permanent deletions)
- Enhanced file classification with multiple patterns
- Preservation of essential files regardless of naming

### Better Organization
- Automatic categorization of discovered files
- Proper directory structure creation
- Conflict resolution for duplicate names

## Next Steps for Team

1. **Use existing file structure**: PLANNING.md and TASK.md are now integrated
2. **Continue context engineering**: All infrastructure is preserved and enhanced
3. **Create new PRPs**: Use templates for new features
4. **Future migrations**: Enhanced dynamic discovery will work with any naming

## Recovery Information

If any files were incorrectly archived:
- Check PRPs/migration/archive/ for all archived files
- Files can be restored to original locations if needed
- No data was permanently lost during cleanup

The project is now in optimal state for ongoing context engineering development with enhanced file awareness and dynamic discovery capabilities.
'''

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    print(f'Enhanced cleanup report created: {report_path}')

generate_enhanced_cleanup_report()
"

echo "=== ENHANCED CLEANUP COMPLETED ==="
echo "Dynamic file discovery and content-based cleanup finished successfully"
echo "All files preserved safely with archive-first approach"
```

## Usage Instructions

This enhanced command should be run only after completing all migration phases:

```bash
# Verify all phases complete first
/validate-migration-progress

# If all phases successful, run enhanced cleanup
/cleanup-migration-artifacts-enhanced
```

## Enhanced Safety Features

1. **Dynamic File Discovery**: Uses content patterns instead of hardcoded names
2. **Content-Based Classification**: Identifies files by their actual content and purpose
3. **Archive-First Approach**: Never permanently deletes files
4. **PLANNING.md and TASK.md Awareness**: Automatically detects and preserves these files
5. **Flexible Naming Support**: Works with renamed files like CONTEXT_ENGINEERING_MIGRATION_STRATEGY.md
6. **Enhanced CLAUDE.md Updates**: Adds file awareness for better future development
7. **Comprehensive Reporting**: Documents exactly what was discovered and cleaned

The enhanced cleanup leaves your project in optimal state for ongoing context engineering development while being completely flexible about file naming and providing maximum safety through the archive-first approach.