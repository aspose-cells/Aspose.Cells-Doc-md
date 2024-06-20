---
title: Spécifier le nombre maximum de lignes de formule partagée
type: docs
weight: 40
url: /fr/net/specify-maximum-rows-of-shared-formula/
---

## **Scénarios d'utilisation possibles**

Le nombre maximum de lignes de formule partagée par défaut est de 64. Il pourrait être n'importe quel nombre par exemple 1000. La performance de la formule partagée change avec un nombre différent de lignes. Par conséquent, Aspose.Cells fournit la propriété [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrowsofsharedformula) qui peut être utilisée pour spécifier le nombre maximum de lignes de la formule partagée. La formule partagée sera scindée en plusieurs formules partagées si le total des lignes de la formule partagée est supérieur à celui-ci comme le montre la capture d'écran suivante.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **Spécifier le nombre maximum de lignes de formule partagée**

Le code d'exemple suivant explique l'utilisation de la propriété [**Workbook.Settings.MaxRowsOfSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrowsofsharedformula). Il définit le nombre maximum de lignes de la formule partagée à 5 et ajoute la formule partagée dans la cellule D1 pour 100 lignes et enregistre dans le fichier Excel de sortie. Si vous extrayez le contenu du fichier Excel de sortie et vérifiez le *sheet1.xml*, vous verrez que la formule partagée se divise après chaque 5 lignes comme indiqué dans la capture d'écran ci-dessus.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-SpecifyMaximumRowsOfSharedFormula.cs" >}}
