public class Test {
    public static void main(String[] args) {
        Integer randomNumber = (int)(Math.random()*5);
        System.out.println(randomNumber);
        if(randomNumber == 0){ System.out.println("stay"); }
        else if(randomNumber == 1){ System.out.println("up"); }
        else if (randomNumber==2){ System.out.println("down"); }
        else if(randomNumber == 3){ System.out.println("left"); }
        else if(randomNumber == 4){ System.out.println("right"); }
    }
}
