---  
title: Cargar o importar archivos CSV con fórmulas mediante Node.js  
linktitle: Cargar o Importar archivo CSV con Fórmulas  
type: docs  
weight: 350  
url: /es/nodejs-cpp/load-or-import-csv-file-with-formulas/  
description: Aprenda cómo cargar e importar archivos CSV que contienen fórmulas usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

El archivo CSV generalmente contiene datos textuales y no contiene fórmulas. Sin embargo, a veces sucede que los archivos CSV también contienen fórmulas. Tales archivos CSV deben cargarse configurando [TxtLoadOptions.getHasFormula()](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#getHasFormula--) en **true**. Una vez establecida esta propiedad en **true**, Aspose.Cells no tratará las fórmulas como texto simple. Serán tratadas como fórmulas, y el motor de cálculo de fórmulas de Aspose.Cells los procesará como de costumbre.

{{% /alert %}}  

El siguiente código ilustra cómo cargar e importar un archivo CSV con fórmulas. Puede usar cualquier archivo CSV. Para propósitos ilustrativos, usamos el [archivo CSV simple](5115034.csv) que contiene estos datos. Como puede ver, contiene una fórmula.

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

El código primero carga el archivo CSV, luego lo importa nuevamente en la celda D4. Finalmente, guarda el objeto libro en formato XLSX. El [archivo XLSX de salida](5115052.xlsx) se ve así. Como puede ver, las celdas C3 y F4 contienen fórmulas y su resultado es 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|  
| :- |  


{{< app/cells/assistant language="nodejs-cpp" >}}
