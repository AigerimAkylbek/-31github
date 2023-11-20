/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package menu;

import java.util.Scanner;

/**
 *
 * @author Aigerim Alykulova
 */
public class Menu {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
        System.out.println("Geometry Calculator:\n1. Calculate the Area of a Circle\n2. Calculate the Area of a Rectangle\n3. Quit\nEnter your choice (1 - 3):");
        Scanner keyboard = new Scanner(System.in);
        int choice = keyboard.nextInt();
             // do the switch
         switch(choice)
         {
             case 1:
                 System.out.println("calculating circle area");
                 // prompt
                 // input radius as double
                 //check if it is not neative
                 // calculate and output area
                 // if negative - output error message
                 break;
             case 2: 
                 System.out.println("calculating Area of a Rectangle");
                 break;
             case 3:
                 // does nothing!!
                 System.out.println("Quitting");
             default:
                System.out.println("ERROR! Invalid option. Please enter 1 or 2 or 3");

         }
    }
    
}
