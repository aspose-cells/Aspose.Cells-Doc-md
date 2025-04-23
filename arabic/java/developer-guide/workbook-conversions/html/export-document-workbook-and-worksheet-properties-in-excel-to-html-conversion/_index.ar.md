---
title: تصدير خصائص ورقة عمل ومصنف الوثيقة في تحويل Excel إلى HTML
type: docs
weight: 50
url: /ar/java/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---

## **سيناريوهات الاستخدام المحتملة**

عندما يتم تصدير ملف Microsoft Excel إلى HTML باستخدام Microsoft Excel أو Aspose.Cells، تتم أيضًا تصدير أنواع مختلفة من خصائص المستند وجدول البيانات والجدول كما هو موضح في لقطة الشاشة التالية. يمكنك تجنب تصدير هذه الخصائص عن طريق ضبط الـ [**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportDocumentProperties) والـ [**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorkbookProperties) والـ [**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorksheetProperties) على **false**. القيمة الافتراضية لهذه الخصائص هي **true**. تظهر اللقطة الشاشة التالية كيف تبدو هذه الخصائص في الملف HTML المصدر.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **تصدير خصائص الوثيقة والمصنف وورق العمل في تحويل Excel إلى HTML**

الكود عينة التالي يحمل [ملف إكسل عينة](61767784.xlsx) ويحوله إلى HTML ولا يصدر خصائص المستند وجدول البيانات في [ملف HTML المصدر](61767783.zip).

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.java" >}}
{{< app/cells/assistant language="java" >}}
