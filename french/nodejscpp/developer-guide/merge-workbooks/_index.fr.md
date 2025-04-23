---
title: Fusionner plusieurs classeurs en un seul avec Node.js via C++
linktitle: Fusionneur de classeurs
type: docs
weight: 66
url: /fr/nodejs-cpp/combine-multiple-workbooks-into-a-single-workbook/
description: Apprenez comment fusionner plusieurs classeurs en un seul en utilisant Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

 Parfois, vous devez fusionner des classeurs avec différents contenus comme des images, des graphiques et des données en un seul classeur. Aspose.Cells for Node.js via C++ supporte cette fonctionnalité. Cet article montre comment créer une application console et fusionner des classeurs avec quelques lignes de code simples à l’aide d’Aspose.Cells.

{{% /alert %}}

## **Combinaison de classeurs avec des images et des graphiques**

 Le code d'exemple combine deux classeurs en un seul en utilisant Aspose.Cells for Node.js via C++. Le code charge les classeurs source, utilise la méthode [**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#combine-workbook-) pour les fusionner, puis enregistre le classeur de sortie.

### **Classeurs source**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **Livres de sortie**

- [combined.xlsx](5473095.xlsx)

### **Captures d'écran**

Voici des captures d'écran des classeurs source et de sortie.

{{% alert color="primary" %}}

Vous pouvez utiliser n'importe quel classeur source. Ces images sont uniquement à des fins d'illustration.

{{% /alert %}}

**La première feuille de travail du classeur de graphiques - empilée** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**Deuxième feuille de travail du classeur de graphiques - ligne** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**Première feuille de travail du classeur d'image - image** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**Toutes les trois feuilles de travail dans le classeur combiné - empilé, en ligne, image** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Define the first source
// Open the first excel file.
const sourceBook1 = new AsposeCells.Workbook(path.join(dataDir, "SampleChart.xlsx"));

// Define the second source book.
// Open the second excel file.
const sourceBook2 = new AsposeCells.Workbook(path.join(dataDir, "SampleImage.xlsx"));

// Combining the two workbooks
sourceBook1.combine(sourceBook2);

const outputPath = path.join(dataDir, "Combined.out.xlsx");
// Save the target book file.
sourceBook1.save(outputPath);
```

## **Sujets avancés**
- [Combiner plusieurs feuilles de calcul en une seule feuille](/cells/fr/nodejs-cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [Fusionner des fichiers](/cells/fr/nodejs-cpp/merge-files/)

