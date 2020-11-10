def utopianTree(n)
  result = 1
  n.times do |i|
    puts result
    result = i%2 == 0 ? result*2 : result+1
  end
  return result
end

print utopianTree 4
