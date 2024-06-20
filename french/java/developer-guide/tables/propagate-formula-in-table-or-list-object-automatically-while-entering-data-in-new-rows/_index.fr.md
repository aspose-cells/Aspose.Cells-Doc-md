---
title: Propager la formule dans un tableau ou un objet de liste automatiquement lors de la saisie de données dans de nouvelles lignes
type: docs
weight: 980
url: /fr/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---

## **Scénarios d'utilisation possibles**
Parfois, vous voulez qu'une formule dans votre tableau ou objet liste se propage automatiquement aux nouvelles lignes lors de l'entrée de nouvelles données. C'est le comportement par défaut de Microsoft Excel. Afin d'obtenir le même résultat avec Aspose.Cells, veuillez utiliser la propriété [Formule](https://reference.aspose.com/cells/java/com.aspose.cells/listcolumn#Formule) de ListColumn.
## **Propager la formule dans un tableau ou un objet de liste automatiquement lors de la saisie de données dans de nouvelles lignes**
Le code d'exemple suivant crée un tableau ou un objet liste de telle manière que la formule dans la colonne B se propage automatiquement aux nouvelles lignes lorsque vous saisirez de nouvelles données. Veuillez vérifier le [fichier Excel de sortie](5472519.xlsx) généré avec ce code. Si vous saisissez un nombre dans la cellule A3, vous verrez que la formule dans la cellule B2 se propage automatiquement à la cellule B3.
## **Code d'exemple**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PropagateFormulaInTableorListObject-PropagateFormulaInTableorListObject.java" >}}
