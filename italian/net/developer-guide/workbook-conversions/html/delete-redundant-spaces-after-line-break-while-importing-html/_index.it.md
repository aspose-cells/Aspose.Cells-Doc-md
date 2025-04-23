---
title: Eliminare gli spazi ridondanti dopo un interruzione di riga durante l importazione di HTML
type: docs
weight: 20
url: /it/net/delete-redundant-spaces-after-line-break-while-importing/
---

{{% alert color="primary" %}}

Utilizzare la proprietà [**HTMLLoadOptions.DeleteRedundantSpaces**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/deleteredundantspaces) e impostarla su **true** per eliminare tutti gli spazi ridondanti che seguono il tag di interruzione di riga. Per impostazione predefinita, questa proprietà è **false** e gli spazi ridondanti vengono conservati nei file excel di output.

{{% /alert %}}

## Effetto dell'impostazione della proprietà HTMLLoadOptions.DeleteRedundantSpaces a false e true

Nella seguente schermata è mostrato l'effetto dell'impostazione di questa proprietà su **false** e **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## Eliminare gli spazi ridondanti dopo l'interruzione di riga durante l'importazione di HTML

### Esempio di programmazione

Il seguente codice di esempio mostra l'uso della proprietà [**HTMLLoadOptions.DeleteRedundantSpaces**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/deleteredundantspaces). Si prega di impostarla su **true** o **false** per ottenere l'output mostrato nella schermata sopra.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteRedundantSpacesWhileImportingFromHtml-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
