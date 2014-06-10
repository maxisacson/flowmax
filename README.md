FlowMax
=======

A python library to generate latex code for flow charts.


Max Isacson, max.isacson@cern.ch, tikz stuff by Johan Asplund, johan.asplund@math.uu.se.

INSTALLATION
------------
Download the package using `$ git clone https://github.com/maxisacson/flowmax.git` and move to the created directory `$ cd flowmax`. Now run `install.sh`, like so: `$ ./install.sh`. This creates the executable `bin/flowmax` and the script `setup.sh`. Now you need to set up your environment by sourcing `setup.sh`, do this by `$ source setup.sh`. This needs to be done every time you want to run `flowmax` in a newly started shell. To skip the need for this you can add something like `source /path/to/flowmax/setup.sh` to your `.bashrc`-file, in my case it would be `source ~/flowmax/setup.sh`, which probably works for you as well if you installed in your home directory.

Note that this package requires either ```latex XeLaTeX`` or ```latex PdfLaTeX``` to be installed.

Usage
-----
Create a file `myfile.fm`. In it define your nodes, for example:
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
or simply `$ flowmax myfile.fm` in a `BASH`-like shell environment.

This will give you a pdf file, which is compiled by either `pdflatex` or `xelatex`

TODO
----
- Implement better arrows.
- Fix bugs (mostly has to do with the arrows or nodes)
- Improve the sorting algorithm

LICENSE
-------
This project is distributed under the GNU General Public License https://www.gnu.org/licenses/gpl-3.0.txt
