---
title: تجنب الصفحة الفارغة في الإخراج PDF عندما لا يوجد شيء للطباعة
type: docs
weight: 30
url: /ar/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---
## **سيناريوهات الاستخدام الممكنة**

عندما يكون ملف Excel فارغًا ويقوم المستخدم بحفظه في PDF باستخدام Aspose.Cells ، فإنه يعرض صفحة فارغة في الإخراج PDF. أحيانًا يكون هذا السلوك الافتراضي غير مرغوب فيه. يوفر Aspose.Cells ملف[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) خاصية للتعامل مع هذه القضية. إذا قمت بتعيينه على أنه**خاطئة**، ومن بعد[**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception)سيحدث عندما لا يوجد شيء يمكن طباعته في الإخراج PDF.

## **تجنب الصفحة الفارغة في الإخراج PDF عندما لا يوجد شيء للطباعة**

يقوم نموذج التعليمات البرمجية التالي بإنشاء مصنف فارغ ثم يحفظه كـ PDF بعد تعيين ملف[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) الملكية مثل**خاطئة**. نظرًا لعدم وجود شيء يمكن طباعته في الإخراج PDF ، فإن ملف[**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception)يحدث كما هو موضح أدناه.

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.cs" >}}

## **استثناء**

{{< highlight "java" >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
