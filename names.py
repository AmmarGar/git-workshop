# names.py: A simple script to print participant names.
# Participants will add their names to the list below in their branches.

names = ["Richard"]

def print_names():
    if names:
        print("Workshop participants: " + ", ".join(names))
    else:
        print("No participants added yet.")

if __name__ == "__main__":
    print_names()
