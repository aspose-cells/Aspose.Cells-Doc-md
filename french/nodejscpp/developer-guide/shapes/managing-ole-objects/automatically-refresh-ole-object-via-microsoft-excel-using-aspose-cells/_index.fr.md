---  
title: Rafraîchir automatiquement l objet OLE via Microsoft Excel en utilisant Aspose.Cells for Node.js via C++  
linktitle: Actualiser automatiquement un objet OLE via Microsoft Excel en utilisant Aspose.Cells  
type: docs  
weight: 270  
url: /fr/nodejs-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/  
description: Apprenez comment rafraîchir automatiquement les objets OLE dans Excel en utilisant Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Aspose.Cells propose la propriété [**OleObject.getAutoLoad()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getAutoLoad--) pour rafraîchir l'objet OLE lorsque le fichier Excel est ouvert dans Microsoft Excel. Grâce à cette propriété, l'objet OLE affichera l'image OLE correcte générée par Microsoft Excel.  
{{% /alert %}}  

Le code d'exemple suivant charge le [fichier Excel d'exemple](5115231.xlsx) qui contient une image OLE non réelle. L'objet OLE est en fait un document Microsoft Word mais le fichier Excel d'exemple affiche l'image d'animal au lieu de l'image de Microsoft Word. Mais si vous ouvrez le [fichier Excel de sortie](5115225.xlsx), vous verrez que Microsoft Excel affiche l'image OLE correcte.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object from your sample excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample_oleobject.xlsx"));

// Access first worksheet
const sheet = workbook.getWorksheets().get(0);

// Set auto load property of first ole object to true
sheet.getOleObjects().get(0).setAutoLoad(true);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "RefreshOLEObjects_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  
