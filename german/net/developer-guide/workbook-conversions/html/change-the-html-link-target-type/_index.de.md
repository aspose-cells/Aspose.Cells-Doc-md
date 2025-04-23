---
title: Ändern Sie den HTML Linkzieltyp
type: docs
weight: 320
url: /de/net/change-the-html-link-target-type/
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht es Ihnen, den Typ des HTML-Links zu ändern. Ein HTML-Link sieht so aus

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Wie Sie sehen können, ist das target-Attribut im obigen HTML-Link **_self**. Sie können dieses target-Attribut mit der [**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype)-Eigenschaft steuern. Diese Eigenschaft nimmt das [**HtmlLinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmllinktargettype)-Enum, das folgende Werte hat.

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

Der folgende Code veranschaulicht die Verwendung der [**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype)-Eigenschaft. Er ändert den Link-Zieltyp auf **blank**. Standardmäßig ist es **parent**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ChangeHtmlLinkTarget-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
