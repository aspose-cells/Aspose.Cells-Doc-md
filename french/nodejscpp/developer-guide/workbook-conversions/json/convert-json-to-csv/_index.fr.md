---  
title: Convertir JSON en CSV avec Node.js via C++  
linktitle: Convertir JSON en CSV  
type: docs  
weight: 210  
url: /fr/nodejs-cpp/convert-json-to-csv/  
description: Apprenez comment convertir des données JSON en CSV à l’aide de Aspose.Cells for Node.js via C++.  
---  

## **Convertir JSON en CSV**  

 Aspose.Cells supporte la conversion de JSON simple ainsi que imbriqué en CSV. Pour cela, l’API fournit les classes [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions) et [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility). La classe [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions) fournit des options pour la disposition du JSON comme [**JsonLayoutOptions.getArrayAsTable()**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions/#getArrayAsTable--) (traite le tableau comme une table). La classe [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility) traite le JSON en utilisant les options de mise en page définies avec la classe [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions).  

L'exemple de code suivant montre l'utilisation des classes [**JsonLayoutOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonlayoutoptions) et [**JsonUtility**](https://reference.aspose.com/cells/nodejs-cpp/jsonutility) pour charger le fichier JSON source et générer le fichier CSV de sortie.  

### **Code d'exemple**  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");


// Create sample JSON if missing
const jsonPath = path.join(sourceDir, "SampleJson.json");

// Read JSON file
const str = fs.readFileSync(jsonPath, "utf-8");

// Create empty workbook
const workbook = new AsposeCells.Workbook();

// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();

// Set JsonLayoutOptions
const importOptions = new AsposeCells.JsonLayoutOptions();
importOptions.setConvertNumericOrDate(true);
importOptions.setArrayAsTable(true);
importOptions.setIgnoreTitle(true);
AsposeCells.JsonUtility.importData(str, cells, 0, 0, importOptions);

// Save Workbook
workbook.save(outputDir + "SampleJson_out.csv");
```  

