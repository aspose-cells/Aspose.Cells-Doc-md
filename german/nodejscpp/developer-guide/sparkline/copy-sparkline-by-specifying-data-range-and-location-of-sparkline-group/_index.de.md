---  
title: Kopieren Sie Sparkline durch Angabe des Datenbereichs und des Standorts der Sparkline Gruppe mit Node.js über C++  
linktitle: Sparkline kopieren durch Festlegen des Datenbereichs und des Speicherorts der Sparkline Gruppe  
type: docs  
weight: 300  
url: /de/nodejs-cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/  
description: Erfahren Sie, wie Sie eine Sparkline in Excel kopieren, indem Sie Datenbereich und Standort der Sparkline Gruppe mit Aspose.Cells for Node.js via C++ angeben.  
---  

{{% alert color="primary" %}}  
Microsoft Excel ermöglicht es Ihnen, eine Sparkline zu kopieren, indem Sie den Datenbereich und den Speicherort einer Sparkline-Gruppe angeben. Aspose.Cells unterstützt diese Funktion.  
{{% /alert %}}  

Um eine Sparkline in andere Zellen in Microsoft Excel zu kopieren:  

1. Wählen Sie die Zelle aus, die die Sparkline enthält.  
1. Wählen Sie **Daten bearbeiten** im **Sparkline**-Abschnitt des **Entwurfs**-Registers aus.  
1. Wählen Sie **Gruppenposition & Daten bearbeiten** aus.  
1. Geben Sie den Datenbereich und den Speicherort an.  
1. Klicken Sie auf **OK**.  

Aspose.Cells bietet die `SparklineCollection.add(dataRange, row, column)`-Methode, um einen Datenbereich und einen Standort für eine Sparkline-Gruppe festzulegen. Der folgende Beispielcode lädt die Quelldatei Excel wie im Screenshot oben, greift auf die erste Sparkline-Gruppe zu und fügt Datenbereiche und Standorte in die Sparkline-Gruppe ein. Schließlich schreibt er die Ausgabedatei auf die Festplatte, die auch im Screenshot oben zu sehen ist.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "copy_sparkline.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first sparkline group
const group = worksheet.getSparklineGroups().get(0);

// Add Data Ranges and Locations inside this sparkline group
group.getSparklines().add("Sheet1!D5:O5", 4, 15);
group.getSparklines().add("Sheet1!D6:O6", 5, 15);
group.getSparklines().add("Sheet1!D7:O7", 6, 15);
group.getSparklines().add("Sheet1!D8:O8", 7, 15);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

