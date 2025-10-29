---  
title: Conversion de feuille de calcul en image et feuille de calcul en images par page avec Node.js via C++  
linktitle: Conversion de la feuille de calcul en image et de la feuille de calcul en image par page  
type: docs  
weight: 80  
url: /fr/nodejs-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/  
---  

{{% alert color="primary" %}}  
Ce document est conçu pour fournir aux développeurs une compréhension détaillée de la manière de convertir une feuille de calcul en un fichier image et une feuille à pages multiples en un fichier image par page.  

Parfois, vous pourriez avoir besoin de présenter des feuilles de calcul en tant qu'images, par exemple, pour les utiliser dans des applications ou des pages web. Vous pourriez avoir besoin d'insérer les images dans un document Word, un fichier PDF, une présentation PowerPoint ou les utiliser dans un autre scénario. Fondamentalement, vous voulez afficher la feuille de calcul sous forme d'image. Aspose.Cells prend en charge la conversion des feuilles de calcul dans les fichiers Microsoft Excel en images. De plus, Aspose.Cells prend en charge la conversion d'un classeur en plusieurs fichiers image, un par page.  

Vous pourriez utiliser l'automatisation Office pour y parvenir, mais l'automatisation Office a ses propres inconvénients. Il existe plusieurs raisons et problèmes impliqués : par exemple la sécurité, la stabilité, la scalabilité/la vitesse, le prix et les fonctionnalités. En bref, il existe de nombreuses raisons, mais la principale est que Microsoft elle-même déconseille fortement l'automatisation Office.  
{{% /alert %}}  

## **Utiliser Aspose.Cells for Node.js via C++ pour convertir une feuille de calcul en fichier image**  

Cet article montre comment créer une application console, convertir une feuille de calcul en image, et convertir une feuille en une seule image pour chaque feuille avec quelques lignes de code simples en utilisant l'API Aspose.Cells.  

Vous devez importer plusieurs classes utiles liées aux fonctionnalités de rendu dans votre programme ou projet, telles que [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/nodejs-cpp/workbookrender/), etc. La classe [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/) représente une feuille de calcul pour rendre des images de la feuille et possède une méthode [**toImage(number)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-) surchargée qui peut convertir directement une feuille en fichiers image avec tous attributs ou options définis. Elle peut renvoyer un objet image et vous pouvez enregistrer un fichier image sur le disque/flux. Plusieurs formats d'image sont supportés, par exemple BMP, PNG, GIF, JPG, JPEG, TIFF, EMF, et autres.  

Cet article explique comment :  

- Convertir une feuille de calcul en une image  
- Convertir chaque page d'une feuille de calcul en une image  

Cette tâche montre comment utiliser Aspose.Cells pour convertir une feuille de calcul à partir d'un classeur modèle en un fichier image.  

### **Configurer le projet**  

1. Tout d'abord, [téléchargez Aspose.Cells for Node.js via C++](https://downloads.aspose.com/cells/nodejs-cpp).  
1. Installez-le sur votre ordinateur de développement. Tous les composants [Aspose](http://www.aspose.com/) installés fonctionnent en mode d'évaluation. Ce mode n'a pas de limite de temps et n'injecte que des filigranes dans les documents produits. Démarrez votre environnement de développement et créez une nouvelle application console. Cet exemple utilise une application console Node.js, mais vous pouvez utiliser n'importe quelle configuration intégrée avec Node.js. Ajoutez une référence à Aspose.Cells dans le projet créé.  

### **Convertir une feuille de calcul en un fichier image**  

J'ai créé un nouveau classeur dans Microsoft Excel et ajouté des données dans la première feuille de calcul : **Testbook.xlsx** (1 feuille de calcul). Ensuite, convertissez la feuille de calcul du fichier modèle en un fichier image appelé SheetImage.jpg.  

Voici le code utilisé par le composant pour accomplir la tâche. Il convertit la Feuille1 dans **Testbook.xlsx** en un fichier image pour expliquer à quel point cette conversion est facile.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open a template excel file
const filePath = path.join(sourceDir, "sampleConvertWorksheettoImageFile.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();
imgOptions.setOnePagePerSheet(true);

// Specify the image format
imgOptions.setImageType(AsposeCells.ImageType.Jpeg);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Save the image file
const outputFilePath = outputDir + "outputConvertWorksheettoImageFile.jpg";

sr.toImage(0, outputFilePath);
```  

## **Utiliser Aspose.Cells for Node.js via C++ pour convertir une feuille de calcul en fichier image par page**  

Cet exemple montre comment utiliser Aspose.Cells pour convertir une feuille de calcul d'un classeur modèle comportant plusieurs pages en un fichier image unique par page.  

### **Convertir une feuille de calcul en image par page**  

J'ai créé un nouveau classeur dans Microsoft Excel et ajouté des données dans la première feuille de calcul : **Testbook2.xlsx** (1 feuille de calcul).  

Maintenant, convertissez la feuille de calcul du fichier modèle en fichiers image (un fichier par page). Comme j'ai déjà créé l'application console pour effectuer la tâche de copie, je vais ignorer ces étapes de création de l'application console et passer directement aux étapes de conversion de la feuille de calcul.  

Voici le code utilisé par le composant pour accomplir la tâche. Il convertit Sheet1 dans Testbook2.xlsx en fichiers image par page.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleConvertWorksheetToImageByPage.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

const options = new AsposeCells.ImageOrPrintOptions();
options.setHorizontalResolution(200);
options.setVerticalResolution(200);
options.setImageType(AsposeCells.ImageType.Tiff);

// Sheet2Image By Page conversion
const sr = new AsposeCells.SheetRender(sheet, options);
for (let j = 0; j < sr.getPageCount(); j++) 
{
sr.toImage(j, outputDir + "outputConvertWorksheetToImageByPage_" + (j + 1) + ".tif");
}
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
