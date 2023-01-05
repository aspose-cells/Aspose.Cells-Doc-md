---
title: Importer et exporter des données
type: docs
weight: 130
url: /fr/java/import-and-export-data/
---
{{% alert color="primary" %}}

Cet article traite de certaines techniques d'importation et d'exportation de données auxquelles les développeurs ont accès via Aspose.Cells.

{{% /alert %}}

## Importer des données dans la feuille de calcul

Les données représentent le monde tel qu'il est. Pour donner un sens aux données, nous les analysons et acquérons une compréhension du monde. Les données se transforment en informations.

Il existe de nombreuses façons d'effectuer une analyse : mettre des données dans des feuilles de calcul et les manipuler de différentes manières est une méthode courante. Avec Aspose.Cells, il est facile de créer des feuilles de calcul qui prennent des données à partir d'une gamme de sources externes et de les préparer pour l'analyse.

Cet article traite de certaines techniques d'importation de données auxquelles les développeurs ont accès via Aspose.Cells.

### Importation de données à l'aide de Aspose.Cells

Lorsque vous ouvrez un fichier Excel avec Aspose.Cells, toutes les données du fichier sont automatiquement importées. Aspose.Cells peut également importer des données à partir d'autres sources de données :

- [Déployer](/cells/fr/java/import-and-export-data/).
- [Liste des tableaux](/cells/fr/java/import-and-export-data/).
- [Ensemble de résultats](/cells/fr/java/import-and-export-data/).
- [JSON](/cells/fr/java/import-and-export-data/)

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , qui représente un fichier Excel Microsoft. Le[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la classe contient la collection[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) classe. Le[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la classe offre une[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) le recueil.[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)fournit des méthodes très utiles pour importer des données à partir d'autres sources de données. Cet article explique comment ces méthodes peuvent être utilisées.

#### Importation à partir d'un tableau

 Pour importer des données dans une feuille de calcul à partir d'un tableau, appelez la méthode importArray de la[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)le recueil. Il existe de nombreuses versions surchargées de la méthode importArray, mais une surcharge typique prend les paramètres suivants :

- **Déployer**, l'objet tableau à partir duquel vous importez le contenu.
- **Numéro de ligne**le numéro de ligne de la première cellule dans laquelle les données seront importées.
- **Numéro de colonne**, le numéro de colonne de la première cellule dans laquelle les données seront importées.
- **Est vertical**, une valeur booléenne qui spécifie s'il faut importer les données verticalement ou horizontalement.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArray-ImportingFromArray.java" >}}

#### Importation à partir de tableaux multidimensionnels

 Pour importer des données dans une feuille de calcul à partir de tableaux multidimensionnels, appelez la surcharge importArray appropriée du[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)le recueil:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromMultiDimensionalArray-ImportingFromMultiDimensionalArray.java" >}}

#### Importer depuis une ArrayList

 Pour importer des données d'un*Liste des tableaux* aux feuilles de travail, appelez le[**ImportArrayListImportArrayListImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList(java.util.ArrayList,%20int,%20int,%20boolean) ) méthode de la[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) le recueil. Le[**ImportArrayListImportArrayListImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList(java.util.ArrayList,%20int,%20int,%20boolean)) prend les paramètres suivants :

- **Liste des tableaux** , le*Liste des tableaux*objet dont le contenu sera importé.
- **Numéro de ligne**, le numéro de ligne de la première cellule de la plage de cellules à partir de laquelle le contenu sera importé.
- **Numéro de colonne**, le numéro de colonne de la première cellule à partir de laquelle les données seront importées.
- **Est vertical**est une valeur booléenne qui spécifie s'il faut importer les données verticalement ou horizontalement.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### Importation d'objets personnalisés vers une zone fusionnée

Pour importer des données d'une collection d'objets vers une feuille de calcul contenant des cellules fusionnées, utilisez[**ImportTableOptions.CheckMergedCellsImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)la propriété. Si le modèle Excel contient des cellules fusionnées, définissez la valeur de[**ImportTableOptions.CheckMergedCellsImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)propriété à vrai. Passe le[**ImportTableOptionsImportTableOptionsImportTableOptionsImportTableOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImportTableOptions)objet avec la liste des colonnes/propriétés de la méthode pour afficher la liste d'objets souhaitée. L'exemple de code suivant illustre l'utilisation de[**ImportTableOptions.CheckMergedCellsImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)propriété pour importer des données d'objets personnalisés vers des cellules fusionnées. Veuillez regarder la pièce jointe[source Excel](90112035.xlsx)dossier et le[sortie Excel](90112036.xlsx)fichier pour référence.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### Importation de données depuis JSON

 Aspose.Cells fournit un[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) classe de traitement JSON.[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) la classe a un[**Importer des données**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData(java.lang.String,%20com.aspose.cells.Cells,%20int,%20int,%20com.aspose.cells.JsonLayoutOptions) ) méthode d'importation des données JSON. Aspose.Cells fournit également un[**JsonLayoutOptionsJsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)classe qui représente les options de mise en page JSON. Le[**Importer des données**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData(java.lang.String,%20com.aspose.cells.Cells,%20int,%20int,%20com.aspose.cells.JsonLayoutOptions) ) méthode accepte[**JsonLayoutOptionsJsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) comme paramètre. Le[**JsonLayoutOptionsJsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) classe fournit les propriétés suivantes.

- [**TableauCommeTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable): Indique dans le tableau qu'il doit être traité ou non comme une table.
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ConvertNumericOrDate): Obtient ou définit une valeur qui indique si la chaîne dans JSON doit être convertie en numérique ou en date.
- [**Format de date**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#DateFormat): Obtient et définit le format de la valeur de date.
- [**IgnoreArrayTitleIgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle): Indique s'il faut ignorer le titre si la propriété de l'objet est un tableau
- [**IgnorerNull**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreNull): Indique si la valeur nulle doit être ignorée ou non.
- [**IgnoreObjectTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreObjectTitle): Indique s'il faut ignorer le titre si la propriété de l'objet est un objet.
- [**Format de nombre**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#NumberFormat): Obtient et définit le format de la valeur numérique.
- [**Style de titre**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#TitleStyle): Obtient et définit le style du titre.

 L'exemple de code ci-dessous illustre l'utilisation du[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) et[**JsonLayoutOptionsJsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) classes pour importer les données JSON.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportingFromJson-1.java" >}}

## Exporter les données de la feuille de calcul

Aspose.Cells permet non seulement à ses utilisateurs d'importer des données dans des feuilles de calcul à partir de sources de données externes, mais leur permet également d'exporter des données de feuille de calcul vers un tableau.

### Exportation de données à l'aide de Aspose.Cells - Exportation de données vers un tableau

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , qui représente un fichier Excel Microsoft. Le[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe contient un[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) classe. Le[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la classe offre une[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) le recueil.

 Les données peuvent facilement être exportées vers un objet Array à l'aide de la[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) classe'[**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int)) méthode.

#### Colonnes contenant des données fortement typées

 Les feuilles de calcul stockent les données sous la forme d'une séquence de lignes et de colonnes. Utilisez le[**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int) ) pour exporter les données d'une feuille de calcul vers un tableau.[**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int) ) prend les paramètres suivants pour exporter les données de la feuille de calcul en tant que*Déployer* objet:

- Numéro de ligne, le numéro de ligne de la première cellule à partir de laquelle les données seront exportées.
- Numéro de colonne, le numéro de colonne de la première cellule à partir de laquelle les données seront exportées
- Nombre de lignes, le nombre de lignes à exporter.
- Nombre de colonnes, le nombre de colonnes à exporter.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ExportingDataFromWorksheets-1.java" >}}

## **Sujets avancés**
- [Importer des données de l'objet ResultSet de la base de données Access Microsoft dans la feuille de calcul](/cells/fr/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/)
- [Spécifier les champs de formule lors de l'importation de données dans la feuille de calcul](/cells/fr/java/specify-formula-fields-while-importing-data-to-worksheet/)
