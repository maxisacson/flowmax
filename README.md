FlowMax
=======

A python library to generate latex code for flow charts.


Max Isacson, max.isacson@cern.ch, tikz stuff by Johan Asplund, johan.asplund@math.uu.se.

INSTALLATION
------------
From the command line, do:
```shell
$ git clone https://github.com/maxisacson/flowmax.git
$ cd flowmax
$ ./install.sh
$ source setup.sh
```
The command `$ source setup.sh` sets up the `$PATH` and `$PYTHONPATH` environment variables to include the directories `flowmax/bin` and `flowmax/lib`. It has to be run every time you start a fresh shell and want to use the library. To avoid this you can add the line `source /path/to/flowmax/setup.sh` to your `.bashrc` file, where `/path/to` is the path to the directory you `git clone`'ed in. If you did this in your home directory you can just add `source ~/flowmax/setup.sh`.

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
```shell
$ flowmax myfile.fm
```
This will give you a file called `out.tex` which you can compile with e.g. `pdflatex`, `xelatex` or `lualatex`.

You can also include use the libraries in your own python script. Just do something like this:
```python
import flowmax
import tikzexport

flowmax.run("myfile.fm")
tikzexport.makeFig(flowmax.node.nodes,"target")
```

This will give you a file called `target.tex` which you again can compile with your favourite `latex` flavour.

TODO
----
- Implement better arrows.
- Fix bugs (mostly has to do with the arrows or nodes)
- Improve the sorting algorithm

LICENSE
-------
This project is distributed under the GNU General Public License https://www.gnu.org/licenses/gpl-3.0.txt
