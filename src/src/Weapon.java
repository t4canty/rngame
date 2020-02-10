package src;

public class Weapon {
	private String name;
	private int damage;
	private int value;
	public Weapon(String name, int damage, int value) {
		this.name = name;
		this.damage = damage;
		this.value = value;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getName() {
		return name;
	}
	public int getDamage() {
		return damage;
	}
	public int getValue() {
		return value;
	}
}
