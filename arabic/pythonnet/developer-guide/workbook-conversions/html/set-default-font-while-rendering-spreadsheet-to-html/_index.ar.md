---
title: تعيين الخط الافتراضي أثناء تحويل جدول بيانات إكسل إلى HTML
type: docs
weight: 370
url: /ar/python-net/set-default-font-while-rendering-spreadsheet-to/
---

{{% alert color="primary" %}}

يتيح Aspose.Cells لك تعيين الخط الافتراضي أثناء تحويل جدول بيانات إكسل إلى HTML. يرجى استخدام [**HtmlSaveOptions.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/default_font_name) لهذا الغرض. هذا الخاصية مفيدة عندما تكون هناك خلايا في جدول البيانات تحتوي على خطوط خطأ أو غير موجودة. ثم سيتم عرض تلك الخلايا بالخط المحدد بالخاصية [**HtmlSaveOptions.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/default_font_name).

{{% /alert %}}

## تعيين الخط الافتراضي أثناء تحويل جدول بيانات إكسل إلى HTML

الكود العيني التالي يقوم بإنشاء دفتر عمل وإضافة نص معين في الخلية B4 من أول ورقة عمل ويقوم بتعيين خطه إلى خط غير معروف / غير موجود. ثم يقوم بحفظ الدفتر العمل بتنسيق HTML عن طريق تعيين أسماء خط مختلفة كـ Courier New, Arial, Times New Roman وما إلى ذلك.

تُظهر اللقطة الشاشية تأثير تعيين أسماء خط مختلفة كقيمة [**HtmlSaveOptions.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/default_font_name).

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

يُولّد الكود ملف [HTML الناتج بخط Courier New](5115516), [HTML الناتج بخط Arial](5115518), و [HTML الناتج بخط Times New Roman](5115517).

## كود عينة

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-SetDefaultFontWhileRendering-1.py" >}}
