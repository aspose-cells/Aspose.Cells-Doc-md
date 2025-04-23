---  
title: Gestion des images avec Node.js via C++  
linktitle: Gestion des images  
type: docs  
weight: 10  
url: /fr/nodejs-cpp/managing-pictures/  
description: Apprenez à ajouter et à positionner des images dans les feuilles de calcul en utilisant Aspose.Cells for Node.js via C++.  
---  

Aspose.Cells permet aux développeurs d'ajouter des images à des feuilles de calcul en cours d'exécution. De plus, le positionnement de ces images peut être contrôlé en cours d'exécution, ce qui est discuté plus en détail dans les sections suivantes.

Cet article explique comment ajouter des images et comment insérer une image qui montre le contenu de certaines cellules.

## **Ajout d'images**

Ajouter des images à une feuille de calcul est très facile. Il suffit de quelques lignes de code :  
Il suffit d'appeler la méthode [**Add**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-string-) de la collection [**Pictures**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection) (encapsulée dans l'objet [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)). La méthode [**Add**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-string-) prend les paramètres suivants :

- **Index de la ligne supérieure gauche**, l'index de la ligne supérieure gauche.
- **Index de la colonne supérieure gauche**, l'index de la colonne supérieure gauche.
- **Nom du fichier image**, le nom du fichier image, complet avec le chemin.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a picture at the location of a cell whose row and column indices
// Are 5 in the worksheet. It is "F6" cell
worksheet.getPictures().add(5, 5, path.join(dataDir, "logo.jpg"));

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Positionnement des images**

Il existe deux façons possibles de contrôler le positionnement des images à l'aide d'Aspose.Cells :

- Positionnement proportionnel: définir une position proportionnelle à la hauteur et à la largeur de la ligne.
- Positionnement absolu : définissez la position exacte sur la page où l'image sera insérée, par exemple, 40 pixels à gauche et 20 pixels en dessous du bord de la cellule.

### **Positionnement proportionnel**

Les développeurs peuvent positionner les images proportionnellement à la hauteur des lignes et à la largeur des colonnes en utilisant les propriétés [**getUpperDeltaX()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getUpperDeltaX--) et [**getUpperDeltaY()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getUpperDeltaY--) de l'objet [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/). Un objet [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/) peut être obtenu de la collection [**Pictures**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection) en passant son index d'image. Cet exemple place une image dans la cellule F6.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a picture at the location of a cell whose row and column indices
// Are 5 in the worksheet. It is "F6" cell
const pictureIndex = worksheet.getPictures().add(5, 5, path.join(dataDir, "logo.jpg"));

// Accessing the newly added picture
const picture = worksheet.getPictures().get(pictureIndex);

// Positioning the picture proportional to row height and column width
picture.setUpperDeltaX(200);
picture.setUpperDeltaY(200);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Positionnement Absolu**

Les développeurs peuvent également positionner les images de façon absolue en utilisant les propriétés [**getLeft()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getLeft--) et [**getTop()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTop--) de l'objet [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/). Cet exemple place une image dans la cellule F6, à 60 pixels du bord gauche et à 10 pixels du haut de la cellule.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "logo.jpg");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a picture at the location of a cell whose row and column indices
// Are 5 in the worksheet. It is "F6" cell
const pictureIndex = worksheet.getPictures().add(5, 5, filePath);

// Accessing the newly added picture
const picture = worksheet.getPictures().get(pictureIndex);

// Absolute positioning of the picture in unit of pixels
picture.setLeft(60);
picture.setTop(10);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Insérer une image basée sur la référence de cellule**

Aspose.Cells vous permet d'afficher le contenu d'une cellule de feuille de calcul dans une forme d'image. Vous pouvez lier l'image à la cellule qui contient les données que vous souhaitez afficher. Étant donné que la cellule ou la plage de cellules est liée à l'objet graphique, les modifications apportées aux données dans cette cellule ou plage de cellules apparaissent automatiquement dans l'objet graphique.

Ajoutez une image à la feuille en appelant la méthode [**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-) de la collection [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection) (encapsulée dans l'objet [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)). Spécifiez la plage de cellules en utilisant l'attribut [**getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getFormula--) de l'objet [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/).

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

const picts = workbook.getWorksheets().get(0).getPictures();
// Add a blank picture to the D1 cell
const picIndex = picts.add(0, 3, 10, 6, null);
const pic = picts.get(picIndex);

// Specify the formula that refers to the source range of cells

pic.setFormula("A1:C10");

// Update the shapes selected value in the worksheet
workbook.getWorksheets().get(0).getShapes().updateSelectedValue();

// Save the Excel file.
workbook.save(path.join(dataDir, "output.out.xls"));
```

## **Sujets avancés**
- [Ajouter un ensemble d'icônes conditionnelles avec le texte de la cellule](/cells/fr/nodejs-cpp/add-conditional-icons-set-with-the-cell-text/)
- [Insérer une image liée à partir d'une adresse web](/cells/fr/nodejs-cpp/insert-a-linked-picture-from-web-address/)
- [Insérer une image en fonction de la référence de la cellule](/cells/fr/nodejs-cpp/insert-a-picture-based-on-cell-reference/)
- [Charger une image Web à partir d'une URL dans une feuille de calcul Excel](/cells/fr/nodejs-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)

