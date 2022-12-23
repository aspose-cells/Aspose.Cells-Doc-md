---
title: Créer et formater un tableau
type: docs
weight: 10
url: /fr/cpp/create-and-format-table/
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

|**Sélection de la plage de données pour la création d'un objet Liste**|
|:- |
|![tâche : image_autre_texte](jHcNq4o.png)|
Cela affiche la boîte de dialogue Créer une liste.

|**Boîte de dialogue Créer une liste**|
|:- |
|![tâche : image_autre_texte](kJmukRF.png)|
 Implémentation de l'objet List pour les données et spécification de la ligne totale (Select**Données** , ensuite**Lister** , suivie par**Ligne totale**).

|**Création d'un objet liste**|
|:- |
|![tâche : image_autre_texte](ECSGVdR.png)|
### **En utilisant Aspose.Cells API**
 Aspose.Cells fournit une classe[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) qui représente un fichier Excel Microsoft. Le[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) classe contient un[Feuilles de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

 Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe. Le[Feuille de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) fournit un large éventail de méthodes pour gérer une feuille de calcul. Pour créer un[IListObject](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object) dans une feuille de calcul, utilisez la[GetIListObjects](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a4356bc4b8cffee624891f10ea49a4705) mode de collecte de la[Feuille de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe. Chaque `[IListObject]` est en fait, un objet de la[IListObjectCollectionIListObjectCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object_collection) classe, qui fournit en outre la[Ajouter](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object_collection#ae4afda31b69b75a78558a65bef65ee42)méthode pour ajouter un objet `[IListObject]` et spécifier une plage de cellules pour la liste.

 Selon la plage de cellules spécifiée, l'objet `[IListObject]` est créé par Aspose.Cells. Utilisez des attributs (par exemple[AfficherTotaux](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object#a9026460927f035f374f5e1ea74e639f2) et[ListeColonnes](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object#afeeb7bfabd0971e9fe34a09f0b83ae73)etc.) de la classe `[IListObject]` pour contrôler la liste.

Dans l'exemple ci-dessous, nous avons créé le même `[IListObject]` en utilisant Aspose.Cells API que nous avons créé en utilisant Microsoft Excel dans la section ci-dessus.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-CreatingListObjects.cpp" >}}
## **Formater un tableau**
Pour gérer et analyser un groupe de données liées, il est possible de transformer une plage de cellules en un objet liste (également appelé tableau Excel). Un tableau est une série de lignes et de colonnes qui contiennent des données associées gérées indépendamment des données des autres lignes et colonnes. Par défaut, chaque colonne du tableau a un filtrage activé dans la ligne d'en-tête afin que vous puissiez filtrer ou trier rapidement les données d'objet de votre liste. Vous pouvez ajouter une ligne de total (une ligne spéciale dans une liste qui fournit une sélection de fonctions d'agrégation utiles pour travailler avec des données numériques) à l'objet de liste qui fournit une liste déroulante de fonctions d'agrégation pour chaque cellule de ligne de totaux. Aspose.Cells fournit des options pour créer et gérer des listes (ou des tables).
### **Formater un objet de liste**
 Aspose.Cells fournit une classe[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) qui représente un fichier Excel Microsoft. Le[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) classe contient un[Feuilles de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

 Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe. Le[Feuille de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) La classe fournit un large éventail de méthodes de gestion des feuilles de calcul. Créer un*ListObject*dans une feuille de calcul, utilisez `IListObjectCollection`. Chaque `[IListObject]` est en fait un objet de la classe `IListObjectCollection`, qui fournit en outre le[Ajouter](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object_collection#ae4afda31b69b75a78558a65bef65ee42)méthode pour ajouter un objet `[IListObject]` et spécifier la plage de cellules qu'il doit englober. Selon la plage de cellules spécifiée, un*ListObject* est créé dans la feuille de calcul par Aspose.Cells. Utilisez des attributs (par exemple,[Type de style de table](https://reference.aspose.com/cells/cpp/class/aspose.cells.tables.i_list_object#a5de8b5321b0ccb30dfb09cefe6536462)) de la classe `[IListObject]` pour formater la table selon vos besoins.

L'exemple ci-dessous ajoute des exemples de données à une feuille de calcul, ajoute un `[IListObject]` et lui applique des styles par défaut. Les styles `[IListObject]` sont pris en charge par Microsoft Excel 2007/2010.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-FormatTable.cpp" >}}
