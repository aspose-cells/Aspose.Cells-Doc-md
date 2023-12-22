---
title: Ajouter et récupérer des données
type: docs
weight: 20
url: /fr/cpp/add-and-retrieve-data/
---
{{% alert color="primary" %}} 

 Dans[Accéder au Cells d'une feuille de calcul](/cells/fr/cpp/accessing-cells-of-a-worksheet/), nous avons discuté des approches de base pour accéder aux cellules dans une feuille de calcul. Cet article utilise l'une de ces approches pour ajouter différents types de données aux cellules.

{{% /alert %}} 
##  **Ajout de données au Cells**
 Aspose.Cells propose un cours[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Excel Microsoft. Le[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la classe contient un[Des feuilles de calcul](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection qui permet d’accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe. Le[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) la classe fournit un[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection. Chaque élément du[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) la collection représente un objet de la[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)classe.

 Aspose.Cells permet aux développeurs d'ajouter des données aux cellules des feuilles de calcul en appelant le[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) classe[Valeur de put](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) méthode. Aspose.Cells fournit des versions surchargées du[Valeur de put](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) méthode qui permet aux développeurs d’ajouter différents types de données aux cellules. En utilisant ces versions surchargées du[Valeur de put](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)méthode, il est possible d'ajouter une valeur booléenne, chaîne, double, entière ou date/heure, etc. à la cellule.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-AddingDataToCells-new.cpp" >}}
###  **Améliorer l'efficacité**
 Si tu utilises[Valeur de put](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)Pour placer une grande quantité de données dans une feuille de calcul, vous devez ajouter des valeurs aux cellules, d'abord par lignes, puis par colonnes. Cette approche améliore considérablement l’efficacité de vos applications.
##  **Récupération des données du Cells**
 Aspose.Cells propose un cours[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Excel Microsoft. Le[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la classe contient un[Des feuilles de calcul](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection qui permet d’accéder aux feuilles de calcul du fichier. Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe. Le[Feuille de travail](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) la classe fournit un[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection. Chaque élément du[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) la collection représente un objet de la[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)classe.

 Le[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)La classe fournit plusieurs méthodes qui permettent aux développeurs de récupérer les valeurs des cellules en fonction de leurs types de données. Ces méthodes comprennent :

- [ObtenirStringValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/), renvoie la valeur de chaîne de la cellule.
- [ObtenirDoubleValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/), renvoie la valeur double de la cellule.
- [ObtenirBoolValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getboolvalue/), renvoie la valeur booléenne de la cellule.
- [ObtenirDateTimeValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdatetimevalue/), renvoie la valeur date/heure de la cellule.
- [ObtenirFloatValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/), renvoie la valeur flottante de la cellule.
- [ObtenirIntValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getintvalue/)renvoie la valeur entière de la cellule.

 Lorsqu'un champ n'est pas rempli, les cellules avec[ObtenirDoubleValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/) ou[ObtenirFloatValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/)lève une exception.

 Le type de données contenues dans une cellule peut également être vérifié en utilisant le[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) classe[ObtenirType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) méthode. En fait, le[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) classe[ObtenirType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) la méthode est basée sur[CellValueType](https://reference.aspose.com/cells/cpp/aspose.cells/cellvaluetype/)énumération dont les valeurs prédéfinies sont répertoriées ci-dessous :

|**Cell Types de valeur**|**Description**|
| :- | :- |
|CellValueType_IsBool|Spécifie que la valeur de la cellule est booléenne.|
|CellValueType_IsDateTime|Spécifie que la valeur de la cellule est date/heure.|
|CellValueType_IsNull|Représente une cellule vide.|
|CellValueType_IsNumeric|Spécifie que la valeur de la cellule est numérique.|
|CellValueType_IsString|Spécifie que la valeur de la cellule est une chaîne.|
|CellValueType_IsUnknown|Spécifie que la valeur de la cellule est inconnue.|
Vous pouvez également utiliser les types de valeurs de cellule prédéfinis ci-dessus pour comparer avec le type de données présentes dans chaque cellule.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-RetrievingDataFromCells-new.cpp" >}}
