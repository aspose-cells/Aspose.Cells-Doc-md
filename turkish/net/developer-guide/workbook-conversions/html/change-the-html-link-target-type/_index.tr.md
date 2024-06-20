---
title: HTML Bağlantısı Hedef Türünü Değiştirme
type: docs
weight: 320
url: /tr/net/change-the-html-link-target-type/
---

{{% alert color="primary" %}}

Aspose.Cells, HTML bağlantı hedef türünü değiştirmenize olanak tanır. HTML bağlantısı şuna benzer

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Yukarıdaki HTML bağlantısında hedef özniteliği **_self** olarak gösterilir. Bu hedef özniteliğini [**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype) özelliğini kullanarak kontrol edebilirsiniz. Bu özellik, aşağıdakileri içeren [**HtmlLinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmllinktargettype) enumunu alır.

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

Aşağıdaki kod, [**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype) özelliğinin kullanımını gösterir. Bağlantı hedef türünü varsayılan olarak **parent** olarak değiştirir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ChangeHtmlLinkTarget-1.cs" >}}
