---
title: Sistem Gereksinimleri
type: docs
weight: 30
url: /tr/go-cpp/system-requirements/
---

Aspose.Cells for Go via C++, Office Otomasyonu veya Microsoft Excel uygulamasına ihtiyaç duymadan programatik olarak elektronik tablo oluşturma, değiştirme ve dönüştürme yapan yerli Go kütüphanesidir.

## Desteklenen İşletim Sistemleri

Aspose.Cells for Go, aşağıdaki 64-bit işletim sistemi ve platformları destekler:

<table>  
 <tr>
   <td style="font-weight: bold; width:400px">İşletim Sistemi</td>
   <td style="font-weight: bold; width:400px">Sürümler</td>
  </tr>
  <tr>
   <td>Microsoft Windows</td>
   <!--- <td><ul><li>Windows 2008 Server (x64)</li><li>Windows 2012 Server (x64)</li><li>Windows 2012 R2 Server (x64)</li><li>Windows 2016 Server (x64)</li><li>Windows 2019 Server (x64)</li><li>Windows Vista (x64)</li><li>Windows 7 (x64)</li><li>Windows 8, 8.1 (x64)</li><li>Windows 10 (x64)</li><li>Windows 11 (x64)</li></ul></td> --->
   <td><ul><li>Windows x86_64</li></ul></td>
  </tr>
  <tr>
   <td>Linux</td>
   <td><ul><li>Linux x86_64</li><!---li>Ubuntu 20.04 veya sonrası</li><li>Fedora</li><li>OpenSUSE</li><li>CentOS</li---></ul></td>
  </tr>
</table>

## Geliştirme Ortamı

Windows ve Linux için uygulamalar geliştirmede Aspose.Cells for Go via C++ kullanabilirsiniz.

### Windows

Aspose.Cells for Go via C++, [Microsoft Visual Studio v142 Platform Toolset](https://docs.microsoft.com/en-us/go/porting/binary-compat-2015-2017?view=msvc-160) desteği sunan herhangi bir geliştirme ortamında uygulama geliştirmek için kullanılabilir, ancak aşağıdaki tabloda listelenen ortamlar açıkça desteklenmektedir:

### Linux

Aspose.Cells for Go via C++, Go 1.13 veya üstü destekleyen geliştirme ortamında uygulama geliştirmek için kullanılabilir, ancak aşağıdaki derleyici ve araçlar açıkça desteklenmektedir:

<table>  
 <tr>
   <td style="font-weight: bold; width:800px">Derleyiciler</td>
  </tr>
  <tr>
   <td><ul><li>GCC 9.4.0 veya sonrası</li></ul></td>
   </tr>
</table>

### Linux'ta Ek Bağımlılık

Aspose.Cells for Go on Linux depends on <a href="https://www.freedesktop.org/wiki/Software/fontconfig/">fontconfig</a> binaries both dynamic library and tool. Please install it before using:

1. Installing fontconfig on Ubuntu or Debian<br>
`sudo apt install libfontconfig fontconfig`
1. Installing fontconfig on Fedora or CentOs<br>
`sudo yum install fontconfig`
