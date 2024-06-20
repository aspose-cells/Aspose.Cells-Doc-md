---
title: Création d un objet de liste
type: docs
weight: 20
url: /fr/python-java/creating-a-list-object/
---

L'utilisation de feuilles de calcul facilite le travail avec différents types de listes, par exemple listes de téléphone, listes de tâches, etc. Aspose.Cells prend en charge la création et la gestion de listes.

## **Avantages d'un objet Liste**

Il existe plusieurs avantages lorsque vous convertissez une liste de données en un véritable objet de liste :

- De nouvelles lignes et colonnes sont automatiquement incluses.
- Une ligne de total en bas de votre liste peut être facilement ajoutée pour afficher la SOMME, la MOYENNE, le NOMBRE, etc.
- Les colonnes ajoutées à droite sont automatiquement incorporées dans l'objet Liste.
- Les graphiques basés sur les lignes et colonnes seront automatiquement étendus.
- Les plages nommées affectées aux lignes et colonnes seront automatiquement étendues.
- La liste est protégée contre les suppressions accidentelles de lignes et de colonnes.

## **Création d'un objet Liste à l'aide de Microsoft Excel**

**Sélection de la plage de données pour la création d'un objet liste** 

![todo:image_alt_text](picture1.png)

Cela affiche la boîte de dialogue Créer une liste.

**Boîte de dialogue Créer une liste** 

![todo:image_alt_text](picture2.png)

Mise en œuvre de l'objet de liste et spécification de la ligne totale (Sélectionnez **Données**, puis **Liste**, suivi de **Ligne totale**).

**Création d'un objet liste** 

![todo:image_alt_text](picture3.png)

## **Création d'un objet de liste à l'aide de l'API Aspose.Cells**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/python/asposecells.api/Workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python/asposecells.api/Workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python/asposecells.api/Worksheet) fournit un large éventail de propriétés et de méthodes pour gérer une feuille de calcul. Pour créer une [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject) dans une feuille de calcul, utilisez la propriété de collection de la classe [**ListObjects**](https://reference.aspose.com/cells/python/asposecells.api/worksheet#ListObjects). Chaque [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject) est en fait un objet de la classe [**ListObjectCollection**](https://reference.aspose.com/cells/python/asposecells.api/ListObjectCollection), qui fournit en outre la méthode [**add**](https://reference.aspose.com/cells/python/asposecells.api/listobjectcollection#add(int,%20int,%20int,%20int,%20boolean)) pour ajouter un objet Liste et spécifier une plage de cellules pour la liste.

Selon la plage de cellules spécifiée, l'objet Liste est créé dans la feuille de calcul par Aspose.Cells. Utilisez les attributs (par exemple, ShowTotals, ListColumns, etc.) de la classe [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject) pour contrôler la liste.

Dans l'exemple ci-dessous, nous avons créé le même [**ListObject**](https://reference.aspose.com/cells/python/asposecells.api/ListObject) en utilisant Aspose.Cells for Python via Java API comme nous l'avons créé en utilisant Microsoft Excel dans la section précédente.

## Code source

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-CreatingListObject.py" >}}
