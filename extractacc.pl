#! usr/bin/perl -w
# Extract acession numbers from a genbank file

use strict;
my $save_input_separator = $/;
my $accession_count = 0;
my $no_accession = 0;

$/ = "//";      # break up records on genbank // delimiter

system("clear"); #clears terminal before continuing

print "----------------------------------------------------------------------\n";
print "                               ExtractAcc\n";
print "  program to extract just accession numbers from genbank file\n";
print "----------------------------------------------------------------------\n\n";
print " Usage: perl extractacc.pl genbankfile.gb accessionlist.txt\n\n\n";

unless (@ARGV) {
	print "No arguments, you must specify two input files\n";
	print "Usage: perl extractacc.pl genbankfile.gb accessionlist.txt\n\n";
	exit;
}

# first term from input is genbank file
my $genbankfile= $ARGV[0];
unless (-e $genbankfile && -r $genbankfile) {
	die "$genbankfile does not seem to exist or cannot be read from... exiting\n\n";
}
print " INPUT: genbank file is $genbankfile\n";

# second term from input is file to write accession numbers to
my $accessionfile= $ARGV[1];
if (-e $accessionfile) {
	die "OUTPUT: file $accessionfile already exists\n\tYou must specify a new file... exiting\n\n";
}
print "OUTPUT: accession numbers will be written to file $accessionfile\n";

# open accession number file to *append* list to
open (ACCNFILE, ">>$accessionfile") || die "cannot open $accessionfile: $!";

# open genbank file
open (GBFILE, $genbankfile) || die "cannot open $genbankfile for reading: $!";

# take stream and search for accession field
while (<>) 
{
   if (/ACCESSION[ ]*(\S+)/) #matches ACCESSION number
   { 
   print ACCNFILE "$1\n";
   ++$accession_count; #add 1 to accession number count
   }
   else 
   {
   ++$no_accession; #add 1 to records with NO accession number count
   } 
}

close GBFILE;
close ACCNFILE;

print "\twrote $accession_count accession numbers to file $accessionfile\n\n";
# this bit always returns at least 1, maybe counts final space as a record?
# if ($no_accession >=1){
# print "$no_accession records had no accession number\n\n";
# }

exit;