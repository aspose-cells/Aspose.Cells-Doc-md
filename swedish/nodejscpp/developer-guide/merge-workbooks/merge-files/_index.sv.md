---
title: Sammanfoga filer med Node.js via C++
linktitle: Slå samman filer
type: docs
weight: 20
url: /sv/nodejs-cpp/merge-files/
---

## **Introduktion**

Aspose.Cells tillhandahåller olika metoder för att slå ihop filer. För enkla filer med data, formatering och formler kan [**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#combine-workbook-)-metoden användas för att kombinera flera arbetsböcker, och [**Worksheet.copy(Worksheet)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#copy-worksheet-)-metoden för att kopiera kalkylblad till en ny arbetsbok. Dessa metoder är enkla att använda och effektiva, men om du har många filer att sammanfoga kan du märka att de tar mycket systemresurser. För att undvika detta, använd den [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#mergeFiles-stringarray-string-string-) statiska metoden, ett mer effektivt sätt att slå ihop flera filer.

## **Sammanfoga filer med Aspose.Cells for Node.js via C++**

Följande kodexempel visar hur man sammanfogar stora filer med [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#mergeFiles-stringarray-string-string-)-metoden. Det tar två enkla men stora filer, Book1.xls och Book2.xls. Filmerna innehåller endast formaterad data och formler.

{{% alert color="primary" %}}

Metoden [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#mergeFiles-stringarray-string-string-) stöder endast sammanfogning av data, format, formatering och formler. Objekt som diagram, bilder, kommentarer eller andra objekt kanske inte sammanfogas med denna metod. Dessutom används en cachelagrad fil för att lagra tillfälliga data för processen.

{{% /alert %}}

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an Array (length=2)
const files = new Array(2);
// Specify files with their paths to be merged
files[0] = path.join(dataDir, "book1.xls");
files[1] = path.join(dataDir, "Book2.xlsx");

// Create a cachedFile for the process
const cacheFile = path.join(dataDir, "test.txt");

// Output File to be created
const dest = path.join(dataDir, "output.xlsx");

// Merge the files in the output file. Supports only .xls files
AsposeCells.CellsHelper.mergeFiles(files, cacheFile, dest);
console.log(cacheFile);
// Now if you need to rename your sheets, you may load the output file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "output.xlsx"));

let i = 1;

// Browse all the sheets to rename them accordingly
const worksheets = workbook.getWorksheets();
for (let j = 0; j < worksheets.getCount(); j++) {
worksheets.get(j).setName(`Sheet1${i}`);
i++;
}

// Re-save the file
workbook.save(path.join(dataDir, "output.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
