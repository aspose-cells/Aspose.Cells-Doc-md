---
title: Importer et exporter des données
type: docs
weight: 130
url: /fr/java/import-and-export-data/
---

{{% alert color="primary" %}}

Cet article discute de certaines techniques d'importation et d'exportation de données auxquelles les développeurs ont accès via Aspose.Cells.

{{% /alert %}}

## Importer des données dans la feuille de calcul

Les données représentent le monde tel qu'il est. Pour donner du sens aux données, nous les analysons et comprenons le monde. Les données se transforment en informations.

Il existe de nombreuses façons de réaliser une analyse: mettre des données dans des feuilles de calcul et les manipuler de différentes manières est une méthode courante. Avec Aspose.Cells, il est facile de créer des feuilles de calcul qui récupèrent des données à partir d'une gamme de sources externes et les préparent pour l'analyse.

Cet article traite de certaines techniques d'importation de données auxquelles les développeurs ont accès grâce à Aspose.Cells.

### Importation de données avec Aspose.Cells

Lorsque vous ouvrez un fichier Excel avec Aspose.Cells, toutes les données du fichier sont automatiquement importées. Aspose.Cells peut également importer des données à partir d'autres sources de données:

- [Tableau](/cells/fr/java/import-and-export-data/).
- [Liste de tableaux](/cells/fr/java/import-and-export-data/).
- [Ensemble de résultats](/cells/fr/java/import-and-export-data/).
- [JSON](/cells/fr/java/import-and-export-data/)

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contient la collection [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) fournit une collection [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells). La collection [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) fournit des méthodes très utiles pour importer des données à partir d'autres sources de données. Cet article explique comment ces méthodes peuvent être utilisées.

#### Importation à partir d'un tableau

Pour importer des données vers une feuille de calcul à partir d'un tableau, appelez la méthode importArray de la collection [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells). Il existe de nombreuses versions surchargées de la méthode importArray mais une surcharge typique prend les paramètres suivants:

- **Tableau**, l'objet tableau à partir duquel vous importez le contenu.
- **Numéro de ligne**, le numéro de ligne de la première cellule dans laquelle les données seront importées.
- **Numéro de colonne**, le numéro de colonne de la première cellule dans laquelle les données seront importées.
- **Est vertical**, une valeur booléenne qui spécifie si les données doivent être importées verticalement ou horizontalement.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArray-ImportingFromArray.java" >}}

#### Importation à partir de tableaux multidimensionnels

Pour importer des données vers une feuille de calcul à partir de tableaux multidimensionnels, appelez la surcharge correspondante de la méthode importArray de la collection [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells):

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromMultiDimensionalArray-ImportingFromMultiDimensionalArray.java" >}}

#### Importation à partir d'une liste de tableaux

Pour importer des données à partir d'un *ArrayList* dans des feuilles de calcul, appelez la méthode [**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList(java.util.ArrayList,%20int,%20int,%20boolean)) de la collection [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells). La méthode [**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList(java.util.ArrayList,%20int,%20int,%20boolean)) prend les paramètres suivants:

- **ArrayList**, l'objet *ArrayList* dont le contenu sera importé.
- **Numéro de ligne**, le numéro de ligne de la première cellule de la plage de cellules à partir de laquelle les contenus seront importés.
- **Numéro de colonne**, le numéro de colonne de la première cellule à partir de laquelle les données seront importées.
- **Est vertical**, est une valeur booléenne qui spécifie si les données doivent être importées verticalement ou horizontalement.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### Importation à partir d'objets personnalisés vers une zone fusionnée

Pour importer des données à partir d'une collection d'objets vers une feuille de calcul contenant des cellules fusionnées, utilisez la propriété [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells). Si le modèle Excel contient des cellules fusionnées, définissez la valeur de la propriété [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells) sur true. Passez l'objet [**ImportTableOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImportTableOptions) avec la liste de colonnes/propriétés à la méthode pour afficher votre liste désirée d'objets. L'exemple de code suivant démontre l'utilisation de la propriété [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells) pour importer des données à partir d'objets personnalisés vers des cellules fusionnées. Consultez le fichier Excel source joint (90112035.xlsx) et le fichier Excel de sortie joint (90112036.xlsx) pour référence.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### Importation de données à partir de JSON

Aspose.Cells fournit une classe [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) pour le traitement du JSON. La classe [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) a une méthode [**ImportData**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData(java.lang.String,%20com.aspose.cells.Cells,%20int,%20int,%20com.aspose.cells.JsonLayoutOptions)) pour l'importation de données JSON. Aspose.Cells fournit également une classe [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) qui représente les options de disposition JSON. La méthode [**ImportData**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData(java.lang.String,%20com.aspose.cells.Cells,%20int,%20int,%20com.aspose.cells.JsonLayoutOptions)) accepte [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) en tant que paramètre. La classe [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) fournit les propriétés suivantes.

- [**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable) : Indique si le tableau doit être traité comme un tableau ou non.
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ConvertNumericOrDate) : Obtient ou définit une valeur indiquant si la chaîne de JSON doit être convertie en numérique ou en date.
- [**DateFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#DateFormat) : Obtient et définit le format de la valeur de date.
- [**IgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle) : Indique s'il faut ignorer le titre si la propriété de l'objet est un tableau.
- [**IgnoreNull**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreNull) : Indique si la valeur nulle doit être ignorée ou non.
- [**IgnoreObjectTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreObjectTitle) : Indique s'il faut ignorer le titre si la propriété de l'objet est un objet.
- [**NumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#NumberFormat): Obtient et définit le format de la valeur numérique.
- [**TitleStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#TitleStyle): Obtient et définit le style du titre.

Le code d'exemple ci-dessous démontre l'utilisation des classes [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) et [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) pour importer des données JSON.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportingFromJson-1.java" >}}

## Exportation de données à partir de feuille de calcul

Aspose.Cells permet non seulement à ses utilisateurs d'importer des données dans des feuilles de calcul à partir de sources de données externes, mais leur permet également d'exporter des données de feuille de calcul vers un tableau.

### Exportation de données en utilisant Aspose.Cells - Exportation de données vers un tableau

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contient une [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) qui permet l'accès à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) fournit une collection [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells).

Les données peuvent facilement être exportées vers un objet tableau en utilisant la méthode [**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int)) de la classe [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells).

#### Colonnes contenant des données fortement typées

Les feuilles de calcul stockent les données sous forme de séquence de lignes et de colonnes. Utilisez la méthode [**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int)) pour exporter les données d'une feuille de calcul vers un tableau. [**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int)) prend les paramètres suivants pour exporter les données de la feuille de calcul en tant qu'objet *Array*:

- Numéro de ligne, le numéro de la première cellule à partir de laquelle les données seront exportées.
- Numéro de colonne, le numéro de colonne de la première cellule à partir de laquelle les données seront exportées.
- Nombre de lignes, le nombre de lignes à exporter.
- Nombre de colonnes, le nombre de colonnes à exporter.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ExportingDataFromWorksheets-1.java" >}}

## **Sujets avancés**
- [Importer des données à partir de l'objet de jeu de résultats de base de données Microsoft Access dans la feuille de calcul](/cells/fr/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/)
- [Spécifier les champs de formule lors de l'importation de données dans la feuille de calcul](/cells/fr/java/specify-formula-fields-while-importing-data-to-worksheet/)
