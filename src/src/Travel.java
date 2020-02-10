package src;
//Returns strings to be displayed or acted upon in driver.
public class Travel {
	/**Event method, called every second and is what happens in between planets.  
	 * 
	 * @param p
	 * Player object.
	 * @return
	 * Returns string of what happened at event(), meant to be passed into paint() method and acted upon.
	 */
	
	public String event(Player p) {
		int id = (int) Math.random() * 100;
		switch(id) {
		case 0:
			return bad(1,p);
		case 10 :  // 2
			return bad(2,p);
		case 20 :  // 3
			return bad(3,p);
		case 27:  // 3
			return bad(4,p);
		case 40 :  // 5
			return bad(5,p);
		case 45:  // 5 total 20
			return bad(6,p);
		case 54:  // 6
			return good(1,p);
		case 66:  // 4
			return good(2,p);
		case 77:  // 3
			return good(3,p);
		case 78:  // 1
			return good(7,p);
		case 90:  // 3
			return good(4,p);
		case 98:  // 2
			return good(5,p);
		case 100:  // 1 total 20
			return good(6,p);
		default:
			return good(-1, p);
		}
	}
	
	private String good(int id, Player p) {
		switch (id) {
		case 1:
			p.progress += 1;
			return "Congrats! you managed to find more coffee rations!";
		case 2:
			p.health += (int) Math.random() * 20;
			return "You managed to pach up the hull a bit, after finding some spare parts.";
		case 3:
			p.progress += 5;
			return "You find a cache of hyperfuel, allowing you to progress much faster!";
		case 4:
			return "You find some freindly traders who are willing to fix your ship and spare some hyperfuel!";
		case 5:
			return "upgrade"; //calls loot() from driver
		case 6:
			p.progress += 4 * ((int) Math.random() * 6);
			return "You find a  wormhole and are magically transported inside, allowing you to cross vast distances instatly!";
		case 7:
			return "god"; //calls god() method from driver
		default:
			return "nothing"; //calls nothing() function in npc
		}
	}
	
	private String bad(int id, Player p) {
		switch(id) {
		case 1:
			p.health -= 3 * (int) Math.random() * 10;
			return "You are struck with a massive meteor, Sustaining MASSIVE hull damage.";
		case 2:
			p.progress -= 20;
			return "You are caught in a ion storm! you have to spend a good week and a half trying to get out.";
		case 3:
			p.health -= 3 * (int) Math.random() * 5;
			return "Congrats! \\n You are caught in a meteor shower! \\n your hull is torn to bits.\\n";
		case 4:
			return "fight"; //calls fight() in enemy
		case 5:
			p.progress -= 3;
			return "upgrade"; // calls loot() from driver
		case 6:
			p.progress += 4 * ((int) Math.random() * 6);
			return "You have lost your way, again, you dolt.";
		default:
			return "nothing"; // calls nothing() in npc
		}
	}
	/**
	 * Called on Space God event, and returns vales to be displayed onto jframe. Recives input from buttons. 
	 */
	public void spaceGod() {
		//handle input here from jframe
		//https://javatutorial.net/jframe-buttons-listeners-text-fields
	}
	/**
	 * Called on loot event, and returns vales to be displayed onto jframe. Recives input from buttons. Modifies inventory.
	 */
	public void loot() {
		//handle input here from jframe
	}
}
