---
title: تغيير نوع الوجهة للرابط HTML
type: docs
weight: 320
url: /ar/python-net/change-the-html-link-target-type/
description: توضح هذه الموضوع كيفية تغيير نوع الوجهة لرابط HTML باستخدام Aspose.Cells for Python via NET.
keywords: تغيير نوع الوجهة لرابط HTML، نوع الوجهة الفارغ، نوع الوجهة الأصلي، نوع الوجهة العلوي، نوع الوجهة الذاتي.
---

{{% alert color="primary" %}}

تتيح Aspose.Cells for Python via NET لك تغيير نوع الوجهة لرابط HTML. يبدو رابط HTML مثل هذا

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

كما ترون، فإن سمة الوجهة في الرابط HTML أعلاه هي **_self**. يمكنك التحكم في هذه سمة الوجهة باستخدام ال [**HtmlSaveOptions.link_target_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/link_target_type/). تأخذ هذه الخاصية ال [**HtmlLinkTargetType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmllinktargettype) الذي يحتوي على القيم التالية.

- HtmlLinkTargetType.BLANK
- HtmlLinkTargetType.PARENT
- HtmlLinkTargetType.SELF
- HtmlLinkTargetType.TOP

{{% /alert %}}

يوضح الكود التالي استخدام الخاصية [**HtmlSaveOptions.link_target_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/link_target_type/). يقوم بتغيير نوع الوجهة للرابط إلى **BLANK**. بشكل افتراضي، يكون النوع الأصلي **PARENT**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ChangeHtmlLinkTarget-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
