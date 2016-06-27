
Dir.chdir "tmp_xml_de"
Dir["*.xml"].each do |filename|
  puts filename
  file = File.read(filename)
  file.gsub!(/"pl\d"/, "\"pl\"")
  File.open("../xml_de/" + filename, "w") do |f|
    f.write file
  end
end
Dir.chdir ".."

Dir.chdir "tmp_xml_en"
Dir["*.xml"].each do |filename|
  puts filename
  file = File.read(filename)
  file.gsub!(/"pl\d"/, "\"pl\"")
  File.open("../xml_en/" + filename, "w") do |f|
    f.write file
  end
end
Dir.chdir ".."

