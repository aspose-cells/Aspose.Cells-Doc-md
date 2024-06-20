---
title: Ajouter et récupérer des données
type: docs
weight: 20
url: /fr/cpp/add-and-retrieve-data/
---

{{% alert color="primary" %}} 

Dans [Accéder aux cellules d'une feuille de calcul](/cells/fr/cpp/accessing-cells-of-a-worksheet/), nous avons discuté des approches de base pour accéder aux cellules d'une feuille de calcul. Cet article utilise l'une de ces approches pour ajouter différents types de données aux cellules.

{{% /alert %}} 
## **Ajout de données aux cellules**
Aspose.Cells fournit une classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contient une collection [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) permettant d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fournit une collection [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Chaque élément de la collection [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) représente un objet de la classe [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells permet aux développeurs d'ajouter des données aux cellules des feuilles de calcul en appelant la méthode [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) de la classe [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/). Aspose.Cells fournit des versions surchargées de la méthode [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) permettant aux développeurs d'ajouter différents types de données aux cellules. En utilisant ces versions surchargées de la méthode [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/), il est possible d'ajouter des valeurs booléennes, des chaînes, des nombres à virgule flottante, des entiers ou des valeurs de date/heure, etc. à la cellule.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-AddingDataToCells-new.cpp" >}}
### **Améliorer l'efficacité**
Si vous utilisez la méthode [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) pour insérer une grande quantité de données dans une feuille de calcul, vous devriez ajouter des valeurs aux cellules, d'abord par lignes, puis par colonnes. Cette approche améliore considérablement l'efficacité de vos applications.
## **Récupération de données à partir des cellules**
Aspose.Cells fournit une classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contient une collection [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) permettant d'accéder aux feuilles de calcul du fichier. Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fournit une collection [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Chaque élément de la collection [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) représente un objet de la classe [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

La classe [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) fournit plusieurs méthodes permettant aux développeurs de récupérer des valeurs à partir des cellules selon leurs types de données. Ces méthodes comprennent :

- [GetStringValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/), renvoie la valeur de chaîne de la cellule.
- [GetDoubleValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/), renvoie la valeur en virgule flottante de la cellule.
- [GetBoolValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getboolvalue/), renvoie la valeur booléenne de la cellule.
- [GetDateTimeValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdatetimevalue/), renvoie la valeur date/heure de la cellule.
- [GetFloatValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/), renvoie la valeur flottante de la cellule.
- [GetIntValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getintvalue/), renvoie la valeur entière de la cellule.

Lorsqu'un champ n'est pas rempli, les cellules avec [GetDoubleValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/) ou [GetFloatValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/) lèvent une exception.

Le type de données contenu dans une cellule peut également être vérifié en utilisant la méthode [GetType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) de la classe [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/). En fait, la méthode [GetType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) de la classe [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) est basée sur l'énumération [CellValueType](https://reference.aspose.com/cells/cpp/aspose.cells/cellvaluetype/) dont les valeurs prédéfinies sont énumérées ci-dessous :

|**Types de valeur de cellule**|**Description**|
| :- | :- |
|CellValueType_IsBool|Indique que la valeur de la cellule est booléenne.
|CellValueType_IsDateTime|Indique que la valeur de la cellule est date/heure.
|CellValueType_IsNull|Représente une cellule vide.
|CellValueType_IsNumeric|Indique que la valeur de la cellule est numérique.
|CellValueType_IsString|Indique que la valeur de la cellule est une chaîne de caractères.
|CellValueType_IsUnknown|Indique que la valeur de la cellule est inconnue.
Vous pouvez également utiliser les types de valeur de cellule prédéfinis ci-dessus pour comparer avec le type de données présent dans chaque cellule.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-RetrievingDataFromCells-new.cpp" >}}
