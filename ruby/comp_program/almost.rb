n = gets.to_i
a = gets.split(" ").map(&:to_i)

ans = max = 0
2.upto(a.max) do |i|
  c = a.count { |e| e % i == 0}
  if max < c
    max = c
    ans = i
  end
end

puts ans
