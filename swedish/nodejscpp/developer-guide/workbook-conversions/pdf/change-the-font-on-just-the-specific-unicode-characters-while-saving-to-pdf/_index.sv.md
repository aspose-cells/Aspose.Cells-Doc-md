---
title: Ändra typsnittet på endast de specifika Unicode tecknen när du sparar till PDF med Node.js via C++
linktitle: Byt typsnitt på specifika Unicode tecken vid sparande till PDF
type: docs
weight: 260
url: /sv/nodejs-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Lär dig hur du ändrar typsnitt för specifika Unicode tecken när du sparar till PDF med Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}} 

Vissa Unicode-tecken visas inte med det användarvalda typsnittet. Ett sådant Unicode-tecken är **Icke-linjär bindestreck** (U+2011) och dess Unicode-nummer är 8209. Detta tecken kan inte visas med **Times New Roman**, men det kan visas med andra typsnitt som **Arial Unicode MS**.

 När ett sådant tecken förekommer inuti ett ord eller en mening som är i ett specifikt typsnitt som Times New Roman, ändrar Aspose.Cells teckensnittet för hela ordet eller meningen till ett typsnitt som kan visa detta tecken, t.ex. Arial Unicode till MS.

 Detta är dock oönskat beteende för vissa användare och de vill bara ändra typsnittet för det specifika tecknet istället för att ändra hela ordet eller meningen.

 För att hantera detta problem, tillhandahåller Aspose.Cells egenskapen `PdfSaveOptions.isFontSubstitutionCharGranularity` som bör ställas in på true så att bara typsnittet för specifika tecken som inte kan visas byts till ett visningsbart typsnitt, medan resten av ordet eller meningen förblir i det ursprungliga typsnittet.

{{% /alert %}} 

## **Exempel**
Följande skärmbild jämför de två utdata-PDF:erna som genererats av koden nedan.

 En genereras utan att ställa in `PdfSaveOptions.isFontSubstitutionCharGranularity` egenskapen och den andra genererades efter att ha ställt in egenskapen `PdfSaveOptions.isFontSubstitutionCharGranularity` till true.

 Som du kan se i den första PDF:en har hela meningen ändrats från Times New Roman till Arial Unicode MS på grund av icke-brytande bindestrecket. I den andra PDF:en har endast tecknet icke-brytande bindestrecket ändrats.

|**Första PDF-filen**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**Andra PDF-filen**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **Exempelkod**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cells
const cell1 = worksheet.getCells().get("A1");
const cell2 = worksheet.getCells().get("B1");

// Set the styles of both cells to Times New Roman
let style = cell1.getStyle();
style.getFont().setName("Times New Roman");
cell1.setStyle(style);
cell2.setStyle(style);

// Put the values inside the cell
cell1.putValue("Hello without Non-Breaking Hyphen");
cell2.putValue("Hello" + String.fromCharCode(8209) + " with Non-Breaking Hyphen");

// Autofit the columns
worksheet.autoFitColumns();

// Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
workbook.save(path.join(dataDir, "SampleOutput_out.pdf"));

// Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true
const opts = new AsposeCells.PdfSaveOptions();
opts.setIsFontSubstitutionCharGranularity(true);
workbook.save(path.join(dataDir, "SampleOutput2_out.pdf"), opts);
```



{{< app/cells/assistant language="nodejs-cpp" >}}
