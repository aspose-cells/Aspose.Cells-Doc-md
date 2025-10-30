---
title: Trimma ledande tomma rader och kolumner vid export av kalkylblad till CSV format med Node.js via C++
linktitle: Strimla ledande tomma rader och kolumner vid export av kalkylblad till CSV format
type: docs
weight: 100
url: /sv/nodejs-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Lär dig att trimma ledande tomma rader och kolumner när du exporterar kalkylblad till CSV format med Aspose.Cells for Node.js via C++.
---

## **Möjliga användningsscenario**

Ibland har din Excel eller CSV-fil ledande tomma kolumner eller rader. Till exempel, överväg den här raden

{{< highlight javascript >}}

 ,,,data1,data2

{{< /highlight >}}

Här är de första tre cellerna eller kolumnerna tomma. När du öppnar en sådan CSV-fil i Microsoft Excel, då tar Microsoft Excel bort dessa ledande tomma rader och kolumner.

Som standard, klär inte Aspose.Cells for Node.js via C++ av ledande tomma kolumner och rader vid spara. Om du vill ta bort dem precis som Microsoft Excel gör, tillhandahåller Aspose.Cells [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--)-egenskapen. Vänligen ställ in den till **true** så att alla ledande tomma rader och kolumner kommer att kasseras vid sparande.

{{% alert color="primary" %}}

Före släppet av Aspose.Cells for Node.js via C++ 20.4 var standardvärdet för [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--) **false**. Sedan version 20.4 är standardvärdet för [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--) **true.**

{{% /alert %}}

## **Rensa ledande blanka rader och kolumner vid export av kalkylblad till CSV-format**

Följande exempel laddar [käll-Excel-filen](sampleTrimBlankColumns.xlsx) som har två ledande tomma kolumner. Den sparar först filen som CSV utan några ändringar, och ställer sedan in [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--)-egenskapen till **true** och sparar den igen. Skärmbilden visar [käll-Excel-fil](sampleTrimBlankColumns.xlsx), [utdata CSV utan trimning](outputWithoutTrimBlankColumns.csv) och [utdata CSV med trimning](outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Exempelkod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load source workbook
const wb = new AsposeCells.Workbook(path.join(dataDir, "sampleTrimBlankColumns.xlsx"));

// Save in csv format
wb.save(path.join(dataDir, "outputWithoutTrimBlankColumns.csv"), AsposeCells.SaveFormat.Csv);

// Now save again with TrimLeadingBlankRowAndColumn as true
const opts = new AsposeCells.TxtSaveOptions();
opts.setTrimLeadingBlankRowAndColumn(true);

// Save in csv format
wb.save(path.join(dataDir, "outputTrimBlankColumns.csv"), opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
