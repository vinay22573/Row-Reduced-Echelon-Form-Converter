# Taking input in file
fname="input_file.txt"
with open(fname,"r") as f:
    matrix=[]
    for line in f:
        line=line.split()
        values=[int(i) for i in line]
        matrix.append(values)

# Making RREF using libraries
rows=len(matrix)
column=len(matrix[0])
from sympy import*
M=Matrix(matrix)
RREF=M.rref()
print(RREF)

print()
# Getting pivot columns using the above rref matrix
pivot_columns=list(RREF[1])
piv_col=[]
for items in pivot_columns:
    items=items+1
    piv_col.append(items)
print(f"{piv_col} are the pivot columns")

print()
if len(piv_col)!=column:
    print("The matrix gives no solution or infinitely many solution")
else:
    print("Unique solution")
print()
# Getting non pivot column
npiv_col=[]
for j in range(column):
    if j in pivot_columns:
        continue
    else:
        a="x"+str(j+1)
        npiv_col.append(a)
print(f"{npiv_col} are free variables")        
nul=M.nullspace()

print()
# getting the null space
null=[]
for item in nul:
    itme=str(item)
    item=itme[7:(len(itme)-1)]
    null.append(item)
print()




if len(piv_col)!=column:
    print()
    last_row=null[-1]
    last_elt=last_row[-3]
    if last_elt==0:
        print("No solution")
    else:
        print("Infinite solution")

print()
# printing the null space with the corresponding variable
if len(piv_col)!=column:
    fin_ans=[(npiv_col[i],null[i]) for i in range(len(null))]
    print(fin_ans)