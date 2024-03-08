---
title: System Anforderungen
type: docs
weight: 30
url: /de/cpp/system-requirements/
---
Aspose.Cells for C++ ist eine native C++-Bibliothek, die es C++-Entwicklern ermöglicht, Tabellenkalkulationen programmgesteuert zu erstellen, zu bearbeiten und zu konvertieren, ohne dass Office Automation oder eine Excel-Anwendung erforderlich ist.

##  Unterstützte Betriebssysteme

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
			<td><ul><li>Linux x86_64</li><!---li>Ubuntu 20.04 or later</li><li>Fedora</li><li>OpenSUSE</li><li>CentOS</li---><li>Linux für ARM (aarch64)</li></ul></td>
		</tr>
  <tr>
			<td>Mac OS</td>
			<td><ul><li>macOS 11 oder höher (arm64, x86_64)</li></ul></td>
		</tr>
</table>

##  Entwicklungsumgebung

Sie können Aspose.Cells for C++ verwenden, wenn Sie Anwendungen für Windows, Linux oder macOS entwickeln.

###  Windows

 Aspose.Cells for C++ kann zum Entwickeln von Anwendungen in jeder Entwicklungsumgebung verwendet werden, die dies unterstützt[Microsoft Visual Studio v142 Plattform-Toolset](https://docs.microsoft.com/en-us/cpp/porting/binary-compat-2015-2017?view=msvc-160), aber die in der folgenden Tabelle aufgeführten Umgebungen werden explizit unterstützt:

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">Entwicklungsumgebungen</td>
		</tr>
  <tr>
			<td><ul><li>Microsoft Visual Studio 2019</li><li>Microsoft Visual Studio 2022</li></ul></td>
			</tr>
</table>

###  Linux

Aspose.Cells for C++ kann zum Entwickeln von Anwendungen in der Entwicklungsumgebung verwendet werden, die C++11 oder höher unterstützen, aber der folgende Compiler und das folgende Tool werden ausdrücklich unterstützt:

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">Compiler</td>
		</tr>
  <tr>
			<td><ul><li>GCC 9.4.0 oder höher</li></ul></td>
			</tr>
</table>

###  Zusätzliche Abhängigkeit von Linux
 Aspose.Cells for C++ unter Linux hängt davon ab<a href="https://www.freedesktop.org/wiki/Software/fontconfig/">Schriftartkonfiguration</a> Binärdateien, sowohl dynamische Bibliothek als auch Tool. Bitte installieren Sie es vor der Verwendung:

1. Fontconfig unter Ubuntu oder Debian installieren<br>
`sudo apt install libfontconfig fontconfig`
1. Fontconfig auf Fedora oder CentOs installieren<br>
`sudo yum install fontconfig`

###  Mac OS
Aspose.Cells for C++ kann zur Anwendungsentwicklung in den folgenden Entwicklungsumgebungen verwendet werden:
* Xcode 12.5.1 oder höher
* Clang und libc++ (die standardmäßig mit Xcode ausgeliefert werden)
