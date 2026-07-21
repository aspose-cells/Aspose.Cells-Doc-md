---
title: Actualiser et calculer un tableau croisé dynamique avec des éléments calculés
type: docs
weight: 40
url: /fr/nodejs-cpp/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ supporte désormais le rafraîchissement et le calcul des tableaux croisés dynamiques comportant des éléments calculés. Veuillez utiliser comme d’habitude [**PivotTable.refreshData**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#refreshdata--) et [**PivotTable.calculateData**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#calculatedata--) pour effectuer cette opération.

{{% /alert %}}

## **Actualiser et calculer un tableau croisé dynamique avec des éléments calculés**

Le code d’exemple suivant charge le fichier excel source (5115238.xlsx) contenant un tableau croisé dynamique avec trois éléments calculés tels que "add", "div", "div2". Nous modifions d’abord la valeur de la cellule D2 à 20, puis actualisons et recalculons le tableau croisé dynamique en utilisant les API Aspose.Cells for Node.js via C++ et enregistrons le classeur au format PDF. Les résultats dans le PDF de sortie (5115229.pdf) montrent que Aspose.Cells for Node.js via C++ a actualisé et recalculé avec succès le tableau croisé dynamique contenant des éléments calculés. Vous pouvez vérifier cela manuellement en mettant la valeur 20 dans la cellule D2, en actualisant le tableau via la raccourci Alt+F5 ou en cliquant sur le bouton Actualiser du tableau croisé dynamique.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTable-RefreshAndCalculateItems-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
