# Parse the program instructions from the input
instructions = []
for line in open('input.txt'):
  # Split the line into the instruction and the value (if any)
  parts = line.strip().split(' ')
  instruction = parts[0]
  value = int(parts[1]) if len(parts) > 1 else None
  
  # Store the instruction and value in a tuple
  instructions.append((instruction, value))
  
# Initialize the X register to 1
x = 1

# Initialize the cycle counter to 1
cycle = 1

# Execute the instructions until the end of the program
while cycle <= len(instructions):
  # Get the current instruction and value
  instruction, value = instructions[cycle - 1]
  
  # Execute the instruction
  if instruction == 'noop':
    # noop does nothing
    pass
  elif instruction == 'addx':
    # addx increases the value of X by the specified amount
    x += value
  
  # Check if the current cycle is one of the specified cycles
  if cycle in (20, 60, 100, 140, 180, 220):
    # Calculate the signal strength for the current cycle
    signal = cycle * x
    
    # Print the signal strength
    print(f'Signal strength for cycle {cycle}: {signal}')
  
  # Move to the next cycle
  cycle += 1
#This solution parses the program instructions from the input file and stores them in a list. It then simulates the program's execution by executing each instruction in turn, tracking the value of the X register and printing the signal strength for the specified cycles.




