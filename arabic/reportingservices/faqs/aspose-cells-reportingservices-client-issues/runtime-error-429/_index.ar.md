---
title: خطأ وقت التشغيل 429
type: docs
weight: 60
url: /ar/reportingservices/runtime-error-429/
---
##### **وصف**
 خطأ وقت التشغيل: "429"
 لا يمكن لمكون ActiveX إنشاء كائن
 السطر المسبب للخطأ هو:
 قم بتعيين AsposeClientTools = CreateObject ("Aspose.Cells.ReportingServices.Client.AsposeClient").
##### **المحلول**
{{% alert color="primary" %}} 

 إعادة التسجيل**Aspose.Cells.ReportingServices.Client.dll** باستخدام**Regasm.exe** خدمة:

1. قم بتشغيل cmd.exe كمسؤول.
1. cd $ (مجلد تثبيت Aspose.Cells for Reporting Services).
1.  نفذ - اعدم**regasm.exe** للتسجيل**Aspose.Cells.ReportingServices.Client.dll** يدويا.

{{< highlight "java" >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm  Aspose.Cells.ReportingServices.Client.dll  /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase

{{< /highlight >}}

 يرجى التحقق من بيئة التشغيل لنظامك. فمثلا:

-  إذا كان Microsoft Office الخاص بك هو x64 ، فقم بتشغيل الأمر

{{< highlight "java" >}}

 @: ...%WINDIR%\Microsoft.NET\Framework64\v2.0.50727\regasm.exe

{{< /highlight >}}

-  إذا كان Microsoft Office الخاص بك هو x86 ، فقم بتشغيل الأمر

{{< highlight "java" >}}

 @: ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm.exe

{{< /highlight >}}

يرجى الرجوع إلى المثال / الأمر التالي:

{{< highlight "java" >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm "C:\Program Files (x86)\Aspose\Aspose.Cells for Reporting Services\Bin\Aspose.Cells.ReportingServices.Client.dll" /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase 

{{< /highlight >}}

{{% /alert %}}
