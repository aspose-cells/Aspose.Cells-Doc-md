---
title: Einstellen der ScaleCrop und LinksUpToDate Eigenschaften der eingebauten Dokumenteigenschaften mit Node.js via C++
linktitle: Festlegung der ScaleCrop und LinksUpToDate Eigenschaften der integrierten Dokumenteigenschaften
type: docs
weight: 320
url: /de/nodejs-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: Erfahren Sie, wie Sie die Eigenschaften ScaleCrop und LinksUpToDate der eingebauten Dokumenteigenschaften mit Aspose.Cells for Node.js via C++ setzen.
---

## **Mögliche Verwendungsszenarien**
[BuiltInDocumentPropertyCollection.getScaleCrop()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getScaleCrop--) und [BuiltInDocumentPropertyCollection.getLinksUpToDate()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLinksUpToDate--) sind zwei erweiterte eingebaute Dokumenteigenschaften, die im OpenXml-Format definiert sind. Der Zweck dieser Eigenschaften ist folgendes.

## **1) ScaleCrop**
Dieses Element zeigt den Anzeigemodus der Dokumentminiaturansicht an. Setzen Sie dieses Element auf **TRUE**, um das Skalieren der Dokumentminiaturansicht zu ermöglichen. Setzen Sie dieses Element auf **FALSE**, um das Beschränken der Dokumentminiatur auf die Anzeige nur von Abschnitten, die in die Anzeige passen, zu ermöglichen.

Die möglichen Werte für dieses Element sind durch den Datentyp boolean des W3C XML-Schemas definiert.

## **2) LinksUpToDate**
Dieses Element zeigt an, ob Hyperlinks in einem Dokument aktuell sind. Setzen Sie dieses Element auf **TRUE**, um anzuzeigen, dass die Hyperlinks aktualisiert sind. Setzen Sie dieses Element auf **FALSE**, um anzuzeigen, dass die Hyperlinks veraltet sind.

Die möglichen Werte für dieses Element sind durch den Datentyp boolean des W3C XML-Schemas definiert.

## **Screenshot, der diese Eigenschaften in der app.xml-Datei zeigt**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **Festlegen der Eigenschaften ScaleCrop und LinksUpToDate der integrierten Dokumenteigenschaften**
Der folgende Beispielcode setzt die erweiterten eingebauten Dokumenteigenschaften [BuiltInDocumentPropertyCollection.getScaleCrop()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getScaleCrop--) und [BuiltInDocumentPropertyCollection.getLinksUpToDate()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLinksUpToDate--) des Arbeitsblatts. Bitte prüfen Sie die [Ausgabedatei](5115500.xlsx), die mit diesem Code generiert wurde. Ändern Sie die Erweiterung in .zip, extrahieren Sie den Inhalt und öffnen Sie app.xml wie im obigen Screenshot gezeigt.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object.
const workbook = new AsposeCells.Workbook();

// Setting ScaleCrop and LinksUpToDate BuiltIn Document Properties.
workbook.getBuiltInDocumentProperties().getScaleCrop(true);
workbook.getBuiltInDocumentProperties().setLinksUpToDate(true);

// Saving the Excel file.
workbook.save(path.join(dataDir, "output.xls"), AsposeCells.SaveFormat.Auto);
```
