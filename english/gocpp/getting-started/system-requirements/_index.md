---
title: System Requirements
type: docs
weight: 30
url: /go-cpp/system-requirements/
---

Aspose.Cells for Go via C++ is a native Go library that enables Go developers to create, manipulate and convert spreadsheets programmatically without requiring Office Automation or Microsoft Excel application.

## Supported Operating Systems

Aspose.Cells for Go supports the following 64-bit operating systems and platforms:

<table>  
 <tr>
   <td style="font-weight: bold; width:400px">Operating System</td>
   <td style="font-weight: bold; width:400px">Versions</td>
  </tr>
  <tr>
   <td>Microsoft Windows</td>
   <!--- <td><ul><li>Windows 2008 Server (x64)</li><li>Windows 2012 Server (x64)</li><li>Windows 2012 R2 Server (x64)</li><li>Windows 2016 Server (x64)</li><li>Windows 2019 Server (x64)</li><li>Windows Vista (x64)</li><li>Windows 7 (x64)</li><li>Windows 8, 8.1 (x64)</li><li>Windows 10 (x64)</li><li>Windows 11 (x64)</li></ul></td> --->
   <td><ul><li>Windows x86_64</li></ul></td>
  </tr>
  <tr>
   <td>Linux</td>
   <td><ul><li>Linux x86_64</li><!---li>Ubuntu 20.04 or later</li><li>Fedora</li><li>OpenSUSE</li><li>CentOS</li---></ul></td>
  </tr>
</table>

## Development Environment

You can use Aspose.Cells for Go via C++ when developing applications for Windows and Linux.

### Windows

Aspose.Cells for Go via C++ can be used to develop applications in any development environment which supports [Microsoft Visual Studio v142 Platform Toolset](https://docs.microsoft.com/en-us/go/porting/binary-compat-2015-2017?view=msvc-160), but the environments listed in the following table are explicitly supported:

### Linux

Aspose.Cells for Go via C++ can be used to develop applications in a development environment that supports Go 1.13 or higher, but the following compiler and tool are explicitly supported:

<table>  
 <tr>
   <td style="font-weight: bold; width:800px">Compilers</td>
  </tr>
  <tr>
   <td><ul><li>GCC 9.4.0 or later</li></ul></td>
   </tr>
</table>

### Additional Dependency on Linux

Aspose.Cells for Go on Linux depends on <a href="https://www.freedesktop.org/wiki/Software/fontconfig/">fontconfig</a> binaries, both the dynamic library and the tool. Please install it before using:

1. Installing fontconfig on Ubuntu or Debian<br>
   `sudo apt install libfontconfig fontconfig`
2. Installing fontconfig on Fedora or CentOS<br>
   `sudo yum install fontconfig`