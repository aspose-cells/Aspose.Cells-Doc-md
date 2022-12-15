---
title: Création d'un objet de liste
type: docs
weight: 20
url: /fr/python-java/creating-a-list-object/
---
L'utilisation de feuilles de calcul facilite le travail avec différents types de listes, par exemple. listes téléphoniques, listes de tâches. etc. Aspose.Cells prend en charge la création et la gestion de listes.

## **Avantages d'un objet de liste**

La conversion d'une liste de données en un véritable objet de liste présente de nombreux avantages :

- Les nouvelles lignes et colonnes sont automatiquement incluses.
- Une ligne de total au bas de votre liste peut être facilement ajoutée pour afficher SUM, AVERAGE, COUNT, etc.
- Les colonnes ajoutées à droite sont automatiquement incorporées dans l'objet Liste.
- Les graphiques basés sur des lignes et des colonnes seront développés automatiquement.
- Les plages nommées attribuées aux lignes et aux colonnes seront développées automatiquement.
- La liste est protégée contre la suppression accidentelle de lignes et de colonnes.

## **Création d'un objet de liste à l'aide d'Excel Microsoft**

**Sélection de la plage de données pour la création d'un objet de liste** 

![tâche : image_autre_texte](picture1.png)

Cela affiche la boîte de dialogue Créer une liste.

**Boîte de dialogue Créer une liste** 

![tâche : image_autre_texte](picture2.png)

Implémenter l'objet List et spécifier Total Row (Select**Données**, alors**Liste**, suivie par**Ligne totale**).

**Création d'un objet Liste** 

![tâche : image_autre_texte](picture3.png)

## **Création d'un objet de liste à l'aide de Aspose.Cells API**

Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/python/asposecells.api/Workbook), qui représente un fichier Excel Microsoft. La[**Cahier**](https://reference.aspose.com/cells/python/asposecells.api/Workbook)classe contient un[**Des feuilles de calcul**](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection)collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)classer. La[**Feuille de travail**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)La classe fournit un large éventail de propriétés et de méthodes pour gérer une feuille de calcul. Créer un[**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)dans une feuille de calcul, utilisez[**ListeObjets**](https://reference.aspose.com/cells/python/asposecells.api/worksheet#ListObjects)propriété de collection de la[**Feuille de travail**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet)classer. Chaque[**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)est en fait un objet de la[**ListObjectCollection**](https://reference.aspose.com/cells/python/asposecells.api/ListObjectCollection)classe, qui fournit en outre la[**ajouter**](https://reference.aspose.com/cells/python/asposecells.api/listobjectcollection#add(int,%20int,%20int,%20int,%20boolean)) pour ajouter un objet List et spécifier une plage de cellules pour la liste.

Selon la plage de cellules spécifiée, l'objet List est créé dans la feuille de calcul par Aspose.Cells. Utilisez les attributs (par exemple, ShowTotals, ListColumns, etc.)[**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)classe pour contrôler la liste.

Dans l'exemple ci-dessous, nous avons créé le même[**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject)en utilisant Aspose.Cells for Python via Java API comme nous l'avons créé en utilisant Microsoft Excel dans la section ci-dessus.

## Code source

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-CreatingListObject.py" >}}
