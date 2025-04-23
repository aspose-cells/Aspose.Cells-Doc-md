---
title: حفظ كل ورقة عمل في ملف PDF مختلف
type: docs
weight: 50
url: /ar/java/save-each-worksheet-to-a-different-pdf-file/
---

{{% alert color="primary" %}}

يدعم Aspose.Cells تحويل ملفات جدول البيانات (التي تحتوي على صور، رسوم بيانية، إلخ) إلى مستندات PDF. يمكن لـ Aspose.Cells for Java العمل بشكل مستقل لتحويل جدول البيانات إلى مستند PDF ولا تحتاج إلى استخدام Aspose.PDF for Java للتحويل بعد الآن. لا يتطلب التحويل إنشاء / استخدام أي ملفات مؤقتة أيضًا حيث يمكن أن يتم العملية بأكملها في الذاكرة.

{{% /alert %}}

إذا كنت بحاجة إلى حفظ كل ورقة عمل في ملف إكسيل النموذجي الخاص بك لإنشاء ملفات PDF مختلفة. يمكن تحقيق ذلك بسهولة. يمكنك محاولة تعيين فهرس ورقة واحدة إلى الخيار [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-) في كل مرة لتقديمه إلى ملف PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveEachWorksheettoDifferentPDF-SaveEachWorksheettoDifferentPDF.java" >}}

{{% alert color="primary" %}}

إذا كان جدول البيانات يحتوي على صيغ، من الأفضل استدعاء الطريقة [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) قبل تقديم جدول البيانات إلى PDF. هذا يضمن إعادة حساب القيم التي تعتمد على الصيغ، وتقديم القيم الصحيحة في مستند PDF.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
