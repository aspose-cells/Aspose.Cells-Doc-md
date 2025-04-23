---  
title: Spécifier la version du document du fichier Excel en utilisant les propriétés intégrées du document avec Node.js via C++  
linktitle: Spécifier la version du document du fichier Excel en utilisant les propriétés de document intégrées  
type: docs  
weight: 20  
url: /fr/nodejs-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/  
description: Apprenez comment spécifier la version du document d un fichier Excel de manière programmatique en utilisant les propriétés intégrées du document avec Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**  

 Vous pouvez modifier le **Numéro de version** d'un fichier Excel en cliquant avec le bouton droit sur le fichier, puis en sélectionnant Propriétés > Détails et en modifiant le champ **Numéro de version**. Veuillez utiliser la propriété [**BuiltInDocumentPropertyCollection.getDocumentVersion()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getDocumentVersion--) pour la changer de manière programmatique avec Aspose.Cells APIs.  

## **Spécifier la version du document du fichier Excel à l'aide des propriétés de document intégrées**  

 Le code d'exemple suivant crée un classeur et modifie ses propriétés intégrées du document, notamment le Titre, les Auteurs et le Numéro de version. Veuillez consulter le [fichier Excel de sortie](64716811.xlsx) généré par le code et la capture d'écran qui montre la modification du numéro de version par la propriété [**BuiltInDocumentPropertyCollection.getDocumentVersion()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getDocumentVersion--).  

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)  

## **Code d'exemple**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "outputSpecifyDocumentVersionOfExcelFile.xlsx");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access built-in document property collection
const bdpc = wb.getBuiltInDocumentProperties();

// Set the title
bdpc.setTitle("Aspose File Format APIs");

// Set the author
bdpc.setAuthor("Aspose APIs Developers");

// Set the document version
bdpc.setDocumentVersion("Aspose.Cells Version - 18.3");

// Save the workbook in xlsx format
wb.save(filePath, AsposeCells.SaveFormat.Xlsx);
```  

