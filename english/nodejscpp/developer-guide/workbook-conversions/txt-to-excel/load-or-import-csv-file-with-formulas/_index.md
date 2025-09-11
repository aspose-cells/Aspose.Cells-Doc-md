---  
title: Load or Import CSV file with Formulas via Node.js  
linktitle: Load or Import CSV file with Formulas  
type: docs  
weight: 350  
url: /nodejs-cpp/load-or-import-csv-file-with-formulas/  
description: Learn how to load and import CSV files containing formulas using Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

CSV file mostly contains textual data and they do not contain any formulas. However, sometimes it happens that CSV files also contain formulas. Such CSV files should be loaded by setting the [TxtLoadOptions.getHasFormula()](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#getHasFormula--) as **true**. Once this property will be set **true**, Aspose.Cells will not treat formulas as simple text. They will be treated as formulas, and Aspose.Cells formula calculation engine will process them as usual.

{{% /alert %}}  

The following code illustrates how you can load as well as import a CSV file with formulas. You can use any CSV file. For illustration purposes, we use the [simple csv file](5115034.csv) which contains this data. As you see it contains a formula.

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

The code first loads the CSV file, then imports it again at cell D4. Finally, it saves the workbook object in XLSX format. The [output XLSX file](5115052.xlsx) looks like this. As you see, cell C3 and F4 contain formulas and their result is 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|  
| :- |  

  
{{< app/cells/assistant language="nodejs-cpp" >}}