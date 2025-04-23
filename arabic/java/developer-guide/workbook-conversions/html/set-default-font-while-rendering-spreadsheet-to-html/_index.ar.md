---
title: تعيين الخط الافتراضي أثناء تحويل جدول بيانات إكسل إلى HTML
type: docs
weight: 830
url: /ar/java/set-default-font-while-rendering-spreadsheet-to/
---

{{% alert color="primary" %}} 

يسمح Aspose.Cells لك بتعيين الخط الافتراضي أثناء تقديم جدول الخلية إلى HTML. يرجى استخدام [HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName) لهذا الغرض. يكون هذا الخاصية مفيدًا عندما تكون بعض الخلايا في جدول الخلية تحتوي على خطوط غير صالحة أو غير موجودة. بعد ذلك ستتم تقديم تلك الخلايا في خط محدد باستخدام خاصية [HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName).

{{% /alert %}} 
## **تعيين الخط الافتراضي أثناء تقديم جدول بيانات إلى HTML**
الكود العيني التالي يقوم بإنشاء دفتر عمل وإضافة نص معين في الخلية B4 من أول ورقة عمل ويقوم بتعيين خطه إلى خط غير معروف / غير موجود. ثم يقوم بحفظ الدفتر العمل بتنسيق HTML عن طريق تعيين أسماء خط مختلفة كـ Courier New, Arial, Times New Roman وما إلى ذلك.

اللقطة الشاشية تظهر تأثير تعيين أسماء خط افتراضية مختلفة من خلال الخاصية [HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName).

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

الكود يولد [ملف HTML الناتج بـ Courier New](5472568)، [ملف HTML الناتج بـ Arial](5472567) و [ملف HTML الناتج بـ Times New Roman](5472565).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToHTML-.java" >}}
{{< app/cells/assistant language="java" >}}
