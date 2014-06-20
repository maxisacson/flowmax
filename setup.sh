CURRENTDIR=/Users/asplund/Documents/flowmax
if test -z `echo $PYTHONPATH | grep -q $CURRENTDIR/lib`; then
export PYTHONPATH=$PYTHONPATH:$CURRENTDIR/lib
fi
if test -z `echo $PATH | grep -q $CURRENTDIR/bin`; then
export PATH=$PATH:$CURRENTDIR/bin
fi
