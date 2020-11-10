require "csv"

test = {"sample" => 1, "test" => 2}

puts test.has_key?("sample")

puts "100".to_i

#puts test.methods

puts %(Hello "Ruby".)

str1 = 1
str2 = 1
str3 = "test"
str4 = "test"

puts str1.object_id
puts str2.object_id
puts str3.object_id
puts str4.object_id
puts str3.intern
