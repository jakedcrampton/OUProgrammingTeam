import java.util.*;
import java.lang.*;
public class ImageDecoding {
	public static void main(String[] args){
		Scanner scanny=new Scanner(System.in);
		boolean dot=false;
		boolean first=true;
		StringBuilder output=new StringBuilder();
		while(true){
			boolean error=false;
			int lastLine=-1;
			int n=scanny.nextInt();
			if(n>0){
				if(!first){
					output.append('\n');
				}
				first=false;
				for(int i=0;i<n;i++){
					int lineLength=0;
					char start=scanny.next().charAt(0);
					if(start=='.')
						dot=true;
					else dot=false;
					String[] nums=scanny.nextLine().split(" ");
					
					for(int q=1;q<nums.length;q++){
						int p=Integer.parseInt(nums[q]);
						lineLength+=p;
						for(int j=0;j<p;j++){
							output.append(dot?'.':'#');
						}
						dot=!dot;
					}
					if(lastLine > -1 && lineLength != lastLine) {
						error = true;
					}
					lastLine=lineLength;
					output.append('\n');
				}
				if(error){
					output.append("Error decoding image\n");
				}
			}
			else{break;}
		}
		System.out.print(output);
	}
}
