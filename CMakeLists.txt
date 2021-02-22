cmake_minimum_required(VERSION 3.13) # Cmake version check
project(cv_detection) # Create project
set(CMAKE_CXX_STANDARD 14) # Enable C++ 14

file(
        GLOB_RECURSE
        source_files
        sources/*.cpp
)

file(
        GLOB_RECURSE
        header_files
        headers/*
)

add_executable(cv_detection ${source_files} ${header_files})

