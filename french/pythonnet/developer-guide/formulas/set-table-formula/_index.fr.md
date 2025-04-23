---
title: Propager la formule dans un tableau ou un objet de liste automatiquement lors de la saisie de données dans de nouvelles lignes
linktitle: Définit la formule de tableau
type: docs
weight: 260
url: /fr/python-net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---

## **Scénarios d'utilisation possibles**
Parfois, vous souhaitez qu'une formule dans votre Table ou Objet de Liste se propage automatiquement aux nouvelles lignes lors de la saisie de nouvelles données. C'est le comportement par défaut de Microsoft Excel. Pour obtenir la même chose avec Aspose.Cells pour Python via .NET, veuillez utiliser la propriété [**ListColumn.formula**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listcolumn/formula).

## **Propager la formule dans un tableau ou un objet de liste automatiquement lors de la saisie de données dans de nouvelles lignes**
Le code d'exemple suivant crée un tableau ou un objet de liste de telle manière que la formule dans la colonne B se propage automatiquement aux nouvelles lignes lorsque vous entrez de nouvelles données. Veuillez vérifier le [fichier Excel de sortie](5115469.xlsx) généré avec ce code. Si vous entrez un nombre dans la cellule A3, vous verrez que la formule dans la cellule B2 se propage automatiquement à la cellule B3.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-PropagateFormulaInTable-1.py" >}}

