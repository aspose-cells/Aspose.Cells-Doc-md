---
title: Använd Sheet.SheetId egenskapen i OpenXml med Aspose.Cells for Node.js via C++
linktitle: Använd Sheet.SheetId egenskapen i OpenXml med hjälp av Aspose.Cells
type: docs
weight: 200
url: /sv/nodejs-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/
description: Denna artikel visar hur man använder Sheet.SheetId egenskapen i OpenXml med Excel manipulation dubbelprogrammering med Aspose.Cells for Node.js via C++.
keywords: blad id egenskap av openxml nod.js via C++, blad id excel arksnod.js via C++
---

## **Möjliga användningsscenario**

*Sheet.SheetId* egenskapen är tillgänglig inom *DocumentFormat.OpenXml.Spreadsheet* modul och är en del av OpenXml. Du kan se denna egenskap och dess värde i *workbook.xml* som visas i följande skärmskärm. Aspose.Cells tillhandahåller motsvarande egenskap som [**Worksheet.getTabId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getTabId--).

![todo:image_alt_text](utilize-sheet-sheetid-property-of-openxml-using-aspose-cells_1.png)

## **Använd Sheet.SheetId-egenskapen av OpenXml med Aspose.Cells for Node.js via C++**

Följande exempelkod laddar [provs-exelfilen](51740716.xlsx), läser av dess flik- eller flik-id, tilldelar det ett nytt flik-id och sparar det som [utdata-exelfil](51740717.xlsx). Se även konsolens utmatning för kodreferens.

## **Exempelkod**

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

## **Konsoloutput**

{{< highlight text >}}

Sheet or Tab Id: 1297

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
