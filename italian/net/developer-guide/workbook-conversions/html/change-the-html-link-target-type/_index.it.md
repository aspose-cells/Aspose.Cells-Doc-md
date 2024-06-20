---
title: Modifica il Tipo di Destinazione del Link HTML
type: docs
weight: 320
url: /it/net/change-the-html-link-target-type/
---

{{% alert color="primary" %}}

Aspose.Cells ti permette di cambiare il tipo di destinazione del link HTML. Il link HTML appare così

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Come puoi vedere, l'attributo di destinazione nel link HTML sopra è **_self**. È possibile controllare questo attributo di destinazione utilizzando la proprietà [**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype). Questa proprietà richiede l'enum [**HtmlLinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmllinktargettype) che ha i seguenti valori.

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

Il seguente codice illustra l'uso della proprietà [**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype). Cambia il tipo di destinazione del link a **blank**. Per default, è **parent**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ChangeHtmlLinkTarget-1.cs" >}}
