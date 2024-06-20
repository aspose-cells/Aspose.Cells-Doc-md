---
title: تجنب الصفحة الفارغة في ملف PDF الناتج عندما لا يوجد شيء للطباعة
type: docs
weight: 30
url: /ar/java/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---

## **سيناريوهات الاستخدام المحتملة**

عندما يكون ملف Excel فارغًا ويقوم المستخدم بحفظه إلى PDF باستخدام Aspose.Cells ، يقوم بعرض صفحة فارغة في PDF الناتج. في بعض الأحيان ، هذا السلوك الافتراضي غير مرغوب فيه. توفر Aspose.Cells الخاصية [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint) للتعامل مع هذه المشكلة. إذا قمت بتعيينها على **false** ، فسيحدث [**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException) كلما لم يكن هناك شيء للطباعة في PDF الناتج.

## **تجنب الصفحة الفارغة في ملف PDF الناتج عندما لا يوجد شيء للطباعة**

كود العينة التالي ينشئ دفتر عمل فارغ ثم يحفظه كملف PDF الإخراج بعد ضبط الخاصية [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint) على **false**. نظرًا لعدم وجود أي شيء للطباعة في ملف PDF الإخراج ، يحدث [**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException) كما هو مبين أدناه.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.java" >}}

## **استثناء**

{{< highlight java >}}

 Exception in thread "main" com.aspose.cells.CellsException: There is nothing to output/print.

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.Workbook.a(Unknown Source)

	at com.aspose.cells.Workbook.save(Unknown Source)

{{< /highlight >}}
