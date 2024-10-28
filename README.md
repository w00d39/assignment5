# Pokémon Strongest Finder

This project contains a Python script that determines the strongest Pokémon (highest stat total) based on a given generation. The script reads data from a CSV file and processes it to find the Pokémon with the highest total stats for the specified generation.

## Files

- `assignment5.py`: The main script that contains the function to find the strongest Pokémon and reads data from the CSV file.
- `pokemon_data.csv`: The CSV file containing Pokémon data, including their names, generations, and total stats.

## Functionality

### `strongest(givenGen)`

This function takes a generation number as input and returns the Pokémon with the highest total stats for that generation. If multiple Pokémon have the same highest total stats, it returns all of them.

#### Parameters

- `givenGen` (int): The generation number to search for the strongest Pokémon.

#### Returns

- A list of tuples containing the names and total stats of the strongest Pokémon for the given generation.
- A string message if no Pokémon are found for the given generation or if there is an error in processing the data.

## Usage

1. Ensure you have the `pokemon_data.csv` file in the same directory as the `assignment5.py` script.
2. Run the `assignment5.py` script.
3. Enter the generation number when prompted.
4. The script will output the strongest Pokémon for the given generation.

### Example

```sh
$ python assignment5.py
Enter a generation: 5
[('Zekrom', 680), ('Reshiram', 680)]
