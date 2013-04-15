#! usr/bin/perl

$/ = "//";      # break up records on genbank // delimiter
while (<>) {
#    next unless /LOCUS[ ]*(\S+)[ ]*(\d+) bp[ ]*(\w+)/; #matches LOCUS line
#    $locus = $1;
#    $bp = $2;
#    $type = $3;
    /ACCESSION[ ]*(\S+)/; #matches ACCESSION line
    $accession = $1;
    /SOURCE[ ]*(\S+)/; #matches first word of source only sometimes= genus
    $source = $1;
    /AUTHORS[ ]*(\w+),/; #Matchs first author surname
    $author = $1;
    /TITLE[ ]*(\S+)/; #matches TITLE line
    $title = $1;
    /organism="[ ]*(\S+)[ ]*(\w+).|"/; #matches genus and species
    $genus = $1;
    $species = $2;
    /isolate[ ]*(\S+)/; #matches isolate line, often location
    $isolate = $1;
    /ORIGIN(.*)$/s; #matches from after ORIGIN to end of file
    $seq = $1;
    $seq =~ tr/tcagTCAGnrswymNRSWYM//cd; #removes non-DNA characters
    $seq =~ s/(.{60}.)/$1\n/g; #prints 60chars wide
#    print ">gb|$accession $locus $type $source $author $isolate $genus $species\n$seq\n";
    print ">$genus $species $accession\n$seq\n";
}

