---
title: Comment changer l arrière plan d un commentaire dans Excel avec Node.js via C++
linktitle: Arrière plan du commentaire
type: docs
weight: 190
url: /fr/nodejs-cpp/how-to-set-comment-background/
description: Comment changer la couleur du commentaire et insérer une image ou une photo dans un commentaire dans Excel en utilisant Aspose.Cells for Node.js via C++.
keywords: Ajouter une image insérée, une couleur de commentaire, un fond Excel Node.js via C++
---

{{% alert color="primary" %}}
Les commentaires sont ajoutés aux cellules pour enregistrer des remarques, des détails sur la manière dont une formule fonctionne, la provenance d'une valeur ou des questions des relecteurs. Les commentaires jouent un rôle extrêmement important lorsque plusieurs personnes discutent ou examinent le même document à différents moments. Comment distinguer les commentaires de différentes personnes ? Oui, nous pouvons définir une couleur de fond différente pour chaque commentaire. Mais lorsque nous devons traiter beaucoup de documents et de nombreux commentaires, le faire manuellement est un désastre. Heureusement, [**Aspose.Cells**](https://products.aspose.com/cells/nodejs-cpp/) offre une API qui permet de faire cela dans le code.
{{% /alert %}}

## **Comment changer la couleur dans le commentaire dans Excel**

Lorsque vous n'avez pas besoin de la couleur de fond par défaut pour les commentaires, vous pouvez la remplacer par une couleur qui vous intéresse. Comment puis-je changer la couleur de l'arrière-plan de la boîte de commentaires dans Excel ?

Le code suivant vous guidera sur la façon d'utiliser [**Aspose.Cells**](https://products.aspose.com/cells/nodejs-cpp/) pour ajouter votre couleur d'arrière-plan préférée aux commentaires de votre choix.

Voici un [fichier d'exemple](exmaple.xlsx) préparé pour vous. Ce fichier sert à initialiser l'objet Workbook dans le code ci-dessous.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Initialize a new workbook.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "example.xlsx"));

// Accessing the newly added comment
const comment = workbook.getWorksheets().get(0).getComments().get(0);

// change background color
const shape = comment.getCommentShape();
shape.getFill().getSolidFill().setColor(AsposeCells.Color.Red);

// Save the Excel file
workbook.save(path.join(dataDir, "result.xlsx"));
```

Exécutez le code ci-dessus et vous obtiendrez un [fichier de sortie](result.xlsx).

## **Comment insérer une image ou une photo dans le commentaire dans Excel**

Microsoft Excel permet aux utilisateurs de personnaliser considérablement l'apparence des feuilles de calcul. Il est même possible d'ajouter des images de fond aux commentaires. L'ajout d'une image d'arrière-plan peut être un choix esthétique ou utilisé pour renforcer la marque.

Le code d'exemple ci-dessous crée un fichier XLSX à partir de zéro en utilisant l'API [**Aspose.Cells**](https://products.aspose.com/cells/nodejs-cpp/), et ajoute un commentaire avec une image d'arrière-plan à la cellule A1.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

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
const fs = require("fs");
const bmp = fs.readFileSync(path.join(dataDir, "image2.jpg"));
const ms = Buffer.from(bmp);

// Set image data to the shape associated with the comment
comment.getCommentShape().getFill().setImageData(ms);

// Save the workbook
const outputFilePath = path.join(dataDir, "commentwithpicture1.out.xlsx");
workbook.save(outputFilePath, AsposeCells.SaveFormat.Xlsx);
```

{{< app/cells/assistant language="nodejs-cpp" >}}
