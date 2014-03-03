import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;

import edu.mit.jwi.*;
import edu.mit.jwi.item.*;



public class TestJWI
{
	public static void main(String[] args) throws IOException{
			// construct the URL to the Wordnet dictionary directory
			String path = "lib/WordNet-3.0/dict";
			URL url = new URL ( "file" , null , path ) ;
			// construct the dictionary object and open it
			IDictionary dict = new Dictionary ( url ) ;
			dict . open () ;
			// look up first sense of the word " dog "
			IIndexWord idxWord = dict . getIndexWord ( " dog " , POS . NOUN ) ;
			IWordID wordID = idxWord . getWordIDs () . get (0) ;
			IWord word = dict . getWord ( wordID ) ;
			System . out . println ( " Id = " + wordID ) ;
			System . out . println ( " Lemma = " + word . getLemma () ) ;
			System . out . println ( " Gloss = " + word . getSynset () . getGloss () ) ;
			
	}

}