---  
title: Définir la couleur de l onglet de la feuille avec Node.js via C++  
linktitle: Définir la couleur de l onglet de la feuille de calcul  
type: docs  
weight: 120  
url: /fr/nodejs-cpp/set-worksheet-tab-color/  
description: Cet article présente un exemple de code qui définit la couleur de l onglet d une feuille Excel automatiquement en utilisant Node.js via C++.  
keywords: définir la couleur de l onglet Excel avec Node.js via C++, code pour définir la couleur de l onglet Excel en Node.js via C++  
---  

{{% alert color="primary" %}}  

Aspose.Cells vous permet de changer la couleur des onglets de feuille de calcul individuels pour les rendre plus visibles par rapport au reste. Par exemple, vous pouvez mettre Dépenses en rouge, Ventes en vert, Actifs en bleu, etc.

{{% /alert %}}  
## **Définition de la couleur de l'onglet de feuille de calcul avec Microsoft Excel**  
1. Cliquez avec le bouton droit sur un onglet dans la feuille d'onglets en bas de la feuille de calcul actuelle.  
1. Sélectionnez **Couleur d'onglet**.  
1. Sélectionnez une couleur dans la palette.  
1. Cliquez sur **OK**.  
## **Définir la couleur de l'onglet de la feuille de calcul avec Aspose.Cells**  
Le code d'exemple ci-dessous montre comment définir la couleur de l'onglet avec Aspose.Cells.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"));

// Get the first worksheet in the book
const worksheet = workbook.getWorksheets().get(0);

// Set the tab color
worksheet.setTabColor(AsposeCells.Color.Red);

// Save the Excel file
workbook.save(path.join(dataDir, "worksheettabcolor.out.xls"));
```  

