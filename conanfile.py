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
