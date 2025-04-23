---
title: Header oder Footer mit Node.js via C++ abrufen
linktitle: Header oder Footer erhalten
type: docs
weight: 30
url: /de/nodejs-cpp/get-headers-or-footers/
description: Dieser Artikel erklärt, wie man programmatisch Header und Footer aus Excel oder OpenOffice Dateien mit der Node.js via C++ API abrufen kann.
---

{{% alert color="primary" %}}

Header und Fußzeilen werden nur in der Seitenlayoutansicht, der Druckvorschau und auf gedruckten Seiten angezeigt. 

Sie können auch das Dialogfeld Seitenlayout verwenden, wenn Sie Header oder Footer für mehr als ein Arbeitsblatt gleichzeitig anzeigen möchten. 

Für andere Blatttypen wie Diagrammblätter oder Diagramme können Header und Fußzeilen nur über das Dialogfeld Seitenlayout eingefügt werden.

{{% /alert %}}

## **Header und Fußzeilen in MS Excel erhalten**
1. Klicken Sie auf das Arbeitsblatt, auf dem Sie Header oder Footer anzeigen bzw. ändern möchten.
2. Klicken Sie auf der Ansicht-Registerkarte in der Gruppe Arbeitsblattansichten auf Seitenlayout.
   Excel zeigt das Arbeitsblatt in der Seitenlayoutansicht an.
3. Klicken Sie zum Anzeigen oder Bearbeiten eines Headers oder Footers auf die linke, mittlere oder rechte Kopf- oder Fußzeile am oberen oder unteren Rand der Arbeitsblattseite (unter Kopfzeile oder über Fußzeile).


## **Headers und Footers mit Aspose.Cells for Node.js via C++ abrufen**
Mit den Methoden [**PageSetup.getHeader(number)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getHeader-number-) und [**PageSetup.getFooter(number)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFooter-number-) können Node.js-Entwickler Header oder Footer aus der Datei einfach abrufen.

1. Erstellen Sie eine Arbeitsmappe, um die Datei zu öffnen.
2. Holen Sie sich das Arbeitsblatt, auf dem Sie Header oder Footer abrufen möchten.
3. Holen Sie sich den Header oder Footer mit einer bestimmten Abschnitts-ID.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "HeaderFooter.xlsx");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Gets left section of header
console.log(sheet.getPageSetup().getHeader(0));
// Gets center section of header
console.log(sheet.getPageSetup().getHeader(1));
// Gets right section of header
console.log(sheet.getPageSetup().getHeader(2));
// Gets center section of footer
console.log(sheet.getPageSetup().getFooter(1));
```

## **Kopf- und Fußzeilen zu Befehlsliste parsen**
Der Header- oder Footer-Text kann spezielle Befehle enthalten, z.B. einen Platzhalter für die Seitenzahl, das aktuelle Datum oder Textformatierungsattribute.

Spezialbefehle werden durch einen einzelnen Buchstaben mit einem vorangestellten Und-Zeichen ("&") dargestellt.

Die Header- und Footer-Strings werden unter Verwendung der ABNF-Grammatik aufgebaut. Ohne Viewer ist es schwer verständlich.

Aspose.Cells for Node.js via C++ bietet [**PageSetup.getCommands(string)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getCommands-string-) Methode, um Header und Footer als Befehlsliste zu parsen.

Die folgenden Codes zeigen, wie man den Header oder Footer als Befehlsliste parst und Befehle verarbeitet:

```javascript
try {
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "HeaderFooter.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Gets left section of header
const headerSection = sheet.getPageSetup().getHeader(0);
const commands = sheet.getPageSetup().getCommands(headerSection) || [];

commands.forEach(c => {
switch (c.getType()) {
case AsposeCells.HeaderFooterCommandType.SheetName:
// embedded the name of the sheet to header or footer
break;
}
```
