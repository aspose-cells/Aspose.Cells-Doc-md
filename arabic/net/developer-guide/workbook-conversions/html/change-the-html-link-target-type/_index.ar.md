---
title: تغيير نوع الوجهة للرابط HTML
type: docs
weight: 320
url: /ar/net/change-the-html-link-target-type/
---

{{% alert color="primary" %}}

تُتيح Aspose.Cells لك تغيير نوع الوجهة للرابط HTML. يبدو الرابط HTML على النحو التالي

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

كما ترون، فإن سمة الوجهة في الرابط HTML أعلاه هي **_self**. يمكنك التحكم في هذه سمة الوجهة باستخدام ال [**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype). تأخذ هذه الخاصية ال [**HtmlLinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmllinktargettype) الذي يحتوي على القيم التالية.

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

الشفرة العينية التالية توضح استخدام ال [**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype). يغيّر نوع الوجهة للرابط إلى **blank**. بشكل افتراضي، يكون هو الـ **الرئيسي**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ChangeHtmlLinkTarget-1.cs" >}}
