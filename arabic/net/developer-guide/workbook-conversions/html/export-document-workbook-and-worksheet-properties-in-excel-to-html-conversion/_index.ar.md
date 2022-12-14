---
title: تصدير مصنف المستند وخصائص ورقة العمل في تحويل Excel إلى HTML
type: docs
weight: 50
url: /ar/net/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---
## **سيناريوهات الاستخدام الممكنة**

عندما يتم تصدير ملف Excel Microsoft إلى HTML باستخدام Microsoft Excel أو Aspose.Cells ، فإنه يقوم أيضًا بتصدير أنواع مختلفة من خصائص المستند ، والمصنف ، وورقة العمل كما هو موضح في لقطة الشاشة التالية. يمكنك تجنب تصدير هذه الخصائص عن طريق تعيين ملف[**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportdocumentproperties), [**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworkbookproperties)و[**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetproperties) كما**خاطئة** . القيمة الافتراضية لهذه الخصائص هي**حقيقي**. توضح لقطة الشاشة التالية كيف تبدو هذه الخصائص في HTML المُصدَّر.

![ما يجب القيام به: image_بديل_نص](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **تصدير خصائص المستند والمصنف وورقة العمل في تحويل Excel إلى HTML**

 يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[نموذج لملف Excel](61767776.xlsx) ويقوم بتحويله إلى HTML ولا يقوم بتصدير خصائص المستند ، والمصنف ، وورقة العمل بتنسيق[إخراج HTML](61767779.zip).

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.cs" >}}
