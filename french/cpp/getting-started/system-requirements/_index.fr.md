---
title: Configuration requise
type: docs
weight: 30
url: /fr/cpp/system-requirements/
---
Aspose.Cells for C++ est une bibliothèque native C++ qui permet aux développeurs C++ de créer, manipuler et convertir des feuilles de calcul par programme sans nécessiter d'application Office Automation ou Microsoft Excel.

##  Systèmes d'exploitation pris en charge

Aspose.Cells for C++ prend en charge les systèmes d'exploitation et plates-formes 64 bits ou 32 bits suivants :

<table>  
	<tr>
			<td style="font-weight: bold; width:400px">Système opérateur</td>
			<td style="font-weight: bold; width:400px">Versions</td>
		</tr>
  <tr>
			<td>Microsoft Windows</td>
			<!--- <td><ul><li>Windows 2008 Server (x64)</li><li>Windows 2012 Server (x64)</li><li>Windows 2012 R2 Server (x64)</li><li>Windows 2016 Server (x64)</li><li>Windows 2019 Server (x64)</li><li>Windows Vista (x64)</li><li>Windows 7 (x64)</li><li>Windows 8, 8.1 (x64)</li><li>Windows 10 (x64)</li><li>Windows 11 (x64)</li></ul></td> --->
			<td><ul><li>Windowsx86</li><li>Windowsx86_64</li></ul></td>
  </tr>
  <tr>
			<td>Linux</td>
			<td><ul><li>Linuxx86_64</li><!---li>Ubuntu 20.04 or later</li><li>Fedora</li><li>OpenSUSE</li><li>CentOS</li---><li>Linux pour ARM (aarch64)</li></ul></td>
		</tr>
  <tr>
			<td>macOS</td>
			<td><ul><li>macOS 11 ou version ultérieure (arm64, x86_64)</li></ul></td>
		</tr>
</table>

##  Environnement de développement

Vous pouvez utiliser Aspose.Cells for C++ lors du développement d'applications pour Windows, Linux ou macOS.

###  Windows

 Aspose.Cells for C++ peut être utilisé pour développer des applications dans n'importe quel environnement de développement prenant en charge[Microsoft Ensemble d'outils de plate-forme Visual Studio v142](https://docs.microsoft.com/en-us/cpp/porting/binary-compat-2015-2017?view=msvc-160), mais les environnements répertoriés dans le tableau suivant sont explicitement pris en charge :

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">Environnements de développement</td>
		</tr>
  <tr>
			<td><ul><li>Microsoft Visual Studio 2019</li><li>Microsoft Visual Studio 2022</li></ul></td>
			</tr>
</table>

###  Linux

Aspose.Cells for C++ peut être utilisé pour développer une application dans un environnement de développement prenant en charge C++11 ou supérieur, mais le compilateur et l'outil suivants sont explicitement pris en charge :

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">Compilateurs</td>
		</tr>
  <tr>
			<td><ul><li>GCC 9.4.0 ou version ultérieure</li></ul></td>
			</tr>
</table>

###  Dépendance supplémentaire sur Linux
 Aspose.Cells for C++ sous Linux dépend de<a href="https://www.freedesktop.org/wiki/Software/fontconfig/">configuration de police</a> binaires à la fois bibliothèque dynamique et outil. Veuillez l'installer avant d'utiliser :

1. Installer fontconfig sur Ubuntu ou Debian<br>
`sudo apt install libfontconfig fontconfig`
1. Installation de fontconfig sur Fedora ou CentOs<br>
`sudo yum install fontconfig`

###  macOS
Aspose.Cells for C++ peut être utilisé pour développer des applications dans les environnements de développement suivants :
* Xcode 12.5.1 ou version ultérieure
* Clang et libc++ (qui sont livrés par défaut avec Xcode)
