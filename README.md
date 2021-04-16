# lat-long
latitude/longitude data and azimuth calculator.

DEMO: http://yak.net/azimuth.html

## US Airport Data

I CANNOT BE SURE THAT THIS INFORMATION OR MY CRUDE SCRAPING
IS ACTUALLY CORRECT.  USE IT AT YOUR OWN RISK.

This data was scraped from https://www.ngs.noaa.gov/AERO/uddf/
where it should be public information from the US government.
I used wget with these options, which takes about twenty minutes:

```
-m -nv -np -Ubrowser -w1 --random-wait https://www.ngs.noaa.gov/AERO/uddf/
```

I casually reverse-engineered just enough of the format to pull
the city and state with what seems to be the
approximate latitude and longitude of each airport.

In my application, I don't really care about airports.
I just want rough coordinates for some points nearby cities,
and by averaging the cities to get a point for each state,
to compute directions for pointing amateur radio antennae.

`proc-aero.sh` is my bash script to scrape the files from wget.

`latlong-us-aero.txt` is the result.

## Scripts

```
python2 latlong-to-web.py < latlong-us-aero.txt
```

Take that output and paste it into `azimuth.html`
where it belongs.

## work in progress

. . .
