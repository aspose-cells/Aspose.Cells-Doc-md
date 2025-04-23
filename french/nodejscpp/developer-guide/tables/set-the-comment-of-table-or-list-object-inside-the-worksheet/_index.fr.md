---
title: Définir le commentaire d un objet de table ou de liste à l intérieur de la feuille de calcul avec Node.js via C++
linktitle: Définissez le commentaire de la table ou de l objet Liste à l intérieur de la feuille de calcul
type: docs
weight: 40
url: /fr/nodejs-cpp/set-the-comment-of-table-or-list-object-inside-the-worksheet/
description: Découvrez comment définir le commentaire de la table ou de l objet de liste à l intérieur de la feuille de calcul en utilisant Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Vous pouvez définir le commentaire de la Table ou de l'Objet de Liste à l'intérieur de la feuille de calcul en utilisant la propriété [**ListObject.getComment()**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#getComment--). Le commentaire sera visible dans le fichier xl/tables/tableName.xml.

{{% /alert %}}

## **Définir le Commentaire d'un Tableau ou Objet Liste à l'intérieur de la Feuille de Calcul**

Le code d'exemple suivant charge le [fichier Excel source](5115514.xlsx), définit le commentaire de la première table ou objet liste à l'intérieur de la feuille de calcul.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open the template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "table_comment.xlsx"));
// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Access first list object or table.
const lstObj = worksheet.getListObjects().get(0);
// Set the comment of the list object
lstObj.setComment("This is Aspose.Cells comment.");
// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "SetCommentOfTableOrListObject_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
