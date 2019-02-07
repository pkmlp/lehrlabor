
import java.util.Scanner;

public class dreiecksBestimmung {


    /**
     * Pruefen, ob der Eingabe String genau drei Integer-Werte enthaehlt
     * @param String eingabe 
     * @return boolean 
     *          true wenn Eingabe-String genau drei nteger Werte enthaelt
     *          false wenn Eingabe-String nicht nur drei Integer-Werte enthaelt
     */
    static boolean eingabePruefen(String eingabe) {

        String[] dreiecksSeiten = eingabe.split(" ");

        if (dreiecksSeiten.length == 3) {
            
            int[] seiten = new int[3];
    
            try {
                seiten[0] = Integer.parseInt(dreiecksSeiten[0]);
                seiten[1] = Integer.parseInt(dreiecksSeiten[1]);
                seiten[2] = Integer.parseInt(dreiecksSeiten[2]);

                return true;

            } catch (Exception e) {

                return false;

            }
    
        } else {

            return false;

        }

    }


    /**
     * Prueft ob die drei Seitenlaengen ein Dreieck sein koennen
     * @param a, b, c Seitenlaenge als int
     * @return boolean 
     */
    static boolean gueltigesDreieck(int a, int b, int c) {
    
        boolean gueltigesDreieck = false;

        if (a >= b && a >= c) {
            if (b + c > a) { 
                gueltigesDreieck = true;
            }
        } else if (b >= c && b >= a) { 
            if (a + c > b) {  
                gueltigesDreieck = true;
            }
        } else {  
            if (a + b > c) {  
                gueltigesDreieck = true;
            }
        }
        return gueltigesDreieck;

    }


    /**
     * Berechnet den Winkel Gamma
     * @param a, b, c Seitenlaenge als int
     * @return double winkel gamma 
     */
    static double winkelBerechnen(int a_int, int b_int, int c_int) {

        double a = (double)a_int;
        double b = (double)b_int;
        double c = (double)c_int;
        
        double acos = Math.acos((a*a + b*b - c*c) / (2*a*b));
        double winkelGamma = Math.toDegrees(acos);

        return winkelGamma;

    }


    /**
     * Prueft welche Seiteart das Dreick aufweist
     * @param String Seitenart
     * @return boolean 
     */
    static String dreieckSeiten(int a, int b, int c) {
    
        if (a == b && a == c) {
            return "gleichseitig";
        } else if (a == b || a == c || b == c) { 
            return "gleichschenklig";
        } else {  
            return "ungleichseitig";
        }

    }


    /**
     * Prueft welche Winkelart das Dreick aufweist
     * @param double Winkel Gamma
     * @return String mit Winkelart 
     */
    static String dreieckWinkel(double gamma) {
    
        if (gamma > 90.0) {
            return "stumpfwinklig";
        } else if (gamma < 90.0) { 
            return "spitzwinklig";
        } else {  
            return "rechtwinklig";
        }

    }


    public static void main(String[] args) {

        Scanner eingabeZeile = new Scanner(System.in);

        System.out.println("                                                                   ");
        System.out.println("-------------------------------------------------------------------");
        System.out.println("Programm zur Bestimmung eines Dreiecks anhand der drei Seitenlängen");
        System.out.println("-------------------------------------------------------------------");
        System.out.println("                                                                   ");
        System.out.println("  Bitte drei ganzzahlige Werte (getrennt mit Leerschlag) eingeben  ");
        System.out.println("    Um das Programm zu beenden alle drei Seiten mit 0 eingeben     ");
        System.out.println("                                                                   ");
        System.out.println("-------------------------------------------------------------------");
        System.out.println("                                                                   ");
    

        while (true) {

            System.out.println();
            System.out.print("Eingabe der drei Seitenlaengen, "
                             + "getrennt mit Leerschlag: ");

            String eingabe = eingabeZeile.nextLine();

            if (eingabePruefen(eingabe)) {

                String[] dreiecksSeiten = eingabe.split(" ");

                int seite_a = Integer.parseInt(dreiecksSeiten[0]);
                int seite_b = Integer.parseInt(dreiecksSeiten[1]);
                int seite_c = Integer.parseInt(dreiecksSeiten[2]);

                if (seite_a == 0 && seite_b == 0 && seite_c == 0) {
                    System.out.println("Programm beendet");
                    break;
                }

                if (gueltigesDreieck(seite_a, seite_b, seite_c)) {

                    double winkel = winkelBerechnen(seite_a, seite_b, seite_c);
                    String winkelArt = dreieckWinkel(winkel);
                    String seitenArt = dreieckSeiten(seite_a, seite_b, seite_c);
                    System.out.println("Gueltiges Dreieck: " + winkelArt + "-" + seitenArt);

                } else {

                    System.out.println("ungueltiges Dreieck");

                }

                
            } else {

                System.out.println("ungueltige Eingabe");

            }
            
        }

        eingabeZeile.close();
        System.out.println();

    }

}
