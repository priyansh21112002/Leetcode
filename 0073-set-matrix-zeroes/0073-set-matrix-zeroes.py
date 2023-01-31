class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        col_set = set()
        col_list=[]
        for row in matrix:
            if row.count(0) > 0:
                for j,val in enumerate(row):
                    if val == 0:
                        col_list.append(j)
                    row[j] = 0

        for row in matrix:
            for j in col_list:
                row[j] = 0