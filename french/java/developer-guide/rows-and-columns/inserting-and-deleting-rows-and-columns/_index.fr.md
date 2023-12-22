---
title: Insertion et suppression de lignes et de colonnes
type: docs
weight: 60
url: /fr/java/inserting-and-deleting-rows-and-columns/
description: Découvrez comment insérer et supprimer des lignes et des colonnes via les API Aspose.Cells for Java.
keywords: How to Insert and Delete Rows and Columns in Java, Insert Rows and Columns using Java, Java Delete Rows and Columns, Insert Rows or Columns with Java, Delete Rows or Columns via Java.
---
##  **Introduction**
Qu'il s'agisse de créer une nouvelle feuille de calcul à partir de zéro ou de travailler sur une feuille de calcul existante, nous devrons peut-être ajouter des lignes ou des colonnes supplémentaires pour accueillir plus de données. Inversement, nous pouvons également avoir besoin de supprimer des lignes ou des colonnes à partir de positions spécifiées dans la feuille de calcul.

Pour répondre à ces exigences, Aspose.Cells fournit un ensemble très simple de classes et de méthodes, décrites ci-dessous.
##  **Comment gérer les lignes/colonnes**
 Aspose.Cells fournit un[Cahier d'exercices](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe qui représente un fichier Excel Microsoft. Le[Cahier d'exercices](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la classe contient un[Collection de feuilles de calcul](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) classe. Le[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la classe fournit un[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)collection qui représente toutes les cellules de la feuille de calcul.

 Le[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)collection fournit plusieurs méthodes pour gérer les lignes et les colonnes dans une feuille de calcul. Certains d’entre eux sont discutés ci-dessous.

{{% alert color="primary" %}} 

Lorsque des lignes ou des colonnes sont ajoutées, le contenu de la feuille de calcul est décalé vers le bas ou vers la droite, mais si des lignes ou des colonnes sont supprimées, le contenu est décalé vers le haut ou vers la gauche.

{{% /alert %}} 
##  **Comment insérer une ligne**
 Insérez une ligne à n'importe quel endroit en appelant le[insérer des lignes](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\) ) méthode de[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collection. Le[insérer des lignes](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\))la méthode prend l'index de la ligne où la nouvelle ligne sera insérée comme premier argument, et le nombre de lignes à insérer comme deuxième argument.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingARow-InsertingARow.java" >}}
##  **Comment insérer plusieurs lignes**
 Pour insérer plusieurs lignes dans la feuille de calcul, appelez le[insérer des lignes](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\) ) méthode de[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collection. Le[insérer des lignes](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)) la méthode prend deux paramètres :

- Index de ligne : l'index de la ligne à partir de laquelle les nouvelles lignes seront insérées.
- Nombre de lignes : le nombre total de lignes à insérer.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingMultipleRows-InsertingMultipleRows.java" >}}
##  **Comment insérer une ligne avec formatage**
Pour insérer une ligne avec des options de formatage, utilisez le[insérer des lignes](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int,%20com.aspose.cells.InsertOptions\)surcharge qui prend[Options d'insertion](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)comme paramètre. Met le[CopierFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/insertoptions#CopyFormatType)propriété de[Options d'insertion](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)cours avec[CopierFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)Énumération. Le[CopierFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)L'énumération compte trois membres énumérés ci-dessous.

- [SAME_AS_ABOVE](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_ABOVE): Formate la ligne de la même manière que la ligne ci-dessus.
- [SAME_AS_BELOW](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_BELOW): Formate la ligne de la même manière que la ligne ci-dessous.
- [CLEAR](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#CLEAR): Efface le formatage.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-InsertingARowWithFormatting-1.java" >}}
##  **Comment supprimer une ligne**
 Pour supprimer une ligne à n'importe quel emplacement, appelez le[supprimer des lignes](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\) ) méthode de[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collection. Le[supprimer des lignes](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) la méthode prend deux paramètres :

- Index de ligne : l'index de la ligne à partir de laquelle les lignes seront supprimées.
- Nombre de lignes : le nombre total de lignes à supprimer.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteARow-DeleteARow.java" >}}
##  **Comment supprimer plusieurs lignes**
 Pour supprimer plusieurs lignes d'une feuille de calcul, appelez le[supprimer des lignes](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\) ) méthode de[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collection. Le[supprimer des lignes](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) la méthode prend deux paramètres :

- Index de ligne : l'index de la ligne à partir de laquelle les lignes seront supprimées.
- Nombre de lignes : le nombre total de lignes à supprimer.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteMultipleRows-DeleteMultipleRows.java" >}}
##  **Comment insérer une ou plusieurs colonnes**
 Les développeurs peuvent également insérer une colonne dans la feuille de calcul à n'importe quel endroit en appelant le[insérer des colonnes](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\) ) méthode de[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collection. Le[insérer des colonnes](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\)) la méthode prend deux paramètres :

- Index de colonne, l'index de la colonne à partir de laquelle la colonne sera insérée
- Nombre de colonnes, le nombre total de colonnes à insérer

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingAColumn-InsertingAColumn.java" >}}
##  **Comment supprimer une colonne**
 Pour supprimer une colonne de la feuille de calcul à n'importe quel endroit, appelez le[supprimerColonnes](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\) ) méthode de[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collection. Le[supprimerColonnes](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\)) la méthode prend les paramètres suivants :

- Index de colonne : l'index de la colonne à partir de laquelle la colonne sera supprimée.
- Nombre de colonnes : le nombre total de colonnes à supprimer.
- Mettre à jour la référence : paramètre booléen pour indiquer s'il faut mettre à jour les références dans d'autres feuilles de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteAColumn-DeleteAColumn.java" >}}

