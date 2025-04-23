---
title: Regrouper, dégrouper les lignes et les colonnes
type: docs
weight: 30
url: /fr/go-cpp/grouping-ungrouping-rows-and-columns/
---

## **Introduction**

Dans un fichier Microsoft Excel, vous pouvez créer un plan pour les données afin de vous permettre d'afficher et de masquer les niveaux de détail d'un simple clic de souris.

Cliquez sur les **Symboles de l'arborescence**, 1,2,3, + et - pour afficher rapidement uniquement les lignes ou colonnes contenant des résumés ou des en-têtes pour les sections d'une feuille de calcul, ou vous pouvez utiliser les symboles pour voir les détails sous un résumé ou une en-tête individuel.

## **Gestion des groupes de lignes et de colonnes**

Aspose.Cells propose une classe, [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/), qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) contient une collection [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) permettant d’accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) offre une collection [Cells](https://reference.aspose.com/cells/go-cpp/cells/) qui représente toutes les cellules de la feuille.

La collection [Cells](https://reference.aspose.com/cells/go-cpp/cells/) fournit plusieurs méthodes pour gérer les lignes ou colonnes d’une feuille de calcul, dont quelques-unes sont discutées ci-dessous en détail.

### **Regroupement des lignes et des colonnes**

Il est possible de grouper des lignes ou des colonnes en appelant les méthodes [GroupRows](https://reference.aspose.com/cells/go-cpp/cells/grouprows/) et [GroupColumns](https://reference.aspose.com/cells/go-cpp/cells/groupcolumns/) de la collection [Cells](https://reference.aspose.com/cells/go-cpp/cells/). Les deux méthodes prennent les paramètres suivants :

- L'indice de la première ligne/colonne, la première ligne ou colonne du groupe.
- L'indice de la dernière ligne/colonne, la dernière ligne ou colonne du groupe.
- Est caché, un paramètre booléen qui spécifie s'il faut masquer ou non les lignes/colonnes après le regroupement.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GroupingRowsColumns.go" >}}

#### **Paramètres de regroupement**

Microsoft Excel vous permet de configurer les paramètres de regroupement pour l'affichage :

- Lignes de récapitulatif en dessous des détails.
- Colonnes de récapitulatif à droite des détails.

## **Dégroupement des lignes & des colonnes**

Pour désgrupper des lignes ou colonnes, appelez les méthodes [UngroupRows](https://reference.aspose.com/cells/go-cpp/cells/ungrouprows/) et [UngroupColumns](https://reference.aspose.com/cells/go-cpp/cells/ungroupcolumns/) de la collection [Cells](https://reference.aspose.com/cells/go-cpp/cells/). Chacune de ces méthodes prend deux paramètres :

- L'indice de la première ligne ou colonne, la première ligne/colonne à dissocier.
- L'indice de la dernière ligne ou colonne, la dernière ligne/colonne à dissocier.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UnGroupingRowsColumns.go" >}}
