---
title: احفظ كل ورقة عمل في ملف PDF مختلف
type: docs
weight: 130
url: /ar/net/save-each-worksheet-to-a-different-pdf-file/
---
{{% alert color="primary" %}} 

يدعم Aspose.Cells تحويل ملفات XLS (التي تحتوي على صور ومخططات وما إلى ذلك) إلى وثائق PDF. يمكن أن يعمل Aspose.Cells for .NET بشكل مستقل لتحويل جدول بيانات إلى PDF ولا تحتاج إلى استخدام Aspose.PDF for .NET للتحويل. لا يتطلب التحويل أن يقوم البرنامج بإنشاء أو استخدام أي ملفات مؤقتة حيث يمكن إجراء العملية برمتها في الذاكرة.

{{% /alert %}} 
##  **احفظ كل ورقة عمل في ملف PDF مختلف**
 إذا كنت بحاجة إلى حفظ كل ورقة عمل في ملف Excel النموذجي الخاص بك لإنشاء ملفات PDF مختلفة ، فيمكنك تحقيق ذلك بسهولة. يمكنك محاولة تعيين فهرس ورقة واحدة على**[`PdfSaveOptions.SheetSet`] (https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** الخيار في وقت لتقديم PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SaveEachWorksheetToDifferentPDF-1.cs" >}}

{{% alert color="primary" %}} 

 إذا كان جدول البيانات الخاص بك يحتوي على صيغ ، فمن الأفضل الاتصال[المصنف .CalculateFormula ()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) مباشرة قبل تحويل جدول البيانات إلى تنسيق PDF. سيؤدي القيام بذلك إلى ضمان إعادة حساب القيم التابعة للصيغة ، وتقديم القيم الصحيحة في PDF.

{{% /alert %}}
