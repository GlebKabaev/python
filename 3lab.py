class Triangle:
    def __init__(self,point1,point2,point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        all_point_set = set()
        all_point_set.add(point1)
        all_point_set.add(point2)
        all_point_set.add(point3)
    def move(self,x_or_y,how_much):
        if x_or_y.lower()=='x':
            self.point1[0] = self.point1[0]-how_much
            self.point2[0] = self.point2[0]-how_much
            self.point3[0] = self.point3[0]-how_much
        if x_or_y.lower() == 'y':
            self.point1[1] = self.point1[1] - how_much
            self.point2[1] = self.point2[1] - how_much
            self.point3[1] = self.point3[1] - how_much
    def is_intersect(self,Tetragon):
        if (self.all_point_set).intersection(Tetragon.all_point_set):
            return True
        else : return False


class Tetragon:
    def __init__(self,point1,point2,point3,point4):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.point4 = point4
        all_point_set = set()
        all_point_set.add(point1)
        all_point_set.add(point2)
        all_point_set.add(point3)
        all_point_set.add(point4)
    def move(self,x_or_y,how_much):
        if x_or_y.lower()=='x':
            self.point1[0] = self.point1[0]-how_much
            self.point2[0] = self.point2[0]-how_much
            self.point3[0] = self.point3[0]-how_much
            self.point4[0] = self.point4[0] - how_much
        if x_or_y.lower() == 'y':
            self.point1[1] = self.point1[1] - how_much
            self.point2[1] = self.point2[1] - how_much
            self.point3[1] = self.point3[1] - how_much
            self.point4[1] = self.point4[1] - how_much

triang=Triangle([1,1],[0,0],[1,0])
tetragon1=Tetragon([1,1],[0,0],[1,0],[0,1])
triang.move('y',5)
print(triang.all_point_set)

