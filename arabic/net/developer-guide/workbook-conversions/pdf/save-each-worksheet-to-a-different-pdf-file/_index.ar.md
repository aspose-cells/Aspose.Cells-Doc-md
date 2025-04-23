---
title: حفظ كل ورقة عمل في ملف PDF مختلف
type: docs
weight: 130
url: /ar/net/save-each-worksheet-to-a-different-pdf-file/
---

{{% alert color="primary" %}} 

تدعم Aspose.Cells تحويل ملفات XLS (التي تحتوي على صور، ورسوم بيانية، إلخ) إلى مستندات PDF. يمكن أن يعمل Aspose.Cells for .NET بشكل مستقل لتحويل جدول بيانات إلى ملف PDF ولا تحتاج إلى استخدام Aspose.PDF for .NET للتحويل. لا يتطلب التحويل إنشاء ملفات مؤقتة أو استخدامها حيث يمكن القيام بالعملية بأكملها في الذاكرة.

{{% /alert %}} 
## **حفظ كل ورقة عمل في ملف PDF مختلف**
إذا كنت بحاجة إلى حفظ كل ورقة عمل في ملف الإكسيل النموذجي لتوليد ملفات PDF مختلفة، يمكنك تحقيق هذا بسهولة. يمكنك تجربة ضبط رقم الورقة الواحدة إلى الخيار [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) في كل مرة لتقديم إلى PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SaveEachWorksheetToDifferentPDF-1.cs" >}}

{{% alert color="primary" %}} 

إذا كانت جداول البيانات الخاصة بك تحتوي على صيغ، من الأفضل استدعاء [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) قبل تحويل جدول البيانات إلى تنسيق PDF. وذلك سيضمن إعادة حساب قيم الصيغ الخاصة وتقديم القيم الصحيحة في الملف الناتج PDF.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
