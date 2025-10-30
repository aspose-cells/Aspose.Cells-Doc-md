---
title: Überflüssige Leerzeichen nach Zeilenumbruch beim Importieren von HTML löschen
type: docs
weight: 20
url: /de/python-net/delete-redundant-spaces-after-line-break-while-importing/
description: Dieses Thema zeigt Ihnen, wie Sie überflüssige Leerzeichen nach einem Zeilenumbruch beim Importieren von HTML mithilfe von Aspose.Cells für Python via NET löschen können.
keywords: Löschen Sie überflüssige Leerzeichen nach einem Zeilenumbruch beim Importieren von HTML, Löschen Sie überflüssige Leerzeichen beim Importieren von HTML.
---

{{% alert color="primary" %}}

Bitte verwenden Sie die Eigenschaft [**HTMLLoadOptions.delete_redundant_spaces**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/delete_redundant_spaces/) und setzen Sie sie auf **true**, um alle überflüssigen Leerzeichen nach dem Zeilenumbruch-Tag zu löschen. Standardmäßig ist diese Eigenschaft **false** und überflüssige Leerzeichen werden in den Ausgabe-Excel-Dateien beibehalten.

{{% /alert %}}

## Auswirkung der Einstellung der Eigenschaft HTMLLoadOptions.delete_redundant_spaces auf false und true

Der folgende Screenshot zeigt den Effekt der Einstellung dieser Eigenschaft auf false und true.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## Löschen Sie überflüssige Leerzeichen nach Zeilenumbruch beim Importieren von HTML

### Programmierbeispiel

Das folgende Beispiel zeigt die Verwendung der [**HTMLLoadOptions.delete_redundant_spaces**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlloadoptions/delete_redundant_spaces/)-Eigenschaft. Bitte setzen Sie sie auf **true** oder **false**, um die Ausgabe wie im obigen Screenshot zu erhalten.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-DeleteRedundantSpacesWhileImportingFromHtml-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
