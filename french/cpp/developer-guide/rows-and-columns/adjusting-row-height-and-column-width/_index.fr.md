---
title: Ajuster la hauteur de la ligne et la largeur de la colonne
type: docs
weight: 10
url: /fr/cpp/adjusting-row-height-and-column-width/
---

{{% alert color="primary" %}} 

Lorsque vous travaillez avec des feuilles de calcul et que vous ajoutez des données aux lignes ou aux colonnes, vous pouvez avoir besoin de modifier la hauteur des lignes ou la largeur des colonnes. Parfois, l'application d'un formatage sur les lignes ou les colonnes signifie que la hauteur ou la largeur actuelle doit changer pour afficher les données. Normalement, les utilisateurs ajustent les hauteurs de ligne et les largeurs de colonne dans un environnement WYSIWYG en utilisant Microsoft Excel. Mais, avec Aspose.Cells, les développeurs peuvent effectuer ces opérations à l'exécution.

{{% /alert %}} 
## **Travailler avec des lignes**
### **Ajuster la hauteur de la ligne**
Aspose.Cells fournit une classe, [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contient une [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fournit une collection [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) qui représente toutes les cellules de la feuille de calcul. La collection [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) propose plusieurs méthodes pour gérer les lignes ou les colonnes dans une feuille de calcul. Certaines d'entre elles sont discutées ci-dessous en détail.
#### **Définir la hauteur d'une ligne**
Il est possible de définir la hauteur d'une seule ligne en appelant la méthode [SetRowHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/) de la collection [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). La méthode [SetRowHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/) prend les paramètres suivants comme suit :

- **Index de ligne**, l'index de la ligne pour laquelle vous modifiez la hauteur.
- **Hauteur de la ligne**, la hauteur de la ligne à appliquer sur la ligne.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfRow-new.cpp" >}}


#### **Définir la hauteur de toutes les lignes dans une feuille de calcul**
Si les développeurs ont besoin de définir la même hauteur de ligne pour toutes les lignes dans la feuille de calcul, ils peuvent le faire en utilisant la méthode [SetStandardHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardheight/) de la collection [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/).



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfAllRowsInWorksheet-new.cpp" >}}
## **Travailler avec les colonnes**
### **Définir la largeur d'une colonne**
Définissez la largeur d'une colonne en appelant la méthode [SetColumnWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/) de la collection [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). La méthode [SetColumnWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/) prend les paramètres suivants :

- Index de la colonne, l'index de la colonne dont vous changez la largeur.
- Largeur de colonne, la largeur de colonne souhaitée.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfColumn-new.cpp" >}}
### **Réglage de la largeur de toutes les colonnes dans une feuille de calcul**
Pour définir la même largeur de colonne pour toutes les colonnes dans la feuille de calcul, utilisez la méthode [SetStandardWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardwidth/) de la collection [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/).



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfAllColumnsInWorksheet-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
