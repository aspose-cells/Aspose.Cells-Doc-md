---
title: تصدير التعليقات أثناء حفظ ملف Excel إلى HTML
type: docs
weight: 40
url: /ar/python-net/export-comments-while-saving-excel-file-to/
---

## **سيناريوهات الاستخدام المحتملة**

عند حفظ ملف Excel الخاص بك في HTML، لن يتم تصدير التعليقات. ومع ذلك، يوفر Aspose.Cells لـ Python via .NET هذه الميزة باستخدام خاصية [**HtmlSaveOptions.is_export_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/is_export_comments). إذا قمت بضبطها على **true**، فسيتم عرض التعليقات الموجودة في ملف Excel الخاص بك أيضًا في HTML.

## **تصدير التعليقات أثناء حفظ ملف Excel إلى HTML**

يشرح الكود العيني التالي استخدام الخاصية [**HtmlSaveOptions.is_export_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/is_export_comments). توضح اللقطة الشاشية تأثير الكود على الHTML عندما يتم تعيينها إلى **true**. يرجى تحميل [ملف Excel العيني](50528260.xlsx) و[HTML المُنشئ](5052826.txt) للرجوع إليها.

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportCommentsWhileSavingExcelFileToHtml.py" >}}
{{< app/cells/assistant language="python-net" >}}
