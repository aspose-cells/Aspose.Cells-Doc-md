---
title: Bilder aus Arbeitsblättern mit ImageOrPrintOptions in Node.js via C++ extrahieren
linktitle: Bilder aus Arbeitsblättern mit ImageOrPrintOptions extrahieren
type: docs
weight: 140
url: /de/nodejs-cpp/extract-images-from-worksheets-using-imageorprintoptions/
description: Erfahren Sie, wie Sie Bilder aus Excel Arbeitsblättern extrahieren und mit Aspose.Cells for Node.js via C++ speichern.
---

{{% alert color="primary" %}} 

Microsoft Excel-Benutzer können Bilder zu Tabellen hinzufügen. Mit Aspose.Cells for Node.js via C++ ist es möglich, Bilder aus Microsoft Excel-Dateien zu lesen und auf einem lokalen Laufwerk zu speichern. Dieser Artikel zeigt, wie.

{{% /alert %}} 

Der nachstehende Beispielscode zeigt, wie Bilder aus einer Excel-Datei extrahiert und gespeichert werden können.



```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open a template Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleExtractImagesFromWorksheets.xlsx"));

// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get the first Picture in the first worksheet
const pic = worksheet.getPictures().get(0);

// Set the output image file path
const picformat = pic.getImageType().toString();

// Note: you may evaluate the image format before specifying the image path
// Define ImageOrPrintOptions
const printoption = new AsposeCells.ImageOrPrintOptions();

// Specify the image format
printoption.setImageType(AsposeCells.ImageType.Jpeg);

// Save the image
pic.toImage(path.join(outputDir, "outputExtractImagesFromWorksheets.jpg"), printoption);
```
