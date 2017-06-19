from conans import ConanFile, CMake
import os


channel = os.getenv("CONAN_CHANNEL", "testing")
username = os.getenv("CONAN_USERNAME", "albertosm27")


class CbloscTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "c-blosc/0.2@%s/%s" % (username, channel)
    generators = "cmake"

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")

    def test(self):
        os.chdir("bin")
        self.run("ctest")
