---
title: Insérer une image d arrière plan dans Excel avec Node.js via C++
linktitle: Insérer une image d arrière plan dans Excel
type: docs
weight: 90
url: /fr/nodejs-cpp/insert-background-image-to-excel/
description: "Comment insérer une image d arrière plan dans Excel en utilisant Aspose.Cells for Node.js via C++."
---

{{% alert color="primary" %}} 

Vous pouvez rendre une feuille de calcul plus attrayante en ajoutant une image en arrière-plan. Cette fonctionnalité peut être très efficace si vous avez une illustration graphique d'entreprise spéciale qui ajoute une touche de fond sans obscurcir les données sur la feuille. Vous pouvez configurer une image d'arrière-plan pour une feuille à l'aide de l'API Aspose.Cells.

{{% /alert %}} 

## **Configuration de l'arrière-plan de la feuille dans Microsoft Excel**

Pour définir une image d'arrière-plan de la feuille dans Microsoft Excel (par exemple, Microsoft Excel 2019) :

1. Dans le menu **Mise en page**, recherchez l'option **Configuration de la page**, puis cliquez sur l'option **Arrière-plan**.
1. Sélectionnez une image pour définir l'arrière-plan de la feuille.

   **Configuration d'un arrière-plan de feuille**

![todo:image_alt_text](insert-background-to-excel.jpg)

## ** Définir l'arrière-plan de la feuille avec Aspose.Cells for Node.js via C++**

Le code ci-dessous définit une image d'arrière-plan à l'aide d'une image provenant d'un flux.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const backgroundImagePath = path.join(dataDir, "background.jpg");

// Create a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Set the background image for the worksheet.
sheet.setBackgroundImage(fs.readFileSync(backgroundImagePath).buffer);

// Save the Excel file
workbook.save("outputBackImageSheet.xlsx");

// Save the HTML file
workbook.save("outputBackImageSheet.html", AsposeCells.SaveFormat.Html);
```

## Articles Connexes

- [Travailler avec l'arrière-plan dans les fichiers ODS](/cells/fr/nodejs-cpp/working-with-background-in-ods-files/)

