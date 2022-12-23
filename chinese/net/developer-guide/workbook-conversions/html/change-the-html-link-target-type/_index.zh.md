---
title: 更改 HTML 链接目标类型
type: docs
weight: 320
url: /zh/net/change-the-html-link-target-type/
---
{{% alert color="primary" %}}

Aspose.Cells 允许您更改 HTML 链接目标类型。 HTML 链接看起来像这样

{{< highlight "java" >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

可以看到上面HTML链接中的target属性是**_self**。您可以使用 [**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype) 属性控制此目标属性。此属性采用具有以下值的 [**HtmlLinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmllinktargettype) 枚举。

- HtmlLinkTargetType.空白
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

下面的代码说明了使用[**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype)财产。它将链接目标类型更改为**空白的**.默认情况下，它是**父母**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ChangeHtmlLinkTarget-1.cs" >}}
