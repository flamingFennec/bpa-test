# Classes
class character:
    class hero:
            name = input("Enter the hero's name: ")
            ID = input("Enter the character ID number: ")
            level = input("Enter the hero's level: ")
            loot = input("Enter the hero's loot level: ")
            def __init__ (hero, name, ID, level, loot):
                hero.name = name
                hero.ID = ID
                hero.level = level
                hero.loot = loot
                

    class boss:
            bossName = input("Enter the boss' name: ")
            bossID = input("Enter the character ID number: ")
            bossLevel = input("Enter the boss' level: ")
            bossHp = input("Enter the boss' hp: ")
            bossAttackDamage = input("Enter boss attack damage: ")
            lifespan = float(bossHp) // 300
            
            def __init__ (boss, bossName, bossID, bossLevel, bossHp, bossAttackDamage, lifespan):
                boss.name = bossName
                boss.ID = bossID
                boss.level = bossLevel
                boss.hp = bossHp
                boss.attack_damage = bossAttackDamage
                boss.lifespan = lifespan

#Print information
print("Hero Information:")
print(f"Name: {character.hero.name}")
print(f"ID number: {character.hero.ID}")
print(f"Level: {character.hero.level}")
print(f"Loot: {character.hero.loot}.0")

print("Boss Information:")
print(f"Name: {character.boss.bossName}")
print(f"ID number: {character.boss.bossID}")
print(f"Level: {character.boss.bossLevel}")
print(f"HP: {character.boss.bossHp}.0")
print(f"Attack Damage: {character.boss.bossAttackDamage}")
print(f"Lifespan: {character.boss.lifespan}")