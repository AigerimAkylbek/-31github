import java.util.Scanner;

import javax.lang.model.util.ElementScanner14;

public class Sandbox{
     
    public static void main(String[] args) {
        double a = 3.4;
        boolean k =(a > 10);
        //input a floating poinnt from user
        // check the number is negative  / positive / zero

        Scanner kb = new Scanner(System.in);
        System.out.print("Please enter a number =>");
        double num = kb.nextDouble();

        if(num < 0)
         System.out.println("Number" + num +" is negative.");
        else if(num > 0)
          System.out.println("Number" + num + "is possitive.");
        else 
           System.out.print("It is a Zero!");

        //check the number has 1 digit
        double num2 = Math.abs(num);
        if(num2<=9)
           System.out.print(num + "is not one digit ")

    }
}

    
