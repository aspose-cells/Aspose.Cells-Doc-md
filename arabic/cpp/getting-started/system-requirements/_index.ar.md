---
title: متطلبات النظام
type: docs
weight: 30
url: /ar/cpp/system-requirements/
---
Aspose.Cells for C++ هي مكتبة C++ أصلية تمكن مطوري C++ من إنشاء جداول البيانات ومعالجتها وتحويلها برمجيًا دون الحاجة إلى أتمتة Office أو تطبيق Excel Microsoft.

##  أنظمة التشغيل المدعومة

Aspose.Cells for C++ يدعم نظام التشغيل والمنصات التالية 64 بت:

<table>  
	<tr>
			<td style="font-weight: bold; width:400px">نظام التشغيل</td>
			<td style="font-weight: bold; width:400px">الإصدارات</td>
		</tr>
  <tr>
			<td>Microsoft Windows</td>
			<td><ul><li>Windows خادم 2008 (x64)</li><li>Windows خادم 2012 (x64)</li><li>Windows 2012 خادم R2 (x64)</li><li>Windows خادم 2016 (x64)</li><li>Windows خادم 2019 (x64)</li><li>Windows فيستا (x64)</li><li>Windows 7 (x64)</li><li>Windows 8، 8.1 (x64)</li><li>Windows 10 (x64)</li><li>Windows 11 (x64)</li></ul></td>
		</tr>
  <tr>
			<td>لينكس</td>
			<td><ul><li>أوبونتو 20.04 أو الأحدث</li><li>فيدورا</li><li>أوبن سوزي</li><li>سينت أو إس</li><li>لينكس لـ ARM (aarch64)</li></ul></td>
		</tr>
  <tr>
			<td>ماك</td>
			<td><ul><li>نظام التشغيل MacOS 11 أو الأحدث (arm64، x86_64)</li></ul></td>
		</tr>
</table>

##  بيئة التطوير

يمكنك استخدام Aspose.Cells for C++ عند تطوير التطبيقات لـ Windows أو Linux أو macOS.

###  Windows

 Aspose.Cells for C++ يمكن استخدامها لتطوير التطبيقات في أي بيئة تطوير تدعم[Microsoft مجموعة أدوات النظام الأساسي Visual Studio v142](https://docs.microsoft.com/en-us/cpp/porting/binary-compat-2015-2017?view=msvc-160)، ولكن البيئات المدرجة في الجدول التالي مدعومة بشكل صريح:

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">بيئات التطوير</td>
		</tr>
  <tr>
			<td><ul><li>Microsoft فيجوال ستوديو 2019</li><li>Microsoft فيجوال ستوديو 2022</li></ul></td>
			</tr>
</table>

###  لينكس

يمكن استخدام Aspose.Cells for C++ لتطوير التطبيقات في بيئة التطوير التي تدعم C++11 أو أعلى، ولكن يتم دعم المترجم والأداة التاليين بشكل صريح:

<table>  
	<tr>
			<td style="font-weight: bold; width:800px">المجمعين</td>
		</tr>
  <tr>
			<td><ul><li>دول مجلس التعاون الخليجي 9.4.0 أو في وقت لاحق</li></ul></td>
			</tr>
</table>

###  اعتماد إضافي على لينكس
 Aspose.Cells for C++ على نظام Linux يعتمد على<a href="https://www.freedesktop.org/wiki/Software/fontconfig/">com.fontconfig</a> الثنائيات على حد سواء مكتبة ديناميكية والأداة. يرجى تثبيته قبل الاستخدام:

1. تثبيت Fontconfig على Ubuntu أو Debian<br>
`sudo apt install libfontconfig fontconfig`
1. تثبيت Fontconfig على Fedora أو CentOs<br>
`sudo yum install fontconfig`

###  ماك
يمكن استخدام Aspose.Cells for C++ لتطوير التطبيق في بيئات التطوير التالية:
* Xcode 12.5.1 أو الأحدث
* Clang وlibc++ (اللذان يتم شحنهما افتراضيًا مع Xcode)
