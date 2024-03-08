---
title: Requisitos del sistema
type: docs
weight: 30
url: /es/cpp/system-requirements/
---
Aspose.Cells for C++ es una biblioteca nativa C++ que permite a los desarrolladores C++ crear, manipular y convertir hojas de cálculo mediante programación sin necesidad de automatización de Office o Microsoft aplicaciones de Excel.

##  Sistemas operativos compatibles

Aspose.Cells for C++ admite las siguientes plataformas y sistemas operativos de 64 o 32 bits:

<table>  
	<tr>
			<td style="font-weight: bold; width:400px">Sistema operativo</td>
			<td style="font-weight: bold; width:400px">Versiones</td>
		</tr>
  <tr>
			<td>Microsoft Windows</td>
			<!--- <td><ul><li>Windows 2008 Server (x64)</li><li>Windows 2012 Server (x64)</li><li>Windows 2012 R2 Server (x64)</li><li>Windows 2016 Server (x64)</li><li>Windows 2019 Server (x64)</li><li>Windows Vista (x64)</li><li>Windows 7 (x64)</li><li>Windows 8, 8.1 (x64)</li><li>Windows 10 (x64)</li><li>Windows 11 (x64)</li></ul></td> --->
			<td><ul><li>Windowsx86</li><li>Windows x86_64</li></ul></td>
  </tr>
  <tr>
			<td>linux</td>
			<td><ul><li>Linuxx86_64</li><!---li>Ubuntu 20.04 or later</li><li>Fedora</li><li>OpenSUSE</li><li>CentOS</li---><li>Linux para ARM (aarch64)</li></ul></td>
		</tr>
  <tr>
			<td>Mac OS</td>
			<td><ul><li>macOS 11 o posterior (arm64, x86_64)</li></ul></td>
		</tr>
</table>

##  Entorno de desarrollo

Puede utilizar Aspose.Cells for C++ al desarrollar aplicaciones para Windows, Linux o macOS.

###  Windows

 Aspose.Cells for C++ se puede utilizar para desarrollar aplicaciones en cualquier entorno de desarrollo que admita[Microsoft Conjunto de herramientas de la plataforma Visual Studio v142](https://docs.microsoft.com/en-us/cpp/porting/binary-compat-2015-2017?view=msvc-160), pero los entornos enumerados en la siguiente tabla se admiten explícitamente:

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">Entornos de desarrollo</td>
		</tr>
  <tr>
			<td><ul><li>Microsoft Estudio visual 2019</li><li>Microsoft Estudio visual 2022</li></ul></td>
			</tr>
</table>

###  linux

Aspose.Cells for C++ se puede utilizar para desarrollar aplicaciones en el entorno de desarrollo que admitan C++11 o superior, pero el siguiente compilador y herramienta se admiten explícitamente:

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">Compiladores</td>
		</tr>
  <tr>
			<td><ul><li>GCC 9.4.0 o posterior</li></ul></td>
			</tr>
</table>

###  Dependencia adicional de Linux
 Aspose.Cells for C++ en Linux depende de<a href="https://www.freedesktop.org/wiki/Software/fontconfig/">configuración de fuente</a> binarios tanto biblioteca dinámica como herramienta. Instálelo antes de usarlo:

1. Instalación de fontconfig en Ubuntu o Debian<br>
`sudo apt install libfontconfig fontconfig`
1. Instalación de fontconfig en Fedora o CentOs<br>
`sudo yum install fontconfig`

###  Mac OS
Aspose.Cells for C++ se puede utilizar para desarrollar aplicaciones en los siguientes entornos de desarrollo:
* Xcode 12.5.1 o posterior
* Clang y libc++ (que se envían de forma predeterminada con Xcode)
