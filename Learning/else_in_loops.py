instructions = ["say hello", "say how are you","abort", "ask for money", "say thank you", "say bye"]
Approved_instructions = []

for instruction in instructions:
    print(f"Adding {instruction} instruction")
    Approved_instructions.append(instruction)

    if instruction == "abort":
        print("Aborting !")
        Approved_instructions.clear()
        break

print(f"Fallowing actions will be taken: {Approved_instructions}")