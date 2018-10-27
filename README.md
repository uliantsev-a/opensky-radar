## Simple radar OpenSky
===========
The library accesses the API of OpenSky air data service
and displays a list of aircraft located within a radius of 450 km from StartPoint.
Default point the calculation of nearest radius from coordinates of Paris.

[Description API OpenSky](https://opensky-network.org/apidoc/rest.html#own-states)  
URL connection: *https://opensky-network.org/api/states/all*  

###### Example results:  
```bash  
locatorOpenSky]$ locator_opensky

Callsign: TFL444. Coord: lon 2.2784, lan 49.7277
Callsign: DLH64U. Coord: lon 6.2997, lan 49.2372
Callsign: WZZ4EN. Coord: lon 4.7079, lan 51.0273
...
Callsign: QTR8143. Coord: lon 6.2283, lan 49.6354
Callsign: SWR63J. Coord: lon 2.688, lan 49.0297
Callsign: SWR339. Coord: lon -0.0469, lan 51.4163
Callsign: EZY43BT. Coord: lon -3.5125, lan 47.9965

Len nearest objects: 496

```  