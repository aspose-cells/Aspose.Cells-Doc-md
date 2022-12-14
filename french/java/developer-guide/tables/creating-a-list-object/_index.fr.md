---
title: Création d'un tableau
type: docs
weight: 40
url: /fr/java/creating-a-list-object/
---
{{% alert color="primary" %}}

L'un des avantages des feuilles de calcul est qu'elles vous permettent de créer différents types de listes, par exemple des listes téléphoniques, des listes de tâches, des listes de transactions, d'actifs ou de passifs. Plusieurs utilisateurs peuvent travailler ensemble pour utiliser, créer et maintenir diverses listes.

Aspose.Cells prend en charge la création et la gestion de listes.

{{% /alert %}}

## **Avantages d'un tableau**

La conversion d'une liste de données en un véritable objet de liste présente de nombreux avantages :

- Les nouvelles lignes et colonnes sont automatiquement incluses.
- Une ligne de total au bas de votre liste peut être facilement ajoutée pour afficher SUM, AVERAGE, COUNT, etc.
- Les colonnes ajoutées à droite sont automatiquement incorporées dans l'objet Liste.
- Les graphiques basés sur des lignes et des colonnes seront développés automatiquement.
- Les plages nommées attribuées aux lignes et aux colonnes seront développées automatiquement.
- La liste est protégée contre la suppression accidentelle de lignes et de colonnes.

## **Création d'un tableau à l'aide d'Excel Microsoft**

**Sélection de la plage de données pour la création d'un objet de liste** 

![tâche : image_autre_texte](creating-a-list-object_1.png)

Cela affiche la boîte de dialogue Créer une liste.

**Boîte de dialogue Créer une liste** 

![tâche : image_autre_texte](creating-a-list-object_2.png)

 Implémenter l'objet List et spécifier Total Row (Select**Données** , alors**Liste** , suivie par**Ligne totale**).

**Création d'un objet Liste** 

![tâche : image_autre_texte](creating-a-list-object_3.png)

## **Création d'un tableau à l'aide de Aspose.Cells API**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , qui représente un fichier Excel Microsoft. La[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe contient un[**Des feuilles de calcul**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

 Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classer. La[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) La classe fournit un large éventail de propriétés et de méthodes pour gérer une feuille de calcul. Créer un[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) dans une feuille de calcul, utilisez[**ListeObjets**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects) propriété de collection de la classe Worksheet. Chaque[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) est en fait un objet de la[**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection)class, qui fournit en outre la méthode add pour ajouter un objet List et spécifier une plage de cellules pour la liste.

Selon la plage de cellules spécifiée, l'objet List est créé dans la feuille de calcul par Aspose.Cells. Utilisez les attributs (par exemple, ShowTotals, ListColumns, etc.)[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)classe pour contrôler la liste.

 Dans l'exemple ci-dessous, nous avons créé le même[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)en utilisant Aspose.Cells API comme nous l'avons créé en utilisant Microsoft Excel dans la section ci-dessus.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-CreatingListObject-CreatingListObject.java" >}}
