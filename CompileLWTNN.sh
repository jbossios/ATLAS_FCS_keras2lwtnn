mkdir build/
cd build/
cmake -DBUILTIN_BOOST=true -DBUILTIN_EIGEN=true ../lwtnn-2.12.1/
make -j 4
