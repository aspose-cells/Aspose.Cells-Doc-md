---
title: Afficher la plage de cellules en tant qu étiquettes de données
type: docs
weight: 110
url: /fr/java/showing-cell-range-as-the-data-labels/
---

## Afficher la plage de cellules en tant qu'étiquettes de données dans MS Excel

Dans Microsoft Excel 2013, vous pouvez afficher la Plage de cellules pour les étiquettes de données. Vous pouvez sélectionner cette option en suivant ces étapes

- Sélectionnez les étiquettes de données de la série et cliquez avec le bouton droit pour ouvrir le menu contextuel.
- Cliquez sur **Format des étiquettes de données...** et cela affichera **Options d'étiquetage**.
- Cochez ou décochez la case à cocher **L'étiquette contient - Valeur des cellules**.

### **Case à cocher pour afficher Plage de cellules en tant qu'étiquettes de données**

La capture d'écran suivante met en évidence cette option pour votre référence.

![todo:image_alt_text](showing-cell-range-as-the-data-labels_1.png)

## Afficher la plage de cellules en tant qu'étiquettes de données avec Aspose.Cells

Aspose.Cells fournit la méthode [**DataLabels.setShowCellRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#ShowCellRange) pour cocher ou décocher la case à cocher **L'étiquette contient - Valeur des cellules** comme indiqué dans la capture d'écran ci-dessus.

## Code Java pour afficher la plage de cellules en tant que libellés de données

Le code d'exemple ci-dessous accède aux libellés de données de la série de graphiques, puis définit la méthode [**DataLabels.setShowCellRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#ShowCellRange) comme true pour vérifier l'option **Le libellé contient - Valeur à partir des cellules**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ShowCellRangeAsTheDataLabels-ShowCellRangeAsTheDataLabels.java" >}}
{{< app/cells/assistant language="java" >}}
