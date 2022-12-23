---
title: حذف المسافات الزائدة بعد فاصل السطر أثناء استيراد HTML
type: docs
weight: 620
url: /ar/java/delete-redundant-spaces-after-line-break-while-importing/
---
{{% alert color="primary" %}} 

 الرجاء استخدام[HtmlLoadOptions.DeleteRedundantSpaces](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#DeleteRedundantSpaces) الملكية وتعيينها**حقيقي** لحذف جميع المسافات الزائدة التي تأتي بعد علامة فاصل الأسطر. بشكل افتراضي ، هذه الخاصية هي**خاطئة**ويتم الاحتفاظ بالمسافات الزائدة في ملفات Excel الناتجة.

{{% /alert %}} 
## **تأثير تعيين الخاصية HtmlLoadOptions.DeleteRedundantSpaces إلى false و true**
 توضح لقطة الشاشة التالية تأثير تعيين هذه الخاصية على**خاطئة** و**حقيقي**.

![ما يجب القيام به: image_بديل_نص](delete-redundant-spaces-after-line-break-while-importing-html_1.png)
## **حذف المسافات الزائدة بعد فاصل السطر أثناء استيراد HTML**
 يُظهر نموذج التعليمات البرمجية التالي استخدام امتداد الملف[HtmlLoadOptions.DeleteRedundantSpaces](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#DeleteRedundantSpaces) خاصية. يرجى ضبطه**حقيقي** أو**خاطئة** للحصول على الإخراج كما هو موضح في الصورة أعلاه.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-DeleteRedundantSpacesFromHtml-1.java" >}}
