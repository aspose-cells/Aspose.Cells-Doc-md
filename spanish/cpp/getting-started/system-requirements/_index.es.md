---
title: Requisitos del Sistema
type: docs
weight: 30
url: /es/cpp/system-requirements/
---

Aspose.Cells for C++ es una biblioteca nativa de C++ que permite a los desarrolladores de C++ crear, manipular y convertir hojas de cálculo programáticamente sin necesidad de Automatización de Office o la aplicación Microsoft Excel.

## Sistemas Operativos Compatibles

Aspose.Cells for C++ es compatible con los siguientes sistemas operativos y plataformas de 64 bits o 32 bits:

<table>  
	<tr>
			<td style="font-weight: bold; width:400px">Sistema operativo</td>
			<td style="font-weight: bold; width:400px">Versiones</td>
		</tr>
  <tr>
			<td>Microsoft Windows</td>
			<!--- <td><ul><li>Windows 2008 Server (x64)</li><li>Windows 2012 Server (x64)</li><li>Windows 2012 R2 Server (x64)</li><li>Windows 2016 Server (x64)</li><li>Windows 2019 Server (x64)</li><li>Windows Vista (x64)</li><li>Windows 7 (x64)</li><li>Windows 8, 8.1 (x64)</li><li>Windows 10 (x64)</li><li>Windows 11 (x64)</li></ul></td> --->
			<td><ul><li>Windows x86</li><li>Windows x86_64</li></ul></td>
  </tr>
  <tr>
			<td>Linux</td>
			<td><ul><li>Linux x86_64</li><!---li>Ubuntu 20.04 o posterior</li><li>Fedora</li><li>OpenSUSE</li><li>CentOS</li---><li>Linux para ARM (aarch64)</li></ul></td>
		</tr>
  <tr>
			<td>macOS</td>
			<td><ul><li>macOS 11 o posterior (arm64, x86_64)</li></ul></td>
		</tr>
</table>

Entorno de desarrollo

Puede usar Aspose.Cells for C++ al desarrollar aplicaciones para Windows, Linux o macOS.

### Windows

Aspose.Cells for C++ se puede utilizar para desarrollar aplicaciones en cualquier entorno de desarrollo que admita [Microsoft Visual Studio v142 Platform Toolset](https://docs.microsoft.com/en-us/cpp/porting/binary-compat-2015-2017?view=msvc-160), pero los entornos listados en la tabla siguiente son compatibles explícitamente:

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">Entornos de desarrollo</td>
		</tr>
  <tr>
			<td><ul><li>Microsoft Visual Studio 2019</li><li>Microsoft Visual Studio 2022</li></ul></td>
			</tr>
</table>

### Linux

Aspose.Cells for C++ se puede utilizar para desarrollar aplicaciones en el entorno de desarrollo que admita C++11 o superior, pero el siguiente compilador y herramienta son compatibles explícitamente:

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">Compiladores</td>
		</tr>
  <tr>
			<td><ul><li>GCC 9.4.0 o posterior</li></ul></td>
			</tr>
</table>

Dependencia adicional en Linux
Aspose.Cells for C++ on Linux depends on <a href="https://www.freedesktop.org/wiki/Software/fontconfig/">fontconfig</a> binaries both dynamic library and tool. Please install it before using:

1. Installing fontconfig on Ubuntu or Debian<br>
`sudo apt install libfontconfig fontconfig`
1. Installing fontconfig on Fedora or CentOs<br>
`sudo yum install fontconfig`

### macOS 
Aspose.Cells for C++ se puede utilizar para desarrollar aplicaciones en los siguientes entornos de desarrollo:
* Xcode 12.5.1 o posterior
* Clang y libc++ (que se incluyen por defecto con Xcode)
{{< app/cells/assistant language="cpp" >}}
