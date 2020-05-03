#!/usr/bin/perl

my @files = ();


sub getFiles {
  my ($array, $directory) = @_;
  my $dir;
  opendir($dir, $directory);

  foreach my $file (readdir($dir)) {
    if ($file eq "." or $file eq "..") {
      next();
    }

    my $path = "$directory/$file";
    
    if (-f $path) {
      # print ("$path is a file\n");
      my @stats = stat($path);
      my $mode = sprintf('%04o', @stats[2] & 07777);
      my $user = getpwuid(@stats[4]);
      my $group = getgrgid(@stats[5]);
      push(@$array, "\%attr($mode,root,$group) $path");
      next();
    }

    if (-l $path) {
      push(@$array, $path);
      next();
    }

    if (-d $path) {
      # print ("$path is a directory\n");
      getFiles($array, $path);
      next();
    }
  }
  
  close($dir);
};

getFiles(\@files, $ARGV[0]);


foreach (@files) {
  print("$_\n");
}

# opendir($dir, $directory);


# while (my $file = readdir($dir)) {
#   print("$file\n");
# };

# closedir($dir);