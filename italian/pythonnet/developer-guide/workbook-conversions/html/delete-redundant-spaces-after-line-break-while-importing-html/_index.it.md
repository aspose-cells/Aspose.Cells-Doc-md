---
title: Eliminare gli spazi ridondanti dopo un interruzione di riga durante l importazione di HTML
type: docs
weight: 20
url: /it/python-net/delete-redundant-spaces-after-line-break-while-importing/
description: Questo argomento mostra come eliminare gli spazi ridondanti dopo un interruzione di riga durante l importazione di HTML utilizzando Aspose.Cells for Python via NET.
keywords: Elimina gli spazi ridondanti dopo un interruzione di riga durante l importazione di HTML, elimina gli spazi ridondanti per l importazione di HTML.
---

{{% alert color="primary" %}}

Utilizzare la proprietà [**HTMLLoadOptions.delete_redundant_spaces**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/delete_redundant_spaces/) e impostarla su **true** per eliminare tutti gli spazi ridondanti che seguono il tag di interruzione di riga. Per impostazione predefinita, questa proprietà è **false** e gli spazi ridondanti vengono conservati nei file excel di output.

{{% /alert %}}

## Effetto di impostare la proprietà HTMLLoadOptions.delete_redundant_spaces su false e true

Nella seguente schermata è mostrato l'effetto dell'impostazione di questa proprietà su **false** e **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## Eliminare gli spazi ridondanti dopo l'interruzione di riga durante l'importazione di HTML

### Esempio di programmazione

Il seguente codice di esempio mostra l'uso della proprietà [**HTMLLoadOptions.delete_redundant_spaces**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/delete_redundant_spaces/). Si prega di impostarla su **true** o **false** per ottenere l'output mostrato nella schermata sopra.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-DeleteRedundantSpacesWhileImportingFromHtml-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
