"""
Generator Script for Unit 2 Lecture 2: Hamilton's Principle and Lagrange's Equations
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from u2_l2_content_header import HEADER_CELLS
from u2_l2_content_theory import THEORY_CELLS
from u2_l2_content_example1_pendulum import EXAMPLE_PENDULUM_CELLS
from u2_l2_content_summary import SUMMARY_CELLS

def create_cell(cell_type, source, metadata=None):
    if metadata is None:
        metadata = {}
    
    if isinstance(source, str):
        source = source.split('\n')
        source = [line + '\n' for line in source[:-1]] + [source[-1]]
    
    cell = {
        "cell_type": cell_type,
        "metadata": metadata,
        "source": source
    }
    
    if cell_type == "code":
        cell["execution_count"] = None
        cell["outputs"] = []
    
    return cell

def process_content_cells(cells_list):
    processed = []
    for cell_dict in cells_list:
        cell_type = cell_dict.get("cell_type", "markdown")
        source = cell_dict.get("source", "")
        metadata = cell_dict.get("metadata", {})
        processed_cell = create_cell(cell_type, source, metadata)
        processed.append(processed_cell)
    return processed

def generate_notebook():
    print("="*80)
    print("GENERATING UNIT 2 LECTURE 2 NOTEBOOK")
    print("="*80)
    print("\nAssembling content modules...")
    
    all_cells = []
    
    print("[1/4] Adding header and introduction...")
    all_cells.extend(process_content_cells(HEADER_CELLS))
    
    print("[2/4] Adding Hamilton's Principle theory...")
    all_cells.extend(process_content_cells(THEORY_CELLS))
    
    print("[3/4] Adding Example: Simple Pendulum...")
    all_cells.extend(process_content_cells(EXAMPLE_PENDULUM_CELLS))
    
    print("[4/4] Adding summary...")
    all_cells.extend(process_content_cells(SUMMARY_CELLS))
    
    print(f"\nTotal cells assembled: {len(all_cells)}")
    
    notebook = {
        "cells": all_cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
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
    
    output_path = Path(__file__).parent.parent / "notebooks" / "Teacher" / "T_U2_L2_Lagrangian_Mechanics.ipynb"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    print(f"\nWriting notebook to: {output_path}")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)
    
    print("Notebook generated successfully!")
    
    markdown_cells = sum(1 for cell in all_cells if cell["cell_type"] == "markdown")
    code_cells = sum(1 for cell in all_cells if cell["cell_type"] == "code")
    
    print("\n" + "="*80)
    print("GENERATION STATISTICS")
    print("="*80)
    print(f"Total cells:     {len(all_cells)}")
    print(f"Markdown cells:  {markdown_cells}")
    print(f"Code cells:      {code_cells}")
    print(f"Output file:     {output_path.name}")
    print("="*80)
    
    return output_path

if __name__ == "__main__":
    try:
        output_file = generate_notebook()
        print(f"\nSUCCESS! Notebook ready at:")
        print(f"{output_file}")
    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
