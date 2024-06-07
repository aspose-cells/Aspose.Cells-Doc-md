---
title: 系统要求
type: docs
weight: 30
url: /zh/cpp/system-requirements/
---

Aspose.Cells for C++ 是一种原生 C++ 库，使 C++ 开发人员能够在不需要办公自动化或 Microsoft Excel 应用程序的情况下以编程方式创建、操作和转换电子表格。

## 支持的操作系统

Aspose.Cells for C++ 支持以下 64 位或 32 位操作系统和平台：

<table>  
	<tr>
			<td style="font-weight: bold; width:400px">操作系统</td>
			<td style="font-weight: bold; width:400px">版本</td>
		</tr>
  <tr>
			<td>Microsoft Windows</td>
			<!--- <td><ul><li>Windows 2008 Server (x64)</li><li>Windows 2012 Server (x64)</li><li>Windows 2012 R2 Server (x64)</li><li>Windows 2016 Server (x64)</li><li>Windows 2019 Server (x64)</li><li>Windows Vista (x64)</li><li>Windows 7 (x64)</li><li>Windows 8, 8.1 (x64)</li><li>Windows 10 (x64)</li><li>Windows 11 (x64)</li></ul></td> --->
			<td><ul><li>Windows x86</li><li>Windows x86_64</li></ul></td>
  </tr>
  <tr>
			<td>Linux</td>
			<td><ul><li>Linux x86_64</li><!---li>Ubuntu 20.04 或更高版本</li><li>Fedora</li><li>OpenSUSE</li><li>CentOS</li---><li>Linux for ARM (aarch64)</li></ul></td>
		</tr>
  <tr>
			<td>macOS</td>
			<td><ul><li>macOS 11 或更高版本(arm64，x86_64)</li></ul></td>
		</tr>
</table>

## 开发环境

开发应用程序时，可以在 Windows、Linux 或 macOS 上使用 Aspose.Cells for C++。

### Windows

Aspose.Cells for C++可用于在支持[Microsoft Visual Studio v142 Platform Toolset](https://docs.microsoft.com/zh-cn/cpp/porting/binary-compat-2015-2017?view=msvc-160)的任何开发环境中开发应用程序，但以下表中列出的环境得到了显式支持:

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">开发环境</td>
		</tr>
  <tr>
			<td><ul><li>Microsoft Visual Studio 2019</li><li>Microsoft Visual Studio 2022</li></ul></td>
			</tr>
</table>

### Linux

Aspose.Cells for C++可用于在支持C++11或更高版本的开发环境中开发应用程序，但以下编译器和工具得到了显式支持:

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">编译器</td>
		</tr>
  <tr>
			<td><ul><li>GCC 9.4.0或更高版本</li></ul></td>
			</tr>
</table>

### Linux上的额外依赖
Aspose.Cells for C++ on Linux depends on <a href="https://www.freedesktop.org/wiki/Software/fontconfig/">fontconfig</a> binaries both dynamic library and tool. Please install it before using:

1. Installing fontconfig on Ubuntu or Debian<br>
`sudo apt install libfontconfig fontconfig`
1. Installing fontconfig on Fedora or CentOs<br>
`sudo yum install fontconfig`

### macOS 
Aspose.Cells for C++可在以下开发环境中使用:
* Xcode 12.5.1或更高版本
* Clang和libc++(默认与Xcode一起提供)
