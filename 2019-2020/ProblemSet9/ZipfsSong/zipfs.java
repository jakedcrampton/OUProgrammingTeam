import java.util.*;
import java.lang.*;
import java.util.*;
import java.math.*;
public class zipfs {
	public static void main(String[] args){
		Scanner scanny=new Scanner(System.in);
		int numSongs=scanny.nextInt();
		int numOut=scanny.nextInt();
		ArrayList<Tuple<BigInteger,String,Integer>> songs=new ArrayList<Tuple<BigInteger,String,Integer>>();
		for(int i=1;i<=numSongs;i++){
			Tuple<BigInteger,String,Integer> song= new Tuple<BigInteger,String,Integer>(new BigInteger(scanny.next()).multiply(new BigInteger(""+i)),scanny.next(),i);
			songs.add(song);
		}
		Comparator<Tuple<BigInteger, String,Integer>> comparator = new Comparator<Tuple<BigInteger, String,Integer>>()
	    {
	        public int compare(Tuple<BigInteger, String,Integer> tupleA,
	                Tuple<BigInteger, String,Integer> tupleB)
	        {
	        	return tupleB.score.compareTo(tupleA.score);
	        }
	    };
	    Collections.sort(songs, comparator);
	    for(int i=0;i<numOut;i++){
	    	System.out.println(songs.get(i).getName());
	    }
		
	}
	public static class Tuple<BigInteger, String,Integer>
	{
		private BigInteger score;
		private String name;
		private Integer index;

		public Tuple(BigInteger score, String name, Integer index)
		{
		    this.score=score;
		    this.name=name;
		    this.index=index;
		}
		public String getName(){
			return name;
		}
	}
}