---
title: تعبئة ملف .jasper مع دعم الرسم البياني القابل للتحرير
type: docs
weight: 10
url: /ar/jasperreports/filling-a-jasper-file-with-editable-chart-support/
---
{{% alert color="primary" %}} 

 يتطلب Aspose.Cells لـ JasperReports تعبئة ملف .jasper إلى كائن .jrprint أو كائن JasperPrint قبل أن يمكن تصديره إلى ملف XLS. ليس هناك أي تعديل مطلوب لملف .jrxml على الإطلاق. يخزن إجراء الملء التمثيلات الداخلية للمخططات في كائن JasperPrint والذي يتم استخدامه بعد ذلك لإنشاء مخططات قابلة للتحرير.

{{% /alert %}} 

يرجى قراءة وثائق JasperReports للحصول على وصف تفصيلي لكيفية ملء التقرير.

هذا مثال:

**Java**

{{< highlight "csharp" >}}

 JasperPrint jasperPrint = JasperFillManager.fillReport(jasperFileName, parameters, getConnection());



{{< /highlight >}}
