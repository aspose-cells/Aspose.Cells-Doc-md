---
title: تجنب الصفحة الفارغة في ملف PDF الناتج عندما لا يوجد شيء للطباعة
type: docs
weight: 30
url: /ar/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---

## **سيناريوهات الاستخدام المحتملة**

عندما يكون ملف Excel فارغًا ويقوم المستخدم بحفظه إلى PDF باستخدام Aspose.Cells ، يقوم بعرض صفحة فارغة في PDF الناتج. في بعض الأحيان ، هذا السلوك الافتراضي غير مرغوب فيه. توفر Aspose.Cells الخاصية [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) للتعامل مع هذه المشكلة. إذا قمت بتعيينها على **false** ، فسيحدث [**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception) كلما لم يكن هناك شيء للطباعة في PDF الناتج.

## **تجنب الصفحة الفارغة في ملف PDF الناتج عندما لا يوجد شيء للطباعة**

يقوم الكود المثالي التالي بإنشاء دفتر عمل فارغ ثم يحفظه كملف PDF بعد تعيين الخاصية [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) على **false**. نظرًا لعدم وجود شيء للطباعة في PDF الناتج ، يحدث [**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception) كما هو موضح أدناه.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.cs" >}}

## **استثناء**

{{< highlight java >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
