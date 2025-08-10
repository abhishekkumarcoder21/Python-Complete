try:
    file=open("fileo.txt")
    content=file.read()
    print(content)

except FileNotFoundError:
    print("File not found")

finally:
    file.close()
    print("File operation completed")