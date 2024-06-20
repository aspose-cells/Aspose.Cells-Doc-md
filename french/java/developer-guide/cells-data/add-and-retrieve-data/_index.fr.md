---
title: Ajouter et récupérer des données
type: docs
weight: 20
url: /fr/java/add-and-retrieve-data/
---

{{% alert color="primary" %}} 

Dans [Accéder aux cellules d'une feuille de calcul](/cells/fr/java/accessing-cells-of-a-worksheet/), nous avons discuté des approches de base pour accéder aux cellules d'une feuille de calcul. Cet article utilise l'une de ces approches pour ajouter différents types de données aux cellules.

{{% /alert %}} 
## **Ajout de données aux cellules**
Aspose.Cells fournit une classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) contient une [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) fournit une collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Chaque élément de la collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) représente un objet de la classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

Aspose.Cells permet aux développeurs d'ajouter des données aux cellules des feuilles de calcul en appelant la propriété [setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) de la classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell). En utilisant la propriété [setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value), il est possible d'ajouter des valeurs booléennes, des chaînes, des doubles, des entiers ou des valeurs date/heure, etc. à la cellule.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingDataToCells-AddingDataToCells.java" >}}
### **Améliorer l'efficacité**
{{% alert color="primary" %}} 

Si vous utilisez la propriété [setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) pour ajouter une grande quantité de données à une feuille de calcul, vous devez d'abord ajouter des valeurs aux cellules par lignes, puis par colonnes. Cette approche améliore considérablement l'efficacité de vos applications.

{{% /alert %}} 

Lors de travailler sur des feuilles de calcul, les utilisateurs peuvent ajouter différents types de données dans les cellules. Ces éléments de données peuvent inclure des valeurs booléennes, des entiers, des nombres à virgule flottante, du texte ou des valeurs date/heure. Vous pouvez obtenir les valeurs appropriées des cellules selon leurs types de données en utilisant Aspose.Cells.
## **Récupération de données à partir des cellules**
Aspose.Cells fournit une classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) qui représente un fichier Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) contient une [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) fournit une collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Chaque élément de la collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) représente un objet de la classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

La classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) fournit plusieurs propriétés qui permettent aux développeurs de récupérer les valeurs des cellules selon leurs types de données. Ces propriétés comprennent :

- [StringValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue), la valeur de chaîne de la cellule.
- [DoubleValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DoubleValue), renvoie la valeur double de la cellule.
- [BoolValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#BoolValue), la valeur booléenne de la cellule.
- [DateTimeValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DateTimeValue), la valeur date/heure de la cellule.
- [FloatValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FloatValue), la valeur flottante de la cellule.
- [IntValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#IntValue), la valeur entière de la cellule.

De plus, le type de données contenu dans une cellule peut également être vérifié en utilisant la propriété [Type](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type) de la classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell). En fait, la propriété [Type](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type) de la classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) est basée sur l'énumération [CellValueType](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueType) dont les valeurs prédéfinies sont répertoriées ci-dessous :

|**Types de valeur de cellule**|**Description**|
| :- | :- |
|[IS_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_BOOL)| Indique que la valeur de la cellule est booléenne.
|[IS_DATE_TIME](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_DATE_TIME)| Indique que la valeur de la cellule est une date/heure.
|[IS_ERROR](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_ERROR)| Représente que la cellule contient une valeur d'erreur.
|[IS_NULL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NULL)| Représente une cellule vide.
|[IS_NUMERIC](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NUMERIC)| Indique que la valeur de la cellule est numérique.
|[IS_STRING](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_STRING)| Indique que la valeur de la cellule est une chaîne de caractères.
|[IS_UNKNOWN](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_UNKNOWN)| Indique que la valeur de la cellule est inconnue.
Vous pouvez également utiliser les types de valeur de cellule prédéfinis ci-dessus pour comparer avec le type de données présent dans chaque cellule.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RetrievingDataFromCells-RetrievingDataFromCells.java" >}}
