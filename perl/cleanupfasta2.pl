#! usr/bin/perl
use strict;
use warnings;

my $recordcount=0; #number of fasta records

# read in a fasta file
my $fastafile = 'silvatest.fasta';
chomp $fastafile;

# check if it exists, and then can be opened
unless ( -e $fastafile) {
	print " File \"$fastafile\" does not exist!\n\n";
	exit;
}
unless (open(DNAFILE, $fastafile)){
	print "could not open file $fastafile!\n\n";
	exit;
}

# put data into an array and close original file
my @DNA = <DNAFILE>;
close DNAFILE;

foreach my $line (@DNA) {
	print "line: $line";
	
	# if line  begins with > count record
	if ($line=~/^>/){
		++$recordcount;
		
		$line=~ s/silva\|//g; #delete word silva|
		$line=~ s/\s/_/g; #remove whitespace insert underscore
		$line=~ s/\|1\|/_/g; #remove |1|
		$line=~ s/\|/_/g; #remove remaining pipes
		$line=~ s/__/_/g; #remove double underscores
		$line=~ s/\.//g; #remove periods, replace with nothing
		
		next;
		}
}
	print "There were $recordcount records detected\n\n";

exit;
