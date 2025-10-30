---
title: Beräkning av arrayformel för datatabeller med Node.js via C++
linktitle: Beräkning av Data Table Arrayformel
description: Hur man använder Aspose.Cells biblioteket för att beräkna arrayformler för en datatabell i Microsoft Excel med Node.js via C++. Ladda eller skapa en Excel fil, beräkna arrayformeln och spara den modifierade filen.
keywords: Aspose.Cells, Excel, datatabeller, arrayformler, beräkningar Node.js via C++
type: docs
weight: 70
url: /sv/nodejs-cpp/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

Du kan skapa en datatabell i Microsoft Excel med Data > What-If-Analysis > Data Table.... Aspose.Cells tillåter nu beräkning av arrayformeln för en datatabell. Använd [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) som normalt för att beräkna vilken formel som helst.

{{% /alert %}}

I följande kodexempel använde vi [källa excel-fil](5115535.xlsx). Om du ändrar värdet i cell B1 till 100 blir värdena i datatabellen som är fyllda med gult färgad till 120, vilket visas i följande bilder. Detta kodexempel genererar [utdata PDF](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

Följande kod användes för att generera [utdata PDF](5115538.pdf) från [källa excel-fil](5115535.xlsx). Läs kommentarerna för mer information.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook from source excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "DataTable.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
worksheet.getCells().get("B1").putValue(100);

// Calculate formula, now it also calculates Data Table array formula
workbook.calculateFormula();

// Save the workbook in pdf format
workbook.save(path.join(dataDir, "output_out.pdf"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
