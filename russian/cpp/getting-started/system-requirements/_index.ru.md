---
title: Системные Требования
type: docs
weight: 30
url: /ru/cpp/system-requirements/
---
Aspose.Cells for C++ — это встроенная библиотека C++, которая позволяет разработчикам C++ создавать, манипулировать и преобразовывать электронные таблицы программным способом без необходимости использования Office Automation или приложения Excel Microsoft.

##  Поддерживаемые операционные системы

Aspose.Cells for C++ поддерживает следующие 64-битные или 32-битные операционные системы и платформы:

<table>  
	<tr>
			<td style="font-weight: bold; width:400px">Операционная система</td>
			<td style="font-weight: bold; width:400px">Версии</td>
		</tr>
  <tr>
			<td>Microsoft Windows</td>
			<!--- <td><ul><li>Windows 2008 Server (x64)</li><li>Windows 2012 Server (x64)</li><li>Windows 2012 R2 Server (x64)</li><li>Windows 2016 Server (x64)</li><li>Windows 2019 Server (x64)</li><li>Windows Vista (x64)</li><li>Windows 7 (x64)</li><li>Windows 8, 8.1 (x64)</li><li>Windows 10 (x64)</li><li>Windows 11 (x64)</li></ul></td> --->
			<td><ul><li>Windows х86</li><li>Windows x86_64</li></ul></td>
  </tr>
  <tr>
			<td>Линукс</td>
			<td><ul><li>Linux x86_64</li><!---li>Ubuntu 20.04 or later</li><li>Fedora</li><li>OpenSUSE</li><li>CentOS</li---><li>Linux для ARM (aarch64)</li></ul></td>
		</tr>
  <tr>
			<td>macOS</td>
			<td><ul><li>macOS 11 или новее (arm64, x86_64)</li></ul></td>
		</tr>
</table>

##  Среда разработки

Вы можете использовать Aspose.Cells for C++ при разработке приложений для Windows, Linux или macOS.

###  Windows

 Aspose.Cells for C++ может использоваться для разработки приложений в любой среде разработки, поддерживающей[Microsoft Набор инструментов платформы Visual Studio v142](https://docs.microsoft.com/en-us/cpp/porting/binary-compat-2015-2017?view=msvc-160), но явно поддерживаются среды, перечисленные в следующей таблице:

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">Среды разработки</td>
		</tr>
  <tr>
			<td><ul><li>Microsoft Visual Studio 2019</li><li>Microsoft Visual Studio 2022</li></ul></td>
			</tr>
</table>

###  Линукс

Aspose.Cells for C++ можно использовать для разработки приложений в среде разработки, поддерживающей C++11 или выше, но явно поддерживаются следующие компилятор и инструмент:

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">Составители</td>
		</tr>
  <tr>
			<td><ul><li>GCC 9.4.0 или новее</li></ul></td>
			</tr>
</table>

###  Дополнительная зависимость от Linux
 Aspose.Cells for C++ в Linux зависит от<a href="https://www.freedesktop.org/wiki/Software/fontconfig/">конфигурация шрифта</a> двоичные файлы, как динамическая библиотека, так и инструмент. Пожалуйста, установите его перед использованием:

1. Установка fontconfig в Ubuntu или Debian<br>
`sudo apt install libfontconfig fontconfig`
1. Установка fontconfig в Fedora или CentOs<br>
`sudo yum install fontconfig`

### macOS
Aspose.Cells for C++ можно использовать для разработки приложений в следующих средах разработки:
* Xcode 12.5.1 или новее
* Clang и libc++ (которые по умолчанию поставляются с Xcode)
