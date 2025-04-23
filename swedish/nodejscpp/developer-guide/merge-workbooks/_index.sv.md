---
title: Kombinera flera arbetsböcker till en enda arbetsbok med Node.js via C++
linktitle: Arbetsboksfusion
type: docs
weight: 66
url: /sv/nodejs-cpp/combine-multiple-workbooks-into-a-single-workbook/
description: Lär dig hur man kombinerar flera arbetsböcker till en enda arbetsbok med Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Ibland måste du kombinera arbetsböcker med olika innehåll som bilder, diagram och data till en enda arbetsbok. Aspose.Cells for Node.js via C++ stöder denna funktion. Denna artikel visar hur man skapar en konsolapplikation och kombinerar arbetsböcker med några enkla kodrader med Aspose.Cells.

{{% /alert %}}

## **Kombinera arbetsböcker med bilder och diagram**

Exempelkoden kombinerar två arbetsböcker till en enda arbetsbok med Aspose.Cells for Node.js via C++. Koden läser in kälbarbetsböckerna, använder metoden [**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#combine-workbook-) för att kombinera dem, och sparar den sammanslagna arbetsboken.

### **Källarbetsböcker**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **Resultatarbetsböcker**

- [combined.xlsx](5473095.xlsx)

### **Skärmbilder**

Här är skärmbilder på käll- och resultatarbetsböcker.

{{% alert color="primary" %}}

Du kan använda vilka källarbetsböcker som helst. Dessa bilder är bara för illustration.

{{% /alert %}}

**Den första arbetsbokens arbetsblad - staplad** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**Andra arbetsbladet i arbetsboken - linje** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**Första arbetsbladet i bildarbetsboken - bild** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**Alla tre arbetsblad i den kombinerade arbetsboken - staplad, linje, bild** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Define the first source
// Open the first excel file.
const sourceBook1 = new AsposeCells.Workbook(path.join(dataDir, "SampleChart.xlsx"));

// Define the second source book.
// Open the second excel file.
const sourceBook2 = new AsposeCells.Workbook(path.join(dataDir, "SampleImage.xlsx"));

// Combining the two workbooks
sourceBook1.combine(sourceBook2);

const outputPath = path.join(dataDir, "Combined.out.xlsx");
// Save the target book file.
sourceBook1.save(outputPath);
```

## **Fortsatta ämnen**
- [Kombinera flera arbetsblad till ett enda arbetsblad](/cells/sv/nodejs-cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [Sammanfoga filer](/cells/sv/nodejs-cpp/merge-files/)

