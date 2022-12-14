---
title: Insertion et suppression de lignes et de colonnes d'un fichier Excel
linktitle: Insertion et suppression de lignes et de colonnes
type: docs
weight: 70
url: /fr/net/inserting-and-deleting-rows-and-columns/
---
## **Introduction**

Qu'il s'agisse de créer une nouvelle feuille de calcul à partir de zéro ou de travailler sur une feuille de calcul existante, nous devrons peut-être ajouter des lignes ou des colonnes supplémentaires pour accueillir plus de données. Inversement, nous pouvons également avoir besoin de supprimer des lignes ou des colonnes à partir de positions spécifiées dans la feuille de calcul.
Pour répondre à ces exigences, Aspose.Cells fournit un ensemble très simple de classes et de méthodes, décrites ci-dessous.

### **Gérer les lignes et les colonnes**

Aspose.Cells fournit une classe[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , qui représente un fichier Excel Microsoft. La[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contient un[**Des feuilles de calcul**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classer. La[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe offre une[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collection qui représente toutes les cellules de la feuille de calcul.

 La[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collection fournit plusieurs méthodes de gestion des lignes et des colonnes dans une feuille de calcul. Certains d'entre eux sont discutés ci-dessous.

{{% alert color="primary" %}}

Lorsque des lignes ou des colonnes sont ajoutées, le contenu de la feuille de calcul est décalé vers le bas ou vers la droite, et si des lignes ou des colonnes sont supprimées, le contenu est décalé vers le haut ou vers la gauche.

{{% /alert %}}


## **Insérer des lignes et des colonnes**

### **Insérer une ligne**

 Insérez une ligne dans la feuille de calcul à n'importe quel endroit en appelant le[**Insérer une ligne**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) méthode de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) le recueil. La[**Insérer une ligne**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow)La méthode prend l'index de la ligne où la nouvelle ligne sera insérée.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARow-1.cs" >}}

### **Insérer plusieurs lignes**

 Pour insérer plusieurs lignes dans une feuille de calcul, appelez le[**Insérer des lignes**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) méthode de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) le recueil. La[**Insérer des lignes**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)La méthode prend deux paramètres :

- Index de ligne, l'index de la ligne à partir de laquelle les nouvelles lignes seront insérées.
- Nombre de lignes, le nombre total de lignes qui doivent être insérées.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.cs" >}}

### **Insérer une ligne avec mise en forme**

Pour insérer une ligne avec des options de formatage, utilisez la[**Insérer des lignes**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)surcharge qui prend[**InsérerOptions**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) comme paramètre. Met le[**CopyFormatTypeCopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) propriété de[**InsérerOptions**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) classe avec[**CopyFormatTypeCopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) Énumération. La[**CopyFormatTypeCopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)L'énumération a trois membres comme indiqué ci-dessous.

- SameAsAbove : formate la ligne de la même manière que la ligne ci-dessus.
- SameAsBelow : formate la ligne de la même manière que la ligne ci-dessous.
- Effacer : efface le formatage.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.cs" >}}

### **Insérer une colonne**

 Les développeurs peuvent également insérer une colonne dans la feuille de calcul à n'importe quel endroit en appelant le[**Insérer une colonne**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn) méthode de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)le recueil. La[**Insérer une colonne**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn)prend l'index de la colonne où la nouvelle colonne sera insérée.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingAColumn-1.cs" >}}

## **Supprimer des lignes et des colonnes**

### **Supprimer plusieurs lignes**

Pour supprimer plusieurs lignes d'une feuille de calcul, appelez le[**Supprimer les lignes**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows) méthode de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) le recueil. La[**Supprimer les lignes**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows)La méthode prend deux paramètres :

- Index de ligne, l'index de la ligne à partir de laquelle les lignes seront supprimées.
- Nombre de lignes, le nombre total de lignes qui doivent être supprimées.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.cs" >}}


### **Supprimer une colonne**

 Pour supprimer une colonne de la feuille de calcul à n'importe quel endroit, appelez le[**SupprimerColonne**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn) méthode de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) le recueil. La[**SupprimerColonne**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn)prend l'index de la colonne à supprimer.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingAColumn-1.cs" >}}
