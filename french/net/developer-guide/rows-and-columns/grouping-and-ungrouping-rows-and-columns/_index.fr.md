---
title: Regroupement et dégroupement des lignes et des colonnes
type: docs
weight: 50
url: /fr/net/grouping-and-ungrouping-rows-and-columns/
---

## **Introduction**

Dans un fichier Microsoft Excel, vous pouvez créer un plan pour les données afin de vous permettre d'afficher et de masquer les niveaux de détail d'un simple clic de souris.

Cliquez sur les **symboles de plan**, 1,2,3, + et - pour afficher rapidement uniquement les lignes ou colonnes fournissant des résumés ou des en-têtes de sections dans une feuille de calcul, ou vous pouvez utiliser les symboles pour voir les détails sous un résumé ou une en-tête individuelle comme le montre la figure ci-dessous:

|**Regroupement des lignes et des colonnes.**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Gestion des groupes de lignes et de colonnes**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contient un [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fournit une [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) qui représente toutes les cellules de la feuille de calcul.

La collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) propose plusieurs méthodes pour gérer les lignes ou colonnes dans une feuille de calcul, dont certaines sont discutées plus en détail ci-dessous.

### **Regrouper des lignes et des colonnes**

Il est possible de regrouper des lignes ou des colonnes en appelant les méthodes [**GroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/grouprows/index) et [**GroupColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/groupcolumns/index) de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Les deux méthodes prennent les paramètres suivants :

- Indice de la première ligne/colonne, la première ligne ou colonne du groupe.
- Indice de la dernière ligne/colonne, la dernière ligne ou colonne du groupe.
- Est caché, un paramètre booléen qui spécifie s'il faut masquer ou non les lignes/colonnes après le regroupement.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-GroupingRowsAndColumns-1.cs" >}}

#### **Paramètres de regroupement**

Microsoft Excel vous permet de configurer les paramètres de regroupement pour l'affichage :

- Lignes de récapitulatif en dessous des détails.
- Colonnes de récapitulatif à droite des détails.

Les développeurs peuvent configurer ces paramètres de regroupement en utilisant la propriété [**Outline**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/outline) de la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

### **Lignes de résumé en dessous des détails**

Il est possible de contrôler si les lignes de récapitulatif sont affichées en dessous des détails en définissant la propriété [**SummaryRowBelow**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summaryrowbelow) de la classe [**Outline**](https://reference.aspose.com/cells/net/aspose.cells/outline) à **true** ou **false**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowBelow-1.cs" >}}

### **Colonnes récapitulatives à droite du détail**

Les développeurs peuvent également contrôler l'affichage des colonnes de récapitulatif à droite des détails en définissant la propriété [**SummaryColumnRight**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summarycolumnright) de la classe [**Outline**](https://reference.aspose.com/cells/net/aspose.cells/outline) à **true** ou **false**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowRight-1.cs" >}}

## **Désagréger les lignes et les colonnes**

Pour dissocier les lignes ou colonnes regroupées, appelez les méthodes [**UngroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index) et [**UngroupColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungroupcolumns) de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Les deux méthodes prennent deux paramètres :

- Indice de la première ligne ou colonne, la première ligne/colonne à dissocier.
- Indice de la dernière ligne ou colonne, la dernière ligne/colonne à dissocier.

[**UngroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index) a une surcharge qui prend un troisième paramètre booléen. Le définir sur **true** supprime toutes les informations regroupées. Sinon, seules les informations de groupe externe sont supprimées.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-UngroupingRowsAndColumns-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
