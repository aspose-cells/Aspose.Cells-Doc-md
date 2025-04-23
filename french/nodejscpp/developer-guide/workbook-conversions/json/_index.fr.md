---  
title: Json avec Node.js via C++  
linktitle: Json  
type: docs  
weight: 300  
url: /fr/nodejs-cpp/convert-workbook-to-json/  
description: Apprenez à convertir un classeur Excel en JSON en utilisant Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Aspose.Cells supporte la conversion d'un classeur en fichier Json (JavaScript Object Notation).  
{{% /alert %}}  

## **Convertir un classeur Excel en JSON**  

L’API Aspose.Cells prend en charge la conversion des feuilles de calcul au format JSON. Pour exporter le classeur en JSON, passez [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) comme deuxième paramètre de la méthode [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-). Vous pouvez également utiliser la classe [**JsonSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonsaveoptions) pour spécifier des paramètres additionnels lors de l’exportation de la feuille de calcul au format JSON.  

L’exemple de code suivant montre comment exporter la feuille de calcul active en JSON en utilisant le membre d’énumération [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat/#json). Voir le code pour convertir le [fichier source](book1.xlsx) en [fichier JSON de sortie](book1.Json) généré par le code à titre de référence.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save(path.join(dataDir, "book1.json"));
```  

## **Sujets avancés**  
- [Convertir CSV en JSON](/cells/fr/nodejs-cpp/convert-csv-to-json/)  
- [Convertir Excel en JSON](/cells/fr/nodejs-cpp/convert-excel-to-json/)  
- [Convertir JSON en CSV](/cells/fr/nodejs-cpp/convert-json-to-csv/)  
- [Convertir JSON en Excel](/cells/fr/nodejs-cpp/convert-json-to-excel/)  

