---
title: HTML Bağlantısı Hedef Türünü Değiştirme
type: docs
weight: 320
url: /tr/python-net/change-the-html-link-target-type/
description: Bu konu, Aspose.Cells için Python via NET kullanarak HTML Bağlantı Hedef Türünü Değiştirme nasıl yapılacağını gösterir.
keywords: HTML Bağlantı Hedef Türünü Değiştirme, boş hedef tür, ana hedef tür, üst hedef tür, kendini hedef tür.
---

{{% alert color="primary" %}}

Aspose.Cells için Python via NET, HTML bağlantı hedef türünü değiştirmenize olanak tanır. HTML bağlantısı şu şekilde görünür

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Yukarıdaki HTML bağlantısında hedef özniteliği **_self** olarak gösterilir. Bu hedef özniteliğini [**HtmlSaveOptions.link_target_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/link_target_type/) özelliğini kullanarak kontrol edebilirsiniz. Bu özellik, aşağıdakileri içeren [**HtmlLinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmllinktargettype) enumunu alır.

- HtmlLinkTargetType.BLANK
- HtmlLinkTargetType.PARENT
- HtmlLinkTargetType.SELF
- HtmlLinkTargetType.TOP

{{% /alert %}}

Aşağıdaki kod, [**HtmlSaveOptions.link_target_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/link_target_type/) özelliğinin kullanımını gösterir. Bağlantı hedef türünü varsayılan olarak **PARENT** olarak değiştirir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ChangeHtmlLinkTarget-1.py" >}}
