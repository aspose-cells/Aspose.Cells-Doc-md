---  
title: Actualiser les valeurs des formes liées avec Node.js via C++  
linktitle: Actualiser les valeurs des formes liées  
type: docs  
weight: 3200  
url: /fr/nodejs-cpp/refresh-values-of-linked-shapes/  
description: Apprenez comment actualiser les valeurs des formes liées dans Excel en utilisant Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Parfois, vous avez une forme liée dans votre fichier Excel qui est reliée à une cellule. Dans Microsoft Excel, modifier la valeur de la cellule liée modifie également la valeur de la forme liée. Ceci fonctionne également avec Aspose.Cells for Node.js via C++ si vous souhaitez sauvegarder votre classeur en format XLS ou XLSX. Cependant, si vous souhaitez sauvegarder en PDF ou en HTML, vous devrez appeler la méthode [**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#updateSelectedValue--) pour actualiser la valeur de la forme liée.  

{{% /alert %}}  

## Exemple  

La capture d'écran suivante montre le fichier Excel source utilisé dans l'exemple ci-dessous. Il dispose d'une image liée liée aux cellules A1 à E4. Nous allons changer la valeur de la cellule B4 avec Aspose.Cells puis appeler la méthode [**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#updateSelectedValue--) pour actualiser la valeur de l'image et l'enregistrer au format PDF.  

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)  

Vous pouvez télécharger le [fichier Excel source](95584291.xlsx) et le [PDF de sortie](95584292.pdf) à partir des liens donnés.  

### Code Node.js pour actualiser les valeurs des formes liées  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook from source file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleRefreshValueOfLinkedShapes.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Change the value of cell B4
const cell = worksheet.getCells().get("B4");
cell.putValue(100);

// Update the value of the Linked Picture which is linked to cell B4
worksheet.getShapes().updateSelectedValue();

// Save the workbook in PDF format
workbook.save(path.join(outputDir, "outputRefreshValueOfLinkedShapes.pdf"), AsposeCells.SaveFormat.Pdf);
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
