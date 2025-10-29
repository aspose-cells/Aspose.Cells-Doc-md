---  
title: Implémenter une taille de papier personnalisée pour la feuille lors du rendu avec Node.js via C++  
linktitle: Implémenter une taille de papier personnalisée de la feuille de calcul pour le rendu  
type: docs  
weight: 70  
url: /fr/nodejs-cpp/implement-custom-paper-size-of-worksheet-for-rendering/  
description: Cet article explique comment utiliser l’API Node.js via C++ pour définir une taille de papier personnalisée pour vos feuilles désirées lors du rendu d’un fichier Excel au format PDF de manière programmatique.  
keywords: définir une taille de papier personnalisée lors du rendu d’un Excel en PDF Node.js via C++  
---  

## **Scénarios d'utilisation possibles**  

Il n’existe pas d’option directe pour créer des tailles de papier personnalisées dans MS Excel, cependant, vous pouvez définir une taille de papier personnalisée pour vos feuilles désirées lors du rendu d’un fichier Excel en PDF. Ce document explique comment définir une taille de papier personnalisée d’une feuille en utilisant les API Aspose.Cells.  

## **Implémenter une taille de papier personnalisée de la feuille de calcul pour le rendu**  

Aspose.Cells permet de mettre en œuvre la taille de papier souhaitée pour la feuille de calcul. Vous pouvez utiliser la méthode [**PageSetup.customPaperSize(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#customPaperSize-number-number-) de la classe [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/) pour spécifier une taille de page personnalisée. Le code d'exemple suivant illustre comment spécifier une taille de papier personnalisée pour la première feuille de calcul du classeur. Veuillez également consulter le [PDF de sortie](45056028.pdf) généré avec le code ci-dessous pour référence.  

## **Capture d'écran**  

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)  

## **Code d'exemple**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Set custom paper size in unit of inches
ws.getPageSetup().customPaperSize(6, 4);

// Access cell B4
const b4 = ws.getCells().get("B4");

// Add the message in cell B4
b4.putValue("Pdf Page Dimensions: 6.00 x 4.00 in");

// Save the workbook in pdf format
wb.save(path.join(dataDir, "outputCustomPaperSize.pdf"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
