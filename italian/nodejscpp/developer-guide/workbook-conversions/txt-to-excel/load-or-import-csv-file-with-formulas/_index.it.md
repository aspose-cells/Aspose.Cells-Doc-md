---  
title: Carica o importa file CSV con formule tramite Node.js  
linktitle: Carica o importa file CSV con formule  
type: docs  
weight: 350  
url: /it/nodejs-cpp/load-or-import-csv-file-with-formulas/  
description: Impara come caricare e importare file CSV contenenti formule usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Il file CSV di solito contiene dati testuali e non contiene formule. Tuttavia, a volte può succedere che i file CSV contengano anche formule. Questi file CSV dovrebbero essere caricati impostando [TxtLoadOptions.getHasFormula()](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#getHasFormula--) su **true**. Una volta impostata questa proprietà su **true**, Aspose.Cells non tratterà le formule come semplice testo. Saranno trattate come formule, e il motore di calcolo delle formule di Aspose.Cells le elaborerà come di consueto.

{{% /alert %}}  

Il seguente esempio illustra come puoi caricare e importare un file CSV con formule. Puoi usare qualsiasi file CSV. Per scopi dimostrativi, usiamo il [file CSV semplice](5115034.csv) che contiene questi dati. Come puoi vedere, contiene una formula.

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

Il codice prima carica il file CSV, poi lo importa di nuovo in cella D4. Infine, salva l'oggetto workbook in formato XLSX. Il [file XLSX di output](5115052.xlsx) risulta così. Come puoi vedere, le celle C3 e F4 contengono formule e il loro risultato è 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|  
| :- |  


{{< app/cells/assistant language="nodejs-cpp" >}}
