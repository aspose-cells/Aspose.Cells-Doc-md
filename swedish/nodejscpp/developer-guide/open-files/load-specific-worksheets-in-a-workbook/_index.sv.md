---
title: Ladda specifika kalkylblad i en arbetsbok med Node.js via C++
linktitle: Ladda specifika arbetsblad i en arbetsbok
type: docs
weight: 100
url: /sv/nodejs-cpp/load-specific-worksheets-in-a-workbook/
description: Lär dig hur du laddar specifika kalkylblad i en arbetsbok med Aspose.Cells for Node.js via C++. Förbättra prestanda och minska minnesförbrukningen.
---

{{% alert color="primary" %}}

Som standard laddar Aspose.Cells hela kalkylarket i minnet. Det är möjligt att endast ladda specifika blad. Detta kan förbättra prestanda och använda mindre minne. Detta tillvägagångssätt är användbart när du arbetar med en stor arbetsbok som består av många kalkylblad.

{{% /alert %}}

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Define a new Workbook.
let workbook;

// Load the workbook with the specified worksheet only.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
loadOptions.setLoadFilter(new CustomLoad());

// Create the workbook.
workbook = new AsposeCells.Workbook(path.join(dataDir, "TestData.xlsx"), loadOptions);

// Perform your desired task.

// Save the workbook.
workbook.save(path.join(dataDir, "outputFile.out.xlsx"));
```

Här är implementationen av klassen CustomLoad.

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomLoad extends AsposeCells.LoadFilter {
startSheet(sheet) {
if (sheet.getName() === "Sheet2") {
// Load everything from worksheet "Sheet2"
this.setLoadDataFilterOptions(AsposeCells.LoadDataFilterOptions.All);
} else {
// Load nothing
this.setLoadDataFilterOptions(AsposeCells.LoadDataFilterOptions.Structure);
}
}
}
```


{{< app/cells/assistant language="nodejs-cpp" >}}
