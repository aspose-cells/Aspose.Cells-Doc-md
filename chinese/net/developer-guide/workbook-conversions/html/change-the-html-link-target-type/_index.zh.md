---
title: 更改HTML链接的目标类型
type: docs
weight: 320
url: /zh/net/change-the-html-link-target-type/
---

{{% alert color="primary" %}}

Aspose.Cells 允许您更改 HTML 链接的目标类型。 HTML 链接看起来像这样

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

如您所见，上述HTML链接中的target属性是**_self**。您可以使用[**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype)属性来控制此target属性。此属性采用了[**HtmlLinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmllinktargettype)枚举，其具有以下值。

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

以下代码说明了 [**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype) 属性的用法。 它将链接目标类型更改为 **blank**。 默认情况下，它是 **parent**。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ChangeHtmlLinkTarget-1.cs" >}}
