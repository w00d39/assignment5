#Write a function that determines the strongest Pokemons (highest stat total) based on generation.

def strongest(givenGen):
    try:
        #list that will store the name and total of the pokemon
        pokemonList = []
        for i in range(len(name)): #loops through the length of the name list to match the generation
            if givenGen == gen[i]:
                #appends the name and total to the list in a tuple
                pokemonList.append((name[i], int(total[i])))
        #return pokemonList #tester to see where something is going wrong
                #looks like this: pokemonList = [("Porygon", 395), ("Omanyte", 355), ...]
     

        if pokemonList: #if the list has values
            #starter value based on the first thing in the list
            strongestPokemon = [pokemonList[0]] #sets the strongestPokemon to the first pokemon in the list
            maxTotal = pokemonList[0][1] #sets the maxTotal to the total of the first pokemon in the list

            for pokemon in pokemonList[1:]: #loops through the list of pokemon starting at the second pokemon
                if pokemon[1] > maxTotal: #if the total of the pokemon is greater than the total of the strongestPokemon
                        #set the strongestPokemon to the pokemon
                    strongestPokemon = [pokemon]
                    maxTotal = pokemon[1] #set the maxTotal to the total of the pokemon
                elif pokemon[1] == maxTotal: #if the total of the pokemon is equal to the total of the strongestPokemon
                    strongestPokemon.append(pokemon) #append the pokemon to the list of strongestPokemon
                 #returns the strongest pokemon       
            return strongestPokemon 
        #if the list is empty it will print that no pokemon were found with the given generation
        else:
            return "No Pokémon found in generation " + str(givenGen) + "."
             
    except ValueError:
        return "Invalid input. Please enter a valid generation number."
    except IndexError:
         return "Error processing the data. Please check the input file."

with open("pokemon_data.csv", "r") as file: #opening the file in read mode
    contents = file.read() #reading the contents of the file
    lines = contents.splitlines() #splitting the contents by lines
     #splitting the lines by commas and saving them to a list of columns for my sanity
    columns = [line.split(",") for line in lines] 

    header = columns[0] #grabs the column names

genIndex = header.index("generation") #finds where generation is
totalIndex = header.index("total") #finds where total is
nameIndex = header.index("name") #finds where name is\

gen = [int(row[genIndex]) for row in columns[1:]] #creates the list of generation by using the genIndex but excludes the header
total = [row[totalIndex] for row in columns[1:]] #creates the list of total by using the totalIndex but excludes the header
name = [row[nameIndex] for row in columns[1:]] #creates the list of name by using the nameIndex but excludes the header

#will make the comparison easier for the function

givenGen = int(input("Enter a generation: "))#asks the user to input a generation

print(strongest(givenGen)) #calls the function and passes the given generation