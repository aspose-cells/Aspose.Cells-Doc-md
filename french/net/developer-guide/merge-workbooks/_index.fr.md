---
title: Combiner plusieurs classeurs en un seul classeur
linktitle: Fusionneur de classeurs
type: docs
weight: 66
url: /fr/net/combine-multiple-workbooks-into-a-single-workbook/
---

{{% alert color="primary" %}}

Parfois, vous devez combiner des classeurs avec divers contenus tels que des images, des graphiques et des données dans un seul classeur. Aspose.Cells prend en charge cette fonctionnalité. Cet article montre comment créer une application console dans Visual Studio et combiner des classeurs avec quelques lignes de code simples à l'aide d'Aspose.Cells.

{{% /alert %}}

## **Combinaison de classeurs avec des images et des graphiques**

L'exemple de code combine deux classeurs en un seul classeur à l'aide d'Aspose.Cells. Le code charge les classeurs source, utilise la méthode [**Workbook.combine()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/combine) pour les combiner et enregistre le classeur de sortie.

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CombineMultipleWorkbooksSingleWorkbook-1.cs" >}}

## **Sujets avancés**
- [Combiner plusieurs feuilles de calcul en une seule feuille](/cells/fr/net/combine-multiple-worksheets-into-a-single-worksheet/)
- [Fusionner des fichiers](/cells/fr/net/merge-files/)
{{< app/cells/assistant language="csharp" >}}
