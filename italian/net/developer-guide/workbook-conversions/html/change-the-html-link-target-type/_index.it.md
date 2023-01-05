---
title: Modificare il tipo di destinazione del collegamento HTML
type: docs
weight: 320
url: /it/net/change-the-html-link-target-type/
---
{{% alert color="primary" %}}

Aspose.Cells consente di modificare il tipo di destinazione del collegamento HTML. HTML il collegamento è simile a questo

{{< highlight "java" >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Come puoi vedere, l'attributo target nel link HTML sopra è **_self**. Puoi controllare questo attributo di destinazione utilizzando la proprietà [**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype). Questa proprietà accetta l'enumerazione [**HtmlLinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmllinktargettype) che ha i seguenti valori.

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

 Il codice seguente illustra l'utilizzo di[**HtmlSaveOptions.LinkTargetType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/linktargettype) proprietà. Cambia il tipo di destinazione del collegamento in**vuoto**. Per impostazione predefinita, è il**genitore**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ChangeHtmlLinkTarget-1.cs" >}}
