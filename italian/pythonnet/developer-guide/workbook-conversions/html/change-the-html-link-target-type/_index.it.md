---
title: Modifica il Tipo di Destinazione del Link HTML
type: docs
weight: 320
url: /it/python-net/change-the-html-link-target-type/
description: Questo argomento mostra come modificare il tipo di destinazione del collegamento HTML utilizzando Aspose.Cells per Python via NET.
keywords: Modificare il tipo di destinazione del collegamento HTML, tipo di destinazione vuoto, tipo di destinazione genitore, tipo di destinazione superiore, tipo di destinazione stesso.
---

{{% alert color="primary" %}}

Aspose.Cells per Python via NET consente di modificare il tipo di destinazione del collegamento HTML. Il collegamento HTML appare così

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Come puoi vedere, l'attributo di destinazione nel link HTML sopra è **_self**. È possibile controllare questo attributo di destinazione utilizzando la proprietà [**HtmlSaveOptions.link_target_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/link_target_type/). Questa proprietà richiede l'enum [**HtmlLinkTargetType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmllinktargettype) che ha i seguenti valori.

- HtmlLinkTargetType.BLANK
- HtmlLinkTargetType.PARENT
- HtmlLinkTargetType.SELF
- HtmlLinkTargetType.TOP

{{% /alert %}}

Il codice seguente illustra l'uso della proprietà [**HtmlSaveOptions.link_target_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/link_target_type/). Modifica il tipo di destinazione del collegamento a **BLANK**. Per impostazione predefinita, è **PARENT**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ChangeHtmlLinkTarget-1.py" >}}
