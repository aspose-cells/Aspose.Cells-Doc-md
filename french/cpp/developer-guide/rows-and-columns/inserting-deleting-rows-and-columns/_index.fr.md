---
title: Insertion, suppression de lignes et de colonnes
type: docs
weight: 40
url: /fr/cpp/inserting-deleting-rows-and-columns/
---
## **Introduction**
Qu'il s'agisse de créer une nouvelle feuille de calcul à partir de zéro ou de travailler sur une feuille de calcul existante, nous devrons peut-être ajouter des lignes ou des colonnes supplémentaires pour accueillir plus de données. Inversement, nous pouvons également avoir besoin de supprimer des lignes ou des colonnes à partir de positions spécifiées dans la feuille de calcul. Pour répondre à ces exigences, Aspose.Cells fournit un ensemble très simple de classes et de méthodes, décrites ci-dessous.
### **Gestion des lignes et des colonnes**
 Aspose.Cells fournit une classe,[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) , qui représente un fichier Excel Microsoft. La[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) classe contient un[Feuilles de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par le[Feuille de calcul](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classer. La[Feuille de calcul](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe offre une[ICellules](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)collection qui représente toutes les cellules de la feuille de calcul.

 La[ICellules](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)collection fournit plusieurs méthodes de gestion des lignes et des colonnes dans une feuille de calcul. Certains d'entre eux sont discutés ci-dessous.

{{% alert color="primary" %}} 

Lorsque des lignes ou des colonnes sont ajoutées, le contenu de la feuille de calcul est décalé vers le bas ou vers la droite, et si des lignes ou des colonnes sont supprimées, le contenu est décalé vers le haut ou vers la gauche.

{{% /alert %}} 
#### **Insérer une ligne**
 Insérez une ligne dans la feuille de calcul à n'importe quel endroit en appelant le[Insérer une ligne](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ad9c067ccb5f34a7740f5d1cc3dbefbe7) méthode de la[ICellules](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) le recueil. La[Insérer une ligne](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ad9c067ccb5f34a7740f5d1cc3dbefbe7)La méthode prend l'index de la ligne où la nouvelle ligne sera insérée.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertRow.cpp" >}}


#### **Insertion de plusieurs lignes**
 Pour insérer plusieurs lignes dans une feuille de calcul, appelez le[Insérer des lignes](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a61e4cd6dcaeeb0d11afd54616df75ee0) méthode de la[ICellules](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) le recueil. La[Insérer des lignes](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a61e4cd6dcaeeb0d11afd54616df75ee0)La méthode prend deux paramètres :

- Index de ligne, l'index de la ligne à partir de laquelle les nouvelles lignes seront insérées.
- Nombre de lignes, le nombre total de lignes qui doivent être insérées.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertingMultipleRows.cpp" >}}


#### **Suppression de plusieurs lignes**
Pour supprimer plusieurs lignes d'une feuille de calcul, appelez le[Supprimer les lignes](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a251261027b564ebdf27c2c6d5149c0e1) méthode de la[ICellules](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) le recueil. La[Supprimer les lignes](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a251261027b564ebdf27c2c6d5149c0e1)La méthode prend deux paramètres :

- Index de ligne, l'index de la ligne à partir de laquelle les lignes seront supprimées.
- Nombre de lignes, le nombre total de lignes qui doivent être supprimées.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeletingMultipleRows.cpp" >}}


#### **Insérer une colonne**
 Les développeurs peuvent également insérer une colonne dans la feuille de calcul à n'importe quel endroit en appelant le[Insérer une colonne](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a8e8cb6d0812129669258378649b3fd55) méthode de la[ICellules](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) le recueil.[Insérer une colonne](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a8e8cb6d0812129669258378649b3fd55)prend l'index de la colonne où la nouvelle colonne sera insérée.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertColumn.cpp" >}}


#### **Supprimer une colonne**
 Pour supprimer une colonne de la feuille de calcul à n'importe quel endroit, appelez le[SupprimerColonne](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ae00721fd2be220e7b73b2cab6a70e89b) méthode de la[ICellules](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) le recueil. La[SupprimerColonne](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ae00721fd2be220e7b73b2cab6a70e89b)prend l'index de la colonne à supprimer.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeleteColumn.cpp" >}}
