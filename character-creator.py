#!/usr/bin/python3

import random

NAMES = [
    "Abrielle", "Adair", "Adara", "Adriel", "Aiyana", "Alissa", "Alixandra", 
    "Altair", "Amara", "Anatola", "Anya", "Arcadia", "Ariadne", "Arianwen", 
    "Aurelia", "Aurelian", "Aurelius", "Avalon", "Bastian", "Breena", 
    "Brielle", "Cambria", "Cara", "Carys", "Caspian", "Cassia", "Cassiel", 
    "Cassiopeia", "Cassius", "Chaniel", "Cora", "Corbin", "Cyprian", "Daire", 
    "Darius", "Destin", "Drake", "Drystan", "Eira", "Eirian", "Elysia", "Eoin", 
    "Evadne", "Fineas", "Finian", "Fyodor", "Gareth", "Gavriel", "Griffin", 
    "Guinevere", "Hadriel", "Hannelore", "Hermione", "Hesperos", "Iagan", 
    "Ianthe", "Ignacia", "Ignatius", "Iseult", "Isolde", "Jessalyn", "Kara", 
    "Kerensa", "Korbin", "Kyler", "Kyra", "Leala", "Leila", "Lilith", "Liora", 
    "Lucien", "Lyra", "Maia", "Marius", "Mathieu", "Mireille", "Mireya", 
    "Natania", "Nerys", "Nuriel", "Nyssa", "Oisin", "Oralie", "Orion", 
    "Orpheus", "Ozara", "Peregrine", "Persephone", "Perseus", "Petronela", 
    "Phelan", "Qadira", "Quintessa", "Raisa", "Remus", "Rhyan", "Rhydderch", 
    "Riona", "Saoirse", "Sarai", "Sebastian", "Seraphim", "Seraphina", 
    "Sirius", "Sorcha", "Tavish", "Tearlach", "Terra", "Thalia", "Thaniel", 
    "Theia", "Torian", "Torin", "Tressa", "Tristana", "Uriela", "Urien", 
    "Vanora", "Vespera", "Xanthus", "Yadira", "Yseult", "Zaira", "Zephyr", 
    "Zora", "Zorion"
]

class DevTools():
    def __init__(self):
        self.character_list = []

    def add_characters(self, character_count):
        for character in range(character_count):
            print("a")

class Character():
    def __init__(self):
        self.name = 
        self.knowledge = self._roll_stat()
        self.smarts = self._roll_stat()
        self.toughness = self._roll_stat()
        self.sneak = self._roll_stat()
        self.gab = self._roll_stat()

    def get_stats(self):
        return {
            "knowledge": self.knowledge,
            "smarts": self.smarts,
            "toughness": self.toughness,
            "sneak": self.sneak,
            "gab": self.gab
        }

    def _roll_stat(self):
        return random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)

def main():
    grant = Character()
    print(grant.get_stats())

    dev = DevTools()
    print(dev.add_characters(3))

if __name__ == "__main__":
    main()
