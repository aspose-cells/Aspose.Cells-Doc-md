---
title: قم بتغيير نوع هدف الارتباط HTML
type: docs
weight: 450
url: /ar/java/change-the-html-link-target-type/
---
{{% alert color="primary" %}} 

Aspose.Cells يسمح لك بتغيير نوع هدف الارتباط HTML. رابط HTML يبدو كالتالي:

{{< highlight "java" >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

كما ترى السمة الهدف في الرابط أعلاه HTML هي ** _ self **. يمكنك التحكم في هذه السمة الهدف باستخدام خاصية [HtmlSaveOptions.setLinkTargetType ()] (https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType). تأخذ هذه الخاصية التعداد [HtmlLinkTargetType] (https://reference.aspose.com/cells/java/com.aspose.cells/HtmlLinkTargetType) الذي يحتوي على القيم التالية.

- [فارغ](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#BLANK)
- [الأبوين](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#PARENT)
- [الذات](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#SELF)
- [أعلى](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#TOP)

{{% /alert %}} 
## **قم بتغيير نوع هدف الارتباط HTML**
 يوضح الكود التالي استخدام[HtmlSaveOptions.setLinkTargetType ()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType) خاصية. يقوم بتغيير نوع الارتباط الهدف إلى**فارغ**. بشكل افتراضي ، يكون ملف**الأبوين** . يمكنك الحصول على[ملف اكسل المصدر](5472932.xlsx) من هذا الرابط ، يمكنك استخدام أي ملف Excel يحتوي على ارتباط تشعبي HTML بداخله لتشغيل هذا الرمز.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeHTMLLinkTargetType-ChangeHTMLLinkTargetType.java" >}}
