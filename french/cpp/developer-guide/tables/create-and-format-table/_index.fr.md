---
title: Créer et formater un tableau
type: docs
weight: 10
url: /fr/cpp/create-and-format-table/
---
##  **Créer un tableau**
L'un des avantages des feuilles de calcul est qu'elles permettent de créer différents types de listes, par exemple des listes téléphoniques, des listes de tâches, des listes de transactions, d'actifs ou de passifs. Plusieurs utilisateurs peuvent travailler ensemble pour utiliser, créer et maintenir diverses listes.

Aspose.Cells prend en charge la création et la gestion de listes.
###  **Avantages d'un objet liste**
Il existe de nombreux avantages lorsque vous convertissez une liste de données en un véritable objet de liste.

- Les nouvelles lignes et colonnes sont automatiquement incluses.
- Une ligne totale au bas de votre liste peut être facilement ajoutée pour afficher la SOMME, la MOYENNE, le COMPTE, etc.
- Les colonnes ajoutées à droite sont automatiquement incorporées à l'objet List.
- Les graphiques basés sur des lignes et des colonnes seront automatiquement développés.
- Les plages nommées attribuées aux lignes et aux colonnes seront automatiquement développées.
- La liste est protégée contre la suppression accidentelle de lignes et de colonnes.
###  **Création d'un objet de liste à l'aide d'Excel Microsoft**

|**Sélection d'une plage de données pour créer un objet Liste**|
| :- |
|![tâche : image_alt_text](jHcNq4o.png)|
Cela affiche la boîte de dialogue Créer une liste.

|**Boîte de dialogue Créer une liste**|
| :- |
|![tâche : image_alt_text](kJmukRF.png)|
Implémentation de l'objet List pour les données et spécification de la ligne totale (sélectionnez *Data**, puis *List**, suivi de *Total Row**).

|**Création d'un objet liste**|
| :- |
|![tâche : image_alt_text](ECSGVdR.png)|
###  **En utilisant le Aspose.Cells API**
 Aspose.Cells propose un cours[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Excel Microsoft. Le[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la classe contient un[Des feuilles de calcul](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe. Le[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) La classe fournit un large éventail de méthodes pour gérer une feuille de calcul. Pour créer un[ObjetListe](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/) dans une feuille de calcul, utilisez le[ObtenirListeObjects](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getlistobjects/) méthode de collecte des[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe. Chaque `[ListObject]` est en fait un objet du[ListeObjetCollection](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/) classe, qui fournit en outre la[Ajouter](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/)méthode pour ajouter un objet `[ListObject]` et spécifier une plage de cellules pour la liste.

 Selon la plage de cellules spécifiée, l'objet `[ListObject]` est créé par Aspose.Cells. Utilisez des attributs (par exemple[DéfinirAfficherTotaux](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/setshowtotals/) et[ObtenirListeColonnes](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/getlistcolumns/)etc.) de la classe `[ListObject]` pour contrôler la liste.

Dans l'exemple donné ci-dessous, nous avons créé le même `[ListObject]` en utilisant Aspose.Cells API que celui que nous avons créé en utilisant Microsoft Excel dans la section ci-dessus.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-CreatingListObjects-new.cpp" >}}
##  **Formater un tableau**
Pour gérer et analyser un groupe de données associées, il est possible de transformer une plage de cellules en un objet liste (également appelé tableau Excel). Un tableau est une série de lignes et de colonnes contenant des données associées, gérées indépendamment des données des autres lignes et colonnes. Par défaut, le filtrage est activé dans la ligne d'en-tête de chaque colonne du tableau afin que vous puissiez filtrer ou trier rapidement les données de vos objets de liste. Vous pouvez ajouter une ligne de total (une ligne spéciale dans une liste qui fournit une sélection de fonctions d'agrégation utiles pour travailler avec des données numériques) à l'objet de liste qui fournit une liste déroulante de fonctions d'agrégation pour chaque cellule de ligne de totaux. Aspose.Cells fournit des options pour créer et gérer des listes (ou des tableaux).
###  **Formatage d'un objet de liste**
 Aspose.Cells propose un cours[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Excel Microsoft. Le[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la classe contient un[Des feuilles de calcul](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe. Le[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) La classe fournit un large éventail de méthodes pour gérer les feuilles de calcul. Créer un*ObjetListe*dans une feuille de calcul, utilisez `ListObjectCollection`. Chaque `[ListObject]` est en fait un objet de la classe `ListObjectCollection`, qui fournit en outre le[Ajouter](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/)méthode pour ajouter un objet `[ListObject]` et spécifier la plage de cellules qu'il doit englober. Selon la plage de cellules spécifiée, un*ObjetListe* est créé dans la feuille de calcul par Aspose.Cells. Utilisez des attributs (par exemple,[DéfinirTypeStyleTable](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/settablestyletype/)) de la classe `[ListObject]` pour formater le tableau selon vos besoins.

L'exemple ci-dessous ajoute des exemples de données à une feuille de calcul, ajoute un `[ListObject]` et lui applique des styles par défaut. Les styles `[ListObject]` sont pris en charge par Microsoft Excel 2007/2010.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-FormatTable-new.cpp" >}}
