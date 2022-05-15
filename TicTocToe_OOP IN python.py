class TicTocToe:
    def __init__(self,num_of_chart):
        self.num_of_chart=num_of_chart
   
    def create_bord(self):                         #this function just creats a bord and show this
        number_of_chart=int(f"{self.num_of_chart}")
        bord=[]
        print('')
        print('row')
        for i in range(0,number_of_chart):
            row=[]
            for i in range(0,number_of_chart):
                row.append('__')
                
            bord.append(row)
        #just for show the bord with number
        for i in range(0,number_of_chart):
            print(i,end='   ')
            print(bord[i],sep='/n')
        
        espace=' '
        print('column',end='  ')
        for j in range(0,number_of_chart):
            print(espace,j,end=' '*2)
        game_of_bord=bord
        self.complete_the_bord(game_of_bord)
        return bord

    def show_shape_of_the_bord(self,chart):                 #just for show the bord with number       
        number_of_chart=int(f"{self.num_of_chart}")
        print('')
        print('row')
        for i in range(0,number_of_chart):
            print(i,end='   ')
            print(chart[i],sep='/n')
        
        espace=' '
        print('column',end=' ')
        for j in range(0,number_of_chart):
            print(espace,j,end=' '*3)
        chart_of_game=chart
        self.por_bodane_jadval(chart_of_game)

    def complete_the_bord(self,game_of_the_bord): #this function gets row and column number and sign and inserts in bord                               
            print('')
            print('')
            row=int(input('please enter your favorite row: ')) #this is for i
            column=int(input('please enter your favorite column: ')) #this os for j
            sign=(input('input your sign: ').upper())
            game_of_the_bord[row][column]=sign
            print('')
            self.show_shape_of_the_bord(game_of_the_bord)

    def por_bodane_jadval(self,jadvale_bazi):
        por_bodan=None
        Table_filling_detection_list=[]
        for i in range(len(jadvale_bazi)):
            for j in range(len(jadvale_bazi)):
                
                if jadvale_bazi[i][j]=='__':
                    #return True                 #اreturn true if the table is empty
                    Table_filling_detection_list.append('True')            #if it adds true to the cc list,it stillhas an empty cell table
                if jadvale_bazi[i][j]!='__':
                    #return False                #return false if the table is full
                    Table_filling_detection_list.append('False')
                    
        counter=0
        for i in range(len(Table_filling_detection_list)):
            barande_4=self.barande
            if Table_filling_detection_list[i]=='True':                
                self.checking_for_game_winner(jadvale_bazi,por_bodan)
                if barande_4=='X' or barande_4=='O':
                    break
                break
            
            if Table_filling_detection_list[i]=='False':
                counter+=1
                if counter==len(Table_filling_detection_list):
                    print('')
                    print("")
                    print('Jadval por shod')
                    por_bodan='jadval por shod'
                    self.checking_for_game_winner(jadvale_bazi,por_bodan)

 
    def checking_for_game_winner(self,chart_of_the_game,por_bodan_1):
            tedad=int(self.num_of_chart)
            winner=None
            
            if tedad==2:
                if (chart_of_the_game[0][0]=='X' and chart_of_the_game[1][0]=='X') or (chart_of_the_game[0][1]=='X' and chart_of_the_game[1][1]=='X') or (chart_of_the_game[0][0]=='X' and chart_of_the_game[0][1]=='X') or (chart_of_the_game[1][0]=='X' and chart_of_the_game[1][1]=='X') or (chart_of_the_game[0][0]=='X' and chart_of_the_game[1][1]=='X') or (chart_of_the_game[0][1]=='X' and chart_of_the_game[1][0]=='X'):
                    winner='X'
                    self.end_of_the_game(winner)
                    self.barande(winner)
                if (chart_of_the_game[0][0]=='O' and chart_of_the_game[1][0]=='O') or (chart_of_the_game[0][1]=='O' and chart_of_the_game[1][1]=='O') or (chart_of_the_game[0][0]=='O' and chart_of_the_game[0][1]=='O') or (chart_of_the_game[1][0]=='O' and chart_of_the_game[1][1]=='O') or (chart_of_the_game[0][0]=='O' and chart_of_the_game[1][1]=='O') or (chart_of_the_game[0][1]=='O' and chart_of_the_game[1][0]=='O'):
                    winner='O'
                    self.end_of_the_game(winner)
                    self.barande(winner)
            if tedad==3:
                if ((chart_of_the_game[0][0]=='X' and chart_of_the_game[1][0]=='X' and chart_of_the_game[2][0]=='X') or (chart_of_the_game[0][1]=='X' and chart_of_the_game[1][1]=='X' and chart_of_the_game[2][1]=='X') or (chart_of_the_game[0][2]=='X' and chart_of_the_game[1][2]=='X' and chart_of_the_game[2][2]=='X') or (chart_of_the_game[0][0]=='X' and chart_of_the_game[0][1]=='X' and chart_of_the_game[0][2]=='X') or (chart_of_the_game[1][0]=='X' and chart_of_the_game[1][1]=='X' and chart_of_the_game[1][2]=='X') or
                    (chart_of_the_game[2][0]=='X' and chart_of_the_game[2][1]=='X' and chart_of_the_game[2][2]=='X') or (chart_of_the_game[0][0]=='X' and chart_of_the_game[1][1]=='X' and chart_of_the_game[2][2]=='X') or (chart_of_the_game[0][2]=='X' and chart_of_the_game[1][1]=='X' and chart_of_the_game[2][0]=='X')):
                    winner='X' 
                    self.end_of_the_game(winner)
                    self.barande(winner)
                    
                if ((chart_of_the_game[0][0]=='O' and chart_of_the_game[1][0]=='O' and chart_of_the_game[2][0]=='O') or (chart_of_the_game[0][1]=='O' and chart_of_the_game[1][1]=='O' and chart_of_the_game[2][1]=='O') or(chart_of_the_game[0][2]=='O' and chart_of_the_game[1][2]=='O' and chart_of_the_game[2][2]=='O') or (chart_of_the_game[0][0]=='O' and chart_of_the_game[0][1]=='O' and chart_of_the_game[0][2]=='O') or (chart_of_the_game[1][0]=='O' and chart_of_the_game[1][1]=='O' and chart_of_the_game[1][2]=='O' ) or
                    (chart_of_the_game[2][0]=='O' and chart_of_the_game[2][1]=='O' and chart_of_the_game[2][2]=='O') or (chart_of_the_game[0][2]=='O' and chart_of_the_game[1][1]=='O' and chart_of_the_game[2][0]=='O') or (chart_of_the_game[0][0]=='O' and chart_of_the_game[1][1]=='O' and chart_of_the_game[2][2]=='O')):
                    winner='O'
                    self.end_of_the_game(winner)
                    self.barande(winner)
            if tedad==4:
                if ((chart_of_the_game[0][0]=='X' and chart_of_the_game[1][0]=='X' and chart_of_the_game[2][0]=='X' and chart_of_the_game[3][0]=='X') or (chart_of_the_game[0][1]=='X' and chart_of_the_game[1][1]=='X' and chart_of_the_game[2][1]=='X' and chart_of_the_game[3][1]=='X') or (chart_of_the_game[0][2]=='X' and chart_of_the_game[1][2]=='X' and chart_of_the_game[2][2]=='X' and chart_of_the_game[3][2]=='X') or (chart_of_the_game[0][3]=='X' and chart_of_the_game[1][3]=='X' and chart_of_the_game[2][3]=='X' and chart_of_the_game[3][3]=='X') or
                    (chart_of_the_game[0][0]=='X' and chart_of_the_game[0][1]=='X' and chart_of_the_game[0][2]=='X' and chart_of_the_game[0][3]=='X') or (chart_of_the_game[1][0]=='X' and chart_of_the_game[1][1]=='X' and chart_of_the_game[1][2]=='X' and chart_of_the_game[1][3]=='X') or (chart_of_the_game[2][0]=='X' and chart_of_the_game[2][1]=='X' and chart_of_the_game[2][2]=='X' and chart_of_the_game[2][3]=='X') or (chart_of_the_game[3][0]=='X' and chart_of_the_game[3][1]=='X' and chart_of_the_game[3][2]=='X' and chart_of_the_game[3][3]=='X') or
                    (chart_of_the_game[0][0]=='X' and chart_of_the_game[1][1]=='X' and chart_of_the_game[2][2]=='X' and chart_of_the_game[3][3]=='X') or (chart_of_the_game[0][3]=='X' and chart_of_the_game[1][2]=='X' and chart_of_the_game[2][1]=='X' and chart_of_the_game[3][0]=='X')):
                    winner='X'
                    self.end_of_the_game(winner)
                    self.barande(winner)
                if ((chart_of_the_game[0][0]=='O' and chart_of_the_game[1][0]=='O' and chart_of_the_game[2][0]=='O' and chart_of_the_game[3][0]=='O') or (chart_of_the_game[0][1]=='O' and chart_of_the_game[1][1]=='O' and chart_of_the_game[2][1]=='O' and chart_of_the_game[3][1]=='O') or (chart_of_the_game[0][2]=='O' and chart_of_the_game[1][2]=='O' and chart_of_the_game[2][2]=='O' and chart_of_the_game[3][2]=='O') or (chart_of_the_game[0][3]=='O' and chart_of_the_game[1][3]=='O' and chart_of_the_game[2][3]=='O' and chart_of_the_game[3][3]=='O') or
                    (chart_of_the_game[0][0]=='O' and chart_of_the_game[0][1]=='O' and chart_of_the_game[0][2]=='O' and chart_of_the_game[0][3]=='O') or (chart_of_the_game[1][0]=='O' and chart_of_the_game[1][1]=='O' and chart_of_the_game[1][2]=='O' and chart_of_the_game[1][3]=='O') or (chart_of_the_game[2][0]=='O' and chart_of_the_game[2][1]=='O' and chart_of_the_game[2][2]=='O' and chart_of_the_game[2][3]=='O') or (chart_of_the_game[3][0]=='O' and chart_of_the_game[3][1]=='O' and chart_of_the_game[3][2]=='O' and chart_of_the_game[3][3]=='O') or
                    (chart_of_the_game[0][0]=='O' and chart_of_the_game[1][1]=='O' and chart_of_the_game[2][2]=='O' and chart_of_the_game[3][3]=='O') or (chart_of_the_game[0][3]=='O' and chart_of_the_game[1][2]=='O' and chart_of_the_game[2][1]=='O' and chart_of_the_game[3][0]=='O')):
                    winner='O'
                    self.end_of_the_game(winner)
                    self.barande(winner)
            if tedad==5:
                if((chart_of_the_game[0][0]=='X' and chart_of_the_game[0][1]=='X' and chart_of_the_game[0][2]=='X' and chart_of_the_game[0][3]=='X' and chart_of_the_game[0][4]=='X') or (chart_of_the_game[1][0]=='X' and chart_of_the_game[1][1]=='X' and chart_of_the_game[1][2]=='X' and chart_of_the_game[1][3]=='X' and chart_of_the_game[1][4]=='X') or (chart_of_the_game[2][0]=='X' and chart_of_the_game[2][1]=='X' and chart_of_the_game[2][2]=='X' and chart_of_the_game[2][3]=='X' and chart_of_the_game[2][4]=='X') or 
                   (chart_of_the_game[3][0]=='X' and chart_of_the_game[3][1]=='X' and chart_of_the_game[3][2]=='X' and chart_of_the_game[3][3]=='X' and chart_of_the_game[3][4]=='X') or (chart_of_the_game[4][0]=='X' and chart_of_the_game[4][1]=='X' and chart_of_the_game[4][2]=='X' and chart_of_the_game[4][3]=='X' and chart_of_the_game[4][4]=='X') or (chart_of_the_game[0][0]=='X' and chart_of_the_game[1][0]=='X' and chart_of_the_game[2][0]=='X' and chart_of_the_game[3][0]=='X' and chart_of_the_game[4][0]=='X') or 
                   (chart_of_the_game[0][1]=='X' and chart_of_the_game[1][1]=='X' and chart_of_the_game[2][1]=='X' and chart_of_the_game[3][1]=='X' and chart_of_the_game[4][1]=='X') or (chart_of_the_game[0][2]=='X' and chart_of_the_game[1][2]=='X' and chart_of_the_game[2][2]=='X' and chart_of_the_game[3][2]=='X' and chart_of_the_game[4][2]=='X') or (chart_of_the_game[0][3]=='X' and chart_of_the_game[1][3]=='X' and chart_of_the_game[2][3]=='X' and chart_of_the_game[3][3]=='X' and chart_of_the_game[4][3]=='X') or 
                   (chart_of_the_game[0][4]=='X' and chart_of_the_game[1][4]=='X' and chart_of_the_game[2][4]=='X' and chart_of_the_game[3][4]=='X' and chart_of_the_game[4][4]=='X') or (chart_of_the_game[0][0]=='X' and chart_of_the_game[1][1]=='X' and chart_of_the_game[2][2]=='X' and chart_of_the_game[3][3]=='X' and chart_of_the_game[4][4]=='X') or (chart_of_the_game[0][4]=='X' and chart_of_the_game[1][3]=='X' and chart_of_the_game[2][2]=='X' and chart_of_the_game[3][1]=='X' and chart_of_the_game[4][0]=='X')):
                    winner='X'
                    self.end_of_the_game(winner)
                    self.barande(winner)
                if((chart_of_the_game[0][0]=='O' and chart_of_the_game[0][1]=='O' and chart_of_the_game[0][2]=='O' and chart_of_the_game[0][3]=='O' and chart_of_the_game[0][4]=='O') or (chart_of_the_game[1][0]=='O' and chart_of_the_game[1][1]=='O' and chart_of_the_game[1][2]=='O' and chart_of_the_game[1][3]=='O' and chart_of_the_game[1][4]=='O') or (chart_of_the_game[2][0]=='O' and chart_of_the_game[2][1]=='O' and chart_of_the_game[2][2]=='O' and chart_of_the_game[2][3]=='O' and chart_of_the_game[2][4]=='O') or 
                   (chart_of_the_game[3][0]=='O' and chart_of_the_game[3][1]=='O' and chart_of_the_game[3][2]=='O' and chart_of_the_game[3][3]=='O' and chart_of_the_game[3][4]=='O') or (chart_of_the_game[4][0]=='O' and chart_of_the_game[4][1]=='O' and chart_of_the_game[4][2]=='O' and chart_of_the_game[4][3]=='O' and chart_of_the_game[4][4]=='O') or (chart_of_the_game[0][0]=='O' and chart_of_the_game[1][0]=='O' and chart_of_the_game[2][0]=='O' and chart_of_the_game[3][0]=='O' and chart_of_the_game[4][0]=='O') or 
                   (chart_of_the_game[0][1]=='O' and chart_of_the_game[1][1]=='O' and chart_of_the_game[2][1]=='O' and chart_of_the_game[3][1]=='O' and chart_of_the_game[4][1]=='O') or (chart_of_the_game[0][2]=='O' and chart_of_the_game[1][2]=='O' and chart_of_the_game[2][2]=='O' and chart_of_the_game[3][2]=='O' and chart_of_the_game[4][2]=='O') or (chart_of_the_game[0][3]=='O' and chart_of_the_game[1][3]=='O' and chart_of_the_game[2][3]=='O' and chart_of_the_game[3][3]=='O' and chart_of_the_game[4][3]=='O') or 
                   (chart_of_the_game[0][4]=='O' and chart_of_the_game[1][4]=='O' and chart_of_the_game[2][4]=='O' and chart_of_the_game[3][4]=='O' and chart_of_the_game[4][4]=='O') or (chart_of_the_game[0][0]=='O' and chart_of_the_game[1][1]=='O' and chart_of_the_game[2][2]=='O' and chart_of_the_game[3][3]=='O' and chart_of_the_game[4][4]=='O') or (chart_of_the_game[0][4]=='O' and chart_of_the_game[1][3]=='O' and chart_of_the_game[2][2]=='O' and chart_of_the_game[3][1]=='O' and chart_of_the_game[4][0]=='O')):
                    winner='O'
                    self.end_of_the_game(winner)
                    self.barande(winner)
            if tedad==6:
                if((chart_of_the_game[0][0]=='X' and chart_of_the_game[0][1]=='X' and chart_of_the_game[0][2]=='X' and chart_of_the_game[0][3]=='X' and chart_of_the_game[0][4]=='X' and chart_of_the_game[0][5]=='X') or (chart_of_the_game[1][0]=='X' and chart_of_the_game[1][1]=='X' and chart_of_the_game[1][2]=='X' and chart_of_the_game[1][3]=='X' and chart_of_the_game[1][4]=='X' and chart_of_the_game[1][5]=='X') or (chart_of_the_game[2][0]=='X' and chart_of_the_game[2][1]=='X' and chart_of_the_game[2][2]=='X' and chart_of_the_game[2][3]=='X' and chart_of_the_game[2][4]=='X' and chart_of_the_game[2][5]=='X') or 
                   (chart_of_the_game[3][0]=='X' and chart_of_the_game[3][1]=='X' and chart_of_the_game[3][2]=='X' and chart_of_the_game[3][3]=='X' and chart_of_the_game[3][4]=='X' and chart_of_the_game[3][5]=='X') or (chart_of_the_game[4][0]=='X' and chart_of_the_game[4][1]=='X' and chart_of_the_game[4][2]=='X' and chart_of_the_game[4][3]=='X' and chart_of_the_game[4][4]=='X' and chart_of_the_game[4][5]=='X') or (chart_of_the_game[5][0]=='X' and chart_of_the_game[5][1]=='X' and chart_of_the_game[5][2]=='X' and chart_of_the_game[5][3]=='X' and chart_of_the_game[5][4]=='X' and chart_of_the_game[5][5]=='X') or
                   (chart_of_the_game[0][0]=='X' and chart_of_the_game[1][0]=='X' and chart_of_the_game[2][0]=='X' and chart_of_the_game[3][0]=='X' and chart_of_the_game[4][0]=='X' and chart_of_the_game[5][0]=='X') or (chart_of_the_game[0][1]=='X' and chart_of_the_game[1][1]=='X' and chart_of_the_game[2][1]=='X' and chart_of_the_game[3][1]=='X' and chart_of_the_game[4][1]=='X' and chart_of_the_game[5][1]=='X') or (chart_of_the_game[0][2]=='X' and chart_of_the_game[1][2]=='X' and chart_of_the_game[2][2]=='X' and chart_of_the_game[3][2]=='X' and chart_of_the_game[4][2]=='X' and chart_of_the_game[5][2]=='X') or 
                   (chart_of_the_game[0][3]=='X' and chart_of_the_game[1][3]=='X' and chart_of_the_game[2][3]=='X' and chart_of_the_game[3][3]=='X' and chart_of_the_game[4][3]=='X' and chart_of_the_game[5][3]=='X') or (chart_of_the_game[0][4]=='X' and chart_of_the_game[1][4]=='X' and chart_of_the_game[2][4]=='X' and chart_of_the_game[3][4]=='X' and chart_of_the_game[4][4]=='X' and chart_of_the_game[5][4]=='X') or (chart_of_the_game[0][5]=='X' and chart_of_the_game[1][5]=='X' and chart_of_the_game[2][5]=='X' and chart_of_the_game[3][5]=='X' and chart_of_the_game[4][5]=='X' and chart_of_the_game[5][5]=='X') or
                   (chart_of_the_game[0][0]=='X' and chart_of_the_game[1][1]=='X' and chart_of_the_game[2][2]=='X' and chart_of_the_game[3][3]=='X' and chart_of_the_game[4][4]=='X' and chart_of_the_game[5][5]=='X') or (chart_of_the_game[0][5]=='X' and chart_of_the_game[1][4]=='X' and chart_of_the_game[2][3]=='X' and chart_of_the_game[3][2]=='X' and chart_of_the_game[4][1]=='X' and chart_of_the_game[5][0]=='X')):
                    winner='X'
                    self.end_of_the_game(winner)
                    self.barande(winner)
                if((chart_of_the_game[0][0]=='O' and chart_of_the_game[0][1]=='O' and chart_of_the_game[0][2]=='O' and chart_of_the_game[0][3]=='O' and chart_of_the_game[0][4]=='O' and chart_of_the_game[0][5]=='O') or (chart_of_the_game[1][0]=='O' and chart_of_the_game[1][1]=='O' and chart_of_the_game[1][2]=='O' and chart_of_the_game[1][3]=='O' and chart_of_the_game[1][4]=='O' and chart_of_the_game[1][5]=='O') or (chart_of_the_game[2][0]=='O' and chart_of_the_game[2][1]=='O' and chart_of_the_game[2][2]=='O' and chart_of_the_game[2][3]=='O' and chart_of_the_game[2][4]=='O' and chart_of_the_game[2][5]=='O') or 
                   (chart_of_the_game[3][0]=='O' and chart_of_the_game[3][1]=='O' and chart_of_the_game[3][2]=='O' and chart_of_the_game[3][3]=='O' and chart_of_the_game[3][4]=='O' and chart_of_the_game[3][5]=='O') or (chart_of_the_game[4][0]=='O' and chart_of_the_game[4][1]=='O' and chart_of_the_game[4][2]=='O' and chart_of_the_game[4][3]=='O' and chart_of_the_game[4][4]=='O' and chart_of_the_game[4][5]=='O') or (chart_of_the_game[5][0]=='O' and chart_of_the_game[5][1]=='O' and chart_of_the_game[5][2]=='O' and chart_of_the_game[5][3]=='O' and chart_of_the_game[5][4]=='O' and chart_of_the_game[5][5]=='O') or
                   (chart_of_the_game[0][0]=='O' and chart_of_the_game[1][0]=='O' and chart_of_the_game[2][0]=='O' and chart_of_the_game[3][0]=='O' and chart_of_the_game[4][0]=='O' and chart_of_the_game[5][0]=='O') or (chart_of_the_game[0][1]=='O' and chart_of_the_game[1][1]=='O' and chart_of_the_game[2][1]=='O' and chart_of_the_game[3][1]=='O' and chart_of_the_game[4][1]=='O' and chart_of_the_game[5][1]=='O') or (chart_of_the_game[0][2]=='O' and chart_of_the_game[1][2]=='O' and chart_of_the_game[2][2]=='O' and chart_of_the_game[3][2]=='O' and chart_of_the_game[4][2]=='O' and chart_of_the_game[5][2]=='O') or 
                   (chart_of_the_game[0][3]=='O' and chart_of_the_game[1][3]=='O' and chart_of_the_game[2][3]=='O' and chart_of_the_game[3][3]=='O' and chart_of_the_game[4][3]=='O' and chart_of_the_game[5][3]=='O') or (chart_of_the_game[0][4]=='O' and chart_of_the_game[1][4]=='O' and chart_of_the_game[2][4]=='O' and chart_of_the_game[3][4]=='O' and chart_of_the_game[4][4]=='O' and chart_of_the_game[5][4]=='O') or (chart_of_the_game[0][5]=='O' and chart_of_the_game[1][5]=='O' and chart_of_the_game[2][5]=='O' and chart_of_the_game[3][5]=='O' and chart_of_the_game[4][5]=='O' and chart_of_the_game[5][5]=='O') or
                   (chart_of_the_game[0][0]=='O' and chart_of_the_game[1][1]=='O' and chart_of_the_game[2][2]=='O' and chart_of_the_game[3][3]=='O' and chart_of_the_game[4][4]=='O' and chart_of_the_game[5][5]=='O') or (chart_of_the_game[0][5]=='O' and chart_of_the_game[1][4]=='O' and chart_of_the_game[2][3]=='O' and chart_of_the_game[3][2]=='O' and chart_of_the_game[4][1]=='O' and chart_of_the_game[5][0]=='O')):
                    winner='O'
                    self.end_of_the_game(winner)
                    self.barande(winner)
            if tedad==7:
                if ((chart_of_the_game[0][0]=='X' and chart_of_the_game[0][1]=='X' and chart_of_the_game[0][2]=='X' and chart_of_the_game[0][3]=='X' and chart_of_the_game[0][4]=='X' and chart_of_the_game[0][5]=='X' and chart_of_the_game[0][6]=='X') or (chart_of_the_game[1][0]=='X' and chart_of_the_game[1][1]=='X' and chart_of_the_game[1][2]=='X' and chart_of_the_game[1][3]=='X' and chart_of_the_game[1][4]=='X' and chart_of_the_game[1][5]=='X' and chart_of_the_game[1][6]=='X') or (chart_of_the_game[2][0]=='X' and chart_of_the_game[2][1]=='X' and chart_of_the_game[2][2]=='X' and chart_of_the_game[2][3]=='X' and chart_of_the_game[2][4]=='X' and chart_of_the_game[2][5]=='X' and chart_of_the_game[2][6]=='X') or
                    (chart_of_the_game[3][0]=='X' and chart_of_the_game[3][1]=='X' and chart_of_the_game[3][2]=='X' and chart_of_the_game[3][3]=='X' and chart_of_the_game[3][4]=='X' and chart_of_the_game[3][5]=='X' and chart_of_the_game[3][6]=='X') or (chart_of_the_game[4][0]=='X' and chart_of_the_game[4][1]=='X' and chart_of_the_game[4][2]=='X' and chart_of_the_game[4][3]=='X' and chart_of_the_game[4][4]=='X' and chart_of_the_game[4][5]=='X' and chart_of_the_game[4][6]=='X') or (chart_of_the_game[5][0]=='X' and chart_of_the_game[5][1]=='X' and chart_of_the_game[5][2]=='X' and chart_of_the_game[5][3]=='X' and chart_of_the_game[5][4]=='X' and chart_of_the_game[5][5]=='X' and chart_of_the_game[5][6]=='X') or
                    (chart_of_the_game[6][0]=='X' and chart_of_the_game[6][1]=='X' and chart_of_the_game[6][2]=='X' and chart_of_the_game[6][3]=='X' and chart_of_the_game[6][4]=='X' and chart_of_the_game[6][5]=='X' and chart_of_the_game[6][6]=='X') or (chart_of_the_game[0][0]=='X' and chart_of_the_game[1][0]=='X' and chart_of_the_game[2][0]=='X' and chart_of_the_game[3][0]=='X' and chart_of_the_game[4][0]=='X' and chart_of_the_game[5][0]=='X' and chart_of_the_game[6][0]=='X') or (chart_of_the_game[0][1]=='X' and chart_of_the_game[1][1]=='X' and chart_of_the_game[2][1]=='X' and chart_of_the_game[3][1]=='X' and chart_of_the_game[4][1]=='X' and chart_of_the_game[5][1]=='X' and chart_of_the_game[6][1]=='X') or 
                    (chart_of_the_game[0][2]=='X' and chart_of_the_game[1][2]=='X' and chart_of_the_game[2][2]=='X' and chart_of_the_game[3][2]=='X' and chart_of_the_game[4][2]=='X' and chart_of_the_game[5][2]=='X' and chart_of_the_game[6][2]=='X') or (chart_of_the_game[0][3]=='X' and chart_of_the_game[1][3]=='X' and chart_of_the_game[2][3]=='X' and chart_of_the_game[3][3]=='X' and chart_of_the_game[4][3]=='X' and chart_of_the_game[5][3]=='X' and chart_of_the_game[6][3]=='X') or (chart_of_the_game[0][4]=='X' and chart_of_the_game[1][4]=='X' and chart_of_the_game[2][4]=='X' and chart_of_the_game[3][4]=='X' and chart_of_the_game[4][4]=='X' and chart_of_the_game[5][4]=='X' and chart_of_the_game[6][4]=='X') or
                    (chart_of_the_game[0][5]=='X' and chart_of_the_game[1][5]=='X' and chart_of_the_game[2][5]=='X' and chart_of_the_game[3][5]=='X' and chart_of_the_game[4][5]=='X' and chart_of_the_game[5][5]=='X' and chart_of_the_game[6][5]=='X') or (chart_of_the_game[0][6]=='X' and chart_of_the_game[1][6]=='X' and chart_of_the_game[2][6]=='X' and chart_of_the_game[3][6]=='X' and chart_of_the_game[4][6]=='X' and chart_of_the_game[5][6]=='X' and chart_of_the_game[6][6]=='X') or (chart_of_the_game[0][0]=='X' and chart_of_the_game[1][1]=='X' and chart_of_the_game[2][2]=='X' and chart_of_the_game[3][3]=='X' and chart_of_the_game[4][4]=='X' and chart_of_the_game[5][5]=='X' and chart_of_the_game[6][6]=='X') or
                    (chart_of_the_game[0][6]=='X' and chart_of_the_game[1][5]=='X' and chart_of_the_game[2][4]=='X' and chart_of_the_game[3][3]=='X' and chart_of_the_game[4][2]=='X' and chart_of_the_game[5][1]=='X' and chart_of_the_game[6][0]=='X')):
                    winner='X'
                    self.end_of_the_game(winner)
                    self.barande(winner)
                if ((chart_of_the_game[0][0]=='O' and chart_of_the_game[0][1]=='O' and chart_of_the_game[0][2]=='O' and chart_of_the_game[0][3]=='O' and chart_of_the_game[0][4]=='O' and chart_of_the_game[0][5]=='O' and chart_of_the_game[0][6]=='O') or (chart_of_the_game[1][0]=='O' and chart_of_the_game[1][1]=='O' and chart_of_the_game[1][2]=='O' and chart_of_the_game[1][3]=='O' and chart_of_the_game[1][4]=='O' and chart_of_the_game[1][5]=='O' and chart_of_the_game[1][6]=='O') or (chart_of_the_game[2][0]=='O' and chart_of_the_game[2][1]=='O' and chart_of_the_game[2][2]=='O' and chart_of_the_game[2][3]=='O' and chart_of_the_game[2][4]=='O' and chart_of_the_game[2][5]=='O' and chart_of_the_game[2][6]=='O') or
                    (chart_of_the_game[3][0]=='O' and chart_of_the_game[3][1]=='O' and chart_of_the_game[3][2]=='O' and chart_of_the_game[3][3]=='O' and chart_of_the_game[3][4]=='O' and chart_of_the_game[3][5]=='O' and chart_of_the_game[3][6]=='O') or (chart_of_the_game[4][0]=='O' and chart_of_the_game[4][1]=='O' and chart_of_the_game[4][2]=='O' and chart_of_the_game[4][3]=='O' and chart_of_the_game[4][4]=='O' and chart_of_the_game[4][5]=='O' and chart_of_the_game[4][6]=='O') or (chart_of_the_game[5][0]=='O' and chart_of_the_game[5][1]=='O' and chart_of_the_game[5][2]=='O' and chart_of_the_game[5][3]=='O' and chart_of_the_game[5][4]=='O' and chart_of_the_game[5][5]=='O' and chart_of_the_game[5][6]=='O') or
                    (chart_of_the_game[6][0]=='O' and chart_of_the_game[6][1]=='O' and chart_of_the_game[6][2]=='O' and chart_of_the_game[6][3]=='O' and chart_of_the_game[6][4]=='O' and chart_of_the_game[6][5]=='O' and chart_of_the_game[6][6]=='O') or (chart_of_the_game[0][0]=='O' and chart_of_the_game[1][0]=='O' and chart_of_the_game[2][0]=='O' and chart_of_the_game[3][0]=='O' and chart_of_the_game[4][0]=='O' and chart_of_the_game[5][0]=='O' and chart_of_the_game[6][0]=='O') or (chart_of_the_game[0][1]=='O' and chart_of_the_game[1][1]=='O' and chart_of_the_game[2][1]=='O' and chart_of_the_game[3][1]=='O' and chart_of_the_game[4][1]=='O' and chart_of_the_game[5][1]=='O' and chart_of_the_game[6][1]=='O') or 
                    (chart_of_the_game[0][2]=='O' and chart_of_the_game[1][2]=='O' and chart_of_the_game[2][2]=='O' and chart_of_the_game[3][2]=='O' and chart_of_the_game[4][2]=='O' and chart_of_the_game[5][2]=='O' and chart_of_the_game[6][2]=='O') or (chart_of_the_game[0][3]=='O' and chart_of_the_game[1][3]=='O' and chart_of_the_game[2][3]=='O' and chart_of_the_game[3][3]=='O' and chart_of_the_game[4][3]=='O' and chart_of_the_game[5][3]=='O' and chart_of_the_game[6][3]=='O') or (chart_of_the_game[0][4]=='O' and chart_of_the_game[1][4]=='O' and chart_of_the_game[2][4]=='O' and chart_of_the_game[3][4]=='O' and chart_of_the_game[4][4]=='O' and chart_of_the_game[5][4]=='O' and chart_of_the_game[6][4]=='O') or
                    (chart_of_the_game[0][5]=='O' and chart_of_the_game[1][5]=='O' and chart_of_the_game[2][5]=='O' and chart_of_the_game[3][5]=='O' and chart_of_the_game[4][5]=='O' and chart_of_the_game[5][5]=='O' and chart_of_the_game[6][5]=='O') or (chart_of_the_game[0][6]=='O' and chart_of_the_game[1][6]=='O' and chart_of_the_game[2][6]=='O' and chart_of_the_game[3][6]=='O' and chart_of_the_game[4][6]=='O' and chart_of_the_game[5][6]=='O' and chart_of_the_game[6][6]=='O') or (chart_of_the_game[0][0]=='O' and chart_of_the_game[1][1]=='O' and chart_of_the_game[2][2]=='O' and chart_of_the_game[3][3]=='O' and chart_of_the_game[4][4]=='O' and chart_of_the_game[5][5]=='O' and chart_of_the_game[6][6]=='O') or
                    (chart_of_the_game[0][6]=='O' and chart_of_the_game[1][5]=='O' and chart_of_the_game[2][4]=='O' and chart_of_the_game[3][3]=='O' and chart_of_the_game[4][2]=='O' and chart_of_the_game[5][1]=='O' and chart_of_the_game[6][0]=='O')):
                    winner='O'
                    self.end_of_the_game(winner)
                    self.barande(winner)
            if tedad==8:
                if ((chart_of_the_game[0][0]=='X' and chart_of_the_game[0][1]=='X' and chart_of_the_game[0][2]=='X' and chart_of_the_game[0][3]=='X' and chart_of_the_game[0][4]=='X' and chart_of_the_game[0][5]=='X' and chart_of_the_game[0][6]=='X' and chart_of_the_game[0][7]=='X') or (chart_of_the_game[1][0]=='X' and chart_of_the_game[1][1]=='X' and chart_of_the_game[1][2]=='X' and chart_of_the_game[1][3]=='X' and chart_of_the_game[1][4]=='X' and chart_of_the_game[1][5]=='X' and chart_of_the_game[1][6]=='X' and chart_of_the_game[1][7]=='X') or (chart_of_the_game[2][0]=='X' and chart_of_the_game[2][1]=='X' and chart_of_the_game[2][2]=='X' and chart_of_the_game[2][3]=='X' and chart_of_the_game[2][4]=='X' and chart_of_the_game[2][5]=='X' and chart_of_the_game[2][6]=='X' and chart_of_the_game[2][7]=='X') or
                    (chart_of_the_game[3][0]=='X' and chart_of_the_game[3][1]=='X' and chart_of_the_game[3][2]=='X' and chart_of_the_game[3][3]=='X' and chart_of_the_game[3][4]=='X' and chart_of_the_game[3][5]=='X' and chart_of_the_game[3][6]=='X' and chart_of_the_game[3][7]=='X') or (chart_of_the_game[4][0]=='X' and chart_of_the_game[4][1]=='X' and chart_of_the_game[4][2]=='X' and chart_of_the_game[4][3]=='X' and chart_of_the_game[4][4]=='X' and chart_of_the_game[4][5]=='X' and chart_of_the_game[4][6]=='X' and chart_of_the_game[4][7]=='X') or (chart_of_the_game[5][0]=='X' and chart_of_the_game[5][1]=='X' and chart_of_the_game[5][2]=='X' and chart_of_the_game[5][3]=='X' and chart_of_the_game[5][4]=='X' and chart_of_the_game[5][5]=='X' and chart_of_the_game[5][6]=='X' and chart_of_the_game[5][7]=='X') or 
                    (chart_of_the_game[6][0]=='X' and chart_of_the_game[6][1]=='X' and chart_of_the_game[6][2]=='X' and chart_of_the_game[6][3]=='X' and chart_of_the_game[6][4]=='X' and chart_of_the_game[6][5]=='X' and chart_of_the_game[6][6]=='X' and chart_of_the_game[6][7]=='X') or (chart_of_the_game[7][0]=='X' and chart_of_the_game[7][1]=='X' and chart_of_the_game[7][2]=='X' and chart_of_the_game[7][3]=='X' and chart_of_the_game[7][4]=='X' and chart_of_the_game[7][5]=='X' and chart_of_the_game[7][6]=='X' and chart_of_the_game[7][7]=='X') or (chart_of_the_game[0][0]=='X' and chart_of_the_game[1][0]=='X' and chart_of_the_game[2][0]=='X' and chart_of_the_game[3][0]=='X' and chart_of_the_game[4][0]=='X' and chart_of_the_game[5][0]=='X' and chart_of_the_game[6][0]=='X' and chart_of_the_game[7][0]=='X') or 
                    (chart_of_the_game[0][1]=='X' and chart_of_the_game[1][1]=='X' and chart_of_the_game[2][1]=='X' and chart_of_the_game[3][1]=='X' and chart_of_the_game[4][1]=='X' and chart_of_the_game[5][1]=='X' and chart_of_the_game[6][1]=='X' and chart_of_the_game[7][1]=='X') or (chart_of_the_game[0][2]=='X' and chart_of_the_game[1][2]=='X' and chart_of_the_game[2][2]=='X' and chart_of_the_game[3][2]=='X' and chart_of_the_game[4][2]=='X' and chart_of_the_game[5][2]=='X' and chart_of_the_game[6][2]=='X' and chart_of_the_game[7][2]=='X') or (chart_of_the_game[0][3]=='X' and chart_of_the_game[1][3]=='X' and chart_of_the_game[2][3]=='X' and chart_of_the_game[3][3]=='X' and chart_of_the_game[4][3]=='X' and chart_of_the_game[5][3]=='X' and chart_of_the_game[6][3]=='X' and chart_of_the_game[7][3]=='X') or
                    (chart_of_the_game[0][4]=='X' and chart_of_the_game[1][4]=='X' and chart_of_the_game[2][4]=='X' and chart_of_the_game[3][4]=='X' and chart_of_the_game[4][4]=='X' and chart_of_the_game[5][4]=='X' and chart_of_the_game[6][4]=='X' and chart_of_the_game[7][4]=='X') or (chart_of_the_game[0][5]=='X' and chart_of_the_game[1][5]=='X' and chart_of_the_game[2][5]=='X' and chart_of_the_game[3][5]=='X' and chart_of_the_game[4][5]=='X' and chart_of_the_game[5][5]=='X' and chart_of_the_game[6][5]=='X' and chart_of_the_game[7][5]=='X') or (chart_of_the_game[0][6]=='X' and chart_of_the_game[1][6]=='X' and chart_of_the_game[2][6]=='X' and chart_of_the_game[3][6]=='X' and chart_of_the_game[4][6]=='X' and chart_of_the_game[5][6]=='X' and chart_of_the_game[6][6]=='X' and chart_of_the_game[7][6]=='X') or
                    (chart_of_the_game[0][7]=='X' and chart_of_the_game[1][7]=='X' and chart_of_the_game[2][7]=='X' and chart_of_the_game[3][7]=='X' and chart_of_the_game[4][7]=='X' and chart_of_the_game[5][7]=='X' and chart_of_the_game[6][7]=='X' and chart_of_the_game[7][7]=='X') or (chart_of_the_game[0][0]=='X' and chart_of_the_game[1][1]=='X' and chart_of_the_game[2][2]=='X' and chart_of_the_game[3][3]=='X' and chart_of_the_game[4][4]=='X' and chart_of_the_game[5][5]=='X' and chart_of_the_game[6][6]=='X' and chart_of_the_game[7][7]=='X') or (chart_of_the_game[0][7]=='X' and chart_of_the_game[1][6]=='X' and chart_of_the_game[2][5]=='X' and chart_of_the_game[3][4]=='X' and chart_of_the_game[4][3]=='X' and chart_of_the_game[5][2]=='X' and chart_of_the_game[6][1]=='X' and chart_of_the_game[7][0]=='X')):
                    winner='X'
                    self.end_of_the_game(winner)
                    self.barande(winner)
                if ((chart_of_the_game[0][0]=='O' and chart_of_the_game[0][1]=='O' and chart_of_the_game[0][2]=='O' and chart_of_the_game[0][3]=='O' and chart_of_the_game[0][4]=='O' and chart_of_the_game[0][5]=='O' and chart_of_the_game[0][6]=='O' and chart_of_the_game[0][7]=='O') or (chart_of_the_game[1][0]=='O' and chart_of_the_game[1][1]=='O' and chart_of_the_game[1][2]=='O' and chart_of_the_game[1][3]=='O' and chart_of_the_game[1][4]=='O' and chart_of_the_game[1][5]=='O' and chart_of_the_game[1][6]=='O' and chart_of_the_game[1][7]=='O') or (chart_of_the_game[2][0]=='O' and chart_of_the_game[2][1]=='O' and chart_of_the_game[2][2]=='O' and chart_of_the_game[2][3]=='O' and chart_of_the_game[2][4]=='O' and chart_of_the_game[2][5]=='O' and chart_of_the_game[2][6]=='O' and chart_of_the_game[2][7]=='O') or
                    (chart_of_the_game[3][0]=='O' and chart_of_the_game[3][1]=='O' and chart_of_the_game[3][2]=='O' and chart_of_the_game[3][3]=='O' and chart_of_the_game[3][4]=='O' and chart_of_the_game[3][5]=='O' and chart_of_the_game[3][6]=='O' and chart_of_the_game[3][7]=='O') or (chart_of_the_game[4][0]=='O' and chart_of_the_game[4][1]=='O' and chart_of_the_game[4][2]=='O' and chart_of_the_game[4][3]=='O' and chart_of_the_game[4][4]=='O' and chart_of_the_game[4][5]=='O' and chart_of_the_game[4][6]=='O' and chart_of_the_game[4][7]=='O') or (chart_of_the_game[5][0]=='O' and chart_of_the_game[5][1]=='O' and chart_of_the_game[5][2]=='O' and chart_of_the_game[5][3]=='O' and chart_of_the_game[5][4]=='O' and chart_of_the_game[5][5]=='O' and chart_of_the_game[5][6]=='O' and chart_of_the_game[5][7]=='O') or 
                    (chart_of_the_game[6][0]=='O' and chart_of_the_game[6][1]=='O' and chart_of_the_game[6][2]=='O' and chart_of_the_game[6][3]=='O' and chart_of_the_game[6][4]=='O' and chart_of_the_game[6][5]=='O' and chart_of_the_game[6][6]=='O' and chart_of_the_game[6][7]=='O') or (chart_of_the_game[7][0]=='O' and chart_of_the_game[7][1]=='O' and chart_of_the_game[7][2]=='O' and chart_of_the_game[7][3]=='O' and chart_of_the_game[7][4]=='O' and chart_of_the_game[7][5]=='O' and chart_of_the_game[7][6]=='O' and chart_of_the_game[7][7]=='O') or (chart_of_the_game[0][0]=='O' and chart_of_the_game[1][0]=='O' and chart_of_the_game[2][0]=='O' and chart_of_the_game[3][0]=='O' and chart_of_the_game[4][0]=='O' and chart_of_the_game[5][0]=='O' and chart_of_the_game[6][0]=='O' and chart_of_the_game[7][0]=='O') or 
                    (chart_of_the_game[0][1]=='O' and chart_of_the_game[1][1]=='O' and chart_of_the_game[2][1]=='O' and chart_of_the_game[3][1]=='O' and chart_of_the_game[4][1]=='O' and chart_of_the_game[5][1]=='O' and chart_of_the_game[6][1]=='O' and chart_of_the_game[7][1]=='O') or (chart_of_the_game[0][2]=='O' and chart_of_the_game[1][2]=='O' and chart_of_the_game[2][2]=='O' and chart_of_the_game[3][2]=='O' and chart_of_the_game[4][2]=='O' and chart_of_the_game[5][2]=='O' and chart_of_the_game[6][2]=='O' and chart_of_the_game[7][2]=='O') or (chart_of_the_game[0][3]=='O' and chart_of_the_game[1][3]=='O' and chart_of_the_game[2][3]=='O' and chart_of_the_game[3][3]=='O' and chart_of_the_game[4][3]=='O' and chart_of_the_game[5][3]=='O' and chart_of_the_game[6][3]=='O' and chart_of_the_game[7][3]=='O') or
                    (chart_of_the_game[0][4]=='O' and chart_of_the_game[1][4]=='O' and chart_of_the_game[2][4]=='O' and chart_of_the_game[3][4]=='O' and chart_of_the_game[4][4]=='O' and chart_of_the_game[5][4]=='O' and chart_of_the_game[6][4]=='O' and chart_of_the_game[7][4]=='O') or (chart_of_the_game[0][5]=='O' and chart_of_the_game[1][5]=='O' and chart_of_the_game[2][5]=='O' and chart_of_the_game[3][5]=='O' and chart_of_the_game[4][5]=='O' and chart_of_the_game[5][5]=='O' and chart_of_the_game[6][5]=='O' and chart_of_the_game[7][5]=='O') or (chart_of_the_game[0][6]=='O' and chart_of_the_game[1][6]=='O' and chart_of_the_game[2][6]=='O' and chart_of_the_game[3][6]=='O' and chart_of_the_game[4][6]=='O' and chart_of_the_game[5][6]=='O' and chart_of_the_game[6][6]=='O' and chart_of_the_game[7][6]=='O') or
                    (chart_of_the_game[0][7]=='O' and chart_of_the_game[1][7]=='O' and chart_of_the_game[2][7]=='O' and chart_of_the_game[3][7]=='O' and chart_of_the_game[4][7]=='O' and chart_of_the_game[5][7]=='O' and chart_of_the_game[6][7]=='O' and chart_of_the_game[7][7]=='O') or (chart_of_the_game[0][0]=='O' and chart_of_the_game[1][1]=='O' and chart_of_the_game[2][2]=='O' and chart_of_the_game[3][3]=='O' and chart_of_the_game[4][4]=='O' and chart_of_the_game[5][5]=='O' and chart_of_the_game[6][6]=='O' and chart_of_the_game[7][7]=='O') or (chart_of_the_game[0][7]=='O' and chart_of_the_game[1][6]=='O' and chart_of_the_game[2][5]=='O' and chart_of_the_game[3][4]=='O' and chart_of_the_game[4][3]=='O' and chart_of_the_game[5][2]=='O' and chart_of_the_game[6][1]=='O' and chart_of_the_game[7][0]=='O')):
                    winner='O'
                    self.end_of_the_game(winner) 
                    self.barande(winner)
                     #####
            if winner=='X' or winner=='O':
                self.end_of_the_game(winner)
            elif por_bodan_1=='jadval por shod' and (winner!='X' or winner!='O'):
                winner='NO ONE'
                self.end_of_the_game(winner)               
            elif winner==None:
                self.complete_the_bord(chart_of_the_game)

    def barande(self,barande_3):
       self.barande_3=barande_3
                
    def end_of_the_game(self,barande1):
        if barande1=='X' or barande1=='O':
            print('')
            print('')
            print(f"Player {barande1} won")
            print('THE END')        
        elif barande1=='NO ONE':
            print(f"{barande1} won")
            print('THE END')
            
    def start_game(self):       
        self.create_bord()


tictoctoe=TicTocToe(int(input('your favorite chart: ')))
tictoctoe.start_game()
                 