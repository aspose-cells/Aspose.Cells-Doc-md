---
title: 更改 HTML 链接目标类型
type: docs
weight: 320
url: /zh/net/change-the-html-link-target-type/
---

{{% alert color="primary" %}}

Aspose.Cells 允许您更改 HTML 链接的目标类型。HTML 链接看起来是这样的

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

如您所见，以上 HTML 链接中的 target 属性为 **_self**。您可以通过 [**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype) 属性控制此 target 属性。该属性接受 [**HtmlLinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmllinktargettype) 枚举，该枚举包含以下值。

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

以下代码说明了 [**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype) 属性的用法。它将链接目标类型更改为 **blank**。默认情况下，它是 **parent**。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ChangeHtmlLinkTarget-1.cs" >}}
