package src;

public class Node {
	private int id; // id of the textfile
	private String[] data; //send output of file to here.
	private Node nextNode;
	private int txtId; // gets the id from the textFile to point to the next object.
	public Node(int id) {
		this.id = id;
	}
	
}
