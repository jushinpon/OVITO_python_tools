=b
set source path for data files
cutoff=5.0, number_of_bins=100 can be modified
=cut
use warnings;
use strict;
use Cwd;

my $currentPath = getcwd();# dir for all scripts
chdir("..");
my $mainPath = getcwd();# main path of Perl4dpgen dir
chdir("$currentPath");

#########You need to assign the following for your own system
#my @DLP_elements = ("Al","Co", "Cr", "Fe", "Ni");#must follow your DLP element order!!!!!
#my $csro_cut = 2.7; #rcut for calculating csro. Use OVITO to get the proper value
my $sour = ""; #for all data files
#########

#`rm -rf $currentPath/temp`;#remove old temp folder first
my @all_data = `find $currentPath/$sour -type f -name "*.data"`;
map { s/^\s+|\s+$//g; } @all_data;
die "No data files are found!\n" unless(@all_data);
#print "@all_folders\n";

for my $f (@all_data){
    my $path = `dirname $f`;
    $path =~ s/^\s+|\s+$//g;
    my $filename = `basename $f`;
    $filename =~ s/^\s+|\s+$//g;
    my $prefix = $filename;
    $prefix =~ s/\.data//g;
    #print "\$prefix: $prefix, \$filename: $filename \n";
    unlink "$currentPath/input.data";
    unlink "$currentPath/rdf_results.csv";

    `cp $f $currentPath/input.data`;
    `python partial_rdf.py;python rdf_plot.py`;

    unlink "$path/rdf-$prefix.png";
    unlink "$path/rdf-$prefix.csv";
    `mv $currentPath/rdf_results.csv $path/rdf-$prefix.csv`;
    `mv $currentPath/RDF.png $path/rdf-$prefix.png`;
    unlink "$currentPath/input.data";
}
    