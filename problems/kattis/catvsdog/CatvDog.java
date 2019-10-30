import java.util.*;
/*
*
* Raymond Haynes
* 10/8/19
*/
public class CatvDog
{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        int n = input.nextInt();
        
        for(int i = 0; i < n; i++) {
            int c = input.nextInt();
            int d = input.nextInt();
            int v = input.nextInt();
            
            ArrayList<String> keeps = new ArrayList<String>();
            ArrayList<String> thrownOut = new ArrayList<String>();
            
            for(int j = 0; j < v; j++) {
                keeps.add(input.next());
                thrownOut.add(input.next());
            }
            
            int maxHappy = 0;
            for (int j = 0; j < keeps.size(); j++) {
                int happy = 1;
                String keep = keeps.get(j), bye = thrownOut.get(j);
                
                for(int k = 0; k < keeps.size(); k++) {
                    if(k == j)
                        continue;
                    String keepComp = keeps.get(k), byeComp = thrownOut.get(k);
                    
                    if(!keepComp.equals(bye) && !byeComp.equals(keep))
                        happy++;
                    
                    if(happy > maxHappy)
                        maxHappy = happy;
                }
            }
            
            System.out.println(maxHappy);
        }
        input.close();
    }
}
