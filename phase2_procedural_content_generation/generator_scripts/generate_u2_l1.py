"""
Generator Script for Unit 2 Lecture 1: Newton's Laws and Force Formulations
Assembles modular content files into complete Jupyter notebook
"""

import json
import sys
from pathlib import Path

# Import all content modules
sys.path.insert(0, str(Path(__file__).parent))

from u2_l1_content_header import HEADER_CELLS
from u2_l1_content_newtons_laws import NEWTONS_LAWS_CELLS
from u2_l1_content_example1_incline import EXAMPLE_INCLINE_CELLS
from u2_l1_content_example2_atwood import EXAMPLE_ATWOOD_CELLS
from u2_l1_content_practice_summary import PRACTICE_AND_SUMMARY_CELLS

def create_cell(cell_type, source, metadata=None):
    """
    Create a properly formatted notebook cell.
    
    Parameters:
    -----------
    cell_type : str
        'markdown' or 'code'
    source : str or list
        Cell content (string or list of strings)
    metadata : dict, optional
        Cell metadata
    
    Returns:
    --------
    dict : Formatted cell dictionary
    """
    if metadata is None:
        metadata = {}
    
    # Convert string to list of lines if needed
    if isinstance(source, str):
        source = source.split('\n')
        # Add newlines back except for last line
        source = [line + '\n' for line in source[:-1]] + [source[-1]]
    
    cell = {
        "cell_type": cell_type,
        "metadata": metadata,
        "source": source
    }
    
    # Add execution fields for code cells
    if cell_type == "code":
        cell["execution_count"] = None
        cell["outputs"] = []
    
    return cell

def process_content_cells(cells_list):
    """
    Process cells from content modules into proper notebook format.
    
    Parameters:
    -----------
    cells_list : list
        List of cell dictionaries from content modules
    
    Returns:
    --------
    list : Processed cells ready for notebook
    """
    processed = []
    
    for cell_dict in cells_list:
        cell_type = cell_dict.get("cell_type", "markdown")
        source = cell_dict.get("source", "")
        metadata = cell_dict.get("metadata", {})
        
        processed_cell = create_cell(cell_type, source, metadata)
        processed.append(processed_cell)
    
    return processed

def generate_notebook():
    """
    Generate complete Unit 2 Lecture 1 notebook from modular content.
    """
    print("="*80)
    print(" GENERATING UNIT 2 LECTURE 1 NOTEBOOK")
    print("="*80)
    print("\nAssembling content modules...")
    
    # Combine all cells from modules
    all_cells = []
    
    # Module 1: Header and Introduction
    print("  [1/5] Adding header and introduction...")
    all_cells.extend(process_content_cells(HEADER_CELLS))
    
    # Module 2: Newton's Laws Theory
    print("  [2/5] Adding Newton's Laws theory...")
    all_cells.extend(process_content_cells(NEWTONS_LAWS_CELLS))
    
    # Module 3: Example 1 - Inclined Plane
    print("  [3/5] Adding Example 1 (Inclined Plane)...")
    all_cells.extend(process_content_cells(EXAMPLE_INCLINE_CELLS))
    
    # Module 4: Example 2 - Atwood Machine
    print("  [4/5] Adding Example 2 (Atwood Machine)...")
    all_cells.extend(process_content_cells(EXAMPLE_ATWOOD_CELLS))
    
    # Module 5: Practice Problems and Summary
    print("  [5/5] Adding practice problems and summary...")
    all_cells.extend(process_content_cells(PRACTICE_AND_SUMMARY_CELLS))
    
    print(f"\n✓ Total cells assembled: {len(all_cells)}")
    
    # Create notebook structure
    notebook = {
        "cells": all_cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.14.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    # Save notebook
    output_path = Path(__file__).parent.parent / "notebooks" / "Teacher" / "T_U2_L1_Newtons_Laws_Force_Formulation.ipynb"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    print(f"\n📝 Writing notebook to: {output_path}")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)
    
    print("✓ Notebook generated successfully!")
    
    # Statistics
    markdown_cells = sum(1 for cell in all_cells if cell["cell_type"] == "markdown")
    code_cells = sum(1 for cell in all_cells if cell["cell_type"] == "code")
    
    print("\n" + "="*80)
    print(" GENERATION STATISTICS")
    print("="*80)
    print(f"  Total cells:     {len(all_cells)}")
    print(f"  Markdown cells:  {markdown_cells}")
    print(f"  Code cells:      {code_cells}")
    print(f"  Output file:     {output_path.name}")
    print("="*80)
    
    return output_path

if __name__ == "__main__":
    try:
        output_file = generate_notebook()
        print(f"\n✅ SUCCESS! Notebook ready at:")
        print(f"   {output_file}")
        print("\n💡 Next steps:")
        print("   1. Open notebook in Jupyter/VS Code")
        print("   2. Run all cells to verify code executes")
        print("   3. Create student version using generate_all_students.py pattern")
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
