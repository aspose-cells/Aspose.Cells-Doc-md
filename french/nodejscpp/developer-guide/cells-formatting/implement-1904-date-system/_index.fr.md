---
title: Implémentez le système de date 1904 avec Node.js via C++
description: Aspose.Cells est une bibliothèque Node.js pour travailler avec des fichiers de feuilles de calcul. Elle supporte la mise en œuvre du système de date 1904, permettant aux utilisateurs de calculer et de formater en fonction du système de date du 1er janvier 1904. Cet article décrit comment implémenter le système de date 1904 en utilisant la bibliothèque Aspose.Cells.
keywords: Aspose.Cells, système de date 1904, feuille de calcul, calcul, mise en forme, Node.js via C++
type: docs
weight: 7000
url: /fr/nodejs-cpp/implement-1904-date-system/
---

{{% alert color="primary" %}} 

Microsoft Excel supporte deux systèmes de date : le système de date 1900 (le système de date par défaut implémenté dans Excel pour Windows) et le système de date 1904. Le système de date 1904 est généralement utilisé pour assurer la compatibilité avec les fichiers Excel Macintosh et est le système par défaut si vous utilisez Excel pour Macintosh. Vous pouvez définir le système de date 1904 pour les fichiers Excel en utilisant Aspose.Cells for Node.js via C++. 

{{% /alert %}} 

Pour implémenter le système de date 1904 dans Microsoft Excel (par exemple, Microsoft Excel 2003) :

1. Dans le menu **Outils**, sélectionnez **Options**, puis sélectionnez l'onglet **Calcul**.
1. Sélectionnez l'option **Système de date 1904**.
1. Cliquez sur **OK**.

|**Sélection du système de date 1904 dans Microsoft Excel**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|

Consultez le code source suivant sur la manière d'accomplir ceci en utilisant les API Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");
// Initialize a new Workbook
// Open an excel file
const workbook = new AsposeCells.Workbook(filePath);

// Implement 1904 date system
workbook.getSettings().setDate1904(true);

// Save the excel file
workbook.save(path.join(dataDir, "Mybook.out.xlsx"));
```
