#Nested_List
if __name__ == '__main__':
    Main = []
    N = int(input().strip())
    for i in range(N):
        Name = input().strip()
        Grade = float(input().strip())
        Main.append([Name, Grade])
    
    Scores= [row[1] for row in Main]
    Sor_Set = sorted(set(Scores))
    Sor_Lis = Sor_Set[1]
    Same_Name = [row[0] for row in Main if row[1] == Sor_Lis]
    Sor_Name = sorted(Same_Name)
    for name in Sor_Name:
        print(name)