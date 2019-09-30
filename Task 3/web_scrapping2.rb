require 'Nokogiri'
require 'HTTParty'
require 'Pry'

search = HTTParty.get('https://google.com/search?q=linux&num=20')
parsing = Nokogiri::HTML(search)
array = []
parsing.css('.iUh30').css('.TbwUpd').css('.LC201b').map do |a|
    b = a.text
    array.push(b)
end

Pry.start(binding)
