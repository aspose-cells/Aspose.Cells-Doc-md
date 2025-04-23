---  
title: Créer une ligne de signature dans un classeur Excel avec Aspose.Cells for Node.js via C++  
linktitle: Créer une ligne de signature dans un classeur Excel en utilisant Aspose.Cells  
type: docs  
weight: 150  
url: /fr/nodejs-cpp/create-signature-line-in-an-excel-workbook-using-aspose-cells/  
description: Cet article explique comment créer une ligne de signature dans un classeur Excel en utilisant Node.js avec Aspose.Cells for Node.js via C++.  
keywords: Créer une ligne de signature dans un classeur Excel en Node.js via C++, Comment créer une ligne de signature dans un classeur Excel, Comment ajouter une ligne de signature, Comment ajouter une ligne de signature à un fichier Excel.  
---  

## **Introduction**  

Microsoft Excel permet d'ajouter une **ligne de signature** dans les classeurs Excel. Vous pouvez ajouter une ligne de signature en cliquant sur l'onglet **Insertion** puis en sélectionnant **Ligne de signature** dans le groupe **Texte**.  

## **Comment créer une ligne de signature pour Excel**  

Aspose.Cells for Node.js via C++ offre également cette fonctionnalité et a exposé la propriété [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--) à cette fin. Cet article expliquera comment utiliser cette propriété pour ajouter une ligne de signature avec Aspose.Cells.  

Le code d'exemple suivant ajoute une ligne de signature en utilisant la propriété [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--) et enregistre le classeur.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Create signature line object
const signatureLine = new AsposeCells.SignatureLine();
signatureLine.setSigner("John Doe");
signatureLine.setTitle("Development Lead");
signatureLine.setEmail("john.doe@aspose.com");

// Adds a Signature Line to the worksheet.
workbook.getWorksheets().get(0).getShapes().addSignatureLine(1, 1, signatureLine);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

