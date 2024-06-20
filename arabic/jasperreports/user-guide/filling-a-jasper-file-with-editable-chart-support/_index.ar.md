---
title: ملء ملف .jasper مع دعم المخطط القابل للتحرير
type: docs
weight: 10
url: /ar/jasperreports/filling-a-jasper-file-with-editable-chart-support/
---

{{% alert color="primary" %}} 

Aspose.Cells for JasperReportsيتطلب ملف .jasper ليتم ملؤه بملف .jrprint أو كائن JasperPrint قبل أن يمكن تصديره إلى ملف XLS. لا توجد أي تعديلات مطلوبة لملف .jrxml على الإطلاق. إجراء الملء يقوم بتخزين التمثيلات الداخلية للمخططات في كائن JasperPrint الذي يُستخدم بعد ذلك لإنشاء المخططات القابلة للتحرير. 

{{% /alert %}} 

يرجى قراءة وثائق JasperReports للحصول على وصف مفصل حول كيفية ملء التقرير.

إليك مثال:

**Java**

{{< highlight csharp >}}

 JasperPrint jasperPrint = JasperFillManager.fillReport(jasperFileName, parameters, getConnection());



{{< /highlight >}}
