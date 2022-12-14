---
title: Propager automatiquement la formule dans le tableau ou l'objet de liste lors de la saisie de données dans de nouvelles lignes
type: docs
weight: 980
url: /fr/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---
## **Scénarios d'utilisation possibles**
 Parfois, vous souhaitez qu'une formule dans votre tableau ou objet de liste se propage automatiquement à de nouvelles lignes lors de la saisie de nouvelles données. Il s'agit du comportement par défaut de Microsoft Excel. Afin d'obtenir la même chose avec Aspose.Cells, veuillez utiliser[ListColumn.Formula](https://reference.aspose.com/cells/java/com.aspose.cells/listcolumn#Formula)propriété.
## **Propager automatiquement la formule dans le tableau ou l'objet de liste lors de la saisie de données dans de nouvelles lignes**
L'exemple de code suivant crée une table ou un objet de liste de manière à ce que la formule de la colonne B se propage automatiquement aux nouvelles lignes lorsque vous entrez de nouvelles données. S'il vous plaît, vérifiez le[fichier excel de sortie](5472519.xlsx) généré avec ce code. Si vous entrez un nombre dans la cellule A3, vous verrez que la formule dans la cellule B2 se propage automatiquement à la cellule B3.
## **Exemple de code**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PropagateFormulaInTableorListObject-PropagateFormulaInTableorListObject.java" >}}
