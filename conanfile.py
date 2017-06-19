from conans import ConanFile, CMake, tools
import os


class CbloscConan(ConanFile):
    name = "c-blosc"
    description = "An extremely fast, multi-threaded, meta-compressor library"
    version = "0.2"
    license = "BSD"
    url = "https://api.bintray.com/conan/albertosm27/c-blosc-test"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

     def source(self):
        # patch to ensure compatibility
        tools.replace_in_file("c-blosc-0.2/CMakeLists.txt", "PROJECT(blosc)", '''PROJECT(blosc)
            include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
            conan_basic_setup()''')
    
    def build(self):
        cmake = CMake(self)
        shared = "-DBUILD_SHARED_LIBS=ON" if self.options.shared else ""
        self.run('cmake c-blosc-0.2/ -DBUILD_TESTS=OFF %s %s' %
                 (cmake.command_line, shared))
        self.run("cmake --build . --target install %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include")
        self.copy("*.lib", dst="lib", src="lib", keep_path=False)
        self.copy("*.dll", dst="bin", src="bin", keep_path=False)
        self.copy("*.dylib", dst="bin", src="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["blosc"]
