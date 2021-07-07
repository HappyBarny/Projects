package Matrix;

import java.util.Scanner;

public class Matrix {
    private int cols = 6;
    private int rows = 5;
    private String[][] matrix = new String[cols][rows];
    public Character c1 = new Character();
    public Character c2 = new Character();
    public Character c3 = new Character();

    public void God(){
        c1.setName(Color.ANSI_BLUE+"c1");
        c2.setName(Color.ANSI_GREEN + "c2");
        c3.setName(Color.ANSI_RED + "c3");
        generator(matrix);
        fillMatrix(matrix);
        printMatrix(matrix,cols,rows);
        round();

        //TESTING THIS PART OF CODE:
        //current position
        //c1.getCurrentPosition(matrix,cols,rows);

        //trying to make some movement on the matrix
        //c1.move(matrix,cols,rows); //il metodo prende una x e una y nel quale sposterà il mio attuale oggetto c1
        //printMatrix(matrix,cols,rows);

        //c1.getCurrentPosition(matrix,cols,rows);
    }

    public void round(){
        System.out.println(Color.ANSI_BLACK+"press 1 to continue, 2 to stop the program");
        Scanner scanner = new Scanner(System.in);
        Integer option = scanner.nextInt();
        switch (option){
            case 1:
                c1.move(matrix,cols,rows); //il metodo prende una x e una y nel quale sposterà il mio attuale oggetto c1
                c2.move(matrix,cols,rows);
                c3.move(matrix,cols,rows);
                printMatrix(matrix,cols,rows);
                round();
                break;
            case 2:
                System.out.println("programm stopped \n"
                                    +".... \n" +
                                    "closed ");
                break;
                default:
                    System.out.println("redirect to the menu"); round();
        }
    }

    public void generator (String[][] matrix){
        for (int x = 0; x < cols; x++) {
            for (int y = 0; y < rows; y++) {
                matrix[x][y] = Color.ANSI_BLACK + "-";
            }
        }
    }

    public void printMatrix (String[][] matrix, int matrixCol, int matrixRow){
        System.out.println("Your GameMap is : ");
        for (int i = 0; i < matrixCol; i++) {
            for (int j = 0; j < matrixRow; j++) {
                System.out.print(matrix[i][j] + "\t");
            }
            System.out.println();
        }
    }

    public void fillMatrix(String[][] matrix) {
        Scanner scanner = new Scanner(System.in);
        System.out.println(Color.ANSI_BLACK + "Press 1 for the default method. Press 2 for the random method");
        //Integer option = scanner.nextInt();
        /*da eliminare*/ Integer option = 1;
        switch (option){
            case 1:
                matrix[0][0] = c1.name;
                matrix[0][4]= c2.name;
                matrix[5][0]= c3.name;
                //matrix[4][4]= c4.name;
                break;
            case 2:
                matrix[setY()][setX()] = c1.name;
                matrix[setY()][setX()] = c2.name;
                matrix[setY()][setX()] = c3.name;
                break;
            default:
                System.out.println("reindirizzamento al menu: "); fillMatrix(matrix);
        }
    }

    public Integer setX(){
        int x = (int)(Math.random()*5);
        System.out.println("x:"+x);
        return x;
    }
    public Integer setY(){
        int y = (int)(Math.random()*4);
        System.out.println("y:"+y);
        return y;
    }
}

