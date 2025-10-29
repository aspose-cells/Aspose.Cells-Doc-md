---
title: Insertion et suppression de lignes et colonnes dans un fichier Excel
linktitle: Insertion et suppression de lignes et de colonnes
type: docs
weight: 70
url: /fr/python-net/inserting-and-deleting-rows-and-columns/
description: Cet article montre comment insérer et supprimer des lignes et des colonnes à l aide de l API Aspose.Cells for Python via .NET.
keywords: Python Excel Library, Aspose.Cells Python gère les lignes et les colonnes, insertion de lignes et de colonnes en python, suppression de lignes et de colonnes en python, supprimer des lignes et des colonnes.
---

## **Introduction**

Que vous créiez une nouvelle feuille de calcul à partir de zéro ou travailliez sur une feuille de calcul existante, vous pouvez avoir besoin d'ajouter des lignes ou des colonnes supplémentaires pour accueillir plus de données. Inversement, vous pouvez également avoir besoin de supprimer des lignes ou des colonnes à partir de positions spécifiées dans la feuille de calcul.
Pour répondre à ces exigences, Aspose.Cells pour Python via .NET fournit un ensemble très simple de classes et de méthodes, discuté ci-dessous.

### **Gérer les lignes et les colonnes**

Aspose.Cells pour Python via .NET fournit une classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fournit une collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) qui représente toutes les cellules de la feuille de calcul.

La collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) fournit plusieurs méthodes pour gérer les lignes et les colonnes dans une feuille de calcul. Certaines d'entre elles sont discutées ci-dessous.

{{% alert color="primary" %}}

Lors de l'ajout de lignes ou de colonnes, le contenu de la feuille de calcul est déplacé vers le bas ou vers la droite, et si des lignes ou des colonnes sont supprimées, le contenu est déplacé vers le haut ou la gauche.

{{% /alert %}}


## **Insérer des lignes et des colonnes**

### **Comment Insérer une Ligne**

Insérez une ligne dans la feuille de calcul à n'importe quel emplacement en appelant la méthode [**insert_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_row/) de la collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). La méthode [**insert_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_row/) prend l'index de la ligne où la nouvelle ligne sera insérée.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingARow-1.py" >}}

### **Comment Insérer Plusieurs Lignes**

Pour insérer plusieurs lignes dans une feuille de calcul, appelez la méthode [**insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/#int-int) de la collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). La méthode [**insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/#int-int) prend deux paramètres :

- Index de la ligne, l'index de la ligne à partir de laquelle les nouvelles lignes seront insérées.
- Nombre de lignes, le nombre total de lignes à insérer.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.py" >}}

### **Comment insérer une ligne avec mise en forme**

Pour insérer une ligne avec des options de mise en forme, utilisez la surcharge [**insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/#int-int-aspose.cells.InsertOptions) qui prend [**InsertOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/insertoptions) en paramètre. Définissez la propriété [**copy_format_type**](https://reference.aspose.com/cells/python-net/aspose.cells/insertoptions/copy_format_type/) de la classe [**InsertOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/insertoptions) avec l'énumération [**CopyFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells/copyformattype/). L'énumération [**CopyFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells/copyformattype/) a trois membres comme indiqué ci-dessous.

- SAME_AS_ABOVE : Formate la ligne de la même manière que la ligne précédente.
- SAME_AS_BELOW : Formate la ligne de la même manière que la ligne suivante.
- CLEAR : Efface la mise en forme.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.py" >}}

### **Comment insérer une colonne**

Les développeurs peuvent également insérer une colonne dans la feuille de calcul à n'importe quel emplacement en appelant la méthode [**insert_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_column/#int) de la collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). La méthode [**insert_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_column/#int) prend l'index de la colonne où la nouvelle colonne sera insérée.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingAColumn-1.py" >}}

## **Supprimer des lignes et des colonnes**

### **Comment supprimer plusieurs lignes**

Pour supprimer plusieurs lignes d'une feuille de calcul, appelez la méthode [**delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/#int-int) de la collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). La méthode [**delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/#int-int) prend deux paramètres :

- Index de la ligne, l'index de la ligne à partir de laquelle les lignes seront supprimées.
- Nombre de lignes, le nombre total de lignes à supprimer.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.py" >}}


### **Comment supprimer une colonne**

Pour supprimer une colonne de la feuille de calcul à n'importe quel emplacement, appelez la méthode [**delete_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_column/#int) de la collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). La méthode [**delete_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_column/#int) prend l'index de la colonne à supprimer.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-DeletingAColumn-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
