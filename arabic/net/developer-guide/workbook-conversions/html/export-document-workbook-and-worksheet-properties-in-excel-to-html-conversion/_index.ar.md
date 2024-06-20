---
title: تصدير خصائص ورقة عمل ومصنف الوثيقة في تحويل Excel إلى HTML
type: docs
weight: 50
url: /ar/net/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---

## **سيناريوهات الاستخدام المحتملة**

عندما يتم تصدير ملف Microsoft Excel إلى HTML باستخدام Microsoft Excel أو Aspose.Cells ، فإنه يصدر أيضًا أنواعًا مختلفة من خصائص الوثيقة والمصنف وورق العمل كما هو موضح في اللقطة الشاشية التالية. يمكنك تجنب تصدير هذه الخصائص عن طريق تعيين [**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportdocumentproperties)، [**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworkbookproperties) و [**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetproperties) إلى **false**. القيمة الافتراضية لهذه الخصائص هي **true**. توضح اللقطة الشاشية التالية كيفية ظهور هذه الخصائص في HTML المصدر.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **تصدير خصائص الوثيقة والمصنف وورق العمل في تحويل Excel إلى HTML**

يقوم الكود العيني التالي بتحميل [ملف Excel العيني](61767776.xlsx) وتحويله إلى HTML دون تصدير خصائص الوثيقة والمصنف وورق العمل في [HTML الناتج](61767779.zip).

## **الكود المثالي**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.cs" >}}
