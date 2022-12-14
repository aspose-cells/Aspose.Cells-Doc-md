---
title: Créer et gérer des tableaux de fichiers Excel Microsoft.
linktitle: les tables
type: docs
weight: 150
url: /fr/net/create-and-format-table/
description: Insérez, redimensionnez, modifiez, supprimez, formatez le tableau des fichiers Excel à l'aide de la bibliothèque Aspose.Cells.
---
## **Créer un tableau**

L'un des avantages des feuilles de calcul est qu'elles vous permettent de créer différents types de listes, par exemple des listes téléphoniques, des listes de tâches, des listes de transactions, d'actifs ou de passifs. Plusieurs utilisateurs peuvent travailler ensemble pour utiliser, créer et maintenir diverses listes.

Aspose.Cells prend en charge la création et la gestion de listes.

### **Avantages d'un objet de liste**

Il existe de nombreux avantages lorsque vous convertissez une liste de données en un objet de liste réel

- Les nouvelles lignes et colonnes sont automatiquement incluses.
- Une ligne de total au bas de votre liste peut être facilement ajoutée pour afficher SUM, AVERAGE, COUNT, etc.
- Les colonnes ajoutées à droite sont automatiquement incorporées dans l'objet Liste.
- Les graphiques basés sur des lignes et des colonnes seront développés automatiquement.
- Les plages nommées attribuées aux lignes et aux colonnes seront développées automatiquement.
- La liste est protégée contre la suppression accidentelle de lignes et de colonnes.

### **Création d'un objet de liste à l'aide d'Excel Microsoft**

- Sélection de la plage de données pour la création d'un objet List
- Cela affiche la boîte de dialogue Créer une liste.
-  Implémentez l'objet List pour les données et spécifiez la ligne totale (Sélectionnez**Données** , alors**Liste** , suivie par**Ligne totale**).

### **En utilisant Aspose.Cells API**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , qui représente un fichier Excel Microsoft. La[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contient un[**Des feuilles de calcul**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

 Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classer. La[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) La classe fournit un large éventail de propriétés et de méthodes pour gérer une feuille de calcul. Créer un[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) dans une feuille de calcul, utilisez la[**ListeObjets**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects) propriété de collection de la[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classer. Chaque[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) est en fait un objet de la[**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection) classe, qui fournit en outre la[**Ajouter**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index)méthode pour ajouter un objet List et spécifier une plage de cellules pour la liste.

Selon la plage de cellules spécifiée, l'objet List est créé par Aspose.Cells. Utilisez des attributs (par exemple,[**AfficherTotaux**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/showtotals), [**ListeColonnes**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/listcolumns) , etc.) de la[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)classe pour contrôler la liste.

 Dans l'exemple ci-dessous, nous avons créé le même[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)en utilisant Aspose.Cells API comme nous l'avons créé en utilisant Microsoft Excel dans la section ci-dessus.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-CreatingListObject-1.cs" >}}

## **Formater un tableau**

Pour gérer et analyser un groupe de données liées, il est possible de transformer une plage de cellules en un objet liste (également appelé tableau Excel). Un tableau est une série de lignes et de colonnes qui contiennent des données associées gérées indépendamment des données des autres lignes et colonnes. Par défaut, chaque colonne du tableau a un filtrage activé dans la ligne d'en-tête afin que vous puissiez filtrer ou trier rapidement les données d'objet de votre liste. Vous pouvez ajouter une ligne de total (une ligne spéciale dans une liste qui fournit une sélection de fonctions d'agrégation utiles pour travailler avec des données numériques) à l'objet de liste qui fournit une liste déroulante de fonctions d'agrégation pour chaque cellule de ligne de total. Aspose.Cells fournit des options pour créer et gérer des listes (ou des tables).

### **Formater un objet de liste**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , qui représente un fichier Excel Microsoft. La[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contient un[**Des feuilles de calcul**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

 Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classer. La[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) La classe fournit un large éventail de propriétés et de méthodes pour gérer les feuilles de calcul. Créer un[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) dans une feuille de calcul, utilisez[**ListeObjets**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects) propriété de collection de la[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classer. Chaque[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) est en fait un objet de la[**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection) classe, qui fournit en outre la[**Ajouter**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index) pour ajouter un objet List et spécifier la plage de cellules qu'il doit englober. Selon la plage de cellules spécifiée, un[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)est créé dans la feuille de calcul par Aspose.Cells. Utilisez des attributs (par exemple,[**Type de style de table**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/tablestyletype) ) de la[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)class pour formater la table selon vos besoins.

 L'exemple ci-dessous ajoute des exemples de données à une feuille de calcul, ajoute un[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject) et appliquez-lui les styles par défaut.[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)les styles sont pris en charge par Microsoft Excel 2007/2010.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-FormataListObject-1.cs" >}}

## **Sujets avancés**
- [Convertir le tableau en ODS](/cells/fr/net/convert-table-to-ods/)
- [Rechercher des tables de requête et des objets de liste liés aux connexions de données externes](/cells/fr/net/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [Table de lecture et d'écriture avec source de données de table de requête](/cells/fr/net/read-and-write-table-with-query-table-data-source/)
- [Définir le commentaire de la table ou de l'objet de liste dans la feuille de calcul](/cells/fr/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [Tableaux et plages](/cells/fr/net/tables-and-ranges/)

