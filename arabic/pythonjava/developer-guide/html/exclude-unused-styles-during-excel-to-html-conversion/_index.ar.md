---
title: استبعاد الأنماط غير المستخدمة أثناء تحويل Excel إلى HTML
type: docs
weight: 30
url: /ar/python-java/exclude-unused-styles-during-excel-to-html-conversion/
---
## **استبعاد الأنماط غير المستخدمة أثناء تحويل Excel إلى HTML**
Microsoft قد تحتوي ملفات Excel على العديد من الأنماط غير المستخدمة. عندما يتم تصدير هذه الملفات إلى تنسيق HTML ، يتم أيضًا تصدير الأنماط غير المستخدمة. ينتج عن هذا زيادة حجم HTML الناتج. Aspose.Cells for Python via Java يدعم استبعاد هذه الأنماط أثناء تحويل ملف Excel إلى HTML. لهذا ، يوفر API امتداد الملف[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles)منشأه. تحديد قيمة[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) الملكية ل**حقيقي** سوف يستبعد جميع الأنماط غير المستخدمة من الناتج HTML.

تُظهر لقطة الشاشة التالية الأنماط غير المستخدمة في ملف HTML والتي ستتم إزالتها عن طريق تعيين قيمة[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) الملكية ل**حقيقي**.

![ما يجب القيام به: image_بديل_نص](HtmlSaveOptions-Exclude-Unused-Styles.png)

يوضح نموذج التعليمات البرمجية التالي إزالة الأنماط غير المستخدمة أثناء تحويل Excel إلى HTML.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExcludeUnusedStylesInExcelToHTML.py" >}}
