---  
title: Gestion des objets OLE avec Node.js via C++  
linktitle: Gestion des objets OLE  
type: docs  
weight: 50  
url: /fr/nodejs-cpp/managing-ole-objects/  
description: Apprenez comment gérer les objets OLE dans Aspose.Cells for Node.js via C++. Ajoutez, extrayez et manipulez des objets OLE dans les feuilles de calcul.  
---  

## **Introduction**  

OLE (Linking et Embedding d’Objets) est un cadre pour la technologie de documents composés. En bref, un document composé est quelque chose comme un bureau d'affichage pouvant contenir des objets visuels et informatifs de toutes sortes : texte, calendriers, animations, sons, vidéos en mouvement, 3D, actualités mises à jour en continu, contrôles, etc. Chaque objet de bureau est une entité de programme indépendante pouvant interagir avec un utilisateur et aussi communiquer avec d'autres objets sur le bureau.  

OLE est supporté par de nombreux programmes différents et est utilisé pour rendre le contenu créé dans un programme accessible dans un autre. Par exemple, vous pouvez insérer un document Microsoft Word dans Microsoft Excel. Pour voir quels types de contenu vous pouvez insérer, cliquez sur **Objet** dans le menu **Insertion**. Seuls les programmes installés sur l'ordinateur et supportant les objets OLE apparaissent dans la boîte **Type d'objet**.  

### **Insertion d'objets OLE dans la feuille de calcul**  

Aspose.Cells for Node.js via C++ prend en charge l'ajout, l'extraction et la manipulation d'objets OLE dans les feuilles de calcul. Pour cette raison, Aspose.Cells possède la classe [**OleObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/oleobjectcollection), utilisée pour ajouter un nouvel objet OLE à la collection. Une autre classe, [**OleObject**](https://reference.aspose.com/cells/nodejs-cpp/oleobject), représente un objet OLE. Elle possède quelques membres importants:  

- La propriété [**getImageData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getImageData--) spécifie les données d'image (icône) de type tableau d'octets. L'image sera affichée pour montrer l'objet OLE dans la feuille de calcul.  
- La propriété [**getObjectData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getObjectData--) spécifie les données de l'objet sous forme de tableau d'octets. Ces données seront affichées dans leur programme associé lors d'un double-clic sur l'icône de l'objet OLE.  

L'exemple suivant montre comment ajouter un ou des objets OLE dans une feuille de calcul.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define a string variable to store the image path.
const imageUrl = path.join(dataDir, "logo.jpg");

// Get the picture into the streams.
const imageData = fs.readFileSync(imageUrl);

// Get an excel file path in a variable.
const filePath = path.join(dataDir, "book1.xls");

// Get the file into the streams.
const objectData = fs.readFileSync(filePath);

// Add an Ole object into the worksheet with the image
// Shown in MS Excel.
sheet.getOleObjects().add(14, 3, 200, 220, imageData);

// Set embedded ole object data.
sheet.getOleObjects().get(0).setObjectData(objectData);

// Save the excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

### **Extraction d'objets OLE dans le classeur**  

L'exemple suivant montre comment extraire des objets OLE dans un classeur. L'exemple récupère différents objets OLE à partir d'un fichier XLS existant et enregistre différents fichiers (DOC, XLS, PPT, PDF, etc.) en fonction du type de format de fichier de l'objet OLE.  

Après l'exécution du code, nous pouvons enregistrer différents fichiers en fonction de leurs types de format respectifs des objets OLE.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Get the OleObject Collection in the first worksheet.
const oles = workbook.getWorksheets().get(0).getOleObjects();

// Loop through all the oleobjects and extract each object.
for (let i = 0; i < oles.getCount(); i++) {
const ole = oles.get(i);

// Specify the output filename.
let fileName = path.join(dataDir, `ole_${i}.`);

// Specify each file format based on the oleobject format type.
switch (ole.getFileFormatType()) {
case AsposeCells.FileFormatType.Doc:
fileName += "doc";
break;
case AsposeCells.FileFormatType.Xlsx:
fileName += "xlsx";
break;
case AsposeCells.FileFormatType.Ppt:
fileName += "ppt";
break;
case AsposeCells.FileFormatType.Pdf:
fileName += "pdf";
break;
case AsposeCells.FileFormatType.Unknown:
fileName += "jpg";
break;
default:
//........
break;
}

// Save the oleobject as a new excel file if the object type is xls.
if (ole.getFileFormatType() === AsposeCells.FileFormatType.Xlsx) {
const ms = new Uint8Array(ole.getObjectData());
const oleBook = new AsposeCells.Workbook(ms);
oleBook.getSettings().setIsHidden(false);
oleBook.save(path.join(dataDir, `Excel_File${i}.out.xlsx`));
}

// Create the files based on the oleobject format types.
else {
fs.writeFileSync(fileName, ole.getObjectData());
}
}
```  

### **Extraction des fichiers MOL intégrés**  

Aspose.Cells for Node.js via C++ prend en charge l'extraction d'objets de types rares comme MOL (fichier de données moléculaires contenant des informations sur les atomes et les liaisons). Le code suivant démontre l'extraction d'un fichier MOL intégré et sa sauvegarde sur le disque en utilisant ce [fichier Excel d'exemple](94896196.xlsx).  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// Directories
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "EmbeddedMolSample.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
let index = 1;

const worksheets = workbook.getWorksheets();
const sheetCount = worksheets.getCount();
for (let i = 0; i < sheetCount; i++) {
const sheet = worksheets.get(i);
const oles = sheet.getOleObjects();
const oleCount = oles.getCount();
for (let j = 0; j < oleCount; j++) {
const ole = oles.get(j);
const fileName = path.join(outputDir, `OleObject${index}.mol`);
const fileStream = fs.createWriteStream(fileName);
fileStream.write(Buffer.from(ole.getObjectData()));
fileStream.end();
index++;
}
}
```  

## **Sujets avancés**  
- [Accéder et modifier l'étiquette d'affichage de l'objet Ole lié](/cells/fr/nodejs-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/)  
- [Rafraîchir automatiquement un objet OLE via Microsoft Excel en utilisant Aspose.Cells](/cells/fr/nodejs-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)  
- [Extraire des objets OLE du classeur](/cells/fr/nodejs-cpp/extract-ole-objects-from-workbook/)  
- [Obtenir ou définir l'identifiant de classe de l'objet OLE incorporé](/cells/fr/nodejs-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/)  
- [Insérer un fichier WAV en tant qu'objet Ole](/cells/fr/nodejs-cpp/inserting-a-wav-file-as-an-ole-object/)  


