---
title: Elimina gli spazi ridondanti dopo le interruzioni di riga durante l importazione di HTML con Golang via C++
linktitle: Eliminare gli spazi ridondanti dopo un interruzione di riga durante l importazione di HTML
type: docs
weight: 20
url: /it/go-cpp/delete-redundant-spaces-after-line-break-while-importing/
description: Impara come eliminare gli spazi ridondanti dopo le interruzioni di riga durante l importazione di HTML usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Per favore usa la proprietà [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getdeleteredundantspaces/) e impostala **true** per eliminare tutti gli spazi ridondanti che seguono il tag di interruzione di riga. Per impostazione predefinita, questa proprietà è **false** e gli spazi ridondanti vengono preservati nei file Excel di output.

{{% /alert %}}

## Effetto dell'impostazione della proprietà HTMLLoadOptions.DeleteRedundantSpaces a false e true

Nella seguente schermata è mostrato l'effetto dell'impostazione di questa proprietà su **false** e **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## Eliminare gli spazi ridondanti dopo l'interruzione di riga durante l'importazione di HTML

### Esempio di programmazione

Il seguente codice di esempio mostra l'uso della proprietà [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getdeleteredundantspaces/). Si prega di impostarla su **true** o **false** per ottenere l'output mostrato nella schermata sopra.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteRedundantSpacesAfterLineBreakWhileImportingHtml.go" >}}
