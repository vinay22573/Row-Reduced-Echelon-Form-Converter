`# Linear System Solver  This Python script reads a matrix from an input file, performs row reduction to echelon form (RREF), and analyzes the matrix to determine the solution of a system of linear equations.  ## Getting Started  ### Prerequisites  - Python (version 3.x recommended) - sympy library  ```bash # Install required dependencies pip install sympy`

### Installation

1.  Clone the repository:
    
    
    
    `git clone https://github.com/yourusername/linear-system-solver.git cd linear-system-solver`
    
2.  Run the script:
    

    
    `python linear_system_solver.py`
    

Usage
-----

1.  **Input File:** Provide your matrix in the `input_file.txt` file. Each row in the file should represent a row in the matrix, with values separated by spaces.
    
2.  **Run the Script:**
    
    
    
    `python linear_system_solver.py`
    
3.  **Output:**
    
    *   The RREF matrix.
    *   Pivot columns and non-pivot columns.
    *   Information about the solutions (unique, infinite, or none).