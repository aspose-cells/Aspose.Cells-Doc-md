---
title: 更改 HTML 链接目标类型
type: docs
weight: 320
url: /zh/python-net/change-the-html-link-target-type/
description: 本主题向您展示如何使用Aspose.Cells for Python via NET更改HTML链接目标类型。
keywords: 更改 HTML 链接的目标类型，空白目标类型，父级目标类型，顶级目标类型，自身目标类型。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via NET允许您更改HTML链接的目标类型。HTML链接如下所示

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

如您所见，以上 HTML 链接中的 target 属性为 **_self**。您可以通过 [**HtmlSaveOptions.link_target_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/link_target_type/) 属性控制此 target 属性。该属性接受 [**HtmlLinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmllinktargettype) 枚举，该枚举包含以下值。

- HtmlLinkTargetType.BLANK
- HtmlLinkTargetType.PARENT
- HtmlLinkTargetType.SELF
- HtmlLinkTargetType.TOP

{{% /alert %}}

以下代码展示了 [**HtmlSaveOptions.link_target_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/link_target_type/) 属性的用法。它将链接的目标类型更改为 **BLANK**。默认情况下，目标类型是 **PARENT**。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ChangeHtmlLinkTarget-1.py" >}}
