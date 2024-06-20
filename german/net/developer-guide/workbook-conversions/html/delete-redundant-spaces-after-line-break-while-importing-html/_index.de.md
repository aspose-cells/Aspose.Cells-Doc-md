---
title: Überflüssige Leerzeichen nach Zeilenumbruch beim Importieren von HTML löschen
type: docs
weight: 20
url: /de/net/delete-redundant-spaces-after-line-break-while-importing/
---

{{% alert color="primary" %}}

Bitte verwenden Sie die Eigenschaft [**HTMLLoadOptions.DeleteRedundantSpaces**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/deleteredundantspaces) und setzen Sie sie auf **true**, um alle überflüssigen Leerzeichen nach dem Zeilenumbruch-Tag zu löschen. Standardmäßig ist diese Eigenschaft **false** und überflüssige Leerzeichen werden in den Ausgabe-Excel-Dateien beibehalten.

{{% /alert %}}

## Wirkung der Einstellung der HTMLLoadOptions.DeleteRedundantSpaces-Eigenschaft auf falsch und wahr

Der folgende Screenshot zeigt den Effekt der Einstellung dieser Eigenschaft auf false und true.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## Löschen Sie überflüssige Leerzeichen nach Zeilenumbruch beim Importieren von HTML

### Programmierbeispiel

Das folgende Beispiel zeigt die Verwendung der [**HTMLLoadOptions.DeleteRedundantSpaces**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/deleteredundantspaces)-Eigenschaft. Bitte setzen Sie sie auf **true** oder **false**, um die Ausgabe wie im obigen Screenshot zu erhalten.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteRedundantSpacesWhileImportingFromHtml-1.cs" >}}
