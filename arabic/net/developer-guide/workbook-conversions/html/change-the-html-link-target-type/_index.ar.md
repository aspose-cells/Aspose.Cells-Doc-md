---
title: قم بتغيير نوع هدف ارتباط HTML
type: docs
weight: 320
url: /ar/net/change-the-html-link-target-type/
---
{{% alert color="primary" %}}

Aspose.Cells يسمح لك بتغيير نوع هدف ارتباط HTML. رابط HTML يبدو هكذا

{{< highlight "java" >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

كما ترى السمة الهدف في رابط HTML أعلاه هي ** _ self **. يمكنك التحكم في هذه السمة الهدف باستخدام خاصية [** HtmlSaveOptions.LinkTargetType **] (https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype). تأخذ هذه الخاصية [** HtmlLinkTargetType **] (https://reference.aspose.com/cells/net/aspose.cells/htmllinktargettype) التعداد الذي يحتوي على القيم التالية.

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType. أعلى

{{% /alert %}}

 يوضح الكود التالي استخدام[**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype) منشأه. يقوم بتغيير نوع الارتباط الهدف إلى**فارغ**. بشكل افتراضي ، يكون ملف**الأبوين**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ChangeHtmlLinkTarget-1.cs" >}}
