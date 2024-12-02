acc = 1
cycle = 1
queue = []

input = $stdin.readlines
input.each do |command|
  if command.chomp=="noop"
    ()
  else
    params=command.split(" ")
    operand=params[1]
    queue.push([operand.to_i, 2])
  end
end

queue.each do |instruct|
    if queue.size > 0
      
    end
end
p queue
