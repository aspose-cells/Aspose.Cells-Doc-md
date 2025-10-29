---
title: تصدير خصائص دفتر العمل والأوراق في تحويل إكسل إلى HTML باستخدام جولانغ عبر C++
linktitle: تصدير خصائص المستند ودفتر العمل وورقة العمل في تحويل Excel إلى HTML
type: docs
weight: 50
url: /ar/go-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
description: تعلم كيف تصدر أو تتجنب تصدير خصائص المستند ودفتر العمل وورقة العمل عند تحويل ملفات Excel إلى HTML باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

عند تصدير ملف Microsoft Excel إلى HTML باستخدام Microsoft Excel أو Aspose.Cells، يتم أيضًا تصدير أنواع مختلفة من خصائص المستند ودفتر العمل وورقة العمل كما هو موضح في الصورة أدناه. يمكنك تجنب تصدير هذه الخصائص بضبط [**HtmlSaveOptions.GetExportDocumentProperties()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportdocumentproperties/)، [**HtmlSaveOptions.GetExportWorkbookProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworkbookproperties/)، و[**HtmlSaveOptions.GetExportWorksheetProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetproperties/) على **false**. القيمة الافتراضية لهذه الخصائص هي **true**. تُظهر الصورة أدناه كيف تبدو هذه الخصائص في HTML المصدّر.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **تصدير خصائص مستند التصدير، كتاب العمل، وورقة العمل في تحويل إكسل إلى HTML**

يحمل رمز المثال التالي ملف Excel النموذجي ويحوّله إلى HTML بدون تصدير خصائص المستند ودفتر العمل وورقة العمل في [HTML الناتج](61767779.zip).

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportDocumentWorkbookAndWorksheetPropertiesInExcelToHtmlConversion.go" >}}
