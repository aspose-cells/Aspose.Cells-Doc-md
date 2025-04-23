---  
title: Tabellen und Bereiche mit Node.js via C++  
linktitle: Tabellen und Bereiche  
type: docs  
weight: 50  
url: /de/nodejs-cpp/tables-and-ranges/  
---  

## **Einführung**  

Manchmal erstellen Sie eine Tabelle in Microsoft Excel und möchten nicht mit der Funktionalität der Tabelle arbeiten, die damit verbunden ist. Stattdessen möchten Sie etwas, das wie eine Tabelle aussieht. Um Daten in einer Tabelle zu behalten, ohne das Format zu verlieren, konvertieren Sie die Tabelle in einen regulären Datenbereich.  
Aspose.Cells unterstützt diese Funktion von Microsoft Excel für Tabellen und Listenobjekte.  

## **Verwendung von Microsoft Excel**  

Verwenden Sie die **In Bereich konvertieren** -Funktion, um eine Tabelle ohne Formatierung schnell in einen Bereich zu konvertieren. In Microsoft Excel 2007/2010:  

1. Klicken Sie irgendwo in der Tabelle, um sicherzustellen, dass die aktive Zelle in einer Tabellenspalte liegt.  
1. Auf dem Register **Entwurf** klicken Sie in der Gruppe **Tools** auf **In Bereich konvertieren**.  

## **Verwendung von Aspose.Cells**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "table_ranges.xlsx");

// Open an existing file that contains a table/list object in it
const wb = new AsposeCells.Workbook(filePath);

// Convert the first table/list object (from the first worksheet) to normal range
wb.getWorksheets().get(0).getListObjects().get(0).convertToRange();

// Save the file
wb.save(path.join(dataDir, "output.xlsx"));
```  

{{% alert color="primary" %}}  

Die Tabellenfunktionen sind nicht mehr verfügbar, nachdem die Tabelle in einen Bereich konvertiert wurde. Beispielsweise enthalten die Zeilenüberschriften nicht mehr die Sortier- und Filterpfeile, und strukturierte Verweise (Verweise, die Tabellennamen verwenden), die in Formeln verwendet wurden, werden in normale Zellverweise umgewandelt.  

{{% /alert %}}  

## **Tabelle mit Optionen in Bereich konvertieren**  

Aspose.Cells bietet zusätzliche Optionen beim Konvertieren einer Tabelle in einen Bereich durch die Klasse [**TableToRangeOptions**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/). Die Klasse [**TableToRangeOptions**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/) bietet die Eigenschaft [**getLastRow()**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/#getLastRow--), die es Ihnen ermöglicht, den letzten Index der Tabellenzeile festzulegen. Die Tabellenformatierung wird bis zum angegebenen Zeilenindex beibehalten und der Rest der Formatierung wird entfernt.  

Der unten angegebene Beispielcode zeigt die Verwendung der Klasse [**TableToRangeOptions**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "table_ranges.xlsx");
// Open an existing file that contains a table/list object in it
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.TableToRangeOptions();
options.setLastRow(5);

// Convert the first table/list object (from the first worksheet) to normal range
workbook.getWorksheets().get(0).getListObjects().get(0).convertToRange(options);

// Save the file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

