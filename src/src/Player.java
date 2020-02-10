package src;

public class Player {
	public int health = 10;
	private String shipName;
	public int progress = 0;
	private Weapon[] inventory;
	public Player(String shipName) {
		this.shipName = shipName;
	}
	public Player(String shipName, int heath, int progress, Weapon[] inventory) {
		this.shipName = shipName;
		this.health = heath;
		this. progress = progress;
		this.inventory = inventory;
	}
}
