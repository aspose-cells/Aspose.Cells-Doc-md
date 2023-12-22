---
title: Ajustement de la hauteur des lignes et de la largeur des colonnes
type: docs
weight: 10
url: /fr/cpp/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}} 

Lorsque vous travaillez avec des feuilles de calcul et ajoutez des données à des lignes ou des colonnes, vous devrez peut-être modifier la hauteur des lignes ou la largeur des colonnes. Parfois, l'application d'un formatage sur des lignes ou des colonnes signifie que la hauteur ou la largeur actuelle doit être modifiée pour afficher les données. Normalement, les utilisateurs ajustent la hauteur des lignes et la largeur des colonnes dans un environnement WYSIWYG à l'aide d'Excel Microsoft. Mais, avec Aspose.Cells, les développeurs peuvent effectuer ces opérations au moment de l'exécution.

{{% /alert %}} 
##  **Travailler avec des lignes**
###  **Ajustement de la hauteur des rangées**
 Aspose.Cells propose un cours,[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Excel Microsoft. Le[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la classe contient un[Collection de feuilles de calcul](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe. Le[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) la classe fournit un[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection qui représente toutes les cellules de la feuille de calcul. Le[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)La collection fournit plusieurs méthodes pour gérer les lignes ou les colonnes d’une feuille de calcul. Certains d’entre eux sont abordés ci-dessous plus en détail.
####  **Définition de la hauteur d'une ligne**
 Il est possible de définir la hauteur d'une seule ligne en appelant la commande[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) la collection[Définir la hauteur de la ligne](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/) méthode. Le[Définir la hauteur de la ligne](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/)La méthode prend les paramètres suivants comme suit :

- *Indice de ligne**, l'index de la ligne dont vous modifiez la hauteur.
- *Hauteur de ligne**, la hauteur de ligne à appliquer sur la ligne.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfRow-new.cpp" >}}


####  **Définition de la hauteur de toutes les lignes d'une feuille de calcul**
 Si les développeurs doivent définir la même hauteur de ligne pour toutes les lignes de la feuille de calcul, ils peuvent le faire en utilisant l'option[DéfinirHauteurStandard](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardheight/) méthode du[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)collection.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfAllRowsInWorksheet-new.cpp" >}}
##  **Travailler avec des colonnes**
###  **Définition de la largeur d'une colonne**
 Définissez la largeur d'une colonne en appelant le[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) la collection[Définir la largeur de la colonne](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/) méthode. Le[Définir la largeur de la colonne](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/)La méthode prend les paramètres suivants :

- *Indice de colonne**, l'index de la colonne dont vous modifiez la largeur.
- *Largeur de colonne**, la largeur de colonne souhaitée.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfColumn-new.cpp" >}}
###  **Définition de la largeur de toutes les colonnes d'une feuille de calcul**
 Pour définir la même largeur de colonne pour toutes les colonnes de la feuille de calcul, utilisez l'option[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) la collection[Définir la largeur standard](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardwidth/)méthode.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfAllColumnsInWorksheet-new.cpp" >}}
