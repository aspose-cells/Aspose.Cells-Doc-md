---
title: sistem gereksinimleri
type: docs
weight: 30
url: /tr/cpp/system-requirements/
---
Aspose.Cells for C++, C++ geliştiricilerinin Office Otomasyonu veya Microsoft Excel uygulaması gerektirmeden elektronik tabloları programlı olarak oluşturmasına, değiştirmesine ve dönüştürmesine olanak tanıyan yerel bir C++ kitaplığıdır.

##  Desteklenen İşletim Sistemleri

Aspose.Cells for C++, aşağıdaki 64 bit işletim sistemini ve platformlarını destekler:

<table>  
	<tr>
			<td style="font-weight: bold; width:400px">İşletim sistemi</td>
			<td style="font-weight: bold; width:400px">Sürümler</td>
		</tr>
  <tr>
			<td>Microsoft Windows</td>
			<td><ul><li>Windows 2008 Sunucu (x64)</li><li>Windows 2012 Sunucu (x64)</li><li>Windows 2012 R2 Sunucusu (x64)</li><li>Windows 2016 Sunucu (x64)</li><li>Windows 2019 Sunucu (x64)</li><li>Windows Vista (x64)</li><li>Windows 7 (x64)</li><li>Windows 8, 8,1 (x64)</li><li>Windows 10 (x64)</li><li>Windows 11 (x64)</li></ul></td>
		</tr>
  <tr>
			<td>Linux</td>
			<td><ul><li>Ubuntu 20.04 veya üzeri</li><li>Fedora</li><li>OpenSUSE</li><li>CentOS</li><li>ARM için Linux (aarch64)</li></ul></td>
		</tr>
  <tr>
			<td>Mac os işletim sistemi</td>
			<td><ul><li>macOS 11 veya üzeri(arm64, x86_64)</li></ul></td>
		</tr>
</table>

##  Geliştirme Ortamı

Aspose.Cells, Linux veya macOS için uygulama geliştirirken Aspose.Cells for C++’i kullanabilirsiniz.

###  Windows

 Aspose.Cells for C++, destekleyen herhangi bir geliştirme ortamında uygulamalar geliştirmek için kullanılabilir[Microsoft Visual Studio v142 Platform Araç Seti](https://docs.microsoft.com/en-us/cpp/porting/binary-compat-2015-2017?view=msvc-160)ancak aşağıdaki tabloda listelenen ortamlar açıkça desteklenmektedir:

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">Geliştirme ortamları</td>
		</tr>
  <tr>
			<td><ul><li>Microsoft Visual Studio 2019</li><li>Microsoft Visual Studio 2022</li></ul></td>
			</tr>
</table>

###  Linux

Aspose.Cells for C++, C++11 veya üstünü destekleyen geliştirme ortamında uygulama geliştirmek için kullanılabilir ancak aşağıdaki derleyici ve araç açıkça desteklenir:

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">Derleyiciler</td>
		</tr>
  <tr>
			<td><ul><li>GCC 9.4.0 veya üzeri</li></ul></td>
			</tr>
</table>

###  Linux'a Ek Bağımlılık
 Linux'ta Aspose.Cells for C++ şunlara bağlıdır:<a href="https://www.freedesktop.org/wiki/Software/fontconfig/">yazı tipi yapılandırması</a> ikili dosyalar hem dinamik kütüphane hem de araçtır. Lütfen kullanmadan önce yükleyin:

1. Ubuntu veya Debian'a fontconfig kurulumu<br>
`sudo apt install libfontconfig fontconfig`
1. Fontconfig'i Fedora veya CentO'lara yükleme<br>
`sudo yum install fontconfig`

###  Mac os işletim sistemi
Aspose.Cells for C++, aşağıdaki geliştirme ortamlarında uygulama geliştirmek için kullanılabilir:
* Xcode 12.5.1 veya üzeri
* Clang ve libc++ (varsayılan olarak Xcode ile birlikte gönderilir)
