---
title: استبعاد الأنماط غير المستخدمة أثناء تحويل Excel إلى HTML
type: docs
weight: 30
url: /ar/python-java/exclude-unused-styles-during-excel-to-html-conversion/
---

## **استبعاد الأنماط غير المستخدمة أثناء تحويل Excel إلى HTML**
قد تحتوي ملفات Microsoft Excel على العديد من الأنماط غير المستخدمة. عند تصدير هذه الملفات إلى تنسيق HTML، يتم تصدير الأنماط غير المستخدمة أيضًا. وهذا يؤدي إلى زيادة حجم ملف HTML الناتج. تدعم Aspose.Cells for Python via Java استبعاد هذه الأنماط أثناء تحويل ملف Excel إلى HTML. لهذا، توفر الواجهة برمجة التطبيقات (API) خاصية ExcludeUnusedStyles (https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles). سيؤدي ضبط قيمة خاصية ExcludeUnusedStyles (https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) إلى True إلى استبعاد جميع الأنماط غير المستخدمة من ملف الHTML الناتج.

توضح اللقطة الشاشة التالية الأنماط غير المستخدمة في ملف HTML الذي سيتم إزالتها عن طريق ضبط قيمة خاصية ExcludeUnusedStyles (https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) إلى True.

![todo:image_alt_text](HtmlSaveOptions-Exclude-Unused-Styles.png)

يقوم الكود النموذجي التالي بإزالة الأنماط غير المستخدمة أثناء تحويل Excel إلى HTML.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExcludeUnusedStylesInExcelToHTML.py" >}}
