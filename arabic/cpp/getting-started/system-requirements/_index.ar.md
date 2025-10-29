---
title: متطلبات النظام
type: docs
weight: 30
url: /ar/cpp/system-requirements/
---

Aspose.Cells for C++ هي مكتبة C++ أصلية تمكّن مطوري C++ من إنشاء وتلاعب وتحويل جداول البيانات برمجياً بدون الحاجة إلى التشغيل الآلي للمكتب أو تطبيق Microsoft Excel.

## أنظمة التشغيل المدعومة

تدعم Aspose.Cells for C++ الأنظمة الأساسية التي تعمل بنظام 64 بت أو 32 بت التالية:

<table>  
	<tr>
			<td style="font-weight: bold; width:400px">نظام التشغيل</td>
			<td style="font-weight: bold; width:400px">الإصدارات</td>
		</tr>
  <tr>
			<td>Microsoft Windows</td>
			<!--- <td><ul><li>Windows 2008 Server (x64)</li><li>Windows 2012 Server (x64)</li><li>Windows 2012 R2 Server (x64)</li><li>Windows 2016 Server (x64)</li><li>Windows 2019 Server (x64)</li><li>Windows Vista (x64)</li><li>Windows 7 (x64)</li><li>Windows 8, 8.1 (x64)</li><li>Windows 10 (x64)</li><li>Windows 11 (x64)</li></ul></td> --->
			<td><ul><li>Windows x86</li><li>Windows x86_64</li></ul></td>
  </tr>
  <tr>
			<td>Linux</td>
			<td><ul><li>لينكس x86_64</li><!---li>أوبونتو 20.04 أو أحدث</li><li>فيدورا</li><li>أوبن سوزي</li><li>سنت أو إس</li---><li>لينكس لأنظمة ARM (aarch64)</li></ul></td>
		</tr>
  <tr>
			<td>macOS</td>
			<td><ul><li>ماك أو إس 11 أو أحدث (arm64، x86_64)</li></ul></td>
		</tr>
</table>

## بيئة التطوير

يمكنك استخدام Aspose.Cells for C++ عند تطوير تطبيقات لنظام التشغيل Windows أو Linux أو macOS.

### Windows

يمكن استخدام Aspose.Cells for C++ لتطوير التطبيقات في أي بيئة تطوير تدعم [مجموعة أدوات منصة Microsoft Visual Studio v142](https://docs.microsoft.com/en-us/cpp/porting/binary-compat-2015-2017?view=msvc-160)، ولكن البيئات المُدرجة في الجدول التالي تدعم صراحة:

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">بيئات التطوير</td>
		</tr>
  <tr>
			<td><ul><li>Microsoft Visual Studio 2019</li><li>Microsoft Visual Studio 2022</li></ul></td>
			</tr>
</table>

### Linux

يمكن استخدام Aspose.Cells for C++ لتطوير التطبيق في بيئة التطوير التي تدعم C++11 أو أحدث، لكن المترجم والأدوات التالية تتم دعمها بصراحة:

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">المترجمون</td>
		</tr>
  <tr>
			<td><ul><li>GCC 9.4.0 أو أحدث</li></ul></td>
			</tr>
</table>

### التبعيات الإضافية على Linux
Aspose.Cells for C++ on Linux depends on <a href="https://www.freedesktop.org/wiki/Software/fontconfig/">fontconfig</a> binaries both dynamic library and tool. Please install it before using:

1. Installing fontconfig on Ubuntu or Debian<br>
`sudo apt install libfontconfig fontconfig`
1. Installing fontconfig on Fedora or CentOs<br>
`sudo yum install fontconfig`

### macOS 
يمكن استخدام Aspose.Cells for C++ لتطوير التطبيق في البيئات التطويرية التالية:
* Xcode 12.5.1 أو أحدث
* Clang وlibc++ (التي يتم شحنها افتراضيًا مع Xcode)
{{< app/cells/assistant language="cpp" >}}
