---
title: Changer la direction du texte du commentaire avec Node.js via C++
linktitle: Changer la direction du texte du commentaire
type: docs
weight: 10
url: /fr/nodejs-cpp/change-text-direction-of-the-comment/
description: Apprenez comment changer la direction du texte des commentaires en utilisant Aspose.Cells for Node.js via C++. Personnalisez efficacement les paramètres d alignement des commentaires.
---

{{% alert color="primary" %}}

Microsoft Excel permet aux utilisateurs d'ajouter des commentaires aux cellules pour fournir des informations supplémentaires et mettre en évidence des données. Les développeurs peuvent avoir besoin de personnaliser le commentaire pour spécifier les paramètres d'alignement et la direction du texte. Aspose.Cells for Node.js via C++ fournit des API pour accomplir cette tâche.

{{% /alert %}}

Aspose.Cells for Node.js via C++ offre une propriété [**Shape.getTextDirection()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextDirection--) pour définir la direction du texte d'un commentaire. Le code d'exemple ci-dessous démontre l'utilisation de la propriété [**Shape.getTextDirection()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextDirection--) pour définir la direction du texte d'un commentaire.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const wb = new AsposeCells.Workbook();

// Get the first worksheet
const sheet = wb.getWorksheets().get(0);

// Add a comment to A1 cell
const commentIndex = sheet.getComments().add("A1");
const comment = sheet.getComments().get(commentIndex);

// Set its vertical alignment setting            
comment.getCommentShape().setTextVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Set its horizontal alignment setting
comment.getCommentShape().setTextHorizontalAlignment(AsposeCells.TextAlignmentType.Right);

// Set the Text Direction - Right-to-Left
comment.getCommentShape().setTextOrientationType(AsposeCells.TextDirectionType.RightToLeft);

// Set the Comment note
comment.setNote("This is my Comment Text. This is test");

const outputFilePath = path.join(dataDir, "OutCommentShape.out.xlsx");
// Save the Excel file
wb.save(outputFilePath);
```
