---
title: تعيين الخط الافتراضي أثناء تحويل جدول البيانات إلى HTML باستخدام Golang عبر C++
linktitle: تعيين الخط الافتراضي أثناء تحويل جدول بيانات إكسل إلى HTML
type: docs
weight: 370
url: /ar/go-cpp/set-default-font-while-rendering-spreadsheet-to/
description: تعلم كيفية تعيين الخط الافتراضي أثناء تحويل جدول البيانات إلى HTML باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

 تتيح لك Aspose.Cells تعيين الخط الافتراضي أثناء تحويل جدول بيانات إلى HTML. يرجى استخدام [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdefaultfontname/) لهذا الغرض. يكون لهذه الخاصية فائدة عندما تحتوي بعض الخلايا في جدول البيانات على خطوط غير صالحة أو غير موجودة. ثم سيتم عرض تلك الخلايا بخط معين بواسطة الخاصية [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdefaultfontname/).

{{% /alert %}}

## تعيين الخط الافتراضي أثناء تحويل جدول بيانات إكسل إلى HTML

الكود العيني التالي يقوم بإنشاء دفتر عمل وإضافة نص معين في الخلية B4 من أول ورقة عمل ويقوم بتعيين خطه إلى خط غير معروف / غير موجود. ثم يقوم بحفظ الدفتر العمل بتنسيق HTML عن طريق تعيين أسماء خط مختلفة كـ Courier New, Arial, Times New Roman وما إلى ذلك.

تُظهر صورة لقطة الشاشة تأثير تعيين أسماء خطوط افتراضية مختلفة عبر خاصية [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdefaultfontname/).

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

يُولّد الكود ملف [HTML الناتج بخط Courier New](5115516), [HTML الناتج بخط Arial](5115518), و [HTML الناتج بخط Times New Roman](5115517).

## كود عينة

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetDefaultFontWhileRenderingSpreadsheetToHtml.go" >}}
