#!/usr/bin/env python3

"""A collection of tools for interacting with the Steam Web API."""
import sys
import getopt
import requests


def main():
    """
    Given a list of games, check which games are on Steam.

    This program uses C-style command line options to take an input file. Then,
    program uses Steam Web API to get a list of Steam applications. If a given
    game is on Steam, that information is relayed back to the user.

    Raises:
    getopt.GetoptError: If the program is fed invalid commandline options.
    FileNotFoundError: If program tries opening a file that doesn't exist.

    """
    helpDocumentation = ("Steam Tools (steamTools.py) is a collection of "
                         "tools for interacting with Steam Web API. "
                         "Currently, its primary functionality is to take a "
                         "file containing a list of games and using Steam Web "
                         "API to check which of the given games are available "
                         "on Steam. The file should be formatted with one "
                         " game per line. Please see sampleList.txt for an "
                         "example.\n\n"
                         "Usage: python steamTools.py -i <input file>")
    inputFile = ""
    try:
        options, arguments = getopt.getopt(sys.argv[1:], "hi:", ["inputFile="])
    except getopt.GetoptError:
        print(helpDocumentation)
    for option, argument in options:
        if option == "-h":
            print(helpDocumentation)
            sys.exit(2)
        elif option in ("-i", "--inputFile"):
            inputFile = argument
        else:
            print(helpDocumentation)
            sys.exit(2)
    listOfGames = []
    try:
        with open(inputFile) as openFile:
            listOfGames = openFile.read().splitlines()
            validatedGames = validateSteamGames(listOfGames)
    except FileNotFoundError:
        print("{} does not exist.".format(inputFile))
        print("For more information try: python steamTools.py -h")
        sys.exit(2)
    print("Games: {}".format(listOfGames))
    print("In Steam: {}".format(validatedGames))


def validateSteamGames(listOfGames):
    """
    Check to see if games are in Steam's library.

    Iterates through a given list, then iterates through a list of games on
    Steam, adding that game to be returned to the user.

    Returns: A list of given games that are also available on Steam.

    """
    steamGames = listSteamGames()
    inSteam = []
    for game in listOfGames:
        if game in steamGames:
            inSteam.append(game)
    return inSteam


def listSteamGames():
    """
    Generate a list of games on Steam.

    Returns: A list of strings corresponding to games in Steam's library.

    """
    steamGames = []
    fetchedGames = fetchSteamGames()
    for game in fetchedGames["applist"]["apps"]:
        steamGames.append(game["name"])
    return steamGames


def fetchSteamGames():
    """
    Get list of Steam games via API and in JSON format.

    Returns: All the games in Steam in JSON format.

    """
    url = "http://api.steampowered.com/ISteamApps/GetAppList/v0002/"
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    main()
