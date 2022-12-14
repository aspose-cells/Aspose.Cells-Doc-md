---
title: Ändern Sie den Zieltyp des HTML-Links
type: docs
weight: 320
url: /de/net/change-the-html-link-target-type/
---
{{% alert color="primary" %}}

Aspose.Cells ermöglicht es Ihnen, den Zieltyp des HTML-Links zu ändern. Der HTML-Link sieht so aus

{{< highlight "java" >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Wie Sie sehen können, ist das Zielattribut im obigen HTML-Link **_self**. Sie können dieses Zielattribut mit der Eigenschaft [**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype) steuern. Diese Eigenschaft übernimmt die Enumeration [**HtmlLinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmllinktargettype) mit den folgenden Werten.

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

 Der folgende Code veranschaulicht die Verwendung von[**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype) Eigentum. Es ändert den Zieltyp des Links in**leer**. Standardmäßig ist es die**Elternteil**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ChangeHtmlLinkTarget-1.cs" >}}
