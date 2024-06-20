---
title: Systemanforderungen
type: docs
weight: 30
url: /de/cpp/system-requirements/
---

Aspose.Cells for C++ ist eine native C++-Bibliothek, die es C++-Entwicklern ermöglicht, Tabellenkalkulationen programmatisch zu erstellen, zu manipulieren und zu konvertieren, ohne auf die Office-Automatisierung oder die Microsoft Excel-Anwendung angewiesen zu sein.

## Unterstützte Betriebssysteme

Aspose.Cells for C++ unterstützt die folgenden 64-Bit- oder 32-Bit-Betriebssysteme und Plattformen:

<table>  
	<tr>
			<td style="font-weight: bold; width:400px">Betriebssystem</td>
			<td style="font-weight: bold; width:400px">Versionen</td>
		</tr>
  <tr>
			<td>Microsoft Windows</td>
			<!--- <td><ul><li>Windows 2008 Server (x64)</li><li>Windows 2012 Server (x64)</li><li>Windows 2012 R2 Server (x64)</li><li>Windows 2016 Server (x64)</li><li>Windows 2019 Server (x64)</li><li>Windows Vista (x64)</li><li>Windows 7 (x64)</li><li>Windows 8, 8.1 (x64)</li><li>Windows 10 (x64)</li><li>Windows 11 (x64)</li></ul></td> --->
			<td><ul><li>Windows x86</li><li>Windows x86_64</li></ul></td>
  </tr>
  <tr>
			<td>Linux</td>
			<td><ul><li>Linux x86_64</li><!---li>Ubuntu 20.04 oder höher</li><li>Fedora</li><li>OpenSUSE</li><li>CentOS</li---><li>Linux für ARM (aarch64)</li></ul></td>
		</tr>
  <tr>
			<td>macOS</td>
			<td><ul><li>macOS 11 oder höher (arm64, x86_64)</li></ul></td>
		</tr>
</table>

## Entwicklungsumgebung

Sie können Aspose.Cells for C++ beim Entwickeln von Anwendungen für Windows, Linux oder macOS verwenden.

### Windows

Aspose.Cells for C++ kann in jeder Entwicklungsumgebung verwendet werden, die [Microsoft Visual Studio v142 Platform Toolset](https://docs.microsoft.com/en-us/cpp/porting/binary-compat-2015-2017?view=msvc-160) unterstützt, aber die Umgebungen, die in der folgenden Tabelle aufgeführt sind, werden explizit unterstützt:

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">Entwicklungsumgebungen</td>
		</tr>
  <tr>
			<td><ul><li>Microsoft Visual Studio 2019</li><li>Microsoft Visual Studio 2022</li></ul></td>
			</tr>
</table>

### Linux

Aspose.Cells for C++ kann in der Entwicklungsumgebung verwendet werden, die C++11 oder höher unterstützt, aber der folgende Compiler und das folgende Tool werden explizit unterstützt:

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">Compiler</td>
		</tr>
  <tr>
			<td><ul><li>GCC 9.4.0 oder höher</li></ul></td>
			</tr>
</table>

### Zusätzliche Abhängigkeit unter Linux
Aspose.Cells for C++ on Linux depends on <a href="https://www.freedesktop.org/wiki/Software/fontconfig/">fontconfig</a> binaries both dynamic library and tool. Please install it before using:

1. Installing fontconfig on Ubuntu or Debian<br>
`sudo apt install libfontconfig fontconfig`
1. Installing fontconfig on Fedora or CentOs<br>
`sudo yum install fontconfig`

### macOS 
Aspose.Cells for C++ kann in den folgenden Entwicklungsumgebungen verwendet werden:
* Xcode 12.5.1 oder höher
* Clang und libc++ (die standardmäßig mit Xcode geliefert werden)
