##Versioning
How to install Aspose Cells for Go via C++ and create a Hello World application.
**github.com/aspose-cells/aspose-cells-go-cpp/v25** is a Go module path that specifies a particular version of a third-party library. Let's break down this module path and explain its meaning:
Breaking Down the Module Path
1. **GitHub Repository Address**: github.com/aspose-cells/aspose-cells-go-cpp
- This part indicates that the library is hosted on GitHub, under the aspose-cells organization or user, in the repository named aspose-cells-go-cpp.
- Aspose.Cells is a suite of APIs for handling and manipulating spreadsheet files (like Excel).
1. **Version Number**: /v25
- /v25 indicates that this is version 24 of the library. In Go Modules, semantic versioning (SemVer) is supported, where paths containing /vN are used to explicitly specify the major version number.
- When the major version is greater than or equal to 2, the module path must include the version number to ensure compatibility and isolation between different major versions.
### **Meaning**
- **aspose-cells-go-cpp**: This is a Go language binding for a C++ library, allowing you to use Aspose.Cells functionalities within your Go programs to read, write, and manipulate Excel files, among other operations.
- **v25**: This indicates that you are referencing version 24 of the library. Different major versions may introduce incompatible changes, so specifying the version number is crucial to ensure your project depends on the correct API and behavior.
### **Usage**
To use aspose-cells-go-cpp v25 in your Go project, you need to add the following line to your project's go.mod file:
```Go
require github.com/aspose-cells/aspose-cells-go-cpp/v25 v25.x.x
```
Replace v25.x.x with the specific minor and patch version numbers, such as v25.0.0. You can automatically add and download this dependency using the go get command:
```Go
go get github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.x.x
```
