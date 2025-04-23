---
title: Spécifier le nombre maximum de lignes de formule partagée
type: docs
weight: 40
url: /fr/java/specify-maximum-rows-of-shared-formula/
---

## **Scénarios d'utilisation possibles**

Le nombre maximum de lignes de formule partagée par défaut est de 64. Il pourrait être n'importe quel nombre, par exemple, il pourrait être 1000. Les performances de la formule partagée changent avec un nombre différent de lignes. Par conséquent, Aspose.Cells fournit la propriété [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula) qui peut être utilisée pour spécifier le nombre maximum de lignes de formule partagée. La formule partagée sera divisée en plusieurs formules partagées si le nombre total de lignes de la formule partagée est supérieur comme illustré dans la capture d'écran suivante.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **Spécifier le nombre maximum de lignes de formule partagée**

Le code d'exemple suivant explique l'utilisation de la propriété [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula). Il définit le nombre maximum de lignes de formule partagée à 5 et ajoute la formule partagée dans la cellule D1 pour 100 lignes et l'enregistre dans le [fichier Excel de sortie](61767869.xlsx). Si vous extrayez le contenu du fichier Excel de sortie et vérifiez *sheet1.xml*, vous verrez que la formule partagée se divise après chaque 5 lignes comme indiqué dans la capture d'écran ci-dessus.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-SpecifyMaximumRowsOfSharedFormula.java" >}}
{{< app/cells/assistant language="java" >}}
