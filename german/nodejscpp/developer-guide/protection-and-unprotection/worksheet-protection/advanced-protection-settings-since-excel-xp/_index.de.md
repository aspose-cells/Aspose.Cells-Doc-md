---
title: Erweiterte Schutz Einstellungen seit Excel XP mit Node.js über C++
linktitle: Erweiterte Schutzeinstellungen seit Excel XP
type: docs
weight: 30
url: /de/nodejs-cpp/advanced-protection-settings-since-excel-xp/
---


{{% alert color="primary" %}}

Seit der Veröffentlichung von Excel 2002 oder XP hat Microsoft viele erweiterte Schutzeinstellungen hinzugefügt.

{{% /alert %}}


## **Einführung**

Diese Schutzeinstellungen beschränken oder erlauben Benutzern:

- Zeilen oder Spalten löschen.
- Inhalte, Objekte oder Szenarien bearbeiten.
- Zellen, Reihen oder Spalten formatieren.
- Zeilen, Spalten oder Hyperlinks einfügen.
- Gesperrte oder ungesperrte Zellen auswählen.
- Pivot-Tabellen verwenden und vieles mehr.

Aspose.Cells for Node.js via C++ unterstützt alle erweiterten Schutzeinstellungen, die von Excel XP oder späteren Versionen angeboten werden.

### **Erweiterte Schutzeinstellungen mit Excel XP und späteren Versionen verwenden**

Um die Schutzeinstellungen in Excel XP anzuzeigen:

1. Wählen Sie im **Extras**-Menü **Schutz** und danach **Arbeitsblatt schützen** aus. Es wird ein Dialogfeld angezeigt.

Um die verfügbaren Schutzeinstellungen in Excel 2016 anzuzeigen:

1. Wählen Sie im **Datei**-Menü **Arbeitsmappe schützen** und danach **Aktuelles Blatt schützen** aus.
1. Wählen Sie **Arbeitsblatt schützen** im **Überprüfen**-Menü aus.

Die oben genannten Schritte zeigen ein Dialogfeld, in dem Sie Arbeitsblattfunktionen zulassen, einschränken oder ein Passwort für das Arbeitsblatt festlegen können.

### **Erweiterte Schutzeinstellungen mit Aspose.Cells for Node.js via C++**

Aspose.Cells for Node.js via C++ unterstützt alle erweiterten Schutzeinstellungen.

Aspose.Cells stellt eine Klasse, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), bereit, die eine Microsoft Excel-Datei darstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) enthält eine [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) repräsentiert.

Die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) stellt die Eigenschaft [**getProtection()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getProtection--) bereit, die verwendet wird, um diese erweiterten Schutzeinstellungen anzuwenden. Die Eigenschaft [**getProtection()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getProtection--) ist tatsächlich ein Objekt der Klasse [**Protection**](https://reference.aspose.com/cells/nodejs-cpp/protection), das mehrere boolesche Eigenschaften zum Deaktivieren oder Aktivieren von Beschränkungen umschließt.

Unten finden Sie eine kleine Beispielanwendung. Es öffnet eine Excel-Datei und verwendet die meisten von Excel XP und späteren Versionen unterstützten erweiterten Schutzeinstellungen.

```javascript
try {
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.createReadStream(filePath);

// Reading the file stream into a buffer
const fileBuffer = [];
fstream.on('data', chunk => fileBuffer.push(chunk));
fstream.on('end', () => {
const workbook = new AsposeCells.Workbook(Buffer.concat(fileBuffer));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Restricting users to delete columns of the worksheet
worksheet.getProtection().setAllowDeletingColumn(false);

// Restricting users to delete row of the worksheet
worksheet.getProtection().setAllowDeletingRow(false);

// Restricting users to edit contents of the worksheet
worksheet.getProtection().setAllowEditingContent(false);

// Restricting users to edit objects of the worksheet
worksheet.getProtection().setAllowEditingObject(false);

// Restricting users to edit scenarios of the worksheet
worksheet.getProtection().setAllowEditingScenario(false);

// Restricting users to filter
worksheet.getProtection().setAllowFiltering(false);

// Allowing users to format cells of the worksheet
worksheet.getProtection().setAllowFormattingCell(true);

// Allowing users to format rows of the worksheet
worksheet.getProtection().setAllowFormattingRow(true);

// Allowing users to insert columns in the worksheet
worksheet.getProtection().setAllowFormattingColumn(true);

// Allowing users to insert hyperlinks in the worksheet
worksheet.getProtection().setAllowInsertingHyperlink(true);

// Allowing users to insert rows in the worksheet
worksheet.getProtection().setAllowInsertingRow(true);

// Allowing users to select locked cells of the worksheet
worksheet.getProtection().setAllowSelectingLockedCell(true);

// Allowing users to select unlocked cells of the worksheet
worksheet.getProtection().setAllowSelectingUnlockedCell(true);

// Allowing users to sort
worksheet.getProtection().setAllowSorting(true);

// Allowing users to use pivot tables in the worksheet
worksheet.getProtection().setAllowUsingPivotTable(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"), AsposeCells.SaveFormat.Excel97To2003);

// Closing the file stream to free all resources
fstream.close();
```

{{% alert color="primary" %}}

Bitte rufen Sie beim Verwenden der [**getProtection()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getProtection--)-Eigenschaft die [**protect(ProtectionType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#protect-protectiontype-)-Methode der [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse nicht auf. Speichern Sie die Datei außerdem im Excel97To2003- oder Xlsx-Format, da die erweiterten Schutzeinstellungen nur von Excel XP und späteren Versionen unterstützt werden.

{{% /alert %}}

### **Problem mit Zellsperre**

Wenn Sie Nutzer daran hindern möchten, Zellen zu bearbeiten, müssen die Zellen vor der Anwendung der Schutz-Einstellungen gesperrt werden. Andernfalls können die Zellen auch bei aktiviertem Schutz bearbeitet werden. In Microsoft Excel XP können Zellen über den folgenden Dialog gesperrt werden:

|**Dialog zum Sperren von Zellen in Excel XP**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

Es ist auch möglich, Zellen mit der Aspose.Cells-API zu sperren. Jede Zelle kann eine [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-Formatierung erhalten, die eine boolesche Eigenschaft [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--) enthält. Setzen Sie die [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--)-Eigenschaft auf **true** oder **false**, um die Zelle zu sperren oder zu entsperren.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").getStyle().setIsLocked(true);
// Finally, Protect the sheet now.
worksheet.protect(AsposeCells.ProtectionType.All);
workbook.save(path.join(dataDir, "output.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
