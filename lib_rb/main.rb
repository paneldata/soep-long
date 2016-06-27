
system "stata12 split_de.do"
system "mv data_de/pl.dta tmp/de.dta"
system "stata12 split_en.do"
system "mv data_en/pl.dta tmp/en.dta"

system "Rscript run_de.R"
system "Rscript run_en.R"

Dir["*.xml"].each do |filename|
  puts filename
  file = File.read(filename)
  file.gsub!(/pl[0-9]\.dta/, "pl")
  file.gsub!(/[0-9]\.dta/, "")
  File.open(filename, "w") do |f|
    f.write file
  end
end

Dir["*.xml"].each do |filename|
  puts filename
  file = File.read(filename)
  file.gsub!(/pl[0-9]\.dta/, "pl")
  file.gsub!(/[0-9]\.dta/, "")
  File.open(filename, "w") do |f|
    f.write file
  end
end

