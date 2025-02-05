def print_roo():
    print("""
    Here's a friendly kangaroo greeting!
         _  _
        (o)(o)
         (*)
      ___| |___
     /    °    \\
    |           |
     \\  |___|  /
      \\_____/
    """)

def main():
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--roo":
        print_roo()
    else:
        print("Hello, World!")

if __name__ == "__main__":
    main()