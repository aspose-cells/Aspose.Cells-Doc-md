---
title: Insertion, suppression des lignes et des colonnes
type: docs
weight: 40
url: /fr/cpp/inserting-deleting-rows-and-columns/
---

## **Introduction**
Que ce soit pour créer une nouvelle feuille de calcul à partir de zéro ou pour travailler sur une feuille de calcul existante, nous pouvons avoir besoin d'ajouter des lignes ou des colonnes supplémentaires pour accueillir plus de données. Inversement, nous pouvons également avoir besoin de supprimer des lignes ou des colonnes à des positions spécifiées dans la feuille de calcul. Pour répondre à ces exigences, Aspose.Cells fournit un ensemble très simple de classes et de méthodes, discutées ci-dessous.
### **Gestion des lignes et des colonnes**
Aspose.Cells fournit une classe, [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contient une collection [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fournit une collection [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) qui représente toutes les cellules de la feuille de calcul.

La collection [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) propose plusieurs méthodes de gestion des lignes et des colonnes dans une feuille de calcul. Certaines d'entre elles sont discutées ci-dessous.

{{% alert color="primary" %}} 

Lors de l'ajout de lignes ou de colonnes, le contenu de la feuille de calcul est déplacé vers le bas ou vers la droite, et si des lignes ou des colonnes sont supprimées, le contenu est déplacé vers le haut ou la gauche.

{{% /alert %}} 
#### **Insérer une ligne**
Insérez une ligne dans la feuille de calcul à n'importe quel endroit en appelant la méthode [InsertRow](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) de la collection [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). La méthode [InsertRow](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) prend l'index de la ligne où la nouvelle ligne sera insérée.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertRow-new.cpp" >}}


#### **Insertion de plusieurs lignes**
Pour insérer plusieurs lignes dans une feuille de calcul, appelez la méthode [InsertRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) de la collection [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). La méthode [InsertRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) prend deux paramètres :

- Index de la ligne, l'index de la ligne à partir de laquelle les nouvelles lignes seront insérées.
- Nombre de lignes, le nombre total de lignes à insérer.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertingMultipleRows-new.cpp" >}}


#### **Suppression de plusieurs lignes**
Pour supprimer plusieurs lignes d'une feuille de calcul, appelez la méthode [DeleteRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) de la collection [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). La méthode [DeleteRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) prend deux paramètres :

- Index de la ligne, l'index de la ligne à partir de laquelle les lignes seront supprimées.
- Nombre de lignes, le nombre total de lignes à supprimer.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeletingMultipleRows-new.cpp" >}}


#### **Insérer une colonne**
Les développeurs peuvent également insérer une colonne dans la feuille de calcul à n'importe quel emplacement en appelant la méthode [InsertColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) de la collection [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). La méthode [InsertColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) prend l'index de la colonne où la nouvelle colonne sera insérée.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertColumn-new.cpp" >}}


#### **Supprimer une colonne**
Pour supprimer une colonne de la feuille de calcul à n'importe quel emplacement, appelez la méthode [DeleteColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) de la collection [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). La méthode [DeleteColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) prend l'index de la colonne à supprimer.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeleteColumn-new.cpp" >}}
