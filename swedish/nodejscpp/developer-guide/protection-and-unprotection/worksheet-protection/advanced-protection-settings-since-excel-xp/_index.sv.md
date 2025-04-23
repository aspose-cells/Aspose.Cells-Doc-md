---
title: Avancerade skyddsinställningar sedan Excel XP med Node.js via C++
linktitle: Avancerade skyddsinställningar sedan Excel XP
type: docs
weight: 30
url: /sv/nodejs-cpp/advanced-protection-settings-since-excel-xp/
---


{{% alert color="primary" %}}

Sedan utgåvan av Excel 2002 eller XP har Microsoft lagt till många avancerade skyddsinställningar.

{{% /alert %}}


## **Introduktion**

Dessa skyddsinställningar begränsar eller tillåter användare att:

- Ta bort rader eller kolumner.
- Redigera innehåll, objekt eller scenarier.
- Formatera celler, rader eller kolumner.
- Infoga rader, kolumner eller hyperlänkar.
- Välj låsta eller olåsta celler.
- Använd pivottabeller och mycket annat.

Aspose.Cells for Node.js via C++ stöder alla avancerade skyddsinställningar som erbjuds av Excel XP eller senare versioner.

### **Avancerade skyddsinställningar med Excel XP och senare versioner**

För att visa de tillgängliga skyddsinställningarna i Excel XP:

1. Från **Verktyg**-menyn, välj **Skydda** följt av **Skydda kalkylblad**. En dialogruta kommer att visas.

För att visa de tillgängliga skyddsinställningarna i Excel 2016:

1. Från **Arkiv**-menyn, välj **Skydda arbetsbok** följt av **Skydda aktuellt kalkylblad**.
1. Välj **Skydda kalkylblad** i **Granska**-menyn.

Följ stegen ovan visar en dialogruta där du kan tillåta eller begränsa arbetsbladets funktioner eller tillämpa ett lösenord på arbetsbladet.

### **Avancerade skyddsinställningar med Aspose.Cells for Node.js via C++**

Aspose.Cells for Node.js via C++ stöder alla avancerade skyddsinställningar.

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection)-kollektion som möjliggör åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen.

[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen ger egenskapen [**getProtection()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getProtection--) som används för att tillämpa dessa avancerade skyddsinställningar. Egenskapen [**getProtection()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getProtection--) är faktiskt ett objekt av [**Protection**](https://reference.aspose.com/cells/nodejs-cpp/protection)-klassen som kapslar in flera booleska egenskaper för att inaktivera eller aktivera restriktioner.

Nedan finns en liten exempelapplikation. Den öppnar en Excel-fil och använder de flesta av de avancerade skyddsinställningarna som stöds av Excel XP och senare versioner.

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

Vänligen ring inte metoden [**protect(ProtectionType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#protect-protectiontype-) för klassen [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) när du använder egenskapen [**getProtection()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getProtection--). Spara också filen i Excel97Till2003 eller Xlsx-format eftersom de avancerade säkerhetsinställningarna endast stöds av Excel XP och senare versioner.

{{% /alert %}}

### **Cellåsningsproblem**

Om du vill begränsa användare från att redigera celler måste cellerna låsas innan några skyddsinställningar tillämpas. Annars kan cellerna redigeras även om arket är skyddat. I Microsoft Excel XP kan celler låsas genom följande dialog:

|**Dialogruta för att låsa celler i Excel XP**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

Det är också möjligt att låsa celler med Aspose.Cells API. Varje cell kan få [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) formatering som innehåller en Boolean-egenskap, [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--). Sätt [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--) egenskapen till **true** eller **false** för att låsa eller låsa upp cellen.

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
