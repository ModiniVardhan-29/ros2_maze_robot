cmake_minimum_required(VERSION 3.8)
project(bumper_bot)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()

find_package(ament_cmake REQUIRED)

# Install launch files
install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

# Install URDF files
install(
  DIRECTORY urdf
  DESTINATION share/${PROJECT_NAME}
)

# Install models (for obstacles)
install(
  DIRECTORY models
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
