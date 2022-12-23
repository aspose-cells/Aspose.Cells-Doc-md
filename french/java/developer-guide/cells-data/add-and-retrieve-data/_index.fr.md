---
title: Ajouter et récupérer des données
type: docs
weight: 20
url: /fr/java/add-and-retrieve-data/
---
{{% alert color="primary" %}} 

 Dans[Accéder au Cells d'une feuille de calcul](/cells/fr/java/accessing-cells-of-a-worksheet/), nous avons discuté des approches de base pour accéder aux cellules d'une feuille de calcul. Cet article utilise l'une de ces approches pour ajouter différents types de données aux cellules.

{{% /alert %}} 
## **Ajout de données au Cells**
 Aspose.Cells fournit une classe,[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), qui représente un fichier Excel Microsoft. Le[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) classe contient un[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) classe. Le[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la classe offre une[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) le recueil. Chaque élément de la[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collection représente un objet de la[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)classe.

 Aspose.Cells permet aux développeurs d'ajouter des données aux cellules des feuilles de calcul en appelant le[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) classe'[setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)la propriété. En utilisant le[setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value), il est possible d'ajouter des valeurs booléennes, chaîne, double, entier ou date/heure, etc. à la cellule.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingDataToCells-AddingDataToCells.java" >}}
### **Améliorer l'efficacité**
{{% alert color="primary" %}} 

 Si vous utilisez le[setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)Pour ajouter une grande quantité de données à une feuille de calcul, vous devez ajouter des valeurs aux cellules, d'abord par lignes, puis par colonnes. Cette approche améliore considérablement l'efficacité de vos applications.

{{% /alert %}} 

Lorsqu'ils travaillent sur des feuilles de calcul, les utilisateurs peuvent ajouter différents types de données dans les cellules. Ces éléments de données peuvent inclure des valeurs booléennes, entières, à virgule flottante, textuelles ou de date/heure. Vous pouvez obtenir les valeurs appropriées des cellules en fonction de leurs types de données à l'aide de Aspose.Cells.
## **Récupération des données du Cells**
 Aspose.Cells fournit une classe,[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) qui représente un fichier Excel.[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) classe contient un[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)classe. Le[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la classe offre une[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) le recueil. Chaque élément de la[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collection représente un objet de la[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)classe.

 Le[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)La classe fournit plusieurs propriétés qui permettent aux développeurs de récupérer les valeurs des cellules en fonction de leurs types de données. Ces propriétés comprennent :

- [Valeur de chaîne](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue), la valeur de chaîne de la cellule.
- [DoubleValeur](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DoubleValue), renvoie la valeur double de la cellule.
- [BoolValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#BoolValue), la valeur booléenne de la cellule.
- [DateHeureValeur](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DateTimeValue), la valeur date/heure de la cellule.
- [Valeurflottante](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FloatValue), la valeur flottante de la cellule.
- [ValeurEntier](https://reference.aspose.com/cells/java/com.aspose.cells/cell#IntValue), la valeur entière de la cellule.

 De plus, le type de données contenues dans une cellule peut également être vérifié à l'aide de la[Taper](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type) propriété de la[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) classe. En fait, le[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) classe'[Taper](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type) la propriété est basée sur[CellValueType](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueType)énumération dont les valeurs prédéfinies sont listées ci-dessous :

|**Cell Types de valeur**|**Description**|
|:- |:- |
|[IS_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_BOOL)|Spécifie que la valeur de la cellule est booléenne.|
|[EST_DATE_TEMPS](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_DATE_TIME)|Spécifie que la valeur de la cellule est date/heure.|
|[IS_ERROR](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_ERROR)|Représente que la cellule contient une valeur d'erreur|
|[IS_NULL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NULL)|Représente une cellule vide.|
|[IS_NUMERIC](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NUMERIC)|Spécifie que la valeur de la cellule est numérique.|
|[IS_STRING](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_STRING)|Spécifie que la valeur de la cellule est une chaîne.|
|[IS_UNKNOWN](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_UNKNOWN)|Spécifie que la valeur de la cellule est inconnue.|
Vous pouvez également utiliser les types de valeur de cellule prédéfinis ci-dessus pour comparer avec le type de données présentes dans chaque cellule.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RetrievingDataFromCells-RetrievingDataFromCells.java" >}}
