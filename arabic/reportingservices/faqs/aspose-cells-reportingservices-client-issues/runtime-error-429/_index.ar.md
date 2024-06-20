---
title: خطأ تشغيل 429
type: docs
weight: 60
url: /ar/reportingservices/runtime-error-429/
---

##### **الوصف**
خطأ في التشغيل: '429' 
لا يمكن إنشاء كائن مكون ActiveX 
السطر الذي يسبب الخطأ هو: 
Set AsposeClientTools = CreateObject("Aspose.Cells.ReportingServices.Client.AsposeClient"). 
##### **الحل**
{{% alert color="primary" %}} 

إعادة تسجيل **Aspose.Cells.ReportingServices.Client.dll** باستخدام أداة **Regasm.exe**:  

1. قم بتشغيل cmd.exe كمسؤول.
1. cd $(Aspose.Cells for Reporting Services installation folder).
1. قم بتنفيذ **regasm.exe** لتسجيل **Aspose.Cells.ReportingServices.Client.dll** يدوياً. 

{{< highlight java >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm  Aspose.Cells.ReportingServices.Client.dll  /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase

{{< /highlight >}}

يرجى التحقق من بيئة التشغيل لنظامك. على سبيل المثال: 

- إذا كان Microsoft Office الخاص بك x64، قم بتشغيل الأمر 

{{< highlight java >}}

 @: ...%WINDIR%\Microsoft.NET\Framework64\v2.0.50727\regasm.exe

{{< /highlight >}}

- إذا كان Microsoft Office الخاص بك x86، قم بتشغيل الأمر 

{{< highlight java >}}

 @: ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm.exe

{{< /highlight >}}

يرجى الرجوع إلى المثال / الأمر التالي:

{{< highlight java >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm "C:\Program Files (x86)\Aspose\Aspose.Cells for Reporting Services\Bin\Aspose.Cells.ReportingServices.Client.dll" /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase 

{{< /highlight >}}

{{% /alert %}}
