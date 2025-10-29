---
title: Combinez plusieurs classeurs en un seul avec Golang via C++
linktitle: Fusionneur de classeurs
type: docs
weight: 66
url: /fr/go-cpp/combine-multiple-workbooks-into-a-single-workbook/
description: Apprenez à combiner plusieurs classeurs en un seul avec Aspose.Cells et Golang via C++.
---

{{% alert color="primary" %}}

Parfois, vous devez combiner des classeurs avec différents contenus comme des images, des graphiques et des données en un seul classeur. Aspose.Cells supporte cette fonctionnalité. Cet article montre comment créer une application console dans Visual Studio et combiner des classeurs avec quelques lignes de code simples en utilisant Aspose.Cells.

{{% /alert %}}

## **Combinaison de classeurs avec des images et des graphiques**

L'exemple de code combine deux classeurs en un seul classeur à l'aide d'Aspose.Cells. Le code charge les classeurs source, utilise la méthode [**Workbook::Combine()**](https://reference.aspose.com/cells/go-cpp/workbook/combine/) pour les combiner et enregistre le classeur de sortie.

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

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MergeWorkbooks.go" >}}
## **Sujets avancés**
- [Combiner plusieurs feuilles de calcul en une seule feuille](/cells/fr/cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [Fusionner des fichiers](/cells/fr/cpp/merge-files/)
