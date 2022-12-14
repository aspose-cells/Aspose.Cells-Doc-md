---
title: Affichage de la plage Cell comme étiquettes de données
type: docs
weight: 110
url: /fr/java/showing-cell-range-as-the-data-labels/
---
## Afficher la plage de cellules sous forme d'étiquettes de données dans MS Excel

Dans Microsoft Excel 2013, vous pouvez afficher la plage Cell pour les étiquettes de données. Vous pouvez sélectionner cette option en suivant ces étapes

- Sélectionnez les étiquettes de données de la série et cliquez avec le bouton droit pour ouvrir le menu contextuel.
-  Clique le**Formater les étiquettes de données...** et ça montrera**Options d'étiquette**.
-  Cochez ou décochez la case**L'étiquette contient - Valeur à partir de Cells**.

### **Case à cocher pour afficher la plage Cell en tant qu'étiquettes de données**

La capture d'écran suivante met en évidence cette option pour votre référence.

![tâche : image_autre_texte](showing-cell-range-as-the-data-labels_1.png)

## Afficher la plage de cellules sous forme d'étiquettes de données avec Aspose.Cells

 Aspose.Cells fournit le[**DataLabels.setShowCellRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#ShowCellRange) méthode pour cocher ou décocher la case**L'étiquette contient - Valeur à partir de Cells** comme indiqué dans la capture d'écran ci-dessus.

## Code Java pour afficher la plage de cellules sous forme d'étiquettes de données

 L'exemple de code ci-dessous accède aux étiquettes de données de la série de graphiques, puis définit[**DataLabels.setShowCellRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#ShowCellRange) méthode à true pour vérifier**L'étiquette contient - Valeur à partir de Cells** option.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ShowCellRangeAsTheDataLabels-ShowCellRangeAsTheDataLabels.java" >}}
