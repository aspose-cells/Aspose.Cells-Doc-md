---  
title: Verrouillage du filigrane WordArt avec Node.js via C++  
linktitle: Verrouiller le filigrane WordArt  
type: docs  
weight: 170  
url: /fr/nodejs-cpp/locking-wordart-watermark/  
description: Apprenez comment verrouiller les filigranes WordArt en Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Les API Aspose.Cells permettent d’ajouter un filigrane WordArt sur la feuille de calcul de manière à ce que le WordArt devienne un objet que vous pouvez déplacer et positionner sur la feuille de calcul. Il est également possible de verrouiller l’objet WordArt pour toute interaction comme la modification, le déplacement et la sélection. Cet article explique l’utilisation de la méthode [**Shape.setLockedProperty(ShapeLockType, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/shape/#setLockedProperty-shapelocktype-boolean-) pour verrouiller certains aspects du filigrane.

{{% /alert %}}  

Les API Aspose.Cells permettent de verrouiller certains aspects du filigrane afin de limiter ou bloquer complètement l’interaction de l’utilisateur. Le fragment de code suivant démontre l’utilisation de Aspose.Cells for Node.js via C++ pour verrouiller la sélection, le déplacement, la modification et le redimensionnement du filigrane en créant une feuille de calcul à partir de zéro.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();

// Get the first default sheet
const sheet = workbook.getWorksheets().get(0);

// Add Watermark
const wordart = sheet.getShapes().addTextEffect(AsposeCells.MsoPresetTextEffect.TextEffect1,
"CONFIDENTIAL", "Arial Black", 50, false, true, 18, 8, 1, 1, 130, 800);

// Lock Shape Aspects
wordart.setIsLocked(true);
wordart.setLockedProperty(AsposeCells.ShapeLockType.Selection, true);
wordart.setLockedProperty(AsposeCells.ShapeLockType.ShapeType, true);
wordart.setLockedProperty(AsposeCells.ShapeLockType.Move, true);
wordart.setLockedProperty(AsposeCells.ShapeLockType.Resize, true);
wordart.setLockedProperty(AsposeCells.ShapeLockType.Text, true);

// Get the fill format of the word art
const wordArtFormat = wordart.getFill();

// Set the color
wordArtFormat.setOneColorGradient(AsposeCells.Color.Red, 0.2, AsposeCells.GradientStyleType.Horizontal, 2);

// Set the transparency
wordArtFormat.setTransparency(0.9);

// Make the line invisible
wordart.setHasLine(false);

// Save the file
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
