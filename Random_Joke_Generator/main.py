import requests

print("=========================")
print("RANDOM JOKE GENERATOR")
print("=========================")

url="https://official-joke-api.appspot.com/random_joke"

while True:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print("\nJoke:")
        print(data["setup"])

        input("\nPress Enter to reveal the punchline:)")

        print(data["punchline"])

    else:
        print("Failed to fetch joke.")
        break

    while True:
        another_joke = input("\nDo you want another joke? (Y/N):) ")

        if another_joke.lower() == "y":
            print("\n-----------------------------")
            break

        elif another_joke.lower() == "n":
            print("\nThank you for using Random Joke Generator!")
            exit()

        else:
            print("Invalid input! Please enter Y or N.")