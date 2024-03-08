---
title: 系统要求
type: docs
weight: 30
url: /zh/cpp/system-requirements/
---
Aspose.Cells for C++ 是一个本机 C++ 库，使 C++ 开发人员能够以编程方式创建、操作和转换电子表格，而无需 Office 自动化或 Microsoft Excel 应用程序。

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
			<td><ul><li>Windows x86</li><li>Windowsx86_64</li></ul></td>
  </tr>
  <tr>
			<td>Linux</td>
			<td><ul><li>Linux x86_64</li><!---li>Ubuntu 20.04 or later</li><li>Fedora</li><li>OpenSUSE</li><li>CentOS</li---><li>适用于 ARM 的 Linux (aarch64)</li></ul></td>
		</tr>
  <tr>
			<td>苹果系统</td>
			<td><ul><li>macOS 11 或更高版本（arm64、x86_64）</li></ul></td>
		</tr>
</table>

## 开发环境

为 Windows、Linux 或 macOS 开发应用程序时，可以使用 Aspose.Cells for C++。

###  Windows

 Aspose.Cells for C++ 可用于在任何支持的开发环境中开发应用程序[Microsoft Visual Studio v142 平台工具集](https://docs.microsoft.com/en-us/cpp/porting/binary-compat-2015-2017?view=msvc-160)，但明确支持下表中列出的环境：

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">开发环境</td>
		</tr>
  <tr>
			<td><ul><li>Microsoft Visual Studio 2019</li><li>Microsoft Visual Studio 2022</li></ul></td>
			</tr>
</table>

### Linux

Aspose.Cells for C++可用于在支持C++11或更高版本的开发环境中开发应用程序，但明确支持以下编译器和工具：

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">编译器</td>
		</tr>
  <tr>
			<td><ul><li>GCC 9.4.0 或更高版本</li></ul></td>
			</tr>
</table>

### 对 Linux 的额外依赖
Linux 上的 Aspose.Cells for C++ 取决于<a href="https://www.freedesktop.org/wiki/Software/fontconfig/">字体配置</a>动态库和工具的二进制文件。使用前请先安装：

1. 在 Ubuntu 或 Debian 上安装 fontconfig<br>
`sudo apt install libfontconfig fontconfig`
1. 在 Fedora 或 CentOs 上安装 fontconfig<br>
`sudo yum install fontconfig`

### 苹果系统
Aspose.Cells for C++可用于在以下开发环境中开发应用程序：
* Xcode 12.5.1 或更高版本
* Clang 和 libc++（默认情况下随 Xcode 一起提供）
