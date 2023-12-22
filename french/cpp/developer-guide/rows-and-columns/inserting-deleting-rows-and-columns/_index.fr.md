---
title: Insertion, suppression de lignes et de colonnes
type: docs
weight: 40
url: /fr/cpp/inserting-deleting-rows-and-columns/
---
##  **Introduction**
Qu'il s'agisse de créer une nouvelle feuille de calcul à partir de zéro ou de travailler sur une feuille de calcul existante, nous devrons peut-être ajouter des lignes ou des colonnes supplémentaires pour accueillir plus de données. Inversement, nous pouvons également avoir besoin de supprimer des lignes ou des colonnes à partir de positions spécifiées dans la feuille de calcul. Pour répondre à ces exigences, Aspose.Cells fournit un ensemble très simple de classes et de méthodes, décrites ci-dessous.
###  **Gestion des lignes et des colonnes**
 Aspose.Cells propose un cours,[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) , cela représente un fichier Excel Microsoft. Le[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la classe contient un[Des feuilles de calcul](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe. Le[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) la classe fournit un[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)collection qui représente toutes les cellules de la feuille de calcul.

 Le[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)collection fournit plusieurs méthodes de gestion des lignes et des colonnes dans une feuille de calcul. Certains d’entre eux sont discutés ci-dessous.

{{% alert color="primary" %}} 

Lorsque des lignes ou des colonnes sont ajoutées, le contenu de la feuille de calcul est décalé vers le bas ou vers la droite, et si des lignes ou des colonnes sont supprimées, le contenu est décalé vers le haut ou vers la gauche.

{{% /alert %}} 
####  **Insérer une ligne**
 Insérez une ligne dans la feuille de calcul à n'importe quel endroit en appelant le[Insérer une ligne](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) méthode du[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection. Le[Insérer une ligne](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/)La méthode prend l’index de la ligne où la nouvelle ligne sera insérée.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertRow-new.cpp" >}}


####  **Insertion de plusieurs lignes**
 Pour insérer plusieurs lignes dans une feuille de calcul, appelez le[Insérer des lignes](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) méthode du[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection. Le[Insérer des lignes](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/)La méthode prend deux paramètres :

- Index de ligne, l'index de la ligne à partir de laquelle les nouvelles lignes seront insérées.
- Nombre de lignes, nombre total de lignes à insérer.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertingMultipleRows-new.cpp" >}}


####  **Suppression de plusieurs lignes**
 Pour supprimer plusieurs lignes d'une feuille de calcul, appelez le[Supprimer les lignes](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) méthode du[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection. Le[Supprimer les lignes](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/)La méthode prend deux paramètres :

- Index de ligne, l'index de la ligne à partir de laquelle les lignes seront supprimées.
- Nombre de lignes, nombre total de lignes à supprimer.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeletingMultipleRows-new.cpp" >}}


####  **Insérer une colonne**
 Les développeurs peuvent également insérer une colonne dans la feuille de calcul à n'importe quel endroit en appelant le[Insérer une colonne](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) méthode du[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection.[Insérer une colonne](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/)La méthode prend l’index de la colonne où la nouvelle colonne sera insérée.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertColumn-new.cpp" >}}


####  **Supprimer une colonne**
 Pour supprimer une colonne de la feuille de calcul à n'importe quel endroit, appelez le[Supprimer la colonne](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) méthode du[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection. Le[Supprimer la colonne](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/)La méthode prend l’index de la colonne à supprimer.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeleteColumn-new.cpp" >}}
