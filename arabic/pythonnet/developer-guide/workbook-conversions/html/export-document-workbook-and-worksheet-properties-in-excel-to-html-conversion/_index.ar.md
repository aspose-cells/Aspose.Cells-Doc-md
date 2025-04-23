---
title: تصدير خصائص ورقة عمل ومصنف الوثيقة في تحويل Excel إلى HTML
type: docs
weight: 50
url: /ar/python-net/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---

## **سيناريوهات الاستخدام المحتملة**

عندما يتم تصدير ملف Microsoft Excel إلى HTML باستخدام Microsoft Excel أو Aspose.Cells ، فإنه يصدر أيضًا أنواعًا مختلفة من خصائص الوثيقة والمصنف وورق العمل كما هو موضح في اللقطة الشاشية التالية. يمكنك تجنب تصدير هذه الخصائص عن طريق تعيين [**HtmlSaveOptions.export_document_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_document_properties)، [**HtmlSaveOptions.export_workbook_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_workbook_properties) و [**HtmlSaveOptions.export_worksheet_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_worksheet_properties) إلى **false**. القيمة الافتراضية لهذه الخصائص هي **true**. توضح اللقطة الشاشية التالية كيفية ظهور هذه الخصائص في HTML المصدر.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **تصدير خصائص الوثيقة والمصنف وورق العمل في تحويل Excel إلى HTML**

يقوم الكود العيني التالي بتحميل [ملف Excel العيني](61767776.xlsx) وتحويله إلى HTML دون تصدير خصائص الوثيقة والمصنف وورق العمل في [HTML الناتج](61767779.zip).

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.py" >}}
