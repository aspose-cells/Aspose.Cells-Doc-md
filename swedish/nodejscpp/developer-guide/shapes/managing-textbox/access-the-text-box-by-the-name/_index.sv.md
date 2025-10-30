---
title: Åtkomst till TextBox via namn med Node.js via C++
linktitle: Tillgång till textfältet genom namnet
type: docs
weight: 230
url: /sv/nodejs-cpp/access-the-text-box-by-the-name/
description: Lär dig hur du får åtkomst till en textlåda via namn från samlingen i Aspose.Cells for Node.js via C++. 
---

## Åtkomst till textlådan med namnet

Tidigare kunde textlådor nås via index från [**Worksheet.getTextBoxes()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getTextBoxes--)-samlingen, men nu kan du också få åtkomst till textlådan via dess namn i denna samling. Det är ett bekvämt och snabbt sätt att få åtkomst till din textlåda om du redan känner till dess namn.

Följande provkod skapar först en textruta och tilldelar den någon text och namn. Sedan i de följande raderna får vi åtkomst till samma textruta genom dess namn och skriver ut dess text.

### Node.js-kod för att komma åt textlådan via namn

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the TextBox to the worksheet
const idx = sheet.getTextBoxes().add(10, 10, 10, 10);

// Access newly created TextBox using its index & name it
const tb1 = sheet.getTextBoxes().get(idx);
tb1.setName("MyTextBox");

// Set text for the TextBox
tb1.setText("This is MyTextBox");

// Access the same TextBox via its name
const tb2 = sheet.getTextBoxes().get("MyTextBox");

// Display the text of the TextBox accessed via name
console.log(tb2.getText());

console.log("Press any key to continue...");
```

### Konsoloutput som genereras av provkoden

Här är konsoloutputen från ovanstående exempelkod.

{{< highlight javascript >}}
This is MyTextBox
{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
