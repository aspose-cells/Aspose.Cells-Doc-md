---  
title: Convertir une table en ODS avec Node.js via C++  
linktitle: Convertir un tableau en ODS  
type: docs  
weight: 70  
url: /fr/nodejs-cpp/convert-table-to-ods/  
description: Apprenez comment convertir un fichier Excel avec une table au format ODS en utilisant Aspose.Cells for Node.js via C++.  
---  

Aspose.Cells prend en charge la conversion d'un fichier Excel avec une table au format ODS. Il suffit de sauvegarder le fichier au format ODS, et le fichier ODS généré aura une table fonctionnelle.

## Code d'exemple

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open an existing file that contains a table/list object in it
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleTable.xlsx"));

// Save the file
workbook.save(path.join(outputDir, "ConvertTableToOds_out.ods"));
```

Le fichier ODS de sortie généré par le code d'exemple est joint à titre de référence.

[**Output ODS File**](ConvertTableToOds_out.ods)  

{{< app/cells/assistant language="nodejs-cpp" >}}
