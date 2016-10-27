# Aerocube-ImP
This library will handle some of the image processing magic/voodoo for now.


[[https://github.com/UCSB-CS189-2016-17-Aerospace/Aerocube-ImP/blob/master/docs/angel-marker7.png|alt=Angel holding marker 7]]

# Dependencies
## Chilitag Dependencies
See source Chilitags repository for reference: <https://github.com/chili-epfl/chilitags>

Install OpenCV Libraries and CMake

`sudo apt-get install libopencv-dev cmake`

# Instructions
To build the project:
```
mkdir build && cd build
cmake ..
make
```

To build and execute chilitags samples: 

```
mkdir build && cd build
cmake -DWITH_SAMPLES=ON ..
make
./lib/chilitags/samples/detect-live

```



# Feature List
  * ImP - 0.0.0
    * CMake file for OpenCV library compilation
    * Base Hello World Application in OpenCV

  * ImP - 0.0.1 - (10/23-10/29)
    * Chilitags is imported
    * Chilitags dependency is compiling with a global CMake


# Licenses
Credit goes to Chilitags for providing Fiducial Marker tracking software.

Chilitags: Robust Fiducial Markers for Augmented Reality. Q. Bonnard, S. Lemaignan, G. Zufferey, A. Mazzei, S. Cuendet, N. Li, P. Dillenbourg. CHILI, EPFL, Switzerland. http://chili.epfl.ch/software. 2013.

