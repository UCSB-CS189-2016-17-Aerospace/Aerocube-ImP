# detect mistakes --warn-unitialized
cmake_minimum_required (VERSION 2.8)

# Run `cmake -DTESTS=ON ..` in the build directory, then make runTests to generate tests 
option(TESTS "Build all tests" OFF)

set(PROJECT_NAME ImP)
project(${PROJECT_NAME})

# project(openCV_hello_world)

find_package(OpenCV REQUIRED)

include_directories(${OpenCV_INCLUDE_DIRS} ${CMAKE_CURRENT_SOURCE_DIR}/lib/chilitags})

add_executable(${PROJECT_NAME} openCV_hello_world.cpp)

target_link_libraries(${PROJECT_NAME} ${OpenCV_LIBS})

include(${CMAKE_CURRENT_SOURCE_DIR}/lib/chilitags/CMakeLists.txt)


# Define the Test Suite Behavior cmake -DTEST=ON
if (TEST)
  enable_testing()
  find_package(GTest REQUIRED) # GoogleTest now comes in a module, source rqrd 
  include_directories(${GTEST_REQUIRED_DIRS})
  
  add_subdirectory(${PROJECT_SOURCE_DIR}/tests)
  add_executable(runTests ${SOURCE} ${HEADERS})

  # Standard .cpp Linking for the project
  #target_link_libraries(runTests)

  # Link GoogleTest Library and GoogleTest Main Library
  target_link_libraries(runTests ${GTEST_LIBRARIES} pthread)


  # make test
  add_test(NAME test-I-wrote COMMAND runTests)

  # Name and Command can be omitted
  #  add_test(test-I-wrote runTests)
endif()
