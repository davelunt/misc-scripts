#! usr/bin/perl -w

# By Dave Lunt, code assembled from many different sources

# A script to find if two multifasta sequence files contain different record
# names and print out any differences. Useful when concatenating files.

print "\n\n";
print "----------------------------------------------------------------------\n";
print "                               namediff.pl\n";
print "  find fasta header names that are NOT shared between two files\n";
print "----------------------------------------------------------------------\n\n";

# check 2 input files are specified.
unless (@ARGV ==2) { 
	die "You must specify two input files in fasta format.\nUsage: perl namediff.pl fastafile1.fas fastafile2.fas\n\n" 
	}

# first term from input is file1
my ($fasta1) = $ARGV[0];
print "First fasta file is $fasta1\n";

# second term from input is file2
my ($fasta2) = $ARGV[1];
print "Second fasta file is $fasta2\n\n";

# open file1 and feed into array
open (FASTA1, $fasta1) || die "cannot open $fasta1 for reading: $!";
while (my $line1 = (<FASTA1>)) {
 	chomp ($line1); 
{
if ($line1 =~ /^>/) { # if line starts with ">"
	push (@file1, $line1); # push whole header line including > to array
}}}
close FASTA1;

# count records and print unless more than 10
my $file1_count= scalar @file1;

# print "@file1\n";

print "There are $file1_count records in $fasta1\n";
unless ($file1_count >10) {
	print "here are the title lines (names) of $fasta1\n";
	foreach (@file1) {
  		print "  $_\n";
}

	print "\n";
	}

# open file2 and feed into array
open (FASTA2, $fasta2) || die "cannot open $fasta2 for reading: $!";
while (my $line2 = (<FASTA2>)) {
 	chomp ($line2); 
{
if ($line2 =~ /^>/) { # if line starts with ">"
	push (@file2, $line2); # push whole header line including > to array
}}}
close FASTA2;

# count records and print unless more than 10
my $file2_count= scalar @file2;
print "There are $file2_count records in $fasta2\n";
# print "@file2\n";

unless ($file2_count >10) {
	print "here are the title lines (names) of $fasta2\n";
	foreach (@file2) {
  		print "  $_\n";
}

	print "\n";
	}

# find diffs
# count diffs
# not my code!

my %seen = ();                  # lookup table (hash) to test membership of B
my @newonly = ();                 # answer

# build lookup table
foreach $item (@file2) { $seen{$item} = 1 }

# find only elements in @A and not in @B
foreach $item (@file1) {
    unless ($seen{$item}) {
        # it's not in %seen, so add to @newonly
        push(@newonly, $item);
    }
}
my $newcount= scalar @newonly;
print "There are $newcount sequence names in $fasta1 not also in $fasta2\n";

# print new accession if <20

unless ($newcount >20) {
	print "-list of new record titles (names)\n @newonly\n\n";
	}

# second go, reversing everything

# find diffs
# count diffs
# not my code!

my %seen1 = ();                  # lookup table (hash) to test membership of B
my @newonly1 = ();                 # answer

# build lookup table
foreach $item1 (@file1) { $seen1{$item1} = 1 }

# find only elements in @A and not in @B
foreach $item1 (@file2) {
    unless ($seen1{$item1}) {
        # it's not in %seen, so add to @newonly
        push(@newonly1, $item1);
    }
}
my $newcount1= scalar @newonly1;
print "There are $newcount1 sequence names in $fasta2 not also in $fasta1\n";

# print new accession if <20

unless ($newcount1 >20) {
	print "-list of new record titles (names)\n @newonly1\n";
	}

print "-----------END-----------\n\n";

exit;