---  
title: Utilisation de WorkbookMetadata avec Node.js via C++  
linktitle: Métadonnées du classeur  
type: docs  
weight: 320  
url: /fr/nodejs-cpp/using-workbookmetadata/  
description: Apprenez comment modifier les métadonnées du classeur en utilisant Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Aspose.Cells vous permet de charger une version légère d'un classeur en mémoire pour modifier ses informations de métadonnées. Veuillez utiliser la classe [**WorkbookMetadata**](https://reference.aspose.com/cells/nodejs-cpp/workbookmetadata) pour charger le classeur.  
{{% /alert %}}  

Le code d'exemple suivant utilise la classe [**WorkbookMetadata**](https://reference.aspose.com/cells/nodejs-cpp/workbookmetadata) pour modifier les propriétés personnalisées d'un classeur. Une fois que vous avez ouvert le classeur en utilisant la classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), vous pourrez lire les propriétés du document. Voici un exemple de code utilisant la classe [**WorkbookMetadata**](https://reference.aspose.com/cells/nodejs-cpp/workbookmetadata).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open Workbook metadata
const options = new AsposeCells.MetadataOptions(AsposeCells.MetadataType.Document_Properties);
const meta = new AsposeCells.WorkbookMetadata(path.join(dataDir, "Sample1.xlsx"), options);

// Set some properties
meta.getCustomDocumentProperties().add("test", "test");

// Save the metadata info
meta.save(path.join(dataDir, "Sample2.out.xlsx"));

// Open the workbook
const w = new AsposeCells.Workbook(path.join(dataDir, "Sample2.out.xlsx"));

// Read document property
console.log(w.getCustomDocumentProperties().get("test"));

console.log("Press any key to continue...");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
