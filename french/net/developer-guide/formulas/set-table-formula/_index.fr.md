---
title: Propager automatiquement la formule dans le tableau ou l'objet de liste lors de la saisie de données dans de nouvelles lignes
linktitle: Définit la formule du tableau
type: docs
weight: 260
url: /fr/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---
## **Scénarios d'utilisation possibles**
 Parfois, vous souhaitez qu'une formule dans votre tableau ou objet de liste se propage automatiquement à de nouvelles lignes lors de la saisie de nouvelles données. Il s'agit du comportement par défaut de Microsoft Excel. Afin d'obtenir la même chose avec Aspose.Cells, veuillez utiliser[ListColumn.Formula](https://reference.aspose.com/cells/net/aspose.cells.tables/listcolumn/properties/formula)la propriété.
## **Propager automatiquement la formule dans le tableau ou l'objet de liste lors de la saisie de données dans de nouvelles lignes**
L'exemple de code suivant crée une table ou un objet de liste de manière à ce que la formule de la colonne B se propage automatiquement aux nouvelles lignes lorsque vous entrez de nouvelles données. S'il vous plaît, vérifiez le[fichier excel de sortie](5115469.xlsx) généré avec ce code. Si vous entrez un nombre dans la cellule A3, vous verrez que la formule dans la cellule B2 se propage automatiquement à la cellule B3.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PropagateFormulaInTable-1.cs" >}}
