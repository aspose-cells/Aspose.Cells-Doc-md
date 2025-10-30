---
title: Modifica il tipo di destinazione del collegamento HTML con Golang via C++
linktitle: Modifica il Tipo di Destinazione del Link HTML
type: docs
weight: 320
url: /it/go-cpp/change-the-html-link-target-type/
description: Impara come cambiare il tipo di destinazione del collegamento HTML usando Aspose.Cells for C++. Controlla l attributo target nei collegamenti HTML programmaticamente.
---

{{% alert color="primary" %}}

Aspose.Cells ti permette di cambiare il tipo di destinazione del link HTML. Il link HTML appare così

{{< highlight java >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Come puoi vedere, l'attributo di destinazione nel link HTML sopra è **_self**. È possibile controllare questo attributo di destinazione utilizzando la proprietà [**GetLinkTargetType()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getlinktargettype/). Questa proprietà richiede l'enum [**HtmlLinkTargetType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmllinktargettype/) che ha i seguenti valori.

- HtmlLinkTargetType::Blank
- HtmlLinkTargetType::Parent
- HtmlLinkTargetType::Self
- HtmlLinkTargetType::Top

{{% /alert %}}

Il seguente codice illustra l'uso della proprietà [**GetLinkTargetType()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getlinktargettype/). Cambia il tipo di destinazione del link a **blank**. Per default, è **parent**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeTheHtmlLinkTargetType.go" >}}
