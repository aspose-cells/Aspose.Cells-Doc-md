---
title: Der Zieltyp des HTML Links ändern mit Golang via C++
linktitle: Ändern Sie den HTML Linkzieltyp
type: docs
weight: 320
url: /de/go-cpp/change-the-html-link-target-type/
description: Lernen Sie, wie man den HTML Linkzieltyp mit Aspose.Cells for C++ ändert. Kontrollieren Sie das Zielattribut in HTML Links programmatisch.
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht es Ihnen, den Typ des HTML-Links zu ändern. Ein HTML-Link sieht so aus

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Wie Sie sehen können, ist das target-Attribut im obigen HTML-Link **_self**. Sie können dieses target-Attribut mit der [**GetLinkTargetType()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getlinktargettype/)-Eigenschaft steuern. Diese Eigenschaft nimmt das [**HtmlLinkTargetType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmllinktargettype/)-Enum, das folgende Werte hat.

- HtmlLinkTargetType::Blank
- HtmlLinkTargetType::Parent
- HtmlLinkTargetType::Self
- HtmlLinkTargetType::Top

{{% /alert %}}

Der folgende Code veranschaulicht die Verwendung der [**GetLinkTargetType()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getlinktargettype/)-Eigenschaft. Er ändert den Link-Zieltyp auf **blank**. Standardmäßig ist es **parent**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeTheHtmlLinkTargetType.go" >}}
