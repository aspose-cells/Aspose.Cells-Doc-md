---
title: حذف المسافات الزائدة بعد فواصل الأسطر أثناء استيراد HTML
type: docs
weight: 620
url: /ar/java/delete-redundant-spaces-after-line-break-while-importing/
---

{{% alert color="primary" %}} 

يرجى استخدام خاصية [HtmlLoadOptions.DeleteRedundantSpaces](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#DeleteRedundantSpaces) وتعيينها إلى **true** لحذف كل المسافات الزائدة بعد علامة فاصل السطر. افتراضيًا، تكون هذه الخاصية **false** وتُحتفظ المسافات الزائدة في ملفات الـ Excel المنتجة.

{{% /alert %}} 
## **تأثير تعيين خاصية HtmlLoadOptions.DeleteRedundantSpaces إلى false و true**
تُظهر اللقطة الشاشة التالية تأثير تعيين هذه الخاصية إلى **false** و **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)
## **حذف المسافات الزائدة بعد فاصلة السطر أثناء استيراد HTML**
الكود البرمجي عينة يوضح استخدام [HtmlLoadOptions.DeleteRedundantSpaces](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#DeleteRedundantSpaces)  . يرجى تعيينها **true** أو **false** للحصول على الناتج كما هو موضح في اللقطة الشاشية أعلاه.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-DeleteRedundantSpacesFromHtml-1.java" >}}
