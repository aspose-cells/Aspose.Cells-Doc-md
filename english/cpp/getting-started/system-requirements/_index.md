---
title: System Requirements
type: docs
weight: 30
url: /cpp/system-requirements/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Aspose.Cells for C++ is a native C++ library that enables C++ developers to create, manipulate, and convert spreadsheets programmatically without requiring Office Automation or the Microsoft Excel application.

## Supported Operating Systems

Aspose.Cells for C++ supports the following 64‑bit or 32‑bit operating systems and platforms:

<table>  
	<tr>
			<td style="font-weight: bold; width:400px">Operating System</td>
			<td style="font-weight: bold; width:400px">Versions</td>
		</tr>
  <tr>
			<td>Microsoft Windows</td>
			<!--- <td><ul><li>Windows 2008 Server (x64)</li><li>Windows 2012 Server (x64)</li><li>Windows 2012 R2 Server (x64)</li><li>Windows 2016 Server (x64)</li><li>Windows 2019 Server (x64)</li><li>Windows Vista (x64)</li><li>Windows 7 (x64)</li><li>Windows 8, 8.1 (x64)</li><li>Windows 10 (x64)</li><li>Windows 11 (x64)</li></ul></td> ---> 
			<td><ul><li>Windows x86</li><li>Windows x86_64</li></ul></td>
  </tr>
  <tr>
			<td>Linux</td>
			<td><ul><li>Linux x86_64</li><!---li>Ubuntu 20.04 or later</li><li>Fedora</li><li>OpenSUSE</li><li>CentOS</li>---><li>Linux for ARM (aarch64)</li></ul></td>
		</tr>
  <tr>
			<td>macOS</td>
			<td><ul><li>macOS 11 or later (arm64, x86_64)</li></ul></td>
		</tr>
</table>

## Development Environment

You can use Aspose.Cells for C++ when developing applications for Windows, Linux, or macOS.

### Windows

Aspose.Cells for C++ can be used to develop applications in any development environment that supports [Microsoft Visual Studio v142 Platform Toolset](https://docs.microsoft.com/en-us/cpp/porting/binary-compat-2015-2017?view=msvc-160), but the environments listed in the following table are explicitly supported:

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">Development environments</td>
		</tr>
  <tr>
			<td><ul><li>Microsoft Visual Studio 2019</li><li>Microsoft Visual Studio 2022</li></ul></td>
			</tr>
</table>

### Linux

Aspose.Cells for C++ can be used to develop applications in a development environment that supports C++11 or higher, but the following compilers and tools are explicitly supported:

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">Compilers</td>
		</tr>
  <tr>
			<td><ul><li>GCC 9.4.0 or later</li></ul></td>
			</tr>
</table>

### Additional Dependency on Linux
Aspose.Cells for C++ on Linux depends on <a href="https://www.freedesktop.org/wiki/Software/fontconfig/">fontconfig</a> binaries, both the dynamic library and the tool. Please install them before using:

1. Installing fontconfig on Ubuntu or Debian  
   `sudo apt install libfontconfig fontconfig`
2. Installing fontconfig on Fedora or CentOS  
   `sudo yum install fontconfig`

### macOS 
Aspose.Cells for C++ can be used to develop applications in the following development environments:
* Xcode 12.5.1 or later
* Clang and libc++ (which are shipped by default with Xcode)
{{< app/cells/assistant language="cpp" >}}
