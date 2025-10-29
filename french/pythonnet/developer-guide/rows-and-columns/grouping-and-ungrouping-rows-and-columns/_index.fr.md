---
title: Regroupement et dégroupement des lignes et des colonnes
type: docs
weight: 50
url: /fr/python-net/grouping-and-ungrouping-rows-and-columns/
description: Cet article montre comment regrouper et dégrouper des lignes et des colonnes avec l API Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Python Excel, Comment regrouper les lignes et les colonnes en Python, Comment dégrouper les lignes et les colonnes en Python, Gestion des groupes de lignes et de colonnes en Python, Comment définir des lignes de synthèse sous le détail, Comment définir des colonnes de synthèse à droite du détail.
---

## **Introduction**

Dans un fichier Microsoft Excel, vous pouvez créer un plan pour les données afin de vous permettre d'afficher et de masquer les niveaux de détail d'un simple clic de souris.

Cliquez sur les **symboles de plan**, 1,2,3, + et - pour afficher rapidement uniquement les lignes ou colonnes fournissant des résumés ou des en-têtes de sections dans une feuille de calcul, ou vous pouvez utiliser les symboles pour voir les détails sous un résumé ou une en-tête individuelle comme le montre la figure ci-dessous:

|**Regroupement des lignes et des colonnes.**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Gestion des groupes de lignes et de colonnes**

Aspose.Cells for Python via .NET fournit une classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contient un [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fournit une collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) qui représente toutes les cellules de la feuille de calcul.

La collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) propose plusieurs méthodes pour gérer les lignes ou colonnes dans une feuille de calcul, dont certaines sont discutées plus en détail ci-dessous.

### **Comment regrouper des lignes et des colonnes**

Il est possible de regrouper des lignes ou des colonnes en appelant les méthodes [**group_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/group_rows/#int-int-bool) et [**group_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/group_columns/#int-int-bool) de la collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Les deux méthodes prennent les paramètres suivants :

- Indice de la première ligne/colonne, la première ligne ou colonne du groupe.
- Indice de la dernière ligne/colonne, la dernière ligne ou colonne du groupe.
- Est caché, un paramètre booléen qui spécifie s'il faut masquer ou non les lignes/colonnes après le regroupement.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-GroupingRowsAndColumns-1.py" >}}

#### **Paramètres de regroupement**

Microsoft Excel vous permet de configurer les paramètres de regroupement pour l'affichage :

- Lignes de récapitulatif en dessous des détails.
- Colonnes de récapitulatif à droite des détails.

Les développeurs peuvent configurer ces paramètres de regroupement en utilisant la propriété [**outline**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/outline/) de la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).

### **Comment définir les lignes de récapitulatif en dessous des détails**

Il est possible de contrôler si les lignes de récapitulatif sont affichées en dessous des détails en définissant la propriété [**summary_row_below**](https://reference.aspose.com/cells/python-net/aspose.cells/outline/summary_row_below/) de la classe [**Outline**](https://reference.aspose.com/cells/python-net/aspose.cells/outline) à **true** ou **false**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-SummaryRowBelow-1.py" >}}

### **Comment définir les colonnes de récapitulatif à droite des détails**

Les développeurs peuvent également contrôler l'affichage des colonnes de récapitulatif à droite des détails en définissant la propriété [**summary_column_right**](https://reference.aspose.com/cells/python-net/aspose.cells/outline/summary_column_right/) de la classe [**Outline**](https://reference.aspose.com/cells/python-net/aspose.cells/outline) à **true** ou **false**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-SummaryRowRight-1.py" >}}

## **Comment dissocier des lignes et des colonnes**

Pour dissocier les lignes ou colonnes regroupées, appelez les méthodes [**ungroup_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/ungroup_rows/) et [**ungroup_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/ungroup_columns/#int-int) de la collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Les deux méthodes prennent deux paramètres :

- Indice de la première ligne ou colonne, la première ligne/colonne à dissocier.
- Indice de la dernière ligne ou colonne, la dernière ligne/colonne à dissocier.

[**ungroup_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/ungroup_rows/#int-int-bool) a une surcharge qui prend un troisième paramètre booléen. Le définir sur **true** supprime toutes les informations regroupées. Sinon, seules les informations de groupe externe sont supprimées.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-UngroupingRowsAndColumns-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
