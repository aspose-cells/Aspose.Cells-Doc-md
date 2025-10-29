---  
title: Convertir Excel en JSON avec Node.js via C++  
linktitle: Convertir Excel en JSON  
type: docs  
weight: 300  
url: /fr/nodejs-cpp/convert-excel-to-json/  
description: Apprenez comment convertir un fichier Excel en JSON en utilisant Aspose.Cells for Node.js via C++.  
keywords: Exportation du classeur en JSON Node.js via C++, Conversion Excel en JSON Node.js via C++  
---  

{{% alert color="primary" %}}  
 Aspose.Cells supporte la conversion d’un classeur en fichier JSON (JavaScript Object Notation).  
{{% /alert %}}  

## **Convertir un classeur Excel en JSON**  

 Pas besoin de se demander comment convertir un classeur Excel en JSON, car la bibliothèque Aspose.Cells for Node.js via C++ offre la meilleure solution. L’API Aspose.Cells propose une prise en charge de la conversion de tableurs en format JSON. Pour exporter le classeur en JSON, passez [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat/) comme deuxième paramètre de la méthode [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-). Vous pouvez également utiliser la classe [**JsonSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonsaveoptions/) pour spécifier des paramètres supplémentaires lors de l’exportation de la feuille de calcul en JSON.  

L’exemple de code suivant montre comment exporter un classeur Excel en JSON. Veuillez consulter le code pour convertir le [fichier source](sample.xlsx) en fichier JSON généré par le code à titre de référence.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save("sample_out.json");
```  

L’exemple de code suivant utilise la classe JsonSaveOptions pour spécifier des paramètres supplémentaires et montre comment exporter un classeur Excel en JSON. Veuillez consulter le code pour convertir le [fichier source](sample.xlsx) en fichier JSON généré par le code à titre de référence.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an options of saving the file.
const options = new AsposeCells.JsonSaveOptions();

// Set the exporting range.
options.setExportArea(AsposeCells.CellArea.createCellArea("B1", "C4"));

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save("sample_out.json", options);
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
