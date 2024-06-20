---
title: Créer et formater un tableau
type: docs
weight: 10
url: /fr/cpp/create-and-format-table/
---

## **Créer un tableau**
L'un des avantages des feuilles de calcul est qu'elles vous permettent de créer différents types de listes, par exemple des listes de téléphones, des listes de tâches, des listes de transactions, d'actifs ou de passifs. Plusieurs utilisateurs peuvent travailler ensemble pour utiliser, créer et maintenir des listes variées.

Aspose.Cells prend en charge la création et la gestion de listes.
### **Avantages d'un objet Liste**
Il y a quelques avantages lorsque vous convertissez une liste de données en un véritable objet Liste

- De nouvelles lignes et colonnes sont automatiquement incluses.
- Une ligne de total en bas de votre liste peut être facilement ajoutée pour afficher la SOMME, la MOYENNE, le NOMBRE, etc.
- Les colonnes ajoutées à droite sont automatiquement incorporées dans l'objet Liste.
- Les graphiques basés sur les lignes et colonnes seront automatiquement étendus.
- Les plages nommées affectées aux lignes et colonnes seront automatiquement étendues.
- La liste est protégée contre les suppressions accidentelles de lignes et de colonnes.
### **Création d'un objet Liste à l'aide de Microsoft Excel**

|**Sélection de la plage de données pour créer un objet Liste**|
| :- |
|![todo:image_alt_text](jHcNq4o.png)|
Cela affiche la boîte de dialogue Créer une liste.

|**Boîte de dialogue Créer une Liste**|
| :- |
|![todo:image_alt_text](kJmukRF.png)|
Mise en œuvre de l'objet Liste pour les données et spécification de la ligne totale (Sélectionnez **Données**, puis **Liste**, suivi de **Ligne Totale**).

|**Création d'un objet liste**|
| :- |
|![todo:image_alt_text](ECSGVdR.png)|
### **Utilisation de l'API Aspose.Cells**
Aspose.Cells fournit une classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contient une collection [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) propose une large gamme de méthodes pour gérer une feuille de calcul. Pour créer un [ListObject](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/) dans une feuille de calcul, utilisez la méthode de collection [GetListObjects](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getlistobjects/) de la classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Chaque`[ListObject]` est en fait un objet de la classe [ListObjectCollection](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/), qui fournit également la méthode [Add](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/) pour ajouter un objet `[ListObject]` et spécifier une plage de cellules pour la liste.

Selon la plage de cellules spécifiée, l'objet `[ListObject]` est créé par Aspose.Cells. Utilisez les attributs (par exemple [SetShowTotals](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/setshowtotals/) et [GetListColumns](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/getlistcolumns/)) de la classe `[ListObject]` pour contrôler la liste.

Dans l'exemple ci-dessous, nous avons créé le même `[ListObject]` en utilisant l'API Aspose.Cells que celui que nous avons créé à l'aide de Microsoft Excel dans la section ci-dessus.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-CreatingListObjects-new.cpp" >}}
## **Formater un Tableau**
Pour gérer et analyser un groupe de données connexes, il est possible de convertir une plage de cellules en un objet liste (également appelé tableau Excel). Un tableau est une série de lignes et de colonnes qui contiennent des données connexes gérées indépendamment des données dans les autres lignes et colonnes. Par défaut, chaque colonne du tableau dispose de filtres activés dans la ligne d'en-tête, de sorte que vous puissiez rapidement filtrer ou trier vos données d'objet liste. Vous pouvez ajouter une ligne totale (une ligne spéciale dans une liste qui propose une sélection de fonctions d'agrégat utiles pour travailler avec des données numériques) à l'objet liste qui propose une liste déroulante de fonctions d'agrégat pour chaque cellule de ligne totale. Aspose.Cells propose des options pour créer et gérer des listes (ou tableaux).
### **Formatage d'un Objet Liste**
Aspose.Cells fournit une classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contient une collection [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) propose une large gamme de méthodes pour gérer les feuilles de calcul. Pour créer un *ListObject* dans une feuille de calcul, utilisez la `ListObjectCollection`. Chaque `[ListObject]` est en fait un objet de la classe `ListObjectCollection`, qui fournit également la méthode [Add](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobjectcollection/add/) pour ajouter un `[ListObject]` et spécifier la plage de cellules qu'elle doit englober. Selon la plage de cellules spécifiée, un *ListObject* est créé dans la feuille de calcul par Aspose.Cells. Utilisez les attributs (par exemple, [SetTableStyleType](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/settablestyletype/)) de la classe `[ListObject]` pour formater la table selon vos besoins.

L'exemple ci-dessous ajoute des données d'exemple à une feuille de calcul, ajoute un `[ListObject]` et lui applique des styles par défaut. Les styles de `[ListObject]` sont pris en charge par Microsoft Excel 2007/2010.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-FormatTable-new.cpp" >}}
