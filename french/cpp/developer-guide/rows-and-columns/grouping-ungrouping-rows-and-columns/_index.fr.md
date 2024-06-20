---
title: Regrouper, dégrouper les lignes et les colonnes
type: docs
weight: 30
url: /fr/cpp/grouping-ungrouping-rows-and-columns/
---

## **Introduction**
Dans un fichier Microsoft Excel, vous pouvez créer un plan pour les données afin de vous permettre d'afficher et de masquer les niveaux de détail d'un simple clic de souris.

Cliquez sur les **Symboles de l'arborescence**, 1,2,3, + et - pour afficher rapidement uniquement les lignes ou colonnes contenant des résumés ou des en-têtes pour les sections d'une feuille de calcul, ou vous pouvez utiliser les symboles pour voir les détails sous un résumé ou une en-tête individuel.
## **Gestion des groupes de lignes et de colonnes**
Aspose.Cells fournit une classe, [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contient une collection [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) permettant d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fournit une collection [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) représentant toutes les cellules de la feuille de calcul.

La collection [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) fournit plusieurs méthodes pour gérer les lignes ou colonnes d'une feuille de calcul; quelques-unes d'entre elles sont discutées ci-dessous plus en détail.
### **Regroupement des lignes et des colonnes**
Il est possible de regrouper des lignes ou des colonnes en appelant les méthodes [GroupRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/grouprows/) et [GroupColumns](https://reference.aspose.com/cells/cpp/aspose.cells/cells/groupcolumns/) de la collection [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Les deux méthodes prennent les paramètres suivants :

- L'indice de la première ligne/colonne, la première ligne ou colonne du groupe.
- L'indice de la dernière ligne/colonne, la dernière ligne ou colonne du groupe.
- Est caché, un paramètre booléen qui spécifie s'il faut masquer ou non les lignes/colonnes après le regroupement.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-GroupingRowsColumns-new.cpp" >}}
#### **Paramètres de regroupement**
Microsoft Excel vous permet de configurer les paramètres de regroupement pour l'affichage :

- Lignes de récapitulatif en dessous des détails.
- Colonnes de récapitulatif à droite des détails.
## **Dégroupement des lignes & des colonnes**
Pour dissocier des lignes ou des colonnes regroupées, appelez les méthodes [UngroupRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/) et [UngroupColumns](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungroupcolumns/) de la collection [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Les deux méthodes prennent deux paramètres :

- L'indice de la première ligne ou colonne, la première ligne/colonne à dissocier.
- L'indice de la dernière ligne ou colonne, la dernière ligne/colonne à dissocier.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-UnGroupingRowsColumns-new.cpp" >}}
