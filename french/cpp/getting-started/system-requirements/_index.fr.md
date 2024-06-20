---
title: Configuration requise
type: docs
weight: 30
url: /fr/cpp/system-requirements/
---

Aspose.Cells for C++ est une bibliothèque native C++ qui permet aux développeurs C++ de créer, manipuler et convertir des feuilles de calcul de manière programmable sans nécessiter d'automatisation Office ou d'application Microsoft Excel.

## Systèmes d'exploitation pris en charge

Aspose.Cells for C++ prend en charge les systèmes d'exploitation et plateformes 64 bits ou 32 bits suivants :

<table>  
	<tr>
			<td style="font-weight: bold; width:400px">Système d'exploitation</td>
			<td style="font-weight: bold; width:400px">Versions</td>
		</tr>
  <tr>
			<td>Microsoft Windows</td>
			<!--- <td><ul><li>Windows 2008 Server (x64)</li><li>Windows 2012 Server (x64)</li><li>Windows 2012 R2 Server (x64)</li><li>Windows 2016 Server (x64)</li><li>Windows 2019 Server (x64)</li><li>Windows Vista (x64)</li><li>Windows 7 (x64)</li><li>Windows 8, 8.1 (x64)</li><li>Windows 10 (x64)</li><li>Windows 11 (x64)</li></ul></td> --->
			<td><ul><li>Windows x86</li><li>Windows x86_64</li></ul></td>
  </tr>
  <tr>
			<td>Linux</td>
			<td><ul><li>Linux x86_64</li><!---li>Ubuntu 20.04 ou version ultérieure</li><li>Fedora</li><li>OpenSUSE</li><li>CentOS</li---><li>Linux pour ARM (aarch64)</li></ul></td>
		</tr>
  <tr>
			<td>macOS</td>
			<td><ul><li>macOS 11 ou version ultérieure (arm64, x86_64)</li></ul></td>
		</tr>
</table>

## Environnement de développement

Vous pouvez utiliser le Aspose.Cells for C++ lors du développement d'applications pour Windows, Linux ou macOS.

### Windows

Le Aspose.Cells for C++ peut être utilisé pour développer des applications dans tout environnement de développement qui prend en charge le [Microsoft Visual Studio v142 Platform Toolset] (https://docs.microsoft.com/en-us/cpp/porting/binary-compat-2015-2017?view=msvc-160), mais les environnements répertoriés dans le tableau suivant sont explicitement pris en charge :

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">Environnements de développement</td>
		</tr>
  <tr>
			<td><ul><li>Microsoft Visual Studio 2019</li><li>Microsoft Visual Studio 2022</li></ul></td>
			</tr>
</table>

### Linux

Le Aspose.Cells for C++ peut être utilisé pour développer des applications dans un environnement de développement qui prend en charge C++11 ou une version supérieure, mais le compilateur et l'outil suivants sont explicitement pris en charge :

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">Compilateurs</td>
		</tr>
  <tr>
			<td><ul><li>GCC 9.4.0 ou ultérieur</li></ul></td>
			</tr>
</table>

### Dépendance supplémentaire sur Linux
Aspose.Cells for C++ on Linux depends on <a href="https://www.freedesktop.org/wiki/Software/fontconfig/">fontconfig</a> binaries both dynamic library and tool. Please install it before using:

1. Installing fontconfig on Ubuntu or Debian<br>
`sudo apt install libfontconfig fontconfig`
1. Installing fontconfig on Fedora or CentOs<br>
`sudo yum install fontconfig`

### macOS 
Le Aspose.Cells for C++ peut être utilisé pour développer des applications dans les environnements de développement suivants :
* Xcode 12.5.1 ou ultérieur
* Clang et libc++ (qui sont livrés par défaut avec Xcode)
