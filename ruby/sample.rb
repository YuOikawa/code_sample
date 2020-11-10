input = $stdin.readlines

header = input[0].chomp.split(",")
input.delete_at(0)

result = Array.new
points = Array.new
a = Array.new

input.each do |line|
  points = line.chomp.split(",")
  points.each_with_index do |p,s|
    a[s] = Array.new if a[s].nil?
    a[s].push(p.to_i)
  end
end

a.each do |i|
  result.push(i.sum/i.size)
end

puts header.join(",")
print result.join(",")
