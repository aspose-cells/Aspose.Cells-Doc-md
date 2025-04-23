---
title: Création d un tableau
type: docs
weight: 40
url: /fr/java/creating-a-list-object/
---

{{% alert color="primary" %}}

L'un des avantages des feuilles de calcul est qu'elles vous permettent de créer différents types de listes, par exemple des listes de téléphones, des listes de tâches, des listes de transactions, d'actifs ou de passifs. Plusieurs utilisateurs peuvent travailler ensemble pour utiliser, créer et maintenir des listes variées.

Aspose.Cells prend en charge la création et la gestion de listes.

{{% /alert %}}

## **Avantages d'un tableau**

Il existe plusieurs avantages lorsque vous convertissez une liste de données en un véritable objet de liste :

- De nouvelles lignes et colonnes sont automatiquement incluses.
- Une ligne de total en bas de votre liste peut être facilement ajoutée pour afficher la SOMME, la MOYENNE, le NOMBRE, etc.
- Les colonnes ajoutées à droite sont automatiquement incorporées dans l'objet Liste.
- Les graphiques basés sur les lignes et colonnes seront automatiquement étendus.
- Les plages nommées affectées aux lignes et colonnes seront automatiquement étendues.
- La liste est protégée contre les suppressions accidentelles de lignes et de colonnes.

## **Créer un tableau à l'aide de Microsoft Excel**

**Sélection de la plage de données pour la création d'un objet liste** 

![todo:image_alt_text](creating-a-list-object_1.png)

Cela affiche la boîte de dialogue Créer une liste.

**Boîte de dialogue Créer une liste** 

![todo:image_alt_text](creating-a-list-object_2.png)

Implémentation de l'objet Liste et spécification de la ligne totale (Sélectionnez ** Données **, puis ** Liste **, suivi de ** Ligne totale **).

**Création d'un objet liste** 

![todo:image_alt_text](creating-a-list-object_3.png)

## **Créer un tableau à l'aide de l'API Aspose.Cells**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) fournit une grande variété de propriétés et de méthodes pour gérer une feuille de calcul. Pour créer un [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) dans une feuille de calcul, utilisez la propriété de collection [**ListObjects**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects) de la classe Feuille de calcul. Chaque [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) est, en fait, un objet de la classe [**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection), qui fournit en outre la méthode d'ajout pour ajouter un objet Liste et spécifier une plage de cellules pour la liste.

Selon la plage de cellules spécifiée, l'objet Liste est créé dans la feuille de calcul par Aspose.Cells. Utilisez les attributs (par exemple, AfficherTotals, ColonnesListe, etc.) de la classe [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) pour contrôler la liste.

Dans l'exemple ci-dessous, nous avons créé le même [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) en utilisant l'API Aspose.Cells comme nous l'avons créé en utilisant Microsoft Excel dans la section précédente.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-CreatingListObject-CreatingListObject.java" >}}
{{< app/cells/assistant language="java" >}}
