package src;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.Timer;

public class Driver extends JPanel implements MouseListener, ActionListener {
	private Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
	private Node startNode;
	public Driver() {
		JFrame f = new JFrame();
		f.setTitle("RNGame");
		f.setSize(screenSize);
		f.setResizable(false);
		//Adding Listeners
		f.setBackground(Color.black);
		f.addMouseListener(this);
		f.add(this);
		//Adding ticking timer
		t = new Timer(17,this);
		t.start();
		f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		f.setVisible(true);
	}
	private Timer t;
	public static void main(String[] args) {
		Driver d = new Driver();
	}
	@Override
	public void paint(Graphics g) {
		super.paintComponent(g);
		g.setColor(Color.white);
		g.fillRect(0, 0, screenSize.width, screenSize.height);
		g.setColor(Color.black);
		g.fillRect(200, 0, 1, screenSize.height); // create lefthand inventory bar
		g.fillRect(200, screenSize.height-150, screenSize.width, 1 ); // create options.
		//StartNode.paint(g, 210, 0);
		
		
		
	}
	
	
	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		
	}
	@Override
	public void mouseClicked(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}
	@Override
	public void mouseEntered(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}
	@Override
	public void mouseExited(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}
	@Override
	public void mousePressed(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}
	@Override
	public void mouseReleased(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}
}
