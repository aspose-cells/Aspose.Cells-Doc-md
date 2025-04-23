---
title: Arbeitsblätter innerhalb und zwischen Arbeitsmappen kopieren und verschieben mit Node.js via C++
linktitle: Arbeitsblätter innerhalb und zwischen Arbeitsmappen kopieren und verschieben
type: docs
weight: 80
url: /de/nodejs-cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: Erfahren Sie, wie Sie Arbeitsblätter innerhalb und zwischen Arbeitsmappen mit Aspose.Cells for Node.js via C++ kopieren und verschieben. Effizientes Management Ihrer Arbeitsmappestrukturen.
---

{{% alert color="primary" %}}

Manchmal benötigen Sie eine Anzahl von Arbeitsblättern mit gemeinsamer Formatierung und Dateneingabe. Wenn Sie z.B. mit Quartalsbudgets arbeiten, möchten Sie möglicherweise eine Arbeitsmappe mit Blättern erstellen, die dieselben Spaltenüberschriften, Zeilenüberschriften und Formeln enthalten. Es gibt eine Möglichkeit, dies zu tun: indem Sie ein Blatt erstellen und es dann dreimal kopieren.

Aspose.Cells for Node.js via C++ unterstützt das Kopieren oder Verschieben von Arbeitsblättern innerhalb oder zwischen Arbeitsmappen. Arbeitsblätter einschließlich Daten, Formatierungen, Tabellen, Matrizen, Diagrammen, Bildern und anderen Objekten werden mit höchster Präzision kopiert.

{{% /alert %}}

## **Arbeitsblätter kopieren und verschieben**

### **Ein Arbeitsblatt innerhalb einer Arbeitsmappe kopieren**

Die Anfangsschritte sind für alle Beispiele gleich.

1. Erstellen Sie zwei Arbeitsmappen mit einigen Daten in Microsoft Excel. Für dieses Beispiel haben wir zwei neue Arbeitsmappen in Microsoft Excel erstellt und einige Daten in die Arbeitsblätter eingegeben.

- FirstWorkbook.xlsx (3 Tabellenblätter).
- SecondWorkbook.xlsx (1 Tabellenblatt).

1. Laden Sie Aspose.Cells herunter und installieren Sie es:
   1. [Laden Sie Aspose.Cells for Node.js via C++ herunter](https://downloads.aspose.com/cells/nodejs-cpp).
   1. Installieren Sie es auf Ihrem Entwicklungscomputer.
      Alle [Aspose](http://www.aspose.com/) Komponenten funktionieren nach der Installation im Evaluierungsmodus. Der Evaluierungsmodus hat kein Zeitlimit und fügt nur Wasserzeichen in erstellte Dokumente ein.
1. Ein Projekt erstellen:
   1. Starten Sie Ihre Entwicklungsumgebung.
   1. Erstellen Sie eine neue Konsolenanwendung.
1. Fügen Sie Verweise hinzu:
   1. Fügen Sie dem Projekt einen Verweis auf Aspose.Cells hinzu.
      Fügen Sie beispielsweise eine Referenz zu ...\Program Files\Aspose\Aspose.Cells\Bin\NodeJs\Aspose.Cells.dll hinzu
1. Kopieren Sie das Tabellenblatt innerhalb einer Arbeitsmappe.
   Das erste Beispiel kopiert das erste Tabellenblatt (Kopie) innerhalb von FirstWorkbook.xlsx.

Beim Ausführen des Codes wird das Arbeitsblatt namens Kopie innerhalb von FirstWorkbook.xlsx mit dem Namen Last Sheet kopiert.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open a file into the first book.
const excelWorkbook1 = new AsposeCells.Workbook(path.join(dataDir, "FirstWorkbook.xlsx"));

// Copy the first sheet of the first book within the workbook
excelWorkbook1.getWorksheets().get(2).copy(excelWorkbook1.getWorksheets().get("Copy"));

// Save the file.
excelWorkbook1.save(path.join(dataDir, "FirstWorkbookCopied_out.xlsx"));
```

### **Verschieben eines Arbeitsblatts innerhalb eines Arbeitsmappes**

Der untenstehende Code zeigt, wie man ein Arbeitsblatt von einer Position in einer Arbeitsmappe an eine andere verschiebt. Das Ausführen des Codes verschiebt das Arbeitsblatt namens Verschieben vom Index 1 auf den Index 2 in FirstWorkbook.xlsx.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "FirstWorkbook.xlsx");
// Open a file into the first book.
const excelWorkbook2 = new AsposeCells.Workbook(filePath);

// Move the sheet
const worksheets = excelWorkbook2.getWorksheets();
const worksheet = worksheets.get(0);
worksheet.moveTo(1);

// Save the file.
excelWorkbook2.save(path.join(dataDir, "FirstWorkbookMoved_out.xlsx"));
```

### **Kopieren eines Arbeitsblatts zwischen Arbeitsmappen**

Beim Ausführen des Codes wird das Arbeitsblatt namens Copy in SecondWorkbook.xlsx mit dem Namen Sheet2 kopiert.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const excelWorkbook3 = new AsposeCells.Workbook();
const excelWorkbook4 = new AsposeCells.Workbook();

// Create source worksheet
excelWorkbook3.getWorksheets().add("Copy");

// Add new worksheet into second Workbook
excelWorkbook4.getWorksheets().add();

// Copy the first sheet of the first book into second book.
excelWorkbook4.getWorksheets().get(1).copy(excelWorkbook3.getWorksheets().get("Copy"));

// Save the file.
excelWorkbook4.save(path.join(dataDir, "CopyWorksheetsBetweenWorkbooks_out.xlsx"));
```

### **Verschieben eines Arbeitsblatts zwischen Arbeitsmappen**

Das Ausführen des Codes verschiebt das Arbeitsblatt namens Verschieben von FirstWorkbook.xlsx nach SecondWorkbook.xlsx mit dem Namen Blatt3.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create new workbooks instead of opening existing files
const excelWorkbook5 = new AsposeCells.Workbook();
const excelWorkbook6 = new AsposeCells.Workbook();

// Add New Worksheet
excelWorkbook6.getWorksheets().add();

// Copy the sheet from first book into second book.
excelWorkbook6.getWorksheets().get(0).copy(excelWorkbook5.getWorksheets().get(0));

// Remove the copied worksheet from first workbook
excelWorkbook5.getWorksheets().removeAt(0);

// Save the file.
excelWorkbook5.save(path.join(dataDir, "FirstWorkbookWithMove_out.xlsx"));

// Save the file.
excelWorkbook6.save(path.join(dataDir, "SecondWorkbookWithMove_out.xlsx"));
```
