def solution(a, b)
  result = a
  ((a+1)..b).each do |i|
    result = result^i
  end
  puts result
end

solution(5, 8)
