---
title: تجنب الصفحة الفارغة في ملف PDF الناتج عندما لا يوجد شيء للطباعة
type: docs
weight: 30
url: /ar/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: تعلم كيفية تجنب الصفحة الفارغة في ملف PDF الناتج عند عدم وجود شيء للطباعة باستخدام Aspose.Cells for Python via .NET API.
keywords: تجنب الصفحة الفارغة في ملف PDF الناتج عند عدم وجود شيء للطباعة باستخدام Python
---

## **سيناريوهات الاستخدام المحتملة**

عندما يكون ملف Excel فارغًا ويقوم المستخدم بحفظه إلى PDF باستخدام Aspose.Cells for Python via .NET، يقوم بتقديم صفحة فارغة في ملف PDF الناتج. في بعض الأحيان، يعتبر هذا السلوك الافتراضي غير مرغوب فيه. توفر Aspose.Cells for Python via .NET خاصية [**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/) للتعامل مع هذه المشكلة. إذا كنت ستضبطها ك**false**، فستحدث [**CellsException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/) كلما لم يكن هناك شيء للطباعة في ملف PDF الناتج.

## **تجنب الصفحة الفارغة في ملف PDF الناتج عندما لا يوجد شيء للطباعة**

يقوم الكود المثالي التالي بإنشاء دفتر عمل فارغ ثم يحفظه كملف PDF بعد تعيين الخاصية [**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/) على **false**. نظرًا لعدم وجود شيء للطباعة في PDF الناتج ، يحدث [**CellsException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/) كما هو موضح أدناه.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.py" >}}

## **استثناء**

{{< highlight java >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
