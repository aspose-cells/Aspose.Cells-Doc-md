---
title: Extraire des images des feuilles de calcul en utilisant ImageOrPrintOptions avec Node.js via C++
linktitle: Extraire des images des feuilles de calcul à l aide des options d image ou d impression
type: docs
weight: 140
url: /fr/nodejs-cpp/extract-images-from-worksheets-using-imageorprintoptions/
description: Apprenez comment extraire des images des feuilles Excel et les sauvegarder en utilisant Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}} 

Les utilisateurs de Microsoft Excel peuvent ajouter des images aux feuilles de calcul. Avec Aspose.Cells for Node.js via C++, il est possible de lire des images à partir de fichiers Excel Microsoft et de les enregistrer sur un disque local. Cet article montre comment.

{{% /alert %}} 

Le code d'exemple ci-dessous montre comment extraire des images à partir d'un fichier Excel et les enregistrer.



```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open a template Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleExtractImagesFromWorksheets.xlsx"));

// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get the first Picture in the first worksheet
const pic = worksheet.getPictures().get(0);

// Set the output image file path
const picformat = pic.getImageType().toString();

// Note: you may evaluate the image format before specifying the image path
// Define ImageOrPrintOptions
const printoption = new AsposeCells.ImageOrPrintOptions();

// Specify the image format
printoption.setImageType(AsposeCells.ImageType.Jpeg);

// Save the image
pic.toImage(path.join(outputDir, "outputExtractImagesFromWorksheets.jpg"), printoption);
```
