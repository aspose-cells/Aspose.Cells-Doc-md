---
title: Systemkrav
type: docs
weight: 30
url: /sv/cpp/system-requirements/
---

Aspose.Cells for C++ är en nativ C++-bibliotek som gör det möjligt för C++-utvecklare att skapa, manipulera och konvertera kalkylblad programmatiskt utan att kräva Office Automation eller Microsoft Excel-applikation.

## Stödda operativsystem

Aspose.Cells for C++ stöder följande 64-bitars- eller 32-bitars-operativsystem och plattformar:

<table>  
	<tr>
			<td style="font-weight: bold; width:400px">Operativsystem</td>
			<td style="font-weight: bold; width:400px">Versioner</td>
		</tr>
  <tr>
			<td>Microsoft Windows</td>
			<!--- <td><ul><li>Windows 2008 Server (x64)</li><li>Windows 2012 Server (x64)</li><li>Windows 2012 R2 Server (x64)</li><li>Windows 2016 Server (x64)</li><li>Windows 2019 Server (x64)</li><li>Windows Vista (x64)</li><li>Windows 7 (x64)</li><li>Windows 8, 8.1 (x64)</li><li>Windows 10 (x64)</li><li>Windows 11 (x64)</li></ul></td> --->
			<td><ul><li>Windows x86</li><li>Windows x86_64</li></ul></td>
  </tr>
  <tr>
			<td>Linux</td>
			<td><ul><li>Linux x86_64</li><!---li>Ubuntu 20.04 eller senare</li><li>Fedora</li><li>OpenSUSE</li><li>CentOS</li---><li>Linux för ARM (aarch64)</li></ul></td>
		</tr>
  <tr>
			<td>macOS</td>
			<td><ul><li>macOS 11 eller senare (arm64, x86_64)</li></ul></td>
		</tr>
</table>

## Utvecklingsmiljö

Du kan använda Aspose.Cells for C++ vid utveckling av applikationer för Windows, Linux eller macOS.

### Windows

Aspose.Cells for C++ kan användas för att utveckla applikationer i vilken utvecklingsmiljö som stöder [Microsoft Visual Studio v142 Platform Toolset](https://docs.microsoft.com/en-us/cpp/porting/binary-compat-2015-2017?view=msvc-160), men de miljöer som listas i följande tabell stöds explicit:

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">Utvecklingsmiljöer</td>
		</tr>
  <tr>
			<td><ul><li>Microsoft Visual Studio 2019</li><li>Microsoft Visual Studio 2022</li></ul></td>
			</tr>
</table>

### Linux

Aspose.Cells for C++ kan användas för att utveckla applikationer i utvecklingsmiljön som stödjer C++11 eller högre, men följande kompilator och verktyg stöds explicit:

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">Kompilatorer</td>
		</tr>
  <tr>
			<td><ul><li>GCC 9.4.0 eller senare</li></ul></td>
			</tr>
</table>

### Ytterligare beroende på Linux
Aspose.Cells for C++ on Linux depends on <a href="https://www.freedesktop.org/wiki/Software/fontconfig/">fontconfig</a> binaries both dynamic library and tool. Please install it before using:

1. Installing fontconfig on Ubuntu or Debian<br>
`sudo apt install libfontconfig fontconfig`
1. Installing fontconfig on Fedora or CentOs<br>
`sudo yum install fontconfig`

### macOS 
Aspose.Cells for C++ kan användas för att utveckla applikationer i följande utvecklingsmiljöer:
* Xcode 12.5.1 eller senare
* Clang och libc++ (vilket levereras som standard med Xcode)
