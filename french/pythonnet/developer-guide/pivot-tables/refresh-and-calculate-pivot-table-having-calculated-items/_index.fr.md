---
title: Actualiser et calculer un tableau croisé dynamique avec des éléments calculés
type: docs
weight: 40
url: /fr/python-net/refresh-and-calculate-pivot-table-having-calculated-items/
description: Cet article montre comment actualiser et calculer un tableau croisé dynamique avec des éléments calculés à l aide d Aspose.Cells pour Python via .NET.
keywords: Aspose.Cells for Python Excel, bibliothèque Excel en Python, actualiser et calculer un tableau croisé dynamique avec des éléments calculés
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET prend désormais en charge l'actualisation et le calcul des tableaux croisés dynamiques comportant des éléments calculés. Veuillez utiliser les [**PivotTable.refresh_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/refresh_data/#) et [**PivotTable.calculate_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/calculate_data/#) habituels pour exécuter cette fonction.

{{% /alert %}}

## **Actualiser et calculer un tableau croisé dynamique avec des éléments calculés**

Le code d'exemple suivant charge le [fichier Excel source](5115238.xlsx) qui contient un tableau croisé dynamique comportant trois éléments calculés tels que "add", "div", "div2". Nous modifions d'abord la valeur de la cellule D2 à 20, puis nous actualisons et calculons le tableau croisé dynamique à l'aide des API Aspose.Cells pour Python via .NET et sauvegardons le classeur au format PDF. Les résultats dans le [PDF de sortie](5115229.pdf) montrent qu'Aspose.Cells pour Python via .NET a actualisé et calculé avec succès le tableau croisé dynamique comportant des éléments calculés. Vous pouvez le vérifier avec Microsoft Excel en mettant manuellement la valeur 20 dans la cellule D2, puis en actualisant le tableau croisé dynamique via le raccourci clavier Alt+F5 ou en cliquant sur le bouton Actualiser du tableau croisé dynamique.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-RefreshAndCalculateItems-1.py" >}}
