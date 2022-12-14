---
title: Combiner plusieurs classeurs en un seul classeur
linktitle: Fusion de classeurs
type: docs
weight: 66
url: /fr/net/combine-multiple-workbooks-into-a-single-workbook/
---
{{% alert color="primary" %}}

Parfois, vous devez combiner des classeurs avec divers contenus tels que des images, des graphiques et des données dans un seul classeur. Aspose.Cells prend en charge cette fonctionnalité. Cet article montre comment créer une application console dans Visual Studio et combiner des classeurs avec quelques lignes de code simples à l'aide de Aspose.Cells.

{{% /alert %}}

## **Combinaison de classeurs avec des images et des graphiques**

L'exemple de code combine deux classeurs en un seul classeur à l'aide de Aspose.Cells. Le code charge les classeurs source, utilise le[**Classeur.combine()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/combine)méthode pour les combiner et enregistre le classeur de sortie.

### **Classeurs sources**

- [graphiques.xlsx](5473097.xlsx)
- [image.xlsx](5473096.xlsx)

### **Classeurs de sortie**

- [combiné.xlsx](5473095.xlsx)

### **Captures d'écran**

Vous trouverez ci-dessous des captures d'écran des classeurs source et de sortie.

{{% alert color="primary" %}}

Vous pouvez utiliser n'importe quel classeur source. Ces images sont juste à des fins d'illustration.

{{% /alert %}}

**La première feuille de calcul du classeur de graphiques - empilée** 

![tâche : image_autre_texte](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**Deuxième feuille de calcul du classeur de graphiques - ligne** 

![tâche : image_autre_texte](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**Première feuille de travail du classeur d'images - image** 

![tâche : image_autre_texte](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**Les trois feuilles de calcul du classeur combiné - empilées, ligne, image** 

![tâche : image_autre_texte](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CombineMultipleWorkbooksSingleWorkbook-1.cs" >}}

## **Sujets avancés**
- [Combiner plusieurs feuilles de calcul en une seule feuille de calcul](/cells/fr/net/combine-multiple-worksheets-into-a-single-worksheet/)
- [Fusionner des fichiers](/cells/fr/net/merge-files/)
