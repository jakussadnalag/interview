## Obecně
- Během vypracování bude možné zadání i částečná řešení konzultovat se zástupci f. Mergado.
- Úkoly budou vypracovány formou Python scriptů.
- Internet je možné používat k čemukoliv, kromě živé konzultace s jinými osobami.
- Hodnocen bude váš přístup k zadání (zejm. analýza), splnění požadavků, robustnost programu a čistota kódu
- Je možné používat pouze [standardní knihovny Pythonu](https://docs.python.org/3/library/).

## Zadání
### Úkol 1 - Rekurze:
Napište funkci ``word_chain``, která na vstupu dostane libovolně velkou množinu slov a vrátí největší počet slov, které lze zřetězit jeden po druhém tak, že první písmeno druhého slova je stejné jako poslední písmeno prvního slova. Opakování slov není povoleno.

Příklady:

```
word_chain({'goose', 'dog', 'ethanol'}) == 3  # dog – goose – ethanol
word_chain({'why', 'new', 'neural', 'moon'}) == 3  # (moon – new – why)
```


### Úkol 2 - Prvočísla a palindromy
- Připravte program, který vypíše první prvočíslo, které je větší než uživatelem zadaná hodnota a které je zároveň palindromem.

#### Příklady vstupů a očekávané výstupy
| Vstup    | Výstup          |
| -------- | --------------- |
| 100      | 101             |
| 100000   | 1003001         |
| xy       | Invalid input!  |

### Úkol 3 - Hokej
- Z webu https://isport.blesk.cz/vysledky/hokej/liga?action=season&season=3089 vyscrapujte výsledky všechny zápasů
- Vyfiltrujte zápasy, které vyhrál Váš oblíbený tým
- Vypište datum a jméno poraženého týmu

#### Příklad výstupu
```
13. 3. jsme porazili Vítkovice
14. 3. jsme porazili Vítkovice
17. 3. jsme porazili Vítkovice
18. 3. jsme porazili Vítkovice
31. 3. jsme porazili Plzeň
1. 4. jsme porazili Plzeň
4. 4. jsme porazili Plzeň
7. 4. jsme porazili Plzeň
15. 4. jsme porazili Třinec
18. 4. jsme porazili Třinec
19. 4. jsme porazili Třinec
22. 4. jsme porazili Třinec
```

### Úkol 4 - Validace textového souboru
- Připravte script pro validaci [tohoto](https://pastebin.com/tNmieVFn) CSV souboru ve formátu:
    - Jméno knihy; Jméno autora; ISBN; cena
- Validujte, že všechny hodnoty jsou zadané, že ISBN je ve správném formátu a že cena je kladné číslo
    - cena je zadána jako desetinné číslo oddělené tečkou nebo čárkou, doplněné o měnu (Kč nebo €)
- Pokud narazíte na nevalidní řádek, vypište číslo řádku a jaký nastal problém

#### Příklad výstupu
```
Invalid ISBN on line: 21
Missing title on line: 67
Invalid price on line: 90
Missing author on line: 149
Error! 3 column(s) on line 185!
Invalid price on line: 224
```

### Úkol 5 - Třídy:
Napište třídu ``Warrior`` s atributy ``name`` a ``maximum_health``, dynamickým read-only atributem ``is_alive`` a metodami pro sčítání (``+``), odčítání (``-``) a výpisu informací o warriorovi. Popis atributů a metod:

\- ``Warrior.name`` - název warriora inicializovaný přes konstruktor
\- ``Warrior.maximum_health`` - kladné nenulové číslo inicializované přes konstruktor
\- ``Warrior.is_alive`` - boolean hodnota indikující, zdali je warrior na živu, či je mrtev (viz odčítání)

\- ``Warrior + Warrior`` - v případě, kdy oba dva warrioři jsou naživu, vrátí nového Warriora s atributy složenými z atributů dvou sčítaných Warriorů. ``name`` je vytvořen jako spojení názvu prvního a druhého Wariora
oddělené mezerou a ``maximum_health`` je vytvořen jako součet maximálního zdraví prvního a druhého warriora. V opačném případě se nic nestane.
\- ``Warrior - Warrior`` v případě, kdy oba dva warrioři jsou naživu, ubere obou warriorům jeden život. Pokud warriorovi klesne život na hodnotu 0, je na trvalo považován za mrtvého (``is_alive`` bude vracet ``False``)
\- ``str(Warrior)`` - vypíše informace o daném warriorovi ve formátu: ``Warrior(name="{name}", maximum_health={}, is_alive={})``

Příklad:


```
xena = Warrior(name="Xena",  maximum_health=1)
# str(xena) == 'Warrior(name="Xena", maximum_health=1, is_alive=True)'
conan = Warrior(name="Barbar Conan",  maximum_health=2)
# True == xena.is_alive == conan.is_alive

child = xena + conan
# child.is_alive == True
# child.name == "Xena Barbar Conan"
# child.maximum_health == 3

fight = xena - conan
# fight is None
# xena.is_alive == False
# conan.is_alive == True
# str(xena) == 'Warrior(name="Xena", maximum_health=1, is_alive=False)'

child_2 = xena + conan
# child_2 is None
```

# ENG

## General
- During the work, it will be possible to consult the assignment and partial solutions with representatives of Mergado.
- Tasks will be solved in the form of Python scripts.
- The Internet can be used for anything, except for live consultation with other people.
- Your approach to the assignment (especially analysis), fulfillment of requirements, program robustness, and code cleanliness will be evaluated.
- Only [standard Python libraries](https://docs.python.org/3/library/) can be used.

## Assignment
### Task 1 - Recursion:
Write a function `word_chain` that takes an arbitrarily large set of words as input and returns the maximum number of words that can be chained one after another so that the first letter of the second word is the same as the last letter of the previous word. Repeating words is not allowed.

Examples:

```
word_chain({'goose', 'dog', 'ethanol'}) == 3  # dog – goose – ethanol
word_chain({'why', 'new', 'neural', 'moon'}) == 3  # (moon – new – why)
```

### Task 2 - Primes and Palindromes
- Prepare a program that prints the first prime number greater than the value entered by the user and that is also a palindrome.

#### Input Examples and Expected Outputs
| Input    | Output          |
| -------- | --------------- |
| 100      | 101             |
| 100000   | 1003001         |
| xy       | Invalid input!  |

### Task 3 - Hockey
- Scrape the results of all matches from the website https://isport.blesk.cz/vysledky/hokej/liga?action=season&season=3089
- Filter the matches won by your favorite team
- Display the date and the name of the defeated team

#### Example Output
```
13. 3. we defeated Vítkovice
14. 3. we defeated Vítkovice
17. 3. we defeated Vítkovice
18. 3. we defeated Vítkovice
31. 3. we defeated Plzeň
1. 4. we defeated Plzeň
4. 4. we defeated Plzeň
7. 4. we defeated Plzeň
15. 4. we defeated Třinec
18. 4. we defeated Třinec
19. 4. we defeated Třinec
22. 4. we defeated Třinec
```

### Task 4 - Text File Validation
- Prepare a script for validating [this](https://pastebin.com/tNmieVFn) CSV file in the format:
    - Book name; Author name; ISBN; price
- Validate that all values are provided, that the ISBN is in the correct format, and that the price is a positive number.
    - The price is entered as a decimal number separated by a dot or comma, followed by a currency symbol (Kč or €).
- If you encounter an invalid line, print the line number and the nature of the problem.

#### Example Output
```
Invalid ISBN on line: 21
Missing title on line: 67
Invalid price on line: 90
Missing author on line: 149
Error! 3 column(s) on line 185!
Invalid price on line: 224
```

### Task 5 - Classes:
Write a class `Warrior` with attributes `name` and `maximum_health`, a dynamic read-only attribute `is_alive`, and methods for addition (`+`), subtraction (`-`), and displaying information about the warrior. Description of attributes and methods:

- `Warrior.name` - the name of the warrior initialized through the constructor.
- `Warrior.maximum_health` - a positive non-zero number initialized through the constructor.
- `Warrior.is_alive` - a boolean value indicating whether the warrior is alive or dead (see subtraction).

- `Warrior + Warrior` - if both warriors are alive, return a new Warrior with attributes composed of the attributes of the two added warriors. `name` is created by joining the names of the first and second warriors with a space, and `maximum_health` is the sum of the maximum health of the first and second warriors. If one of them is dead, nothing happens.
- `Warrior - Warrior` - if both warriors are alive, subtract one life from both warriors. If a warrior's health drops to 0, they are permanently considered dead (`is_alive` will return `False`).
- `str(Warrior)` - display information about the given warrior in the format: `Warrior(name="{name}", maximum_health={}, is_alive={})`.

Example:

```
xena = Warrior(name="Xena",  maximum_health=1)
# str(xena) == 'Warrior(name="Xena", maximum_health=1, is_alive=True)'
conan = Warrior(name="Barbar Conan",  maximum_health=2)
# True == xena.is_alive == conan.is_alive

child = xena + conan
# child.is_alive == True
# child.name == "Xena Barbar Conan"
# child.maximum_health == 3

fight = xena - conan
# fight is None
# xena.is_alive == False
# conan.is_alive == True
# str(xena) == 'Warrior(name="Xena", maximum_health=1, is_alive=False)'

child_2 = xena + conan
# child_2 is None
```

