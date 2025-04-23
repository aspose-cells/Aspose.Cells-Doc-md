---  
title: Optimierung des Speicherverbrauchs bei der Arbeit mit großen Dateien mit großen Datenmengen mit Node.js via C++  
linktitle: Optimierung des Speicherverbrauchs beim Arbeiten mit großen Dateien und großen Datensätzen  
type: docs  
weight: 180  
url: /de/nodejs-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/  
---  

{{% alert color="primary" %}}  

Beim Erstellen eines Arbeitsbuchs mit großen Datenmengen oder beim Lesen einer großen Microsoft Excel-Datei ist die gesamte RAM-Menge, die der Prozess benötigt, stets ein Thema. Es gibt Maßnahmen, die angepasst werden können, um die Herausforderung zu bewältigen. Aspose.Cells for Node.js via C++ bietet relevante Optionen und API-Aufrufe, um die Speichernutzung zu senken, zu reduzieren und zu optimieren. Es kann auch helfen, den Prozess effizienter arbeiten zu lassen und schneller auszuführen.  

Verwenden Sie die [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/)-Option, um den Speicherverbrauch für Zelleninhalte zu optimieren und die Gesamtspeicherkosten zu senken. Beim Erstellen eines großen Datensatzes für Zellen können Sie im Vergleich zur Verwendung der Standardeinstellung ([**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/)) eine bestimmte Menge Speicher einsparen.  

{{% /alert %}}  

## **Speicheroptimierung**  

### **Lesen großer Excel-Dateien**  

Das folgende Beispiel zeigt, wie eine große Microsoft Excel-Datei im optimierten Modus gelesen wird.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the LoadOptions
const opt = new AsposeCells.LoadOptions();
// Set the memory preferences
opt.setMemorySetting(AsposeCells.MemorySetting.MemoryPreference);

// Instantiate the Workbook
// Load the Big Excel file having large Data set in it
const wb = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"), opt);
```  

### **Schreiben großer Excel-Dateien**  

Das folgende Beispiel zeigt, wie Sie ein großes Datenset im optimierten Modus in ein Arbeitsblatt schreiben.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook();

// Set the memory preferences
wb.getSettings().setMemorySetting(AsposeCells.MemorySetting.MemoryPreference);

// Note: The memory settings also would not work for the default sheet i.e., "Sheet1" etc. automatically created by the Workbook

// To change the memory setting of existing sheets, please change memory setting for them manually:
let cells = wb.getWorksheets().get(0).getCells();
cells.setMemorySetting(AsposeCells.MemorySetting.MemoryPreference);

// Input large dataset into the cells of the worksheet.
// Your code goes here.
// .........

// Get cells of the newly created Worksheet "Sheet2" whose memory setting is same with the one defined in WorkbookSettings:
cells = wb.getWorksheets().add("Sheet2").getCells();
// .........
// Input large dataset into the cells of the worksheet.
// Your code goes here.
// .........
```  

## **Vorsicht**  

Die Standardeinstellung, [**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/), wird für alle Versionen angewandt. Für einige Situationen, z.B. beim Erstellen eines Arbeitsbuchs mit großen Daten für Zellen, kann die [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/)-Option den Speicherverbrauch optimieren und die Speicher kosten für die Anwendung verringern. Diese Option kann jedoch die Leistung in einigen Fällen beeinträchtigen, wie folgt.  

1. **Zugriff auf Zellen zufällig und wiederholt**: Die effizienteste Reihenfolge für den Zugriff auf die Zellenkollektion ist Zelle für Zelle in einer Zeile, dann Zeile für Zeile. Besonders wenn Sie Zeilen/Zellen über den Enumeratoren aus [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells), [**RowCollection**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection), und [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row) zugreifen, maximiert sich die Leistung mit [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/).  
2. **Einfügen & Löschen von Zellen & Zeilen**: Bitte beachten Sie, dass bei vielen Einfüge-/Löschoperationen für Zellen/Zeilen die Leistungsverringerung im Modus *MemoryPreference* im Vergleich zum *Normal*-Modus deutlich sein wird.  
3. **Arbeiten mit verschiedenen Zelltypen**: Wenn die meisten Zellen Textwerte oder Formeln enthalten, sind die Speicher Kosten wie im *Normal*-Modus. Wenn jedoch viele leere Zellen oder Zellwerte numerisch, boolesch usw. sind, wird die [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/)-Option eine bessere Leistung bieten.  

