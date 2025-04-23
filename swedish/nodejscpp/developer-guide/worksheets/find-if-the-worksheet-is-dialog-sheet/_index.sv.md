---
title: Hitta om kalkylbladet är ett dialogark med Node.js via C++
linktitle: Ta reda på om kalkylbladet är Dialog sheet
type: docs
weight: 90
url: /sv/nodejs-cpp/find-if-the-worksheet-is-dialog-sheet/
description: Den här artikeln ger instruktioner och exempel på kod för att programmässigt avgöra om ett Excel kalkylblad är ett Dialogark med Aspose.Cells for Node.js via C++.
keywords: hitta excel kalkylblad dialogtyp Node.js via C++, kalkylblad dialog Node.js via C++
---

## **Möjliga användningsscenario**

Dialogark är ett gammalt format av blad som innehåller en dialogruta. Ett sådant blad kan infogas av en äldre version av Microsoft Excel, t.ex. 2003, som visas i skärmbilden. Det kan också infogas med VBA i nyare versioner, t.ex. Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Du kan avgöra om bladet är ett dialogblad eller någon annan typ av blad med egenskapen [**Worksheet.getType()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getType--) som tillhandahålls av Aspose.Cells for Node.js via C++. Om den returnerar ett enumerationsvärde [**SheetType.Dialog**](https://reference.aspose.com/cells/nodejs-cpp/sheettype), betyder det att du arbetar med ett dialogblad.

## **Ta reda på om kalkylbladet är Dialog sheet**

Följande exempel på kod laddar [exempelfil](64716820.xlsx) som innehåller ett dialogblad. Den kontrollerar egenskapen [**Worksheet.getType()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getType--), jämför den med [**SheetType.Dialog**](https://reference.aspose.com/cells/nodejs-cpp/sheettype) och skriver ut ett meddelande. Se konsolutdata för exemplet nedan för mer hjälp.

## **Exempelkod**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleFindIfWorksheetIsDialogSheet.xlsx");

// Load Excel file containing Dialog Sheet
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = workbook.getWorksheets().get(0);

// Find if the sheet type is dialog and print the message
if (ws.getType() === AsposeCells.SheetType.Dialog) {
console.log("Worksheet is a Dialog Sheet.");
}
```

## **Konsoloutput**

{{< highlight js >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
