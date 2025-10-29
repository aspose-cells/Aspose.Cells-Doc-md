---
title: 使用 Golang 通过 C++ 更改 HTML 链接目标类型
linktitle: 更改HTML链接的目标类型
type: docs
weight: 320
url: /zh/go-cpp/change-the-html-link-target-type/
description: 学习如何使用编号Aspose.Cells for C++更改HTML链接的目标类型，程序化控制HTML链接中的target属性。
---

{{% alert color="primary" %}}

Aspose.Cells 允许您更改 HTML 链接的目标类型。 HTML 链接看起来像这样

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

如您所见，上述HTML链接中的target属性是**_self**。您可以使用[**GetLinkTargetType()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getlinktargettype/)属性来控制此target属性。此属性采用了[**HtmlLinkTargetType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmllinktargettype/)枚举，其具有以下值。

- HtmlLinkTargetType::Blank
- HtmlLinkTargetType::Parent
- HtmlLinkTargetType::Self
- HtmlLinkTargetType::顶部

{{% /alert %}}

以下代码说明了 [**GetLinkTargetType()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getlinktargettype/) 属性的用法。 它将链接目标类型更改为 **blank**。 默认情况下，它是 **parent**。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeTheHtmlLinkTargetType.go" >}}
