pypath=`which python`
if test -z $pypath; then
	echo "No valid python version" >&2
	exit 1
fi

if test \! -d bin; then
	mkdir bin
fi

if test -e bin/flowmax; then
	echo "flowmax seems to already be installed"
	exit 0
fi

CURRENTDIR=`pwd`

echo -e "#!$pypath\n\n" >> bin/flowmax
echo -e "import flowmax, tikzexport, sys" >> bin/flowmax
echo -e "if len(sys.argv) < 2 or sys.argv[1] == '--help' or sys.argv[1] == '-h':\n" >> bin/flowmax
echo -e "\tprint \"Usage: \" + sys.argv[0] + \" <infile> [outfile]\"" >> bin/flowmax
echo -e "\texit(-1)" >> bin/flowmax
echo -e "if len(sys.argv) < 3:" >> bin/flowmax
echo -e "\toutfile = \"out\"" >> bin/flowmax
echo -e "else:" >> bin/flowmax
echo -e "\toutfile = sys.argv[2]" >> bin/flowmax
echo -e "infile = sys.argv[1]" >> bin/flowmax
echo -e "flowmax.run(infile)" >> bin/flowmax
echo -e "tikzexport.makeFig(flowmax.node.nodes, outfile)" >> bin/flowmax
echo -e "exit(0)" >> bin/flowmax

if test -e bin/flowmax; then
	chmod 755 bin/flowmax
else
	echo "Could not create \'flowmax\'" >&2
	exit 2
fi

if test -e setup.sh; then
	rm setup.sh
fi

echo -e "CURRENTDIR=$CURRENTDIR" >> setup.sh
echo -e "if test -z \`echo \$PYTHONPATH | grep -q \$CURRENTDIR/lib\`; then" >> setup.sh
echo -e "export PYTHONPATH=\$PYTHONPATH:\$CURRENTDIR/lib" >> setup.sh
echo -e "fi" >> setup.sh
echo -e "if test -z \`echo \$PATH | grep -q \$CURRENTDIR/bin\`; then" >> setup.sh
echo -e "export PATH=\$PATH:\$CURRENTDIR/bin" >> setup.sh
echo -e "fi" >> setup.sh

echo -e "Installation done. Do \n\t\$ source setup.sh\nto setup your environment.\n\nConsider adding that to your .bashrc ..."
exit 0
