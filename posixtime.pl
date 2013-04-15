#!/usr/bin/perl

# This is a script to time how long it takes your program to complete
# Insert your code into the space occupied by # Script goes here # text
# It should report in a user friendly manner the time taken

# This seems to work fine for me, but check carefully before doing 
# anything critical

use POSIX;
my $starttime = time; # note start time
# note and print start time in readable format
my $start_string = POSIX::strftime("%Y-%m-%d %H:%M:%S", localtime);
print "\nSTART:\t$start_string\n";

# Script goes here #
	print "\n";
	
	use constant TRUE => 1;
	use constant FALSE => 0;
	
	use constant STOPNUMBER => 3;
	
	$count=0;
	
	while ( TRUE ) 
	{
		$count++;
		sleep 1;
		print "$count   Welcome to the wonderful world of timing scripts!\n";
		if ($count == STOPNUMBER)
		{
			last
		}
	}
	print "\n";
# Script ends here #

# Calculate total runtime (current time minus start time) #
my $runtime = time - $starttime; # in seconds
# calculate this in readable format
my $end_string = POSIX::strftime("%Y-%m-%d %H:%M:%S", localtime);

# Print runtime #

printf("END:\t$end_string\n");
printf("\n----------------------------------------------\n");

printf("Runtime: \t$runtime \t\tseconds\n"); # number of secs since start

# The line below should print out 2 digit integer values for hours, mins 
# and seconds by dividing $runtime (seconds) by appropriate amounts
printf("Runtime: \t%02d:%02d:%02d \th:m:s\n",
int($runtime / 3600), int(($runtime % 3600) / 60), int($runtime % 60));

printf("----------------------------------------------\n\n");
exit;


