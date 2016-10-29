# detect mistakes --warn-unitialized
cmake_minimum_required (VERSION 2.8)

option(TEST "Build all tests" OFF)

set(PROJECT_NAME ImP)

project(${PROJECT_NAME})

# project(openCV_hello_world)

find_package(OpenCV REQUIRED)

include_directories(${OpenCV_INCLUDE_DIRS} ${CMAKE_CURRENT_SOURCE_DIR}/lib/chilitags})

add_executable(${PROJECT_NAME} openCV_hello_world.cpp)

target_link_libraries(${PROJECT_NAME} ${OpenCV_LIBS})

include(${CMAKE_CURRENT_SOURCE_DIR}/lib/chilitags/CMakeLists.txt)


# Define the Test Suite Behavior cmake -DTEST=ON
#if (TEST)
#  add_subdirectory(lib/gtest)
#  enable_testing()
#  include_directories(${gtest}
