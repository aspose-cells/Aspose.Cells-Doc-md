---
title: تحويل Excel إلى HTML مع العناوين
type: docs
weight: 10
url: /ar/python-java/convert-excel-to-html-with-headings/
---

## **تحويل Excel إلى HTML مع عناوين**
يوفر Aspose.Cells خيار تصدير ترويسات الصف والعمود أثناء تحويل Excel إلى HTML. يمكن تحقيق ذلك باستخدام خاصية [HtmlSaveOptions.ExportHeadings](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportHeadings) المقدمة من قبل الواجهة البرمجية. القيمة الافتراضية لـ [HtmlSaveOptions.ExportHeadings](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportHeadings) هي **False**. يمرر **True** كمعلمة لعرض الترويسات في ملف HTML الناتج. الصورة التالية تظهر ملف الإخراج الذي تم إنشاؤه بواسطة الكود التالي.

![todo:image_alt_text](PrintHeadings.jpg)

الكود النموذجي التالي يوضح استخدام خاصية [HtmlSaveOptions.ExportHeadings](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportHeadings) لعرض الترويسات في ملف HTML الناتج.
## **الكود المثالي**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-GetHTML5StringFromCell.py" >}}
