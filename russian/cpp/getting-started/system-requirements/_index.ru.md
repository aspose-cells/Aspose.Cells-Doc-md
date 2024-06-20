---
title: Системные требования
type: docs
weight: 30
url: /ru/cpp/system-requirements/
---

Aspose.Cells for C++ – это нативная библиотека C++, позволяющая разработчикам на C++ создавать, изменять и программно преобразовывать электронные таблицы без необходимости использования автоматизации Office или приложения Microsoft Excel.

## Поддерживаемые операционные системы

Aspose.Cells for C++ поддерживает следующие 64-битные или 32-битные операционные системы и платформы:

<table>  
	<tr>
			<td style="font-weight: bold; width:400px">Операционная система</td>
			<td style="font-weight: bold; width:400px">Версии</td>
		</tr>
  <tr>
			<td>Microsoft Windows</td>
			<!--- <td><ul><li>Windows 2008 Server (x64)</li><li>Windows 2012 Server (x64)</li><li>Windows 2012 R2 Server (x64)</li><li>Windows 2016 Server (x64)</li><li>Windows 2019 Server (x64)</li><li>Windows Vista (x64)</li><li>Windows 7 (x64)</li><li>Windows 8, 8.1 (x64)</li><li>Windows 10 (x64)</li><li>Windows 11 (x64)</li></ul></td> --->
			<td><ul><li>Windows x86</li><li>Windows x86_64</li></ul></td>
  </tr>
  <tr>
			<td>Linux</td>
			<td><ul><li>Linux x86_64</li><!---li>Ubuntu 20.04 или более поздняя</li><li>Fedora</li><li>OpenSUSE</li><li>CentOS</li---><li>Linux для ARM (aarch64)</li></ul></td>
		</tr>
  <tr>
			<td>macOS</td>
			<td><ul><li>macOS 11 или более поздняя (arm64, x86_64)</li></ul></td>
		</tr>
</table>

## Среда разработки

Вы можете использовать Aspose.Cells for C++ при разработке приложений для Windows, Linux или macOS.

### Windows

Aspose.Cells for C++ может использоваться для разработки приложений в любой среде разработки, которая поддерживает [пакет средств компиляции v142 Microsoft Visual Studio](https://docs.microsoft.com/en-us/cpp/porting/binary-compat-2015-2017?view=msvc-160), но явно поддерживаются среды, перечисленные в следующей таблице:

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">Среды разработки</td>
		</tr>
  <tr>
			<td><ul><li>Microsoft Visual Studio 2019</li><li>Microsoft Visual Studio 2022</li></ul></td>
			</tr>
</table>

### Linux

Aspose.Cells for C++ можно использовать для разработки приложений в среде разработки, которая поддерживает C++11 или выше, но явно поддерживаются следующие компилятор и инструменты:

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">Компиляторы</td>
		</tr>
  <tr>
			<td><ul><li>GCC 9.4.0 или более поздняя</li></ul></td>
			</tr>
</table>

### Дополнительные зависимости в Linux
Aspose.Cells for C++ on Linux depends on <a href="https://www.freedesktop.org/wiki/Software/fontconfig/">fontconfig</a> binaries both dynamic library and tool. Please install it before using:

1. Installing fontconfig on Ubuntu or Debian<br>
`sudo apt install libfontconfig fontconfig`
1. Installing fontconfig on Fedora or CentOs<br>
`sudo yum install fontconfig`

### macOS 
Aspose.Cells for C++ можно использовать для разработки приложений в следующих средах разработки:
* Xcode 12.5.1 или более поздняя версия
* Clang и libc++ (которые поставляются по умолчанию с Xcode)
