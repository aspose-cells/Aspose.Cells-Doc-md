---
title: Festlegung der ScaleCrop und LinksUpToDate Eigenschaften der integrierten Dokumenteigenschaften
type: docs
weight: 320
url: /de/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---

## **Mögliche Verwendungsszenarien**
[ScaleCrop](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/scalecrop) und [LinksUpToDate](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/linksuptodate) sind zwei erweiterte integrierte Dokumenteigenschaften, die im OpenXml-Format definiert sind. Der Zweck dieser Eigenschaften ist folgender
## **1) ScaleCrop**
Dieses Element zeigt den Anzeigemodus der Dokumentminiaturansicht an. Setzen Sie dieses Element auf **TRUE**, um das Skalieren der Dokumentminiaturansicht zu ermöglichen. Setzen Sie dieses Element auf **FALSE**, um das Beschränken der Dokumentminiatur auf die Anzeige nur von Abschnitten, die in die Anzeige passen, zu ermöglichen.

Die möglichen Werte für dieses Element sind durch den Datentyp boolean des W3C XML-Schemas definiert.
## **2) LinksUpToDate**
Dieses Element zeigt an, ob Hyperlinks in einem Dokument aktuell sind. Setzen Sie dieses Element auf **TRUE**, um anzuzeigen, dass die Hyperlinks aktualisiert sind. Setzen Sie dieses Element auf **FALSE**, um anzuzeigen, dass die Hyperlinks veraltet sind.

Die möglichen Werte für dieses Element sind durch den Datentyp boolean des W3C XML-Schemas definiert.
## **Screenshot, der diese Eigenschaften in der app.xml-Datei zeigt**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **Festlegen der Eigenschaften ScaleCrop und LinksUpToDate der integrierten Dokumenteigenschaften**
Der folgende Beispielcode setzt die erweiterten integrierten Dokumenteigenschaften ScaleCrop und LinksUpToDate der Arbeitsmappe. Bitte überprüfen Sie die mit diesem Code generierte Ausgabedatei Excel-Datei, ändern Sie ihre Erweiterung in .ZIP und extrahieren Sie ihre Inhalte und sehen Sie sich die app.xml an, wie im obigen Screenshot gezeigt.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingScaleCropAndLinksUpToDateProperties.cs" >}}
