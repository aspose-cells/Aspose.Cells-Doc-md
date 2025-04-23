---
title: Festlegung der ScaleCrop und LinksUpToDate Eigenschaften der integrierten Dokumenteigenschaften
type: docs
weight: 320
url: /de/python-net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---

## **Mögliche Verwendungsszenarien**
[scale_crop](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/scale_crop) und [links_up_to_date](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/links_up_to_date) sind zwei erweiterte integrierte Dokumenteigenschaften, die im OpenXml-Format definiert sind. Der Zweck dieser Eigenschaften ist folgender
## **1) ScaleCrop**
Dieses Element zeigt den Anzeigemodus der Dokumentminiaturansicht an. Setzen Sie dieses Element auf **TRUE**, um das Skalieren der Dokumentminiaturansicht zu ermöglichen. Setzen Sie dieses Element auf **FALSE**, um das Beschränken der Dokumentminiatur auf die Anzeige nur von Abschnitten, die in die Anzeige passen, zu ermöglichen.

Die möglichen Werte für dieses Element sind durch den Datentyp boolean des W3C XML-Schemas definiert.
## **2) LinksUpToDate**
Dieses Element zeigt an, ob Hyperlinks in einem Dokument aktuell sind. Setzen Sie dieses Element auf **TRUE**, um anzuzeigen, dass die Hyperlinks aktualisiert sind. Setzen Sie dieses Element auf **FALSE**, um anzuzeigen, dass die Hyperlinks veraltet sind.

Die möglichen Werte für dieses Element sind durch den Datentyp boolean des W3C XML-Schemas definiert.
## **Screenshot, der diese Eigenschaften in der app.xml-Datei zeigt**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **Festlegen der Eigenschaften ScaleCrop und LinksUpToDate der integrierten Dokumenteigenschaften**
Das folgende Beispiel setzt die erweiterten integrierten Dokumenteigenschaften [scale_crop](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/scale_crop) und [links_up_to_date](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/links_up_to_date) des Arbeitsbuchs. Bitte überprüfen Sie die erzeugte [Excel-Ausgabedatei](5115500.xlsx), ändern Sie die Erweiterung zu .zip und entpacken Sie ihre Inhalte, um in app.xml wie oben im Screenshot gezeigt zu sehen.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-SettingScaleCropAndLinksUpToDateProperties.py" >}}
