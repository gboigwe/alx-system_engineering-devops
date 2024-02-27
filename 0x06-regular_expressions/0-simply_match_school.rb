#!/usr/bin/env ruby
#if $1 == /[school]/
#  puts "Hello"
#end
puts ARGV[0].scan(/[School]/).join
