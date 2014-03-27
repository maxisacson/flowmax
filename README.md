FlowMax
=======

A python library to generate latex code for flowcharts.


Max Isacson, max.isacson@cern.ch, Tikz stuff by Johan Asplund, johan.asplund@math.uu.se

Usage
-----
Create a file 'myfile.fm' or something. In it define you nodes, for example:
```
node 0 {Start here} symbol start connect 1;
node 1 {Yes or No?} symbol query connect 2,3;
node 2 {You answered "yes"} symbol action connect 4;
node 3 {You answered "no"} symbol action connect 4;
node 4 {It ends here} symbol stop;
```
Then you can run the library on the file, like so:
```pyhton
import flowmax

flowmax.run("myfile.fm")
```


TODO
----
- Write the damn thing.

LICENSE
-------
This project is distributed under the GNU General Public License https://www.gnu.org/licenses/gpl-3.0.txt
