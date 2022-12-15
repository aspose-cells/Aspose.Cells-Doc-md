---
title: Ajouter et récupérer des données
type: docs
weight: 20
url: /fr/cpp/add-and-retrieve-data/
---
{{% alert color="primary" %}} 

 Dans[Accéder au Cells d'une feuille de calcul](/cells/fr/cpp/accessing-cells-of-a-worksheet/), nous avons discuté des approches de base pour accéder aux cellules d'une feuille de calcul. Cet article utilise l'une de ces approches pour ajouter différents types de données aux cellules.

{{% /alert %}} 
## **Ajout de données au Cells**
 Aspose.Cells fournit une classe[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) qui représente un fichier Excel Microsoft. La[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) classe contient un[Feuilles de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) collection qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[Feuille de calcul](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classer. La[Feuille de calcul](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe offre une[ICellules](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) le recueil. Chaque élément de la[ICellules](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) collection représente un objet de la[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)classer.

Aspose.Cells permet aux développeurs d'ajouter des données aux cellules des feuilles de calcul en appelant le[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) classer[PutValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9) méthode. Aspose.Cells fournit des versions surchargées du[PutValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9) méthode qui permet aux développeurs d'ajouter différents types de données aux cellules. L'utilisation de ces versions surchargées du[PutValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9), il est possible d'ajouter une valeur booléenne, chaîne, double, entier ou date/heure, etc. à la cellule.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-AddingDataToCells.cpp" >}}
### **Améliorer l'efficacité**
 Si tu utilises[PutValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9)Pour placer une grande quantité de données dans une feuille de calcul, vous devez ajouter des valeurs aux cellules, d'abord par lignes, puis par colonnes. Cette approche améliore considérablement l'efficacité de vos applications.
## **Récupération des données du Cells**
 Aspose.Cells fournit une classe[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) qui représente un fichier Excel Microsoft. La[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) classe contient un[Feuilles de travail](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) collection qui permet d'accéder aux feuilles de calcul du fichier. Une feuille de calcul est représentée par le[Feuille de calcul](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classer. La[Feuille de calcul](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) la classe offre une[ICellules](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) le recueil. Chaque élément de la[ICellules](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) collection représente un objet de la[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)classer.

 La[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)La classe fournit plusieurs méthodes qui permettent aux développeurs de récupérer les valeurs des cellules en fonction de leurs types de données. Ces méthodes comprennent :

- [GetStringValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ac048c664985e2cadc2404840599d7ac3), renvoie la valeur de chaîne de la cellule.
- [ObtenirValeurDouble](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a5f21cd4c755da84135176c74425f230a), renvoie la valeur double de la cellule.
- [GetBoolValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ac61870c4b1d6a68077092fb043bf8741), renvoie la valeur booléenne de la cellule.
- [GetDateTimeValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7932b40c41141f716b096cc521113a61), renvoie la valeur date/heure de la cellule.
- [GetFloatValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4e36c4be4c76447f54f8032b17cecf44), renvoie la valeur flottante de la cellule.
- [GetIntValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7acc93c97c062cbd60a7f1ab00a022d8), renvoie la valeur entière de la cellule.

 Lorsqu'un champ n'est pas rempli, les cellules avec[ObtenirValeurDouble](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a5f21cd4c755da84135176c74425f230a) ou[GetFloatValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4e36c4be4c76447f54f8032b17cecf44)lève une exception.

 Le type de données contenues dans une cellule peut également être vérifié à l'aide de la[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) classer[ObtenirType](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a36708b1bad0bbf45cbf9577ccab101ba) méthode. En fait, le[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) classer[ObtenirType](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a36708b1bad0bbf45cbf9577ccab101ba) méthode est basée sur la[CellValueType](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a745bf00b4815ec8dcf1bd11922fa4b62)énumération dont les valeurs prédéfinies sont listées ci-dessous :

|**Cell Types de valeur**|**La description**|
|:- |:- |
|CellValueType_IsBool|Spécifie que la valeur de la cellule est booléenne.|
|CellValueType_IsDateTime|Spécifie que la valeur de la cellule est date/heure.|
|CellValueType_IsNull|Représente une cellule vide.|
|CellValueType_IsNumeric|Spécifie que la valeur de la cellule est numérique.|
|CellValueType_IsString|Spécifie que la valeur de la cellule est une chaîne.|
|CellValueType_IsUnknown|Spécifie que la valeur de la cellule est inconnue.|
Vous pouvez également utiliser les types de valeur de cellule prédéfinis ci-dessus pour comparer avec le type des données présentes dans chaque cellule.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-RetrievingDataFromCells.cpp" >}}
