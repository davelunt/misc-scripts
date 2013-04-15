#! usr/bin/perl

# Creates an annotation file for treedyn (http://www.treedyn.org/) from a file containing multiple Genbank
# files. Annotations are of the form key{value}. Keys must not contain spaces.

# usage: gb2treedyn.pl infile.gb > outfile.tlf

$/ = "//";      # break up records on genbank // delimiter
while (<>) {
    /ACCESSION[ ]*(\S+)/; # matches ACCESSION line
    $accession = $1;
    /AUTHORS[ ]*(\w+),/; # matches first author surname
    $author = $1;
    /organism="[ ]*(\S+)[ ]*(\w+).|"/; # matches genus and species
    $genus = $1;
    $species = $2;
    /isolate[ ]*(\S+)/; # matches isolate line
    $isolate = $1;

    print "$accession \tgenus {$genus} \tspecies {$species} \taccession {$accession} \tisolate {$isolate} \tauthor {$author}\n";
}
exit;	