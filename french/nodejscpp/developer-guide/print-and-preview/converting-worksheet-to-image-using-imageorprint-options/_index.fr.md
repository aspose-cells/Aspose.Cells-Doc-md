---  
title: Conversion de feuille de calcul en image en utilisant les options ImageOrPrint avec Node.js via C++  
linktitle: Convertir une feuille de calcul en image en utilisant des options ImageOrPrint  
type: docs  
weight: 90  
url: /fr/nodejs-cpp/converting-worksheet-to-image-using-imageorprint-options/  
description: Apprenez comment convertir une feuille de calcul en fichier image et appliquer différentes options d image et d impression en utilisant Aspose.Cells for Node.js via C++.   
---  

{{% alert color="primary" %}}  
Ce document est conçu pour fournir une compréhension détaillée de la manière de convertir une feuille de calcul en fichier image et d'appliquer différentes options d'image et d'impression pour l'image, comme la résolution, la compression TIFF, le format d'image et la qualité de page.  
{{% /alert %}}  

## **Enregistrement de feuilles de calcul en images - différentes approches**  

Parfois, vous pourriez avoir besoin de présenter vos feuilles de calcul sous forme de représentation imagée. Vous devez présenter les images de feuilles de calcul dans vos applications ou pages web. Vous pourriez avoir besoin d'insérer les images dans un document Word, un fichier PDF, une présentation PowerPoint ou les utiliser dans un autre contexte. Tout simplement, vous souhaitez une feuille de calcul rendue sous forme d'image afin de pouvoir l'utiliser ailleurs. Aspose.Cells prend en charge la conversion des feuilles de calcul dans des fichiers Excel en images. De plus, Aspose.Cells prend en charge la définition de différentes options telles que le format d'image, la résolution (verticale et horizontale), la qualité d'image et d'autres options d'image et d'impression.  

Vous pouvez essayer l'automatisation Office, mais celle-ci présente ses propres inconvénients. Il existe plusieurs raisons et problèmes impliqués : par exemple, sécurité, stabilité, évolutivité et vitesse, prix, et fonctionnalités. En résumé, il y a de nombreuses raisons, la principale étant que Microsoft recommande vivement de ne pas utiliser l'automatisation Office à partir de solutions logicielles.  

Cet article montre comment créer une application console dans Visual Studio .NET, effectuer la conversion d'une feuille de calcul en image en utilisant différentes options d'image et d'impression avec quelques lignes de code les plus simples à l'aide de l'API Aspose.Cells.  

La classe [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/) représente une feuille de calcul pour rendre des images, elle a une méthode [**toImage(number)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-) surchargée qui peut convertir directement une feuille en fichier(s) image avec vos attributs ou options souhaités. Elle peut renvoyer un objet que vous pouvez enregistrer en image sur le disque/flux. Plusieurs formats d'image sont supportés, par exemple BMP, PNG, GIF, JPEG, TIFF, EMF, etc.  

## **Utilisation d'Aspose.Cells pour convertir une feuille de calcul en image en utilisant des options ImageOrPrint.**  

### **Création d'un classeur modèle dans Microsoft Excel**  

J'ai créé un nouveau classeur dans MS Excel et ajouté des données dans la première feuille de calcul. Maintenant, je vais convertir la feuille de calcul du fichier modèle "Feuille1" en un fichier image "FeuilleImage.tiff" et appliquer différentes options d'image comme les résolutions horizontales et verticales, la compression Tiff, etc.  

### **Téléchargez et installez Aspose.Cells**  

Tout d'abord, vous devez [télécharger](https://downloads.aspose.com/cells/nodejs-cpp) Aspose.Cells for Node.js via C++. Installez-le sur votre ordinateur de développement. Tous les composants [Aspose](http://www.aspose.com/) installés fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et n'injecte que des filigranes dans les documents produits.  

### **Créer un projet**  

Démarrez votre environnement de développement préféré (par exemple, Visual Studio). Créez une nouvelle application console.  

### **Ajouter des références**  

Ce projet utilisera Aspose.Cells. Vous devez donc ajouter une référence au composant Aspose.Cells dans votre projet. Par exemple, ajoutez une référence à ….\Program Files\Aspose\Aspose.Cells for Node.js via C++\Bin\Aspose.Cells.node  

### **Convertir une feuille de calcul en un fichier image**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Open template
const filePath = path.join(sourceDir, "sampleWorksheetToAnImage.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Apply different Image and Print options
const options = new AsposeCells.ImageOrPrintOptions(); // Corrected: Added the instantiation for ImageOrPrintOptions.

// Set Horizontal Resolution
options.setHorizontalResolution(300);

// Set Vertical Resolution
options.setVerticalResolution(300);

// Set TiffCompression
options.setTiffCompression(AsposeCells.TiffCompression.CompressionLZW);

// Set Image Format
options.setImageType(AsposeCells.ImageType.Tiff);

// Set printing page type
options.setPrintingPage(AsposeCells.PrintingPageType.Default);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, options);

// Render/save the image for the sheet
const pageIndex = 3;
sr.toImage(pageIndex, path.join(outputDir, `outputWorksheetToAnImage_${pageIndex + 1}.tiff`));
```  

## **Options de conversion**  

Il est possible d'enregistrer des pages spécifiques en tant qu'images. Le code suivant convertit les première et deuxième feuilles de calcul dans un classeur en images JPG.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open a template excel file
const filePath = path.join(sourceDir, "sampleSpecificPagesToImages.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();

// Specify the image format
imgOptions.setImageType(AsposeCells.ImageType.Jpeg);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Specify page index to be rendered
const idxPage = 3;

// Render the third image for the sheet
const bitmap = sr.toImage(idxPage);

// Save the image file
const fs = require("fs");
fs.writeFileSync(path.join(outputDir, `outputSpecificPagesToImage_${idxPage + 1}.jpg`), bitmap);
```  

## **Conversion d'image à l'aide de WorkbookRender**  

Une image TIFF peut contenir plus d’un cadre. Vous pouvez enregistrer tout le classeur dans une seule image TIFF avec plusieurs cadres ou pages :  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleUseWorkbookRenderForImageConversion.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const opts = new AsposeCells.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Tiff);

const workbookRender = new AsposeCells.WorkbookRender(workbook, opts);
workbookRender.toImage(path.join(outputDir, "outputUseWorkbookRenderForImageConversion.tiff"));
```  


