---
title: Ajustement de la hauteur des lignes et de la largeur des colonnes
type: docs
weight: 10
url: /fr/cpp/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}} 

Lorsque vous travaillez avec des feuilles de calcul et que vous ajoutez des données à des lignes ou des colonnes, vous devrez peut-être modifier la hauteur des lignes ou la largeur des colonnes. Parfois, l'application d'une mise en forme sur des lignes ou des colonnes signifie que la hauteur ou la largeur actuelle doit changer pour afficher les données. Normalement, les utilisateurs ajustent la hauteur des lignes et la largeur des colonnes dans un environnement WYSIWYG à l'aide de Microsoft Excel. Mais, avec Aspose.Cells, les développeurs peuvent effectuer ces opérations lors de l'exécution.

{{% /alert %}} 
## **Travailler avec des lignes**
### **Réglage de la hauteur de rangée**
 Aspose.Cells fournit une classe,[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) qui représente un fichier Excel Microsoft. Le[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) classe contient un[IWorksheetCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe. Le[Feuille de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) la classe offre une[ICellules](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) collection qui représente toutes les cellules de la feuille de calcul. Le[ICellules](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)collection fournit plusieurs méthodes pour gérer les lignes ou les colonnes dans une feuille de calcul. Certains d'entre eux sont discutés ci-dessous plus en détail.
#### **Définition de la hauteur d'une ligne**
 Il est possible de définir la hauteur d'une seule ligne en appelant le[ICellules](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) de la collection[Définir la hauteur de ligne](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7aa441877e03639232299627261a7d1f) méthode. Le[Définir la hauteur de ligne](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7aa441877e03639232299627261a7d1f)prend les paramètres suivants comme suit :

- **Indice de ligne**, l'index de la ligne dont vous modifiez la hauteur.
- **Hauteur de ligne**, la hauteur de ligne à appliquer sur la ligne.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfRow.cpp" >}}


#### **Définition de la hauteur de toutes les lignes d'une feuille de calcul**
 Si les développeurs doivent définir la même hauteur de ligne pour toutes les lignes de la feuille de calcul, ils peuvent le faire en utilisant le[Définir la hauteur standard](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a0b79a3163e2b601aa1b6a6a1e3f1467f) méthode de la[ICellules](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)le recueil.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfAllRowsInWorksheet.cpp" >}}
## **Travailler avec des colonnes**
### **Définition de la largeur d'une colonne**
 Définissez la largeur d'une colonne en appelant la[ICellules](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) de la collection[DéfinirLargeurColonne](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ab1c6a4e89760d2a022d5bfba8bc40987) méthode. Le[DéfinirLargeurColonne](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ab1c6a4e89760d2a022d5bfba8bc40987)méthode prend les paramètres suivants :

- **Indice de colonne**, l'index de la colonne dont vous modifiez la largeur.
- **Largeur de colonne**, la largeur de colonne souhaitée.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfColumn.cpp" >}}
### **Définition de la largeur de toutes les colonnes dans une feuille de calcul**
 Pour définir la même largeur de colonne pour toutes les colonnes de la feuille de calcul, utilisez la[ICellules](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) de la collection[DéfinirLargeurStandard](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a48f5dbccc3bf4bb9e6e882094b500bd7)méthode.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfAllColumnsInWorksheet.cpp" >}}
