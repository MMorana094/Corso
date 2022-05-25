/*
  Write a program that simulates a risk/risiko fight using 6 dices.

  How does it work?
  When a player attacks another player he uses 3 dices, the red is always the attacker and the blue is the defender.

  You have to compare the dice with the highest number to simulate the fight.
  N = first highest number
  M = second highest number
  O = third highest number

  If the numbers are equal, the defensor (blue) wins.

  Output:
  Red dices:
  6 (N)
  3 (M)
  2 (O)

  Blue dices:
  5 (N)
  3 (M)
  1 (O)

    R    B
  N 6 vs 5 => red win
  M 3 vs 3 => blue win
  O 2 vs 1 => red win
*/
#include <iostream>
#include <cstdlib>

#define turni 3

using namespace std;

class dice {
    private:
      int num_dices;
      int num_faces;
      int **value;
      int len;

    public:
      dice(int num_dices, int num_faces){
        this->num_dices = num_dices;
        this->num_faces = num_faces;
        this->len = num_dices;
        this->value = new int*[num_dices];
        for(int i=0; i<len; i++){
          value[i] = new int(0);
          }
        }
      int getLen(){
        return len;
      }
      void pull(){
        this->value = new int*[getLen()];
        for(int i=0; i<len; i++){
          value[i] = new int(rand()%(num_faces)+1);
        }
      }

      void sort(){
        int *temp;
        for(int i=0; i<getLen(); i++){
          for(int j=0; j<getLen(); j++){
            if(value[i] < value[i+1]){
              temp = value[i];
              value[i] = value[i+1];
              value[i+1] = temp;
            }
          }
        }
      }

      virtual ostream& put(ostream& os){
            os << " attacco =[";
            for(int i=0; i<len; i++){
                os << *value[i] << " ";
            }
            os << "]";
            return os;
        }
};

class player{
  private:
    string nickname;
    string color;
    int quantityTerritory;
    
  public:
    player(string nick, string col, int QT){
      this->nickname = nick;
      this->color = col;
      this->quantityTerritory = QT;

    }

    void setColor(string color){
        this->color = color;
    }

    void setName(string Name){
        this->nickname = Name;
    }
    string getName(){
      return nickname;
    }
    ostream& put(ostream& os){
            os << "\nPlayer = " << nickname << " ";
           return os;
        }

    protected:

};

ostream& operator << (ostream& os, dice& obj){
    return obj.put(os);
}


int main(){

  const int DIM = 1;

  player P1("Pippo", "red", 2);
  player P2("pippineddu", "blue", 4);

  dice* red[DIM];
  dice* blue[DIM];

  cout << "\n " << P1.getName() <<" attacca " << P2.getName() << " tirando il dado per tre volte : " << endl;
  for(int i=0; i<DIM; i++){
    red[i] = new dice(1, 6);
  }

  for(int i=0; i<DIM; i++){
    red[i]->pull();
  }

  for(int i=0; i<DIM; i++){
    red[i]->sort();
  }  

  for(int i=0; i<DIM; i++){
    cout << *red[i] << " ";
  }
  cout << endl;

  cout << "\n " << P2.getName() <<" si difende da " << P1.getName() << " tirando il dado per tre volte : " << endl;
  for(int i=0; i<DIM; i++){
    blue[i] = new dice(1, 6);
  }

  for(int i=0; i<DIM; i++){
    blue[i]->pull();
  }

  for(int i=0; i<DIM; i++){
    blue[i]->sort();
  }  

  for(int i=0; i<DIM; i++){
    cout << *blue[i] << " ";
  }
  cout << endl;

  int contR = 0;
  int contB = 0;
  for(int i=0; i<turni; i++){
    if(red[i] > blue[i]){
      contR++;
    } else {
      contB++;
    }
  }

  if(contR > contB){
    cout << "\n red wins" << endl;
  } else {
    cout << "\n blue wins" << endl;
  }
    
}
