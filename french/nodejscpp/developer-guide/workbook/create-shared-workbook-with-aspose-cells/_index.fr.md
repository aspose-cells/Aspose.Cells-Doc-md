---  
title: Créer un classeur partagé avec Aspose.Cells for Node.js via C++  
linktitle: Créer un classeur partagé avec Aspose.Cells  
type: docs  
weight: 40  
url: /fr/nodejs-cpp/create-shared-workbook-with-aspose-cells/  
description: Apprenez comment créer un classeur partagé en utilisant Aspose.Cells for Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**  

Microsoft Excel vous permet de partager le classeur comme montré dans la capture d'écran suivante. Lorsque vous partagez le classeur, plus d'un utilisateur peut l'éditer sur le réseau. Aspose.Cells for Node.js via C++ permet de créer un classeur partagé avec la propriété [**WorkbookSettings.getShared()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShared--).  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)  

## **Créer un classeur partagé avec Aspose.Cells**  

Le code d'exemple suivant crée un classeur partagé en définissant la propriété [**WorkbookSettings.getShared()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShared--) à **true**. Lorsque vous ouvrez le [fichier Excel de sortie](55541786.xlsx) dans Microsoft Excel, vous verrez **Shared** avec le nom du classeur de sortie comme montré dans cette capture d'écran.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)  

## **Code d'exemple**  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create Workbook object
const wb = new AsposeCells.Workbook();

// Share the Workbook
wb.getSettings().setShared(true);

// Save the Shared Workbook
wb.save("outputSharedWorkbook.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
