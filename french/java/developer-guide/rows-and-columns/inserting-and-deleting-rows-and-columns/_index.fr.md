---
title: Insertion et suppression de lignes et de colonnes
type: docs
weight: 60
url: /fr/java/inserting-and-deleting-rows-and-columns/
description: Découvrez comment insérer et supprimer des lignes et des colonnes à travers les API Aspose.Cells for Java.
keywords: Comment insérer et supprimer des lignes et des colonnes en Java, Insérer des lignes et des colonnes en utilisant Java, Supprimer des lignes et des colonnes en Java, Insérer des lignes ou des colonnes avec Java, Supprimer des lignes ou des colonnes via Java.
---

## **Introduction**
Que vous créiez une nouvelle feuille de calcul à partir de zéro ou travailliez sur une feuille de calcul existante, vous pouvez avoir besoin d'ajouter des lignes ou des colonnes supplémentaires pour accueillir plus de données. Inversement, vous pouvez également avoir besoin de supprimer des lignes ou des colonnes à partir de positions spécifiées dans la feuille de calcul.

Pour répondre à ces exigences, Aspose.Cells fournit un ensemble très simple de classes et de méthodes, discutées ci-dessous.
## **Comment Gérer les Lignes/Colonnes**
Aspose.Cells fournit une [classe Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contient une [collection WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) fournit une collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) qui représente toutes les cellules de la feuille de calcul.

La collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) fournit plusieurs méthodes pour gérer les lignes et les colonnes dans une feuille de calcul. Certaines de ces méthodes sont discutées ci-dessous.

{{% alert color="primary" %}} 

Lorsque des lignes ou des colonnes sont ajoutées, le contenu de la feuille de calcul est déplacé vers le bas ou vers la droite, mais si des lignes ou des colonnes sont supprimées, le contenu est déplacé vers le haut ou vers la gauche.

{{% /alert %}} 
## **Comment Insérer une Ligne**
Insérer une ligne à n'importe quel endroit en appelant la méthode [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) de la collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). La méthode [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) prend en premier lieu l'indice de la ligne où la nouvelle ligne sera insérée, et en second lieu le nombre de lignes à insérer.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingARow-InsertingARow.java" >}}
## **Comment Insérer Plusieurs Lignes**
Pour insérer plusieurs lignes dans la feuille de calcul, appelez la méthode [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) de la collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). La méthode [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) prend deux paramètres :

- Indice de ligne : l'indice de la ligne à partir de laquelle les nouvelles lignes seront insérées.
- Nombre de lignes : le nombre total de lignes à insérer.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingMultipleRows-InsertingMultipleRows.java" >}}
## **Comment insérer une ligne avec mise en forme**
Pour insérer une ligne avec des options de mise en forme, utilisez la surcharge [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-com.aspose.cells.InsertOptions-) qui prend en paramètre [InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions). Définissez la propriété [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/insertoptions#CopyFormatType) de la classe [InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions) avec l’énumération [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType). L’énumération [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType) comporte trois membres, listés ci-dessous.

- [SAME_AS_ABOVE](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME-AS-ABOVE) : Formate la ligne de la même manière que la ligne ci-dessus.
- [SAME_AS_BELOW](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME-AS-BELOW):  Formate la ligne de la même manière que la ligne ci-dessous.
- [CLEAR](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#CLEAR) : Efface le formatage.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-InsertingARowWithFormatting-1.java" >}}
## **Comment supprimer une ligne**
Pour supprimer une ligne à n'importe quel endroit, appelez la méthode [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) de la collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). La méthode [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) prend deux paramètres :

- Indice de ligne : l'indice de la ligne à partir de laquelle les lignes seront supprimées.
- Nombre de lignes : le nombre total de lignes à supprimer.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteARow-DeleteARow.java" >}}
## **Comment supprimer plusieurs lignes**
Pour supprimer plusieurs lignes d'une feuille de calcul, appelez la méthode [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) de la collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). La méthode [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) prend deux paramètres :

- Indice de ligne : l'indice de la ligne à partir de laquelle les lignes seront supprimées.
- Nombre de lignes : le nombre total de lignes à supprimer.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteMultipleRows-DeleteMultipleRows.java" >}}
## **Comment insérer une ou plusieurs colonnes**
Les développeurs peuvent également insérer une colonne dans la feuille de calcul à n'importe quel endroit en appelant la méthode [insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns-int-int-) de la collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). La méthode [insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns-int-int-) prend deux paramètres :

- Index de colonne, l'index de la colonne à partir de laquelle la colonne sera insérée.
- Nombre de colonnes, le nombre total de colonnes à insérer

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingAColumn-InsertingAColumn.java" >}}
## **Comment supprimer une colonne**
Pour supprimer une colonne de la feuille de calcul à n'importe quel endroit, appelez la méthode [deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns-int-int-boolean-) de la collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). La méthode [deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns-int-int-boolean-) prend les paramètres suivants :

- Indice de colonne : l'indice de la colonne à partir de laquelle la colonne sera supprimée.
- Nombre de colonnes : le nombre total de colonnes à supprimer.
- Mettre à jour la référence : paramètre booléen pour indiquer s'il faut mettre à jour les références dans d'autres feuilles de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteAColumn-DeleteAColumn.java" >}}

{{< app/cells/assistant language="java" >}}
