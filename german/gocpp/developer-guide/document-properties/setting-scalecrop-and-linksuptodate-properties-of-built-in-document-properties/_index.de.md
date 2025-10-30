---
title: Einstellung der Properties ScaleCrop und LinksUpToDate der integrierten Dokumenteigenschaften mit Golang über C++
linktitle: Einstellungen der Properties ScaleCrop und LinksUpToDate
type: docs
weight: 320
url: /de/go-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: Erfahren Sie, wie Sie die Properties ScaleCrop und LinksUpToDate der integrierten Dokumenteigenschaften in Aspose.Cells for C++ festlegen.
---

## **Mögliche Verwendungsszenarien**
 [GetScaleCrop()](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getscalecrop/) und [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) sind zwei erweiterte integrierte Dokumenteigenschaften, die im OpenXml-Format definiert sind. Der Zweck dieser Eigenschaften ist wie folgt:

## **1) ScaleCrop**
Dieses Element zeigt den Anzeigemodus der Dokumentminiaturansicht an. Setzen Sie dieses Element auf **TRUE**, um das Skalieren der Dokumentminiaturansicht zu ermöglichen. Setzen Sie dieses Element auf **FALSE**, um das Beschränken der Dokumentminiatur auf die Anzeige nur von Abschnitten, die in die Anzeige passen, zu ermöglichen.

Die möglichen Werte für dieses Element sind durch den Datentyp boolean des W3C XML-Schemas definiert.

## **2) LinksUpToDate**
Dieses Element zeigt an, ob Hyperlinks in einem Dokument aktuell sind. Setzen Sie dieses Element auf **TRUE**, um anzuzeigen, dass die Hyperlinks aktualisiert sind. Setzen Sie dieses Element auf **FALSE**, um anzuzeigen, dass die Hyperlinks veraltet sind.

Die möglichen Werte für dieses Element sind durch den Datentyp boolean des W3C XML-Schemas definiert.

## **Screenshot, der diese Eigenschaften in der app.xml-Datei zeigt**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **Einstellungen der Properties ScaleCrop und LinksUpToDate der Integrierten Dokumenteigenschaften**
 Das folgende Beispiel setzt die erweiterten integrierten Dokumenteigenschaften [GetScaleCrop()](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getscalecrop/) und [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) des Arbeitsblatts. Bitte prüfen Sie die [Ausgabedatei im Excel-Format](5115500.xlsx), die mit diesem Code erstellt wurde, ändern Sie die Erweiterung auf .zip, extrahieren Sie den Inhalt und sehen Sie die app.xml wie im Screenshot oben gezeigt.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingScalecropAndLinksuptodatePropertiesOfBuiltInDocumentProperties.go" >}}
