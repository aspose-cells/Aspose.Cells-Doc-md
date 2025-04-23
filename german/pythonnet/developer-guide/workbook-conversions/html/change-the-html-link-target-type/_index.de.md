---
title: Ändern Sie den HTML Linkzieltyp
type: docs
weight: 320
url: /de/python-net/change-the-html-link-target-type/
description: Dieses Thema zeigt, wie man den HTML Link Zieltyp mit Aspose.Cells für Python via NET ändert.
keywords: Ändere den HTML Link Zieltyp, leere Zieldatentyp, übergeordneter Zieldatentyp, oberster Zieldatentyp, eigener Zieldatentyp.
---

{{% alert color="primary" %}}

Aspose.Cells für Python via NET ermöglicht es Ihnen, den HTML-Link-Zieltyp zu ändern. Der HTML-Link sieht so aus

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Wie Sie sehen können, ist das target-Attribut im obigen HTML-Link **_self**. Sie können dieses target-Attribut mit der [**HtmlSaveOptions.link_target_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/link_target_type/)-Eigenschaft steuern. Diese Eigenschaft nimmt das [**HtmlLinkTargetType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmllinktargettype)-Enum, das folgende Werte hat.

- HtmlLinkTargetType.BLANK
- HtmlLinkTargetType.PARENT
- HtmlLinkTargetType.SELF
- HtmlLinkTargetType.TOP

{{% /alert %}}

Der folgende Code veranschaulicht die Verwendung der [**HtmlSaveOptions.link_target_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/link_target_type/) Eigenschaft. Er ändert den Link-Zieltyp in **BLANK**. Standardmäßig ist es **PARENT**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ChangeHtmlLinkTarget-1.py" >}}
