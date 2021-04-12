#include <bits/stdc++.h>
using namespace std;

void board(vector<string> elements, int progress, int player,int moves);

void lines(int length){
    while(length>0){
        cout << "-";
        length--;
    }

}
void insert(vector<string> elements, int position, int player, int progress, int moves){
    cin >> position;
    if(elements[position-1] != "o" && elements[position-1] != "x" ){
        if(player == 1)
            elements[position-1] = "o";
        else
            elements[position-1] = "x"; 

        moves+=1;
        if(player==1)
        board(elements, progress, 2,moves);
        else
        board(elements, progress, 1,moves);
    } 
    else{
        cout << "Position " << position << " is already blocked.\nEnter a valid position: ";
        insert(elements,position,player,progress,moves);
    }
}
int compare(vector<string> elements, int a, int b, int c){
    if(elements[a] == elements[b] && elements[b] == elements[c])
        return 1;
    else
        return 0;
}

int checkWinner(vector<string> elements, int player){
        int win = 0;
        
        if(compare(elements,0,1,2)){
            if(elements[0] == "o")
                win = 1;
            else
                win = 2;
        }
            
        else if(compare(elements,3,4,5)){
            if(elements[0] == "o")
                win = 1;
            else
                win = 2;
        }
        else if(compare(elements,6,7,8)){
            if(elements[0] == "o")
                win = 1;
            else
                win = 2;
        }
        else if(compare(elements,0,3,6)){
            if(elements[0] == "o")
                win = 1;
            else
                win = 2;
        }
        else if(compare(elements,1,4,7))
        {
            if(elements[0] == "o")
                win = 1;
            else
                win = 2;
        }
        else if(compare(elements,2,5,8)){
            if(elements[0] == "o")
                win = 1;
            else
                win = 2;
        }
        else if(compare(elements,0,4,8)){
            if(elements[0] == "o")
                win = 1;
            else
                win = 2;
        }
        else if(compare(elements,2,4,6)){
            if(elements[0] == "o")
                win = 1;
            else
                win = 2;
        }
        else
            win=0;
            
        return win;
}

void board(vector<string> elements, int progress, int player,int moves){

    if(progress){
        system("clear");
        cout << "Welcome to Tic Tac Toe ~ Made by S Sitaraman\n";

        cout << "\n\n\t  " << elements[0] << "   |   " << elements[1] << "   |   " << elements[2] << "\n\t"; 
        lines(5); cout << " | "; lines(5); cout << " | "; lines(5); cout << endl;
        cout << "\t  " << elements[3] << "   |   " << elements[4] << "   |   " << elements[5] << "\n\t";
        lines(5); cout << " | "; lines(5); cout << " | "; lines(5); cout << endl;
        cout << "\t  " << elements[6] << "   |   " << elements[7] << "   |   " << elements[8] << "\n\n";

        if(checkWinner(elements,player) == 1){
            cout << "\nPlayer 1 wins\nThe Game has ended ..\n";
            progress = 0;
        }
        else if(checkWinner(elements,player) == 2){
            cout << "\nPlayer 2 wins\nThe Game has ended ..\n";
            progress = 0;
        }
        if(moves<9 && progress){ // Maximum number of moves are 9 in a tic tac toe game
            cout << "Player " << player << " , It's your turn\n";
            if(player == 1)
                cout << "Place \'o\' at position : ";        
            else
                cout << "Place \'x\' at position : ";        

            int position;
            insert(elements,position,player,progress,moves);
        }
        else{
            if(moves == 9 && progress){
            cout << "\nThe Game has ended , It's a draw !\n" ;}
            progress= 0; //If progress is false , game ends
        }
    }
    else{
        cout << "\nThe Game has ended , Player " << player << " Won!\n";
    }
}


int main(){
    
    vector<string> elements;
    int progress = 1,moves=0;
    for(int i=0;i<10;i++)
        elements.push_back(to_string(i+1));
    
    cout << "Welcome to Tic Tac Toe ~ Made by S Sitaraman\n";
    board(elements,progress,1,moves);

    return 0;
}


