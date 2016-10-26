cmake_minimum_required (VERSION 2.8)

project(openCV_hello_world)

find_package(OpenCV REQUIRED)

include_directories(${OpenCV_INCLUDE_DIRS} ${CMAKE_CURRENT_SOURCE_DIR}/lib/chilitags})

add_executable(openCV_hello_world openCV_hello_world.cpp)

target_link_libraries(openCV_hello_world ${OpenCV_LIBS})

include(${CMAKE_CURRENT_SOURCE_DIR}/lib/chilitags/CMakeLists.txt)
