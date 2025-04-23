---
title: Spécifier la langue du fichier Excel en utilisant les propriétés intégrées du document avec Node.js via C++
linktitle: Spécifier la langue du fichier Excel en utilisant les propriétés de document intégrées
type: docs
weight: 30
url: /fr/nodejs-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/
---

## **Scénarios d'utilisation possibles**

 Vous pouvez changer la langue d'un fichier Excel en cliquant avec le bouton droit sur le fichier, puis en sélectionnant Propriétés > Détails et en modifiant le champ Langue. Veuillez utiliser la propriété [**BuiltInDocumentPropertyCollection.getLanguage()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLanguage--) pour la changer de manière programmatique avec les API Aspose.Cells for Node.js via C++.

## **Spécifier la langue du fichier Excel en utilisant les propriétés de document intégrées**

 Le code d'exemple suivant crée un classeur et modifie sa propriété du document intégrée nommée langue. Veuillez consulter le [fichier Excel de sortie](64716891.xlsx) généré par le code et la capture d'écran montrant le champ Langue modifié par la propriété [**BuiltInDocumentPropertyCollection.getLanguage()**](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLanguage--).

![todo:image_alt_text](specify-the-language-of-the-excel-file-using-builtin-document-properties_1.png)

## **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create workbook object.
const wb = new AsposeCells.Workbook();

// Access built-in document property collection.
const bdpc = wb.getBuiltInDocumentProperties();

// Set the language of the Excel file.
bdpc.setLanguage("German, French");

// Save the workbook in xlsx format.
wb.save(path.join(outputDir, "outputSpecifyLanguageOfExcelFileUsingBuiltInDocumentProperties.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
