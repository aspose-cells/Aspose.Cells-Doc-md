---
title: Gérer les commentaires et notes avec Node.js via C++
linktitle: Commentaires et notes
type: docs
weight: 128
url: /fr/nodejs-cpp/comments-and-notes/
description: Insérer et gérer des commentaires ou des notes avec Aspose.Cells for Node.js via C++.
keywords: insérer des commentaires, insérer des notes Node.js via C++
---

## **Introduction**

Les commentaires sont utilisés pour ajouter des informations supplémentaires aux cellules. Aspose.Cells for Node.js via C++ propose deux méthodes pour ajouter des commentaires aux cellules. La première consiste à créer des commentaires dans un fichier de conception manuellement. Ces commentaires sont ensuite importés en utilisant Aspose.Cells. La seconde consiste à ajouter des commentaires en utilisant l'API Aspose.Cells à l'exécution. Ce sujet discute de l'ajout de commentaires aux cellules en utilisant l'API Aspose.Cells. La mise en forme des commentaires sera également expliquée.

## **Ajouter un commentaire**

Ajouter un commentaire à une cellule en appelant la méthode [**CommentCollection.add(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#add-number-number-) de la collection [**Comments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection) (encapsulée dans l'objet [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)). Le nouvel objet [**Comment**](https://reference.aspose.com/cells/nodejs-cpp/comment) peut être accessible à partir de la collection [**Comments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection) en passant l'index du commentaire. Après avoir accès à l'objet [**Comment**](https://reference.aspose.com/cells/nodejs-cpp/comment), personnalisez la note du commentaire en utilisant la propriété [**getNote()**](https://reference.aspose.com/cells/nodejs-cpp/comment/#getNote--).

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

// Adding a comment to "F5" cell
const commentIndex = worksheet.getComments().add("F5");

// Accessing the newly added comment
const comment = worksheet.getComments().get(commentIndex);

// Setting the comment note
comment.setNote("Hello Aspose!");

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Mise en forme des commentaires**

Il est également possible de formater l'apparence des commentaires en configurant leur hauteur, leur largeur et leurs paramètres de police.

```javascript
const fs = require("fs");
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

// Adding a comment to "F5" cell
const commentIndex = worksheet.getComments().add("F5");

// Accessing the newly added comment
const comment = worksheet.getComments().get(commentIndex);

// Setting the comment note
comment.setNote("Hello Aspose!");

// Setting the font size of a comment to 14
comment.getFont().setSize(14);

// Setting the font of a comment to bold
comment.getFont().setIsBold(true);

// Setting the height of the font to 10
comment.setHeightCM(10);

// Setting the width of the font to 2
comment.setWidthCM(2);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Ajouter une image au commentaire**

Avec Microsoft Excel 2007, il est également possible d'avoir une image en arrière-plan d'un commentaire de cellule. Dans Excel 2007, cela se fait en suivant les étapes suivantes. (Ils supposent que vous avez déjà ajouté un commentaire de cellule.)

1. Faites un clic droit sur la cellule qui contient le commentaire.
1. Sélectionnez **Afficher/masquer les commentaires**, et effacez tout texte du commentaire.
1. Cliquez sur le bord du commentaire pour le sélectionner.
1. Sélectionnez **Format**, puis **Commentaire**.
1. Sur l'onglet **Couleurs et traits**, développez la liste **Couleur**.
1. Cliquez sur **Remplissage**.
1. Sur l'onglet **Image**, cliquez sur **Sélectionner une image**.
1. Localisez et sélectionnez l'image.
1. Cliquez sur **OK** jusqu'à ce que tous les dialogues se ferment.

Aspose.Cells propose également cette fonctionnalité. Ci-dessous se trouve un exemple de code qui crée un fichier XLSX à partir de zéro, en ajoutant un commentaire à la cellule "A1" avec une image définie comme arrière-plan.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook
const workbook = new AsposeCells.Workbook();

// Get a reference of comments collection with the first sheet
const comments = workbook.getWorksheets().get(0).getComments();

// Add a comment to cell A1
const commentIndex = comments.add(0, 0);
const comment = comments.get(commentIndex);
comment.setNote("First note.");
comment.getFont().setName("Times New Roman");

// Load an image into stream
const bmpPath = path.join(dataDir, "logo.jpg");
const bmpData = fs.readFileSync(bmpPath);

// Set image data to the shape associated with the comment
comment.getCommentShape().getFill().setImageData(bmpData);

// Save the workbook
workbook.save(path.join(dataDir, "book1.out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## **Sujets avancés**
- [Modifier la direction du texte du commentaire](/cells/fr/nodejs-cpp/change-text-direction-of-the-comment/)
- [Comment changer la couleur de police du commentaire](/cells/fr/nodejs-cpp/how-to-change-the-comment-font-color/)
- [Comment définir l'arrière-plan du commentaire](/cells/fr/nodejs-cpp/how-to-set-comment-background/)
- [Commentaires en fil](/cells/fr/nodejs-cpp/threaded-comments/)

{{< app/cells/assistant language="nodejs-cpp" >}}
