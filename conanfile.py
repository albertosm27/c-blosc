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
        shared = {"BUILD_SHARED_LIBS": self.options.shared}
        cmake = CMake(self.settings)
        cmake.configure(self, defs=shared)
        cmake.build(self)

    def package(self):
        self.copy("*.h", dst="include")
        self.copy("*.lib", dst="lib", src="lib", keep_path=False)
        self.copy("*.dll", dst="bin", src="bin", keep_path=False)
        self.copy("*.dylib", dst="bin", src="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["blosc"]
