find ./www.ngs.noaa.gov/AERO/uddf/ -type f |
while read x
do
  nf=$( head -1 $x | awk -F'|' '{print NF}' )
  if test 6 = $nf
  then
    awk -F'|' '''
      NR==3 { city=$2; state=$3 }
      NR==8 { lat=$2; long=$3 }
      END {
        gsub(/^ */, "", city)
        gsub(/^ */, "", state)
        gsub(/^ */, "", lat)
        gsub(/^ */, "", long)
        gsub(/ *$/, "", city)
        gsub(/ *$/, "", state)
        gsub(/ *$/, "", lat)
        gsub(/ *$/, "", long)
        if (lat != "" && long != "") {
          printf "%s;%s;%s;%s\n", state, city, lat, long
        }
      }
    ''' $x
  fi
done | LANG=C sort
