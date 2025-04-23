---
title: Системные требования
type: docs
weight: 30
url: /ru/go-cpp/system-requirements/
---

Aspose.Cells for Go via C++ — это нативная библиотека на Go, которая позволяет разработчикам Go создавать, управлять и конвертировать электронные таблицы программным способом без необходимости использования Office Automation или приложения Microsoft Excel.

## Поддерживаемые операционные системы

Aspose.Cells для Go поддерживает следующие 64-битные операционные системы и платформы:

<table>  
 <tr>
   <td style="font-weight: bold; width:400px">Операционная система</td>
   <td style="font-weight: bold; width:400px">Версии</td>
  </tr>
  <tr>
   <td>Microsoft Windows</td>
   <!--- <td><ul><li>Windows 2008 Server (x64)</li><li>Windows 2012 Server (x64)</li><li>Windows 2012 R2 Server (x64)</li><li>Windows 2016 Server (x64)</li><li>Windows 2019 Server (x64)</li><li>Windows Vista (x64)</li><li>Windows 7 (x64)</li><li>Windows 8, 8.1 (x64)</li><li>Windows 10 (x64)</li><li>Windows 11 (x64)</li></ul></td> --->
   <td><ul><li>Windows x86_64</li></ul></td>
  </tr>
  <tr>
   <td>Linux</td>
   <td><ul><li>Linux x86_64</li><!---li>Ubuntu 20.04 или новее</li><li>Fedora</li><li>OpenSUSE</li><li>CentOS</li---></ul></td>
  </tr>
</table>

## Среда разработки

Вы можете использовать Aspose.Cells for Go via C++ при разработке приложений для Windows, Linux.

### Windows

Aspose.Cells for Go via C++ можно использовать для разработки приложений в любой среде разработки, которая поддерживает [Microsoft Visual Studio v142 Platform Toolset](https://docs.microsoft.com/en-us/go/porting/binary-compat-2015-2017?view=msvc-160), но явно поддерживаются следующие среды:

### Linux

Aspose.Cells for Go via C++ можно использовать для разработки приложений в среде разработки, поддерживающих Go 1.13 или выше, но явно поддерживаются следующие компилятор и инструменты:

<table>  
 <tr>
   <td style="font-weight: bold; width:800px">Компиляторы</td>
  </tr>
  <tr>
   <td><ul><li>GCC 9.4.0 или более поздняя</li></ul></td>
   </tr>
</table>

### Дополнительные зависимости в Linux

Aspose.Cells for Go on Linux depends on <a href="https://www.freedesktop.org/wiki/Software/fontconfig/">fontconfig</a> binaries both dynamic library and tool. Please install it before using:

1. Installing fontconfig on Ubuntu or Debian<br>
`sudo apt install libfontconfig fontconfig`
1. Installing fontconfig on Fedora or CentOs<br>
`sudo yum install fontconfig`
