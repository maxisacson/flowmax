FlowMax
=======

A python library to generate latex code for flow charts.


Max Isacson, max.isacson@cern.ch, tikz stuff by Johan Asplund, johan.asplund@math.uu.se.

Usage
-----
Create a file `myfile.fm` or something. In it define your nodes, for example:
```
node 0 {Start here} symbol start connect 1;
node 1 {Yes or No?} symbol query {Yes}{No} connect 2,3;
node 2 {You answered "yes"} symbol action connect 4;
node 3 {You answered "no"} symbol action connect 4;
node 4 {It ends here} symbol stop;
```
Then you can run the library on the file, like so:
```python
import flowmax
import tikzexport

flowmax.run("myfile.fm")
tikzexport.makeFig(flowmax.node.nodes,"target")
```
or simply `$ flowmax myfile.fm`.

This will give you a file called `target.tex` (`out.tex` in the latter)  which you can compile with e.g. `pdflatex`.

TODO
----
- Implement better arrows.
- Fix bugs (mostly has to do with the arrows or nodes)
- Improve the sorting algorithm

LICENSE
-------
This project is distributed under the GNU General Public License https://www.gnu.org/licenses/gpl-3.0.txt
