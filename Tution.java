/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package tution;

/**
 *
 * @author shalomadejobi
 */
import javax.swing.JOptionPane;

public class Tution {
    public static void main(String[] args) {
        /*double tuition = 10000; // Initial tuition
        double targetTuition = tuition * 2; // Double the initial tuition
        int years = 0;
        double rate = 0.07; // 7% increase per year
        
        // Loop until tuition is at least double
        while (tuition < targetTuition) {
            tuition += tuition * rate;
            years++;
        }
        
        // Display result using JOptionPane
        JOptionPane.showMessageDialog(null, "Tuition will be at least double in " + years + " years.");*/
        
        String output="";
        for (int num=10; num<=25; num++){
            
        if(num % 2 != 0){
           continue; // will not print 11, 13, 15, …
        } 
        output+=" " + num;
        
 }
        JOptionPane.showMessageDialog(null,"" + output);
         System.exit(0);
}
    }

