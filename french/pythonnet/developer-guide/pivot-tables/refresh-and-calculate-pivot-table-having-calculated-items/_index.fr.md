---
title: Actualiser et calculer le tableau croisé dynamique contenant les éléments calculés
type: docs
weight: 40
url: /fr/python-net/refresh-and-calculate-pivot-table-having-calculated-items/
description: Cet article montre comment actualiser et calculer un tableau croisé dynamique contenant des éléments calculés avec Aspose.Cells for Python via .NET.
keywords: Refresh and Calculate Pivot Table with Calculated Items
---
{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET prend désormais en charge l'actualisation et le calcul du tableau croisé dynamique ayant les éléments calculés. Veuillez utiliser le[**Tableau croisé dynamique.refresh_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/refresh_data/#) et[**PivotTable.calculate_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/calculate_data/#) comme d'habitude pour remplir cette fonction.

{{% /alert %}}

##  **Actualiser et calculer le tableau croisé dynamique contenant les éléments calculés**

 L'exemple de code suivant charge le[fichier Excel source](5115238.xlsx)qui contient un tableau croisé dynamique comportant trois éléments calculés tels que "add", "div", "div2". Nous modifions d'abord la valeur de la cellule D2 à 20, puis actualisons et calculons le tableau croisé dynamique à l'aide des API Aspose.Cells for Python via .NET et enregistrons le classeur au format PDF. Les résultats dans le[sortie PDF](5115229.pdf) montre que Aspose.Cells for Python via .NET a actualisé et calculé le tableau croisé dynamique après avoir calculé les éléments avec succès. Vous pouvez le vérifier à l'aide d'Excel Microsoft en mettant manuellement la valeur 20 dans la cellule D2, puis en actualisant le tableau croisé dynamique via la touche de raccourci Alt+F5 ou en cliquant sur le bouton Actualiser le tableau croisé dynamique.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-RefreshAndCalculateItems-1.py" >}}
