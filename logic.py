from random import randrange, shuffle

class sudoku_game:
    def __init__(self) -> None:
        self.graph = []

    def take_out(self):
        cou = 0
        while cou < 50:
            i = randrange( 9)
            j = randrange( 9)
            if self.graph[i][j] != 0:
                cou += 1
                self.graph[i][j] = 0

    def roll_v(self, gri , place):
        rt = []
        for i in range(3):
            ad = []
            for j in place:
                ad.append(gri[i][j])
            rt.append(ad)
        return rt

    def roll_h(self, gri , place):
        rt = []
        for i in place:
            rt.append(gri[i])
        return rt

    def create(self):
        ar = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
        shuffle(ar)

        first_cube = []
        for _ in range(3):
            dim = []
            for _ in range(3):
                dim.append(ar.pop(0))
            first_cube.append(dim)

        rows = {}
        rows[0] = [first_cube]
        rows[1] = []
        rows[2] = []
        places = [[2,0,1] , [1,2,0]] 
        shuffle(places)

        for i , j in enumerate(places):
            g1 = self.roll_v(first_cube , j)
            rows[i + 1].append(g1)

        for i in range(3):
            shuffle(places)
            for j in places:
                rows[i].append(self.roll_h(rows[i][0] , j))
        
        for i in range(3):
            can = rows[i] 
            shuffle(can)

            for j in range(3):
                dim = []
                for k in range(3):
                    dim += can[k][j]

                self.graph.append(dim)


class solution:
    def __init__(self , graph) -> None:
        self.graph = graph

    def nxt(self ,i , j):

        for o in range(j+1 , 9):
            if self.graph[i][o] == 0:
                return False , i , o

        for a in range(i + 1 , 9):
            for b in range(9):
                if self.graph[a][b] == 0:
                    return False , a , b

        return True, -1 , -1

    def valid(self , i , j):
        for a in range(9):
            if a != j and self.graph[i][a] == self.graph[i][j]:
                return False
            if a != i and self.graph[a][j] == self.graph[i][j]:
                return False

        pos1 = i//3
        pos2 = j//3

        for a in range(3):
            for b in range(3):
                if (i != (3*pos1 + a) or j != (3*pos2 +b)) and self.graph[i][j] == self.graph[3*pos1 + a][3*pos2 +b]:
                    return False
                
        return True

    def solve_sudoku(self , i , j):
        for nu in range(1 , 10):
            self.graph[i][j] = nu
            if self.valid(i , j):
                a , b , c = self.nxt(i , j)
                if a:
                    return True
                if self.solve_sudoku(b , c):
                    return True
        self.graph[i][j] = 0
        return False

    
                    


