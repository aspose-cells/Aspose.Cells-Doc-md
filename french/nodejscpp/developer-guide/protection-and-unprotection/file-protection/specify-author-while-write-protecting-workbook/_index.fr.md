---  
title: Spécifier l auteur lors de la protection en écriture d un classeur avec Node.js via C++  
linktitle: Spécifier l auteur lors de la protection par mot de passe du classeur  
type: docs  
weight: 40  
url: /fr/nodejs-cpp/specify-author-while-write-protecting-workbook/  
description: Spécifier un nom d auteur lors de la protection en écriture d un classeur utilisant Aspose.Cells for Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**

Vous pouvez spécifier un nom d'auteur lors de la protection en écriture de votre classeur utilisant l'API Aspose.Cells. Veuillez utiliser la propriété [**Workbook.getAuthor()**](https://reference.aspose.com/cells/nodejs-cpp/writeprotection/#getAuthor--) à cet effet.

## **Spécifier l'auteur lors de la protection en écriture du classeur**

Le code d'exemple suivant explique l'utilisation de la propriété [**Workbook.getAuthor()**](https://reference.aspose.com/cells/nodejs-cpp/writeprotection/#getAuthor--). Le code crée un classeur vide, le protège par mot de passe, spécifie le nom de l'auteur et l'enregistre en tant que [fichier Excel de sortie](67338582.xlsx). La capture d'écran suivante illustre l'effet du code d'exemple sur le fichier Excel de sortie pour votre référence.

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Create empty workbook.
const workbook = new AsposeCells.Workbook();

// Write protect workbook with password.
workbook.getSettings().getWriteProtection().setPassword("1234");

// Specify author while write protecting workbook.
workbook.getSettings().getWriteProtection().setAuthor("SimonAspose");

// Save the workbook in XLSX format.
const outputDir = path.join(__dirname, "output");
workbook.save(path.join(outputDir, "outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx"));
```  

