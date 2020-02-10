package src;

import java.awt.Graphics;
import java.io.FileInputStream;

import javax.swing.JButton;

public class Node {
	private int id; // id of the textfile
	private String[] data; //send output of file to here.
	private Node nextNode;
	private FileInputStream fStream;
	private int txtId; // gets the id from the textFile to point to the next object.
	private JButton[] buttonArray;
	public Node(int id) {
		this.id = id;
	}
	private FileInputStream readFile() {return null;}
	
	public void paint(Graphics g, int x, int y) {
		
	}
	
}
