---  
title: Implementieren Sie benutzerdefinierte Papiergröße des Arbeitsblatts für die Darstellung mit Node.js über C++  
linktitle: Benutzerdefinierte Papiergröße des Arbeitsblatts für die Darstellung implementieren  
type: docs  
weight: 70  
url: /de/nodejs-cpp/implement-custom-paper-size-of-worksheet-for-rendering/  
description: Dieser Artikel erklärt, wie man die Node.js API über C++ verwendet, um eine benutzerdefinierte Papiergröße für die gewünschten Arbeitsblätter beim Programmgesteuerten Exportieren einer Excel Datei in PDF Format festzulegen.  
keywords: Legen Sie eine benutzerdefinierte Papiergröße beim Exportieren von Excel nach PDF in Node.js über C++ fest  
---  

## **Mögliche Verwendungsszenarien**  

Es gibt keine direkte Option, um benutzerdefinierte Papiergrößen in MS Excel zu erstellen, jedoch können Sie beim Programmgesteuerten Exportieren einer Excel-Datei in PDF-Format eine benutzerdefinierte Papiergröße für Ihre gewünschten Arbeitsblätter festlegen. Dieses Dokument erklärt, wie man eine benutzerdefinierte Papiergröße eines Arbeitsblatts mit Aspose.Cells APIs festlegt.  

## **Benutzerdefinierte Papiergröße des Arbeitsblatts für die Darstellung implementieren**  

Aspose.Cells ermöglicht es Ihnen, die gewünschte Papiergröße des Arbeitsblatts festzulegen. Sie können die [**PageSetup.customPaperSize(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#customPaperSize-number-number-)-Methode der [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/)-Klasse verwenden, um eine benutzerdefinierte Seitengröße anzugeben. Der folgende Beispielcode zeigt, wie Sie eine benutzerdefinierte Papiergröße für das erste Arbeitsblatt im Arbeitsbuch festlegen. Bitte beachten Sie auch das [Ausgabe-PDF](45056028.pdf), das mit dem folgenden Code zur Referenz erstellt wurde.  

## **Screenshot**  

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)  

## **Beispielcode**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Set custom paper size in unit of inches
ws.getPageSetup().customPaperSize(6, 4);

// Access cell B4
const b4 = ws.getCells().get("B4");

// Add the message in cell B4
b4.putValue("Pdf Page Dimensions: 6.00 x 4.00 in");

// Save the workbook in pdf format
wb.save(path.join(dataDir, "outputCustomPaperSize.pdf"));
```  

