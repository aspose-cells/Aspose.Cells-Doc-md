---
title: Actualiser et calculer un tableau croisé dynamique avec des éléments calculés
type: docs
weight: 130
url: /fr/java/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

Aspose.Cells prend désormais en charge le rafraîchissement et le calcul des tableaux croisés dynamiques ayant des éléments calculés. Veuillez utiliser [**PivotTable.refreshData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData--) et [**PivotTable.caclulateData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData--) comme d'habitude pour effectuer cette fonction.

{{% /alert %}}

## **Actualiser et calculer un tableau croisé dynamique avec des éléments calculés**

Le code d'exemple suivant charge le [fichier Excel source](5473428.xlsx) qui contient un tableau croisé dynamique ayant trois éléments calculés tels que "add", "div", "div2". Nous changeons d'abord la valeur de la cellule D2 à 20, puis rafraîchissons et calculons le tableau croisé dynamique à l'aide des APIs Aspose.Cells et enregistrons le classeur au format PDF. Les résultats dans le [fichier PDF de sortie](5473431.pdf) montrent qu'Aspose.Cells a rafraîchi et calculé avec succès le tableau croisé dynamique ayant des éléments calculés. Vous pouvez le vérifier en utilisant Microsoft Excel en mettant manuellement la valeur 20 dans la cellule D2, puis en rafraîchissant le tableau croisé via la touche de raccourci Alt+F5 ou en cliquant sur le bouton Rafraîchir du tableau croisé dynamique.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshCalculatePivotTablehavingCalculatedItems-RefreshCalculatePivotTablehavingCalculatedItems.java" >}}
