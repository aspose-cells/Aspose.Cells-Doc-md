---
title: تغيير نوع الوجهة للرابط HTML
type: docs
weight: 450
url: /ar/java/change-the-html-link-target-type/
---

{{% alert color="primary" %}} 

تسمح Aspose.Cells لك بتغيير نوع الوصلة الـ HTML. الوصلة الـ HTML تبدو على النحو التالي:

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

كما ترون، السمة المستهدفة في الوصلة الـ HTML أعلاه هي **_self**. يمكنك التحكم في هذه السمة المستهدفة باستخدام خاصية [HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType). تأخذ هذه الخاصية تعداد [HtmlLinkTargetType](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlLinkTargetType) الذي يحتوي على القيم التالية.

- [BLANK](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#BLANK)
- [PARENT](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#PARENT)
- [SELF](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#SELF)
- [TOP](https://reference.aspose.com/cells/java/com.aspose.cells/htmllinktargettype#TOP)

{{% /alert %}} 
## **تغيير نوع الوصلة HTML المستهدفة**
توضح الشيفرة التالية الاستخدام لخاصية [HtmlSaveOptions.setLinkTargetType()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#LinkTargetType). تغيير نوع الوصلة إلى **فارغ**. بشكل افتراضي، هو **أصل**. يمكنك الحصول على [ملف الإكسل المصدر](5472932.xlsx) من هذا الرابط، ومع ذلك يمكنك استخدام أي ملف إكسل يحتوي على وصلة HTML داخله لتشغيل هذه الشيفرة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeHTMLLinkTargetType-ChangeHTMLLinkTargetType.java" >}}
