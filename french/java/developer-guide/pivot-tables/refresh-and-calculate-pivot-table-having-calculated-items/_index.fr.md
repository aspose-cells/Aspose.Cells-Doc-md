---
title: Actualiser et calculer le tableau croisé dynamique ayant des éléments calculés
type: docs
weight: 130
url: /fr/java/refresh-and-calculate-pivot-table-having-calculated-items/
---
{{% alert color="primary" %}}

 Aspose.Cells prend désormais en charge l'actualisation et le calcul du tableau croisé dynamique ayant des éléments calculés. Veuillez utiliser[**Tableau croisé dynamique.refreshData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData() ) et[**Tableau croisé dynamique.caclulateData()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData()) comme d'habitude pour exécuter cette fonction.

{{% /alert %}}

## **Actualiser et calculer le tableau croisé dynamique ayant des éléments calculés**

 L'exemple de code suivant charge le[fichier excel source](5473428.xlsx)qui contient un tableau croisé dynamique comportant trois éléments calculés tels que "add", "div", "div2". Nous changeons d'abord la valeur de la cellule D2 en 20, puis actualisons et calculons le tableau croisé dynamique à l'aide des API Aspose.Cells et enregistrons le classeur au format PDF. Les résultats dans le[PDF de sortie](5473431.pdf) montre que Aspose.Cells a actualisé et calculé le tableau croisé dynamique ayant calculé les éléments avec succès. Vous pouvez le vérifier en utilisant Microsoft Excel en mettant manuellement la valeur 20 dans la cellule D2, puis en actualisant le tableau croisé dynamique via la touche de raccourci Alt + F5 ou en cliquant sur le bouton Actualiser du tableau croisé dynamique.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshCalculatePivotTablehavingCalculatedItems-RefreshCalculatePivotTablehavingCalculatedItems.java" >}}
