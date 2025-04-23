---
title: تحويل ملف XLS الذي يحتوي على صور أو رسومات إلى PDF
type: docs
weight: 50
url: /ar/net/convert-xls-file-with-images-or-charts-to-pdf/
---

{{% alert color="primary" %}} 

تدعم Aspose.Cells تحويل ملفات XLS التي تحتوي على صور ورسوم بيانية إلى مستندات PDF. يمكن لـ Aspose.Cells for .NET العمل بشكل مستقل لتحويل جدول بيانات إلى PDF: لا يُطلب Aspose.PDF for .NET لعملية التحويل. يمكن القيام بالعملية في الذاكرة لأن العملية لا تعتمد على ملفات XML مؤقتة أو وسيطة. يعني ذلك أنه يمكن تحويل ملفات Excel كبيرة، على سبيل المثال، تلك التي تحتوي على صور ورسوم بيانية وأجسام رسم أخرى، بسرعة وكفاءة.

{{% /alert %}} 
## **الكود المثالي**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertXLSFileToPDF-1.cs" >}}

{{% alert color="primary" %}} 

إذا كان الجدول الزمني يحتوي على صيغ، فمن الأفضل استدعاء طريقة [Workbook.CalculateFormula](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) مباشرة قبل التقديم إلى PDF. يضمن ذلك إعادة حساب القيم المعتمدة على الصيغ، وتقديم القيم الصحيحة في PDF.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
