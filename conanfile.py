from conans import ConanFile, CMake, tools
import os


class CbloscConan(ConanFile):
    name = "c-blosc"
    version = "0.1"
    license = "BSD"
    url = "https://api.bintray.com/conan/albertosm27/c-blosc-test"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = "./*"

    def source(self):
        # This small hack might be useful to guarantee proper /MT /MD linkage in MSVC
        # if the packaged project doesn't have variables to set it properly
        tools.replace_in_file(
            "CMakeLists.txt",
            "PROJECT(MyBlosc)", '''PROJECT(MyBlosc) 
             include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake) conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        shared = "-DBUILD_SHARED_LIBS=ON" if self.options.shared else ""
        self.run('cmake .. -DBUILD_TESTS=OFF %s %s' %
                 (cmake.command_line, shared))
        self.run("cmake --build . --target install%s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include",
                  src="blosc")
        self.copy("*blosc.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["blosc"]
