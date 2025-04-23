---
title: Nutzen Sie die Eigenschaft Sheet.SheetId von OpenXml mit Aspose.Cells for Node.js via C++
linktitle: Verwenden Sie die Sheet.SheetId Eigenschaft von OpenXml mit Aspose.Cells
type: docs
weight: 200
url: /de/nodejs-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/
description: Dieser Artikel zeigt, wie man die Eigenschaft Sheet.SheetId von OpenXml mit Excel Manipulationen durch Aspose.Cells for Node.js via C++ programmatisch nutzt.
keywords: Sheet ID Eigenschaft von OpenXml Node.js über C++, Sheet ID von Excel Arbeitsblatt Node.js über C++
---

## **Mögliche Verwendungsszenarien**

*Sheet.SheetId*-Eigenschaft ist im *DocumentFormat.OpenXml.Spreadsheet*-Modul enthalten und Teil von OpenXml. Diese Eigenschaft und ihr Wert sind in *workbook.xml* sichtbar, wie im folgenden Screenshot gezeigt. Aspose.Cells bietet die entsprechende Eigenschaft als [**Worksheet.getTabId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getTabId--).

![todo:image_alt_text](utilize-sheet-sheetid-property-of-openxml-using-aspose-cells_1.png)

## **Nutzen Sie die Sheet.SheetId-Eigenschaft von OpenXml mit Aspose.Cells for Node.js via C++**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](51740716.xlsx), liest ihre Tabellen- oder Registerkarten-ID, weist ihr dann eine neue Registerkarten-ID zu und speichert sie als [Ausgabe-Excel-Datei](51740717.xlsx). Bitte sehen Sie sich auch die Konsolenausgabe des untenstehenden Codes als Referenz an.

## **Beispielcode**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSheetId.xlsx");

// Load source Excel file
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Print its Sheet or Tab Id on console
console.log("Sheet or Tab Id: " + ws.getTabId());

// Change Sheet or Tab Id
ws.setTabId(358);

// Save the workbook
wb.save("outputSheetId.xlsx");
```

## **Konsolenausgabe**

{{< highlight text >}}

Sheet or Tab Id: 1297

{{< /highlight >}}
