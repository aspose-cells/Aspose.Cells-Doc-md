---
title: Spécifier le nombre maximum de lignes de formule partagée
type: docs
weight: 40
url: /fr/python-net/specify-maximum-rows-of-shared-formula/
---

## **Scénarios d'utilisation possibles**

Le nombre maximum de lignes par formule partagée par défaut est de 64. Il peut être n'importe quel nombre, par exemple 1000. La performance de la formule partagée varie avec le nombre de lignes. Par conséquent, Aspose.Cells pour Python via .NET fournit la propriété [**Workbook.settings.max_rows_of_shared_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_rows_of_shared_formula) qui peut être utilisée pour spécifier le nombre maximum de lignes pour la formule partagée. La formule partagée sera divisée en plusieurs formules partagées si le nombre total de lignes dépasse cette limite, comme illustré dans la capture d'écran suivante.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **Spécifier le nombre maximum de lignes de formule partagée**

Le code d'exemple suivant explique l'utilisation de la propriété [**Workbook.settings.max_rows_of_shared_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_rows_of_shared_formula). Il définit le nombre maximum de lignes de la formule partagée à 5 et ajoute la formule partagée dans la cellule D1 pour 100 lignes et enregistre dans le fichier Excel de sortie. Si vous extrayez le contenu du fichier Excel de sortie et vérifiez le *sheet1.xml*, vous verrez que la formule partagée se divise après chaque 5 lignes comme indiqué dans la capture d'écran ci-dessus.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SpecifyMaximumRowsOfSharedFormula.py" >}}

