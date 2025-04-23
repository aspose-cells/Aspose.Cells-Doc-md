---
title: Lås eller lås upp figurer med Node.js via C++
linktitle: Lås eller lås upp figurer
type: docs
weight: 200
url: /sv/nodejs-cpp/lock-or-unlock-shapes/
description: Detta avsnitt visar kod som förklarar hur man låser eller låser upp figurer för att skydda dem med Aspose.Cells biblioteket för Node.js via C++.
keywords: Node.js Lås figurer för att skydda dem, hur man låser eller låser upp figurer med Node.js via C++, Lås eller lås upp figurer för att skydda dem i Node.js via C++.
---

## **Möjliga användningsscenario**

Ibland behöver du skydda alla figurer i vissa arbetsblad för att förhindra att de förstörs av oönskade situationer. I så fall måste du låsa alla figurer i det angivna arbetsbladet. 

Att låsa figurer i ett kalkylblad eller dokument kan vara fördelaktigt av flera skäl:
1. Förhindra oavsiktliga ändringar: Att låsa figurer säkerställer att de inte oavsiktligt flyttas, resizeas eller tas bort av användare. Detta är särskilt viktigt i komplexa dokument där figurer kan användas för anteckningar, illustrationer eller som en del av dokumentets design.
1. Bibehåll layout och design: Figurer är ofta avgörande för ett dokuments layout och visuella design. Att låsa dem bevarar det avsedda utseendet, vilket säkerställer att dokumentet förblir professionellt och visuellt tilltalande.
1. Dataintegritet: I kalkylblad kan figurer användas för att markera viktiga datapunkter, lägga till kommentarer eller ge visuella förklaringar. Att låsa dessa figurer säkerställer att den kontextuella information de ger är korrekt och intakt.
1. Konsistens i delade dokument: När man samarbetar om dokument kan olika användare ha varierande nivåer av expertis. Att låsa figurer hjälper till att upprätthålla konsekvensen i hela dokumentet genom att förhindra oavsiktliga ändringar.
1. Säkerhet: I känsliga dokument kan låsta figurer vara en del av en bredare strategi för att skydda information. Till exempel kan låsta figurer användas för att skydda specifika anteckningar eller markeringar som ger kritisk kontext.

Ibland behöver du kunna modifiera vissa figurer i vissa skyddade kalkylblad, i vilket fall du behöver låsa upp dessa figurer. Denna artikel kommer att introducera i detalj hur man låser och låser upp angivna figurer.

## **Hur man låser figurer för att skydda dem i Excel**

Så här låser du celler i Microsoft Excel:

1. Öppna din Excel-fil: Öppna Excel-filen som innehåller figurerna du vill låsa.

1. Välj figuren: Klicka på figuren du vill låsa. Du kan också välja flera figurer genom att hålla nere Ctrl-tangenten och klicka på varje figur.

1. Öppna Fomateringspanelen för figur: Högerklicka på den valda figuren eller figurerna och välj "Storlek och egenskaper." Alternativt kan du gå till "Formatera"-fliken på menyfliksområdet och i "Storlek"-gruppen klicka på dialogikonen för att öppna "Formatera figur"-panelen.
1. Lås figuren: I "Formatera figur"-panelen, gå till fliken "Storlek & Egenskaper" (ikonen ser ut som en kvadrat med pilar). Under avsnittet "Egenskaper", bocka i rutan för "Låst."
<br>
<img src="1.png" width=60% />
1. Skydda arket: Gå till "Granska"-fliken på menyfliksområdet. Klicka på "Skydda blad." Ange ett lösenord (valfritt) och välj de behörigheter du vill tillåta (t.ex. välja låsta celler, formatera celler etc.). Klicka på "OK."
<br>
<img src="2.png" width=60% />

## **Hur man låser alla figurer i ett specifikt ark**

För att skydda alla former i ett specificerat kalkblad, använd metoden `worksheet.protect(ProtectionType.Objects)`, som visas i följande exempel.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const text = "This is a test";
const worksheet = workbook.getWorksheets().get(0);

let shape = worksheet.getShapes().addTextBox(1, 0, 1, 0, 30, 100);
shape.setText(text);

shape = worksheet.getShapes().addRectangle(5, 0, 1, 0, 30, 100);
shape.setText(text);

shape = worksheet.getShapes().addButton(9, 0, 1, 0, 30, 100);
shape.setText(text);

shape = worksheet.getShapes().addOval(13, 0, 1, 0, 50, 100);
shape.setText(text);

// Protect all shapes in a specified worksheet 
shape.getWorksheet().protect(AsposeCells.ProtectionType.Objects); // Protects the entire worksheet.
// or shape.getWorksheet().protect(AsposeCells.ProtectionType.All); // Protects all shapes in the specified worksheet.
// or worksheet.protect(AsposeCells.ProtectionType.Objects); // Protects the entire worksheet.
// or worksheet.protect(AsposeCells.ProtectionType.All); // Protects all shapes in the specified worksheet.

workbook.save("Locked.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Hur man låser upp angivna figurer i ett skyddat arbetsblad**

För att låsa upp en specificerad form i ett skyddat kalkblad, använd `shape.isLocked`, som visas i följande exempel.

Notering: `shape.isLocked` är meningsfullt endast när kalkbladet är skyddat.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Locked.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get protected worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get the specified shape to be unlocked
const shape = worksheet.getShapes().get("TextBox 1");

// Unlock the specified shape
if (!worksheet.getProtection().getAllowEditingObject() && shape.isLocked()) {
shape.setIsLocked(false);
}

workbook.save("UnLocked.xlsx", AsposeCells.SaveFormat.Xlsx);
```

