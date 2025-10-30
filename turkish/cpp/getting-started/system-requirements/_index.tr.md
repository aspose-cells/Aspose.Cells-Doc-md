---
title: Sistem Gereksinimleri
type: docs
weight: 30
url: /tr/cpp/system-requirements/
---

Aspose.Cells for C++, Office Automation veya Microsoft Excel uygulaması gerektirmeksizin C++ geliştiricilerinin elektronik tabloları programlı olarak oluşturmalarını, işlemelerini ve dönüştürmelerini sağlayan yerli bir C++ kitaplığıdır.

## Desteklenen İşletim Sistemleri

Aspose.Cells for C++ aşağıdaki 64-bit veya 32-bit işletim sistemleri ve platformlarını destekler:

<table>  
	<tr>
			<td style="font-weight: bold; width:400px">İşletim Sistemi</td>
			<td style="font-weight: bold; width:400px">Sürümler</td>
		</tr>
  <tr>
			<td>Microsoft Windows</td>
			<!--- <td><ul><li>Windows 2008 Server (x64)</li><li>Windows 2012 Server (x64)</li><li>Windows 2012 R2 Server (x64)</li><li>Windows 2016 Server (x64)</li><li>Windows 2019 Server (x64)</li><li>Windows Vista (x64)</li><li>Windows 7 (x64)</li><li>Windows 8, 8.1 (x64)</li><li>Windows 10 (x64)</li><li>Windows 11 (x64)</li></ul></td> --->
			<td><ul><li>Windows x86</li><li>Windows x86_64</li></ul></td>
  </tr>
  <tr>
			<td>Linux</td>
			<td><ul><li>Linux x86_64</li><!---li>Ubuntu 20.04 veya sonrası</li><li>Fedora</li><li>OpenSUSE</li><li>CentOS</li---><li>ARM (aarch64) için Linux</li></ul></td>
		</tr>
  <tr>
			<td>macOS</td>
			<td><ul><li>macOS 11 veya sonrası (arm64, x86_64)</li></ul></td>
		</tr>
</table>

## Geliştirme Ortamı

Windows, Linux veya macOS için uygulama geliştirirken Aspose.Cells for C++'i kullanabilirsiniz.

### Windows

Aspose.Cells for C++, [Microsoft Visual Studio v142 Platform Aracı Seti](https://docs.microsoft.com/en-us/cpp/porting/binary-compat-2015-2017?view=msvc-160) destekleyen herhangi bir geliştirme ortamında kullanılabilir, ancak aşağıdaki tabloda listelenen ortamlar açıkça desteklenmektedir:

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">Geliştirme ortamları</td>
		</tr>
  <tr>
			<td><ul><li>Microsoft Visual Studio 2019</li><li>Microsoft Visual Studio 2022</li></ul></td>
			</tr>
</table>

### Linux

Aspose.Cells for C++, C++11 veya daha yüksek sürümü destekleyen geliştirme ortamında kullanılabilir, ancak aşağıdaki derleyici ve araçlar açıkça desteklenmektedir:

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">Derleyiciler</td>
		</tr>
  <tr>
			<td><ul><li>GCC 9.4.0 veya sonrası</li></ul></td>
			</tr>
</table>

### Linux'ta Ek Bağımlılık
Aspose.Cells for C++ on Linux depends on <a href="https://www.freedesktop.org/wiki/Software/fontconfig/">fontconfig</a> binaries both dynamic library and tool. Please install it before using:

1. Installing fontconfig on Ubuntu or Debian<br>
`sudo apt install libfontconfig fontconfig`
1. Installing fontconfig on Fedora or CentOs<br>
`sudo yum install fontconfig`

### macOS 
Aspose.Cells for C++ aşağıdaki geliştirme ortamlarında kullanılabilir:
* Xcode 12.5.1 veya sonrası
* Varsayılan olarak Xcode ile gönderilen Clang ve libc++
{{< app/cells/assistant language="cpp" >}}
