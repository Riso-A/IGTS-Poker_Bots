import numpy as np

def solve_psne(p1_matrix, p2_matrix):
    p1 = np.asarray(p1_matrix)
    p2 = np.asarray(p2_matrix)
    
    num_rows, num_cols = p1.shape
    
    max_p1_per_col = np.max(p1, axis=0)
    max_p2_per_row = np.max(p2, axis=1)
    
    psne_indices = []
    
    for r in range(num_rows):
        for c in range(num_cols):
            if p1[r, c] == max_p1_per_col[c] and p2[r, c] == max_p2_per_row[r]:
                psne_indices.append((r, c))
                
    return psne_indices