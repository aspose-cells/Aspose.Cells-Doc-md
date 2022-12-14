---
title: Grouper, dégrouper des lignes et des colonnes
type: docs
weight: 30
url: /fr/cpp/grouping-ungrouping-rows-and-columns/
---
## **Introduction**
Dans un fichier Excel Microsoft, vous pouvez créer un plan pour les données afin de vous permettre d'afficher et de masquer les niveaux de détail d'un simple clic de souris.

 Clique le**Symboles de contour**, 1,2,3, + et - pour afficher rapidement uniquement les lignes ou les colonnes qui fournissent des résumés ou des en-têtes pour les sections d'une feuille de calcul, ou vous pouvez utiliser les symboles pour voir les détails sous un résumé ou un en-tête individuel.
## **Gestion de groupe de lignes et de colonnes**
 Aspose.Cells fournit une classe,[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) qui représente un fichier Excel Microsoft. La[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) classe contient un[Feuilles de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) collection qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classer. La[Feuille de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe offre une[ICellules](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)collection qui représente toutes les cellules de la feuille de calcul.

 La[ICellules](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)collection fournit plusieurs méthodes pour gérer les lignes ou les colonnes dans une feuille de calcul, quelques-unes d'entre elles sont décrites ci-dessous plus en détail.
### **Regroupement de lignes et de colonnes**
 Il est possible de grouper des lignes ou des colonnes en appelant le[GroupRows](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a88e0180ed1a4a423e0bd3ac599ef9332) et[GroupeColonnes](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#aaa14179e2a84ba5c2857f8434570d3d8) méthodes de la[ICellules](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)le recueil. Les deux méthodes prennent les paramètres suivants :

- L'index de la première ligne/colonne, la première ligne ou colonne du groupe.
- Le dernier index de ligne/colonne, la dernière ligne ou colonne du groupe.
- Est masqué, un paramètre booléen qui spécifie s'il faut masquer ou non les lignes/colonnes après le regroupement.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-GroupingRowsColumns.cpp" >}}
#### **Paramètres de groupe**
Microsoft Excel vous permet de configurer les paramètres de groupe pour afficher :

- Lignes récapitulatives sous les détails.
- Colonnes récapitulatives à droite du détail.
## **Dégrouper des lignes et des colonnes**
 Pour dégrouper des lignes ou des colonnes groupées, appelez le[ICellules](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) de la collection[Dissocier les lignes](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#adc1f6418506854ab41707bfef453ddb1) et[Dissocier les colonnes](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#aa3bf9a9510d4e85f68db9ebdcadc8406)méthodes. Les deux méthodes prennent deux paramètres :

- L'index de la première ligne ou colonne, la première ligne/colonne à dégrouper.
- Le dernier index de ligne ou de colonne, la dernière ligne/colonne à dissocier.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-UnGroupingRowsColumns.cpp" >}}
