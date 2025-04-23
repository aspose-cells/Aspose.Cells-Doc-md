---  
title: Datumsangaben mit Node.js über C++ in japanische Daten umwandeln  
linktitle: Datumsangaben in japanische Datumsangaben konvertieren  
type: docs  
weight: 350  
url: /de/nodejs-cpp/convert-dates-to-japanese-dates/  
description: Erfahren Sie, wie man Gregorianische Daten mithilfe von Aspose.Cells for Node.js via C++ in japanische Daten umwandelt.  
---  

{{% alert color="primary" %}}  

Im japanischen Kalender beginnt eine neue Ära mit der Regentschaft eines neuen Kaisers. Am 1. Mai 2019 trat ein neuer Kaiser an die Macht, was das Ende der Heisei-Ära und den Beginn der Reiwa-Ära markierte.  

{{% /alert %}}  

Aspose.Cells bietet eine Möglichkeit, Gregorianische Daten in japanische Daten umzuwandeln. Während dieser Umwandlung werden auch Änderungen in der Ära berücksichtigt. Der folgende Codeausschnitt konvertiert die [Quell-Excel](90112015.xlsx) Datei mit Gregorianischen Daten in eine [Ausgabe-PDF](90112016.pdf) mit japanischen Daten, wie im Bild unten gezeigt.  

![todo:image_alt_text](convert-dates-to-japanese-dates_1.jpg)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const options = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
options.setLanguageCode(AsposeCells.CountryCode.Japan);
options.setRegion(AsposeCells.CountryCode.Japan);

const workbook = new AsposeCells.Workbook(path.join(sourceDir, "JapaneseDates.xlsx"), options);
workbook.save(outputDir + "JapaneseDates.pdf", AsposeCells.SaveFormat.Pdf);
```  

