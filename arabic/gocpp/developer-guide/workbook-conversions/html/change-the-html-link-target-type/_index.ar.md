---
title: تغيير نوع هدف رابط HTML باستخدام Golang عبر C++
linktitle: تغيير نوع الوجهة للرابط HTML
type: docs
weight: 320
url: /ar/go-cpp/change-the-html-link-target-type/
description: تعلم كيفية تغيير نوع هدف رابط HTML باستخدام Aspose.Cells for C++. التحكم في سمة الهدف في روابط HTML برمجياً.
---

{{% alert color="primary" %}}

تُتيح Aspose.Cells لك تغيير نوع الوجهة للرابط HTML. يبدو الرابط HTML على النحو التالي

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

كما ترون، فإن سمة الوجهة في الرابط HTML أعلاه هي **_self**. يمكنك التحكم في هذه سمة الوجهة باستخدام ال [**GetLinkTargetType()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getlinktargettype/). تأخذ هذه الخاصية ال [**HtmlLinkTargetType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmllinktargettype/) الذي يحتوي على القيم التالية.

- HtmlLinkTargetType::Blank
- HtmlLinkTargetType::Parent
- HtmlLinkTargetType::Self
- HtmlLinkTargetType::Top

{{% /alert %}}

الشفرة العينية التالية توضح استخدام ال [**GetLinkTargetType()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getlinktargettype/). يغيّر نوع الوجهة للرابط إلى **blank**. بشكل افتراضي، يكون هو الـ **الرئيسي**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeTheHtmlLinkTargetType.go" >}}
