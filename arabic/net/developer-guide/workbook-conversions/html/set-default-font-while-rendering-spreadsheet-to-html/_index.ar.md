---
title: تعيين الخط الافتراضي أثناء تحويل جدول بيانات إكسل إلى HTML
type: docs
weight: 370
url: /ar/net/set-default-font-while-rendering-spreadsheet-to/
---

{{% alert color="primary" %}}

يتيح Aspose.Cells لك تعيين الخط الافتراضي أثناء تحويل جدول بيانات إكسل إلى HTML. يرجى استخدام [**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname) لهذا الغرض. هذا الخاصية مفيدة عندما تكون هناك خلايا في جدول البيانات تحتوي على خطوط خطأ أو غير موجودة. ثم سيتم عرض تلك الخلايا بالخط المحدد بالخاصية [**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname).

{{% /alert %}}

## تعيين الخط الافتراضي أثناء تحويل جدول بيانات إكسل إلى HTML

الكود العيني التالي يقوم بإنشاء دفتر عمل وإضافة نص معين في الخلية B4 من أول ورقة عمل ويقوم بتعيين خطه إلى خط غير معروف / غير موجود. ثم يقوم بحفظ الدفتر العمل بتنسيق HTML عن طريق تعيين أسماء خط مختلفة كـ Courier New, Arial, Times New Roman وما إلى ذلك.

تُظهر اللقطة الشاشية تأثير تعيين أسماء خط مختلفة كقيمة [**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname).

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

يُولّد الكود ملف [HTML الناتج بخط Courier New](5115516), [HTML الناتج بخط Arial](5115518), و [HTML الناتج بخط Times New Roman](5115517).

## كود عينة

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRendering-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
