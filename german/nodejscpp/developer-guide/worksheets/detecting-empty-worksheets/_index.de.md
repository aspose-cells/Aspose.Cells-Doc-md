---  
title: Leere Arbeitsblätter mit Node.js über C++ erkennen  
linktitle: Erkennen leerer Arbeitsblätter  
type: docs  
weight: 410  
url: /de/nodejs-cpp/detecting-empty-worksheets/  
description: Dieser Artikel zeigt Ihnen Code, der erklärt, wie Sie leere Arbeitsblätter von Excel Arbeitsmappen programmatisch mit der Node.js API und der C++ Bibliothek erkennen.  
keywords: Leeres Arbeitsblatt erkennen Node.js über C++, leeres Excel Arbeitsblatt finden Node.js über C++  
---  

## **Überprüfung auf belegte Zellen**

Arbeitsblätter können mit Werten gefüllt sein, wobei es sich um einfache Werte (Text, numerisch, Datum/Uhrzeit) oder Formeln oder formelbasierte Werte handelt. In einem solchen Fall ist es einfach zu erkennen, ob ein Arbeitsblatt leer ist oder nicht. Alles, was wir prüfen müssen, sind die Eigenschaften [**Cells.getMaxDataRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataRow--) oder [**Cells.getMaxDataColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataColumn--). Wenn die oben genannten Eigenschaften Null oder positive Werte zurückgeben, bedeutet dies, dass ein oder mehrere Zellen gefüllt wurden; wenn jedoch eine dieser Eigenschaften -1 zurückgibt, weist dies darauf hin, dass keine Zellen im angegebenen Arbeitsblatt gefüllt sind.

{{% alert color="primary" %}}

Die Sammlungen Zeilen & Spalten haben nullbasierte Indizes; daher bedeutet eine Zelle in Zeile 0 & Spalte 0 die erste Zelle im Arbeitsblatt, nämlich A1.

{{% /alert %}}

## **Überprüfung auf leere initialisierte Zellen**

Alle Zellen mit Werten werden automatisch initialisiert; es besteht jedoch die Möglichkeit, dass ein Arbeitsblatt nur Zellen mit Formatierungen enthält. In einem solchen Szenario geben die Eigenschaften [**Cells.getMaxDataRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataRow--) oder [**Cells.getMaxDataColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataColumn--) -1 zurück, was auf das Fehlen gefüllter Werte hinweist, aber initialisierte Zellen aufgrund von Zellformatierungen können mit diesem Ansatz nicht erkannt werden. Um zu prüfen, ob ein Arbeitsblatt leere initialisierte Zellen hat, wird empfohlen, die Methode `Enumerator.MoveNext` auf den von [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) gesammelten Enumerator anzuwenden. Wenn die Methode `Enumerator.MoveNext` **true** zurückgibt, bedeutet dies, dass es eine oder mehrere initialisierte Zellen im Arbeitsblatt gibt.

## **Überprüfung auf Formen**

Es ist möglich, dass ein Arbeitsblatt keine gefüllten Zellen hat; es könnte jedoch Formen & Objekte wie Steuerelemente, Diagramme, Bilder usw. enthalten. Wenn wir überprüfen möchten, ob ein Arbeitsblatt Formen enthält, können wir dies durch Inspektion der [**ShapeCollection.getCount()**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#getCount--) Eigenschaft tun. Ein positiver Wert zeigt die Anwesenheit von Formen im Arbeitsblatt an.

## **Programmierbeispiel**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const book = new AsposeCells.Workbook(filePath);

// Loop over all worksheets in the workbook
for (let i = 0; i < book.getWorksheets().getCount(); i++) {
const sheet = book.getWorksheets().get(i);
// Check if worksheet has populated cells
if (sheet.getCells().getMaxDataRow() !== -1) {
console.log(`${sheet.getName()} is not empty because one or more cells are populated`);
}
// Check if worksheet has shapes
else if (sheet.getShapes().getCount() > 0) {
console.log(`${sheet.getName()} is not empty because there are one or more shapes`);
}
// Check if worksheet has empty initialized cells
else {
const range = sheet.getCells().getMaxDisplayRange();
const rangeIterator = range.getEnumerator();
if (rangeIterator.moveNext()) {
console.log(`${sheet.getName()} is not empty because one or more cells are initialized`);
}
}
}
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
