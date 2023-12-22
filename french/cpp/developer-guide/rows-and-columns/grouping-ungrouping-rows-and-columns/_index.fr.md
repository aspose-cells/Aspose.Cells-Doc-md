---
title: Regroupement, dissociation de lignes et de colonnes
type: docs
weight: 30
url: /fr/cpp/grouping-ungrouping-rows-and-columns/
---
##  **Introduction**
Dans un fichier Excel Microsoft, vous pouvez créer un aperçu des données afin de vous permettre d'afficher et de masquer les niveaux de détail d'un simple clic de souris.

Cliquez sur les *Symboles de plan**, 1,2,3, + et - pour afficher rapidement uniquement les lignes ou les colonnes qui fournissent des résumés ou des titres pour les sections d'une feuille de calcul, ou vous pouvez utiliser les symboles pour voir les détails sous un résumé individuel ou titre.
##  **Gestion de groupe des lignes et des colonnes**
 Aspose.Cells propose un cours,[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Excel Microsoft. Le[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la classe contient un[Des feuilles de calcul](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection qui permet d’accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe. Le[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) la classe fournit un[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)collection qui représente toutes les cellules de la feuille de calcul.

 Le[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)collection fournit plusieurs méthodes pour gérer les lignes ou les colonnes dans une feuille de calcul, quelques-unes d'entre elles sont abordées ci-dessous plus en détail.
###  **Regroupement de lignes et de colonnes**
 Il est possible de regrouper des lignes ou des colonnes en appelant la commande[Lignes de groupe](https://reference.aspose.com/cells/cpp/aspose.cells/cells/grouprows/) et[GroupeColonnes](https://reference.aspose.com/cells/cpp/aspose.cells/cells/groupcolumns/) méthodes du[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)collection. Les deux méthodes prennent les paramètres suivants :

- L'index de la première ligne/colonne, la première ligne ou colonne du groupe.
- Le dernier index de ligne/colonne, la dernière ligne ou colonne du groupe.
- Est masqué, un paramètre booléen qui spécifie s'il faut masquer ou non les lignes/colonnes après le regroupement.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-GroupingRowsColumns-new.cpp" >}}
####  **Paramètres du groupe**
Microsoft Excel permet de configurer les paramètres de groupe pour l'affichage :

- Les lignes récapitulatives ci-dessous sont détaillées.
- Colonnes récapitulatives à droite du détail.
##  **Dissocier les lignes et les colonnes**
 Pour dissocier des lignes ou des colonnes groupées, appelez le[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) la collection[Dissocier les lignes](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/) et[Dissocier les colonnes](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungroupcolumns/)méthodes. Les deux méthodes prennent deux paramètres :

- Premier index de ligne ou de colonne, première ligne/colonne à dissocier.
- Le dernier index de ligne ou de colonne, la dernière ligne/colonne à dissocier.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-UnGroupingRowsColumns-new.cpp" >}}
