---
title: Spécifier le nombre maximal de lignes de formule partagée
type: docs
weight: 40
url: /fr/java/specify-maximum-rows-of-shared-formula/
---
## **Scénarios d'utilisation possibles**

Le nombre maximum de lignes par défaut de la formule partagée est de 64. Il peut s'agir de n'importe quel nombre, par exemple 1 000. Les performances de la formule partagée changent avec un nombre de lignes différent. Par conséquent, Aspose.Cells fournit le[**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula)propriété qui peut être utilisée pour spécifier le nombre maximum de lignes de la formule partagée. La formule partagée sera divisée en plusieurs formules partagées si le nombre total de lignes de la formule partagée est supérieur à celui-ci, comme indiqué dans la capture d'écran suivante.

![tâche : image_autre_texte](specify-maximum-rows-of-shared-formula_1.png)

## **Spécifier le nombre maximal de lignes de formule partagée**

L'exemple de code suivant explique l'utilisation de[**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRowsOfSharedFormula)propriété. Il définit le nombre maximal de lignes de la formule partagée sur 5 et ajoute la formule partagée dans la cellule D1 pour 100 lignes et enregistre dans[fichier Excel de sortie](61767869.xlsx). Si vous extrayez le contenu du fichier Excel de sortie et vérifiez le*feuille1.xml*, vous verrez la formule partagée se diviser toutes les 5 lignes, comme indiqué dans la capture d'écran ci-dessus.

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-SpecifyMaximumRowsOfSharedFormula.java" >}}
