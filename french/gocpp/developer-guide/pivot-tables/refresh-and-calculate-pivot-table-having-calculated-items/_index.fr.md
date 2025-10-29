---
title: Actualiser et calculer le tableau croisé dynamique avec des éléments calculés avec Golang via C++
linktitle: Actualiser et calculer un tableau croisé dynamique avec des éléments calculés
type: docs
weight: 40
url: /fr/go-cpp/refresh-and-calculate-pivot-table-having-calculated-items/
description: Actualiser et calculer un tableau croisé dynamique avec des éléments calculés en utilisant Aspose.Cells avec Golang via C++.
---

{{% alert color="primary" %}}

Aspose.Cells prend désormais en charge le rafraîchissement et le calcul du tableau croisé dynamique comportant des éléments calculés. Veuillez utiliser les [**PivotTable.RefreshData()**](https://reference.aspose.com/cells/go-cpp/pivottable/refreshdata/) et [**PivotTable.CalculateData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/) comme d'habitude pour effectuer cette fonction.

{{% /alert %}}

## **Actualiser et calculer un tableau croisé dynamique avec des éléments calculés**

 Le code d'exemple suivant charge le [fichier Excel source](5115238.xlsx) contenant un tableau croisé dynamique avec trois éléments calculés tels que "add", "div", "div2". Nous modifions d'abord la valeur de la cellule D2 à 20, puis rafraîchissons et calculons le tableau croisé dynamique en utilisant les API Aspose.Cells et enregistrons le classeur au format PDF. Les résultats dans le [PDF de sortie](5115229.pdf) montrent qu'Aspose.Cells a rafraîchi et calculé avec succès le tableau croisé dynamique contenant des éléments calculés. Vous pouvez le vérifier manuellement avec Microsoft Excel en entrant la valeur 20 dans la cellule D2, puis en rafraîchissant le tableau croisé dynamique via la touche de raccourci Alt+F5 ou en cliquant sur le bouton de rafraîchissement du tableau croisé dynamique.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RefreshAndCalculatePivotTableHavingCalculatedItems.go" >}}
