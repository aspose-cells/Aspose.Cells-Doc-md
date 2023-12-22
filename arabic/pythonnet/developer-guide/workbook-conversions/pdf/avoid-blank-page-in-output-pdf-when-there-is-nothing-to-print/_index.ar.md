---
title: تجنب الصفحة الفارغة في الإخراج PDF عندما لا يكون هناك شيء للطباعة
type: docs
weight: 30
url: /ar/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: تعرف على كيفية تجنب الصفحة الفارغة في الإخراج PDF عندما لا يكون هناك شيء للطباعة باستخدام Aspose.Cells for Python via .NET API.
keywords: Python Avoid Blank Page in Output PDF when there is Nothing to Print
---
##  **سيناريوهات الاستخدام المحتملة**

عندما يكون ملف Excel فارغًا ويقوم المستخدم بحفظه في PDF باستخدام Aspose.Cells for Python via .NET، فإنه يعرض صفحة فارغة في الإخراج PDF. في بعض الأحيان، يكون هذا السلوك الافتراضي غير مرغوب فيه. Aspose.Cells for Python via .NET يوفر[**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/)الملكية للتعامل مع هذه المشكلة. إذا قمت بتعيينه كـ *خطأ**، إذن[**استثناء الخلايا**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/)سيحدث عندما لا يكون هناك شيء لطباعته في الإخراج PDF.

##  **تجنب الصفحة الفارغة في الإخراج PDF عندما لا يكون هناك شيء للطباعة**

يقوم نموذج التعليمات البرمجية التالي بإنشاء مصنف فارغ ثم يحفظه كـ PDF بعد تعيين[**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/)الخاصية كـ *خطأ**. نظرًا لعدم وجود شيء لطباعته في الإخراج PDF، فإن[**استثناء الخلايا**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/)يحدث كما هو موضح أدناه.

##  **عينة من الرموز**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.py" >}}

##  **استثناء**

{{< highlight "java" >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
