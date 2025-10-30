---
title: Löschen Sie redundante Leerzeichen nach Zeilenumbruch beim Importieren von HTML mit Golang über C++
linktitle: Überflüssige Leerzeichen nach Zeilenumbruch beim Importieren von HTML löschen
type: docs
weight: 20
url: /de/go-cpp/delete-redundant-spaces-after-line-break-while-importing/
description: Erfahren Sie, wie Sie redundante Leerzeichen nach Zeilenumbrüchen beim Importieren von HTML mit Aspose.Cells for C++ entfernen.
---

{{% alert color="primary" %}}

Bitte verwenden Sie die Eigenschaft [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getdeleteredundantspaces/) und setzen Sie sie **true**, um alle redundanten Leerzeichen nach dem Zeilenumbruch-Tag zu löschen. Standardmäßig ist diese Eigenschaft **false**, und redundante Leerzeichen bleiben im Ausgabedokument erhalten.

{{% /alert %}}

## Wirkung der Einstellung der HTMLLoadOptions.DeleteRedundantSpaces-Eigenschaft auf falsch und wahr

Der folgende Screenshot zeigt den Effekt der Einstellung dieser Eigenschaft auf false und true.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## Löschen Sie überflüssige Leerzeichen nach Zeilenumbruch beim Importieren von HTML

### Programmierbeispiel

Das folgende Beispiel zeigt die Verwendung der [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getdeleteredundantspaces/)-Eigenschaft. Bitte setzen Sie sie auf **true** oder **false**, um die Ausgabe wie im obigen Screenshot zu erhalten.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteRedundantSpacesAfterLineBreakWhileImportingHtml.go" >}}
