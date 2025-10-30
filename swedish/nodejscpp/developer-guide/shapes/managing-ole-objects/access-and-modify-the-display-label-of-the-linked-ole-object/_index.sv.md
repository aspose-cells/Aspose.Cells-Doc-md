---
title: Åtkomst och modifiera displayetiketten för den länkade Ole objektet med Node.js via C++
linktitle: Åtkomst och ändring av visningsmärket för det länkade OLE objektet
type: docs
weight: 100
url: /sv/nodejs-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/
description: Lär dig hur du får åtkomst till och modifierar displayetiketten för ett länkade Ole objekt med Aspose.Cells for Node.js via C++. 
---

## **Möjliga användningsscenario**

Microsoft Excel tillåter dig att ändra displayetiketten för Ole-objektet, som visas i skärmbilden nedan. Du kan också få åtkomst till eller ändra displayetiketten för Ole-objektet med Aspose.Cells API:er med egenskapen [**OleObject.getLabel()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getLabel--).

![todo:image_alt_text](access-and-modify-the-display-label-of-the-linked-ole-object_1.png)

## **Åtkomst och ändring av visningsmärket för det länkade OLE-objektet**

Se koden nedan, den laddar filen [exempel-Excel](64716810.xlsx) med Ole-Objekt. Koden får tillgång till Ole-objektet och ändrar dess etikett från Sample APIs till Aspose APIs. Se utdata i konsolen nedan som visar effekten av koden på exempel-Excel för referens.

## **Exempelkod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleAccessAndModifyLabelOfOleObject.xlsx");

// Load the sample Excel file 
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access first Ole Object
let oleObject = ws.getOleObjects().get(0);

// Display the Label of the Ole Object
console.log("Ole Object Label - Before: " + oleObject.getLabel());

// Modify the Label of the Ole Object
oleObject.setLabel("Aspose APIs");

// Save workbook to memory stream
const ms = wb.save(AsposeCells.SaveFormat.Xlsx);

// Set the workbook reference to null
wb.dispose();

// Load workbook from memory stream
const wbFromStream = new AsposeCells.Workbook(ms);

// Access first worksheet
const wsFromStream = wbFromStream.getWorksheets().get(0);

// Access first Ole Object
oleObject = wsFromStream.getOleObjects().get(0);

// Display the Label of the Ole Object that has been modified earlier
console.log("Ole Object Label - After: " + oleObject.getLabel());
```

## **Konsoloutput**

{{< highlight javascript >}}

Ole Object Label - Before: Sample APIs

Ole Object Label - After: Aspose APIs

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
