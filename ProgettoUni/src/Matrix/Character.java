package Matrix;

import java.util.HashMap;
import java.util.Map;

public class Character {
    Map<Integer, Integer> coordinates = new HashMap<>();
    public Integer life = 10;
    public String name;
    public String carattere;
    public Integer x;
    public Integer y;

    //NAME SECTION
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }

    public void move(String[][] matrix, Integer cols, Integer rows){
        getCurrentPosition(matrix,cols,rows);
        matrix[y][x]=Color.ANSI_BLACK+"-";
        //tryConnection(matrix,cols,rows);
        Integer randomNumber = (int)(Math.random()*5);
        //int randomNumber = 3;
        if(randomNumber == 0){
            System.out.println("Stay");
        }

        else if(randomNumber == 1){
            System.out.println("up");
            if(y==0){
                if(matrix[cols-1][x].equals(Color.ANSI_BLACK+"-")){ //non partono gli if
                    y=cols-1;
                } else {
                    establishConnection();
                }
            } else {
                if (matrix[y-1][x].equals(Color.ANSI_BLACK+"-")) {
                    y--;
                } else {
                    establishConnection();
                }
            }
        }

        else if (randomNumber==2){
            System.out.println("down");
            if(y==cols-1){
                if(matrix[0][x].equals(Color.ANSI_BLACK+"-")){
                    y=0;
                } else{
                    establishConnection();
                }
            } else{
                if(matrix[y+1][x].equals(Color.ANSI_BLACK+"-")) {
                    y++;
                } else{
                    System.out.println("bug");
                    establishConnection();
                }
            }
        }

        else if(randomNumber == 3){
            System.out.println("left");
            if(x==0){
                if(matrix[y][rows-1].equals(Color.ANSI_BLACK+"-")){
                    x=rows-1;
                }else{
                    establishConnection();
                }
            } else{
                if(matrix[y][x-1].equals(Color.ANSI_BLACK+"-")){
                    x--;
                } else{
                    establishConnection();
                }
            }
        }

        else if(randomNumber == 4){
            System.out.println("right: ");
            if(x==rows-1){
                if (matrix[y][rows-1].equals(Color.ANSI_BLACK+"-")){
                    x=0;
                } else{ establishConnection(); }
            } else{
                if(matrix[y][x+1].equals(Color.ANSI_BLACK+"-")){
                    x++;
                } else {
                  establishConnection();
                }
            }
        }
        life--;
        System.out.println("hp" + life);
        matrix[y][x]=getName();
    }

    public void establishConnection(){
        System.out.println("connessione stabilita");
        life=life+2;
    }

    /*public boolean tryConnection(String[][] matrix, Integer cols, Integer rows){
        if(x==0){ //Sto muovendo il pedone a sinistra
            if(matrix[rows-1][y]!="-"){ return true;}
        } else if(matrix[x-1][y]!="-"){ return true;}
        return false;
    }*/

    public void getCurrentPosition(String[][] matrix, int matrixCol, int matrixRow) {
        for (int i = 0; i < matrixCol; i++) {
            for (int j = 0; j < matrixRow; j++) {
                if (matrix[i][j] == getName()) {
                    y = i;
                    x = j;

                    System.out.println(getName()+ ": " + Color.ANSI_BLACK + "x: " + x + " y: " + y);
                }
            }
        }
    }


}
