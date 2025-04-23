---
title: Combiner plusieurs classeurs en un seul classeur
linktitle: Fusionneur de classeurs
type: docs
weight: 66
url: /fr/python-net/combine-multiple-workbooks-into-a-single-workbook/
---

{{% alert color="primary" %}}

Parfois, vous avez besoin de combiner des classeurs avec différents contenus comme des images, des graphiques et des données dans un seul classeur. Aspose.Cells pour Python via .NET supporte cette fonctionnalité. Cet article montre comment créer une application console dans Visual Studio et combiner des classeurs avec quelques lignes de code simples en utilisant Aspose.Cells pour Python via .NET.

{{% /alert %}}

## **Combinaison de classeurs avec des images et des graphiques**

Le code d'exemple combine deux classeurs en un seul en utilisant Aspose.Cells pour Python via .NET. Le code charge les classeurs sources, utilise la méthode [**Workbook.combine()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/combine) pour les combiner et sauvegarde le classeur résultant.

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Merge-Workbooks-CombineMultipleWorkbooksSingleWorkbook-1.py" >}}

## **Sujets avancés**
- [Combiner plusieurs feuilles de calcul en une seule feuille](/cells/fr/python-net/combine-multiple-worksheets-into-a-single-worksheet/)
- [Fusionner des fichiers](/cells/fr/python-net/merge-files/)

