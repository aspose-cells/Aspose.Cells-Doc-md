---  
title: Extraire les objets OLE du classeur avec Node.js via C++  
linktitle: Extraire les objets OLE du classeur  
type: docs  
weight: 110  
url: /fr/nodejs-cpp/extract-ole-objects-from-workbook/  
---  

{{% alert color="primary" %}}  
Parfois, vous devez extraire les objets OLE d'un classeur. Aspose.Cells supporte l'extraction et la sauvegarde de ces objets OLE.

Cet article montre comment créer une application console en Node.js via C++ et extraire différents objets OLE d'un classeur en quelques lignes de code simples.  
{{% /alert %}}  

## **Extraire les objets OLE d'un classeur**  

### **Création d'un classeur modèle**  

1. Créez un classeur dans Microsoft Excel.  
1. Ajoutez un document Microsoft Word, un classeur Excel et un document PDF en tant qu'objets OLE sur la première feuille.  

|**Document de modèle avec des objets OLE (OleFile.xls)**|  
| :- |  
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|  

Ensuite, extrayez les objets OLE et sauvegardez-les sur le disque dur avec leurs types de fichiers respectifs.  

### **Téléchargez et installez Aspose.Cells**  

1. [Téléchargez Aspose.Cells for Node.js via C++](https://downloads.aspose.com/cells/nodejs-cpp).  
1. Installez-le sur votre ordinateur de développement.  

Tous les composants Aspose, une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et n'injecte que des filigranes dans les documents produits.  

### **Créer un projet**  

Démarrez **Node.js** et créez une nouvelle application console. Cet exemple montrera une application console Node.js, mais vous pouvez également utiliser n'importe quel environnement compatible JavaScript.  

1. Ajouter des dépendances  
   1. Ajoutez une référence au composant Aspose.Cells dans votre projet, par exemple, incluez le package en utilisant la fonction `require` :  
   ```javascript  
   const { Cells } = require("aspose.cells");  
   ```

### **Extraire des objets OLE**  

Le code ci-dessous effectue le travail réel de recherche et d'extraction des objets OLE. Les objets OLE (fichiers DOC, XLS, et PDF) sont enregistrés sur le disque.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "oleFile.xlsx"));

// Get the OleObject Collection in the first worksheet.
const oles = workbook.getWorksheets().get(0).getOleObjects();

// Loop through all the oleobjects and extract each object in the worksheet.
for (let i = 0; i < oles.getCount(); i++) {
const ole = oles.get(i);
// Specify the output filename.
let fileName = path.join(dataDir, "outOle" + i + ".");
// Specify each file format based on the oleobject format type.
switch (ole.getFileFormatType()) {
case AsposeCells.FileFormatType.Doc:
fileName += "doc";
break;
case AsposeCells.FileFormatType.Excel97To2003:
fileName += "Xlsx";
break;
case AsposeCells.FileFormatType.Ppt:
fileName += "Ppt";
break;
case AsposeCells.FileFormatType.Pdf:
fileName += "Pdf";
break;
case AsposeCells.FileFormatType.Unknown:
fileName += "Jpg";
break;
default:
//........
break;
}
// Save the oleobject as a new excel file if the object type is xls.
if (ole.getFileFormatType() === AsposeCells.FileFormatType.Xlsx) {
const ms = Buffer.from(ole.getObjectData());
if (ole.getObjectData() != null) {
const oleBook = new AsposeCells.Workbook(ms);
oleBook.getSettings().setIsHidden(false);
oleBook.save(path.join(dataDir, "outOle" + i + ".out.xlsx"));
}
} else {
if (ole.getObjectData() != null) {
fs.writeFileSync(fileName, ole.getObjectData());
}
}
}
```  

