---
title: Insérer une image basée sur la référence de cellule avec Node.js via C++
linktitle: Insérer une image basée sur la référence de la cellule
type: docs
weight: 150
url: /fr/nodejs-cpp/insert-a-picture-based-on-cell-reference/
description: Apprenez comment insérer une image dans une feuille de calcul en fonction d une référence de cellule en utilisant Aspose.Cells for Node.js via C++. Affichez les données de la cellule dans une image.
---

{{% alert color="primary" %}}
Parfois, vous avez une image vide et vous devez afficher des données ou du contenu dans l'image en définissant une référence de cellule dans la barre de formule. Aspose.Cells prend en charge cette fonctionnalité (Microsoft Excel 2010).
{{% /alert %}}

## Insertion d'une image basée sur la référence de la cellule

Aspose.Cells for Node.js via C++ supporte l'affichage du contenu d'une cellule de feuille dans une forme d'image. Vous pouvez lier l'image à la cellule contenant les données que vous souhaitez afficher. Étant donné que la cellule ou la plage de cellules est liée à l'objet graphique, les modifications que vous apportez aux données de cette cellule ou plage apparaissent automatiquement dans l'objet graphique. Ajoutez une image à la feuille en appelant la méthode [**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-) de la collection [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection) (encapsulée dans l'objet [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)). Spécifiez la plage de cellules en utilisant l'attribut [**Picture.getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getFormula--) de l'objet [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture).

### Exemple de code

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();
// Get the first worksheet's cells collection
const cells = workbook.getWorksheets().get(0).getCells();

// Add string values to the cells
cells.get("A1").putValue("A1");
cells.get("C10").putValue("C10");

// Get the conditional icon's image data
const imagedata = AsposeCells.ConditionalFormattingIcon.getIconImageData(AsposeCells.IconSetType.TrafficLights31, 0);
// Create a stream based on the image data
const stream = Uint8Array.from(imagedata);

// Add a blank picture to the D1 cell
const pic = workbook.getWorksheets().get(0).getShapes().addPicture(0, 3, stream, 10, 10);
// Specify the formula that refers to the source range of cells
pic.setFormula("A1:C10");
// Update the shapes selected value in the worksheet
workbook.getWorksheets().get(0).getShapes().updateSelectedValue();

// Save the Excel file.
workbook.save(path.join(dataDir, "referencedpicture.out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
