$Regex_Pattern = '^([a-z])(\w)(\s)(\W)(\d)(\D)([A-Z])([A-Za-z])([aeiouAEIOU])(\S)(\1)(\2)(\3)(\4)(\5)(\6)(\7)(\8)(\9)(\10)$';

$Test_String = <STDIN> ;
if($Test_String =~ /$Regex_Pattern/){
    print "true";
} else {
    print "false";
}
