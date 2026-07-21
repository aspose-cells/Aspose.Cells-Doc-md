---
title: Actualiser et calculer un tableau croisé dynamique avec des éléments calculés
type: docs
weight: 40
url: /fr/net/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

Aspose.Cells prend désormais en charge le rafraîchissement et le calcul du tableau croisé dynamique comportant des éléments calculés. Veuillez utiliser les [**PivotTable.RefreshData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/refreshdata) et [**PivotTable.CaclulateData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/calculatedata) comme d'habitude pour effectuer cette fonction.

{{% /alert %}}

## **Actualiser et calculer un tableau croisé dynamique avec des éléments calculés**

L'extrait de code suivant charge le [fichier Excel source](5115238.xlsx) qui contient un tableau croisé dynamique comportant trois éléments calculés tels que "add", "div", "div2". Nous changeons d'abord la valeur de la cellule D2 à 20, puis nous rafraîchissons et calculons le tableau croisé dynamique à l'aide des API Aspose.Cells et enregistrons le classeur au format PDF. Les résultats dans le [PDF de sortie](5115229.pdf) montrent qu'Aspose.Cells a rafraîchi et calculé avec succès le tableau croisé dynamique comportant des éléments calculés. Vous pouvez le vérifier en utilisant Microsoft Excel en mettant manuellement la valeur 20 dans la cellule D2, puis en actualisant le tableau croisé dynamique via la touche de raccourci Alt+F5 ou en cliquant sur le bouton Actualiser du tableau croisé dynamique.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-RefreshAndCalculateItems-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
