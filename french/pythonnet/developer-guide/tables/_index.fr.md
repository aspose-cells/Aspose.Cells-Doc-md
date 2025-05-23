---
title: Créez et gérez des tableaux de fichiers Microsoft Excel.
linktitle: Tableaux
type: docs
weight: 150
url: /fr/python-net/create-and-format-table/
description: Insérez, redimensionnez, modifiez, supprimez et formatez des tableaux de fichiers Excel en utilisant la bibliothèque Aspose.Cells.
---

## **Créer un tableau**

L'un des avantages des feuilles de calcul est qu'elles vous permettent de créer différents types de listes, par exemple des listes de téléphones, des listes de tâches, des listes de transactions, d'actifs ou de passifs. Plusieurs utilisateurs peuvent travailler ensemble pour utiliser, créer et maintenir des listes variées.

Aspose.Cells pour Python via .NET supporte la création et la gestion des listes.

### **Avantages d'un objet Liste**

Il y a quelques avantages lorsque vous convertissez une liste de données en un véritable objet Liste

- De nouvelles lignes et colonnes sont automatiquement incluses.
- Une ligne de total en bas de votre liste peut être facilement ajoutée pour afficher la SOMME, la MOYENNE, le NOMBRE, etc.
- Les colonnes ajoutées à droite sont automatiquement incorporées dans l'objet Liste.
- Les graphiques basés sur les lignes et colonnes seront automatiquement étendus.
- Les plages nommées affectées aux lignes et colonnes seront automatiquement étendues.
- La liste est protégée contre les suppressions accidentelles de lignes et de colonnes.

### **Création d'un objet Liste à l'aide de Microsoft Excel**

- Sélection de la plage de données pour la création d'un objet Liste
- Cela affiche la boîte de dialogue Créer Liste.
- Implémenter l'objet Liste pour les données et spécifier la ligne totale (Sélectionnez **Données**, puis **Liste**, suivi de **Ligne Totale**).

### **Utilisation de l’API Aspose.Cells pour Python via .NET**

Aspose.Cells pour Python via .NET fournit une classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contient une collection qui permet d’accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) offre une large gamme de propriétés et de méthodes pour gérer une feuille de calcul. Pour créer un [**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) dans une feuille de calcul, utilisez la propriété de collection [**list_objects**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/list_objects) de la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Chaque [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) est, en fait, un objet de la classe [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection/add/#int-int-int-int-bool), qui fournit en outre la méthode [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection/add/#int-int-int-int-bool) pour ajouter un objet Liste et spécifier une plage de cellules pour la liste.

Selon la plage de cellules spécifiée, l’objet List est créé par Aspose.Cells pour Python via .NET. Utilisez les attributs (par exemple, [**show_totals**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/show_totals), [**ListColumns**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/list_columns), etc.) de la classe [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) pour contrôler la liste.

Dans l’exemple ci-dessous, nous avons créé le même [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) en utilisant l’API Aspose.Cells pour Python via .NET que celui créé avec Microsoft Excel dans la section ci-dessus.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-CreatingListObject-1.py" >}}

## **Formater un Tableau**

Pour gérer et analyser un groupe de données connexes, il est possible de transformer une plage de cellules en un objet liste (également connu sous le nom de tableau Excel). Un tableau est une série de rangées et de colonnes contenant des données liées, gérées indépendamment des données dans d’autres rangées et colonnes. Par défaut, chaque colonne du tableau a le filtrage activé dans la ligne d’en-tête afin que vous puissiez filtrer ou trier rapidement vos données de liste. Vous pouvez ajouter une ligne de total (une ligne spéciale dans une liste qui fournit une sélection de fonctions agrégées utiles pour travailler avec des données numériques) à l’objet liste qui propose une liste déroulante de fonctions agrégées pour chaque cellule de la ligne de total. Aspose.Cells pour Python via .NET offre des options pour créer et gérer des listes (ou tableaux).

### **Formatage d'un Objet Liste**

Aspose.Cells pour Python via .NET fournit une classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) qui permet d’accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) offre une large gamme de propriétés et de méthodes pour gérer les feuilles de calcul. Pour créer un [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) dans une feuille de calcul, utilisez la propriété de collection [**list_objects**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/list_objects) de la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Chaque [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) est, en fait, un objet de la classe [**ListObjectCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection), qui fournit la méthode [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection/add/#int-int-int-int-bool) pour ajouter un objet Liste et spécifier la plage de cellules qu'il doit englober. Selon la plage de cellules spécifiée, un [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) est créé dans la feuille de calcul par Aspose.Cells. Utilisez les attributs (par exemple, [**table_style_type**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/table_style_type)) de la classe [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) pour formater le tableau selon vos besoins.

L'exemple ci-dessous ajoute des données d'exemple à une feuille de calcul, ajoute un [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) et applique des styles par défaut. Les styles [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject) sont pris en charge par Microsoft Excel 2007/2010.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-FormataListObject-1.py" >}}

## **Sujets avancés**
- [Convertir un Tableau en ODS](/cells/fr/python-net/convert-table-to-ods/)
- [Trouver des Tables de Requête et des Objets Liste liés aux Connexions de Données Externes](/cells/fr/python-net/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [Lire et Écrire un Tableau avec une Source de Données de Table de Requête](/cells/fr/python-net/read-and-write-table-with-query-table-data-source/)
- [Définir le Commentaire d'un Tableau ou Objet Liste à l'intérieur de la Feuille de Calcul](/cells/fr/python-net/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [Tables et Plages](/cells/fr/python-net/tables-and-ranges/)


