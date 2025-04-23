---  
title: Charger ou importer un fichier CSV avec des formules via Node.js  
linktitle: Charger ou importer un fichier CSV avec des formules  
type: docs  
weight: 350  
url: /fr/nodejs-cpp/load-or-import-csv-file-with-formulas/  
description: Apprenez comment charger et importer des fichiers CSV contenant des formules en utilisant Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Le fichier CSV contient principalement des données textuelles et ne comporte généralement pas de formules. Cependant, il arrive que des fichiers CSV contiennent aussi des formules. Ces fichiers CSV doivent être chargés en définissant [TxtLoadOptions.getHasFormula()](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#getHasFormula--) à **true**. Une fois cette propriété activée, Aspose.Cells ne traitera pas les formules comme du simple texte. Elles seront traitées comme des formules, et le moteur de calcul de formules d'Aspose.Cells les traitera comme d'habitude.

{{% /alert %}}  

Le code suivant illustre comment charger ainsi qu'importer un fichier CSV avec des formules. Vous pouvez utiliser n'importe quel fichier CSV. À titre d'illustration, nous utilisons le [fichier CSV simple](5115034.csv) qui contient ces données. Comme vous le voyez, il contient une formule.

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

Le code charge d'abord le fichier CSV, puis l'importe à nouveau à la cellule D4. Enfin, il enregistre l'objet classeur au format XLSX. Le [fichier XLSX de sortie](5115052.xlsx) ressemble à ceci. Comme vous le voyez, la cellule C3 et F4 contiennent des formules et leur résultat est 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|  
| :- |  


