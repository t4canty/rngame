package src;

import java.awt.Graphics;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;

import javax.swing.JButton;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.*;

public class Node {
	private int id; // id of the textfile
	private String data; //send output of file to here.
	private Node nextNode;
	private JSONObject j;
	private int txtId; // gets the id from the textFile to point to the next object.
	private ArrayList<JButton> buttonArray;
	public Node(int id) throws FileNotFoundException, IOException, ParseException {
		j = (JSONObject) new JSONParser().parse(new FileReader(id + ".json"));
		String data = (String) j.get("text");
		nextNode = new Node((int) j.get("nextNodeID"));
		JSONArray ja = (JSONArray) j.get("buttons");
		for(int i = 0; i < ja.size(); i++) {
			JSONObject j2 = (JSONObject) ja.get(i);
			buttonArray.add(new JButton((String) j2.get("Choice")));
		}
		this.id = id;
	}
	private FileInputStream readFile() { 

		return null;
		}
	
	public void paint(Graphics g, int x, int y) {
		
	}
	
}
