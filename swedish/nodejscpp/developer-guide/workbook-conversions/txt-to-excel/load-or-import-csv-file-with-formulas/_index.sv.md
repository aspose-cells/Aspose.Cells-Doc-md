---  
title: Ladda eller importera CSV fil med formulär via Node.js  
linktitle: Ladda eller importera CSV fil med formler  
type: docs  
weight: 350  
url: /sv/nodejs-cpp/load-or-import-csv-file-with-formulas/  
description: Lär dig hur du laddar och importerar CSV filer som innehåller formulär med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

CSV-filer innehåller mestadels textdata och innehåller sällan formler. Men ibland kan CSV-filer även innehålla formler. Dessa CSV-filer bör laddas genom att ställa in [TxtLoadOptions.getHasFormula()](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#getHasFormula--) till **true**. När denna egenskap är satt till **true**, kommer Aspose.Cells inte att behandla formler som enkel text. De kommer att behandlas som formler, och Aspose.Cells formelberäkningsmotor kommer att bearbeta dem som vanligt.

{{% /alert %}}  

 Följande kod illustrerar hur du kan ladda samt importera en CSV-fil med formler. Du kan använda vilken CSV-fil som helst. För att illustrera använder vi [enkel CSV-fil](5115034.csv) som innehåller denna data. Som du ser innehåller den en formel.

{{< highlight javascript >}}  
const fs = require('fs');  
const AsposeCells = require('aspose.cells');  

let loadOptions = new AsposeCells.TxtLoadOptions();  
loadOptions.setHasFormula(true);  

let workbook = new AsposeCells.Workbook();  
workbook.open("path/to/your/file.csv", loadOptions);  
workbook.save("path/to/output.xlsx");  
{{< /highlight >}}  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.csv");

// TxtLoadOptions configuration
const opts = new AsposeCells.TxtLoadOptions();
opts.setSeparator(',');
opts.setHasFormula(true);

// Load your CSV file with formulas in a Workbook object
const workbook = new AsposeCells.Workbook(filePath, opts);

// You can also import your CSV file like this
// The code below is importing CSV file starting from cell D4
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().importCSV(filePath, opts, 3, 3);

// Save your workbook in Xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

Koden laddar först CSV-filen, importer den sedan igen till cell D4. Slutligen sparar den arbetsbokobjektet i XLSX-format. [utdata XLSX-fil](5115052.xlsx) ser ut så här. Som du ser, innehåller cell C3 och F4 formler och deras resultat är 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|  
| :- |  


{{< app/cells/assistant language="nodejs-cpp" >}}
