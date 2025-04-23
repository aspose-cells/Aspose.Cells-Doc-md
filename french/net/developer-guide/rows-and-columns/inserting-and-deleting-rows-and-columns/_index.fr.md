---
title: Insertion et suppression de lignes et colonnes dans un fichier Excel
linktitle: Insertion et suppression de lignes et de colonnes
type: docs
weight: 70
url: /fr/net/inserting-and-deleting-rows-and-columns/
description: Cet article montre comment insérer et supprimer des lignes et des colonnes via l API Aspose.Cells for .NET.
keywords: Aspose.Cells C# gérer les lignes et les colonnes, insérer des lignes et colonnes, supprimer des lignes et colonnes
---

## **Introduction**

Que vous créiez une nouvelle feuille de calcul à partir de zéro ou travailliez sur une feuille de calcul existante, vous pouvez avoir besoin d'ajouter des lignes ou des colonnes supplémentaires pour accueillir plus de données. Inversement, vous pouvez également avoir besoin de supprimer des lignes ou des colonnes à partir de positions spécifiées dans la feuille de calcul.
Pour répondre à ces exigences, Aspose.Cells fournit un ensemble très simple de classes et de méthodes, discutées ci-dessous.

### **Gérer les lignes et les colonnes**

Aspose.Cells fournit une classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) permettant d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fournit une collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) qui représente toutes les cellules de la feuille de calcul.

La collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) fournit plusieurs méthodes pour gérer les lignes et les colonnes dans une feuille de calcul. Certaines d'entre elles sont discutées ci-dessous.

{{% alert color="primary" %}}

Lors de l'ajout de lignes ou de colonnes, le contenu de la feuille de calcul est déplacé vers le bas ou vers la droite, et si des lignes ou des colonnes sont supprimées, le contenu est déplacé vers le haut ou la gauche.

{{% /alert %}}


## **Insérer des lignes et des colonnes**

### **Comment Insérer une Ligne**

Insérez une ligne dans la feuille de calcul à n'importe quel emplacement en appelant la méthode [**InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). La méthode [**InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) prend l'index de la ligne où la nouvelle ligne sera insérée.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARow-1.cs" >}}

### **Comment Insérer Plusieurs Lignes**

Pour insérer plusieurs lignes dans une feuille de calcul, appelez la méthode [**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). La méthode [**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) prend deux paramètres :

- Index de la ligne, l'index de la ligne à partir de laquelle les nouvelles lignes seront insérées.
- Nombre de lignes, le nombre total de lignes à insérer.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.cs" >}}

### **Comment insérer une ligne avec mise en forme**

Pour insérer une ligne avec des options de mise en forme, utilisez la surcharge [**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) qui prend [**InsertOptions**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) en paramètre. Définissez la propriété [**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) de la classe [**InsertOptions**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) avec l'énumération [**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype). L'énumération [**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) a trois membres comme indiqué ci-dessous.

- SameAsAbove: Formate la ligne de la même façon que la ligne ci-dessus.
- SameAsBelow: Formate la ligne de la même façon que la ligne ci-dessous.
- Clear: Efface la mise en forme.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.cs" >}}

### **Comment insérer une colonne**

Les développeurs peuvent également insérer une colonne dans la feuille de calcul à n'importe quel emplacement en appelant la méthode [**InsertColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn) de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). La méthode [**InsertColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn) prend l'index de la colonne où la nouvelle colonne sera insérée.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingAColumn-1.cs" >}}

## **Supprimer des lignes et des colonnes**

### **Comment supprimer plusieurs lignes**

Pour supprimer plusieurs lignes d'une feuille de calcul, appelez la méthode [**DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows) de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). La méthode [**DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows) prend deux paramètres :

- Index de la ligne, l'index de la ligne à partir de laquelle les lignes seront supprimées.
- Nombre de lignes, le nombre total de lignes à supprimer.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.cs" >}}


### **Comment supprimer une colonne**

Pour supprimer une colonne de la feuille de calcul à n'importe quel emplacement, appelez la méthode [**DeleteColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn) de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). La méthode [**DeleteColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn) prend l'index de la colonne à supprimer.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingAColumn-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
