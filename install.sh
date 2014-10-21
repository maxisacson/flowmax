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

cat <<EOF > bin/flowmax
#!$pypath
import flowmax, tikzexport, sys
if len(sys.argv) < 2 or sys.argv[1] == '--help' or sys.argv[1] == '-h':
    print "Usage: " + sys.argv[0] + " <infile> [outfile]"
    exit(-1)
if len(sys.argv) < 3:
    outfile = "out"
else:
    outfile = sys.argv[2]
infile = sys.argv[1]
flowmax.run(infile)
tikzexport.makeFig(flowmax.node.nodes, outfile)
exit(0)
EOF

if test -e bin/flowmax; then
	chmod 755 bin/flowmax
else
	echo "Could not create \'flowmax\'" >&2
	exit 2
fi

if test -e setup.sh; then
	rm setup.sh
fi

cat <<EOF > setup.sh
CURRENTDIR=$CURRENTDIR
if test -z \`echo \$PYTHONPATH | grep -q \$CURRENTDIR/lib\`; then
export PYTHONPATH=\$PYTHONPATH:\$CURRENTDIR/lib
fi
if test -z \`echo \$PATH | grep -q \$CURRENTDIR/bin\`; then
export PATH=\$PATH:\$CURRENTDIR/bin
fi
EOF

echo -e "Installation done. Do \n\t\$ source setup.sh\nto setup your environment.\n\nConsider adding that to your .bashrc ..."
exit 0
