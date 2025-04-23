---
title: Importer des données dans la feuille de calcul
type: docs
weight: 170
url: /fr/net/import-data-into-worksheet/
description: Apprenez à importer des données dans une feuille de calcul via l API Aspose.Cells for .NET.
keywords: C# Importer des données dans la feuille de calcul, Importer des données dans Excel avec l interface ICellsDataTable, Importer des données d un tableau, Importer des données d une liste, Importer des données d objets personnalisés, Importer des données d objets personnalisés dans une zone fusionnée, Importer des données d un DataTable, Importer des données d un objet dynamique en tant que source de données, Importer des données d une colonne DataColumn, Importer des données d une DataView, Importer des données d un DataGrid, Importer des données d un GridView, Importer des données formatées en HTML, Importer des données à partir de JSON
---

{{% alert color="primary" %}}

Cet article traite de certaines techniques d'importation de données auxquelles les développeurs ont accès grâce à Aspose.Cells.

{{% /alert %}}

## **Comment importer des données dans une feuille de calcul**

Lorsque vous ouvrez un fichier Excel avec Aspose.Cells, toutes les données du fichier sont automatiquement importées. Aspose.Cells peut également importer des données à partir d'autres sources de données.

Aspose.Cells fournit une classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fournit une collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). La collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) fournit des méthodes utiles pour importer des données à partir de différentes sources de données. Cet article explique comment ces méthodes peuvent être utilisées.

## **Comment importer des données dans Excel avec l'interface ICellsDataTable**
Implémentez [ICellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable) pour encapsuler vos diverses sources de données, puis utilisez [Cells.ImportData()](https://reference.aspose.com/cells/net/aspose.cells/cells/importdata/#importdata) pour importer des données dans une feuille de calcul Excel.
### **Code d'exemple**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "ImportICellsDataTableIntoWorksheet.cs" >}}

L'implémentation des classes *CustomerDataSource*, *Customer* et *CustomerList* est donnée ci-dessous

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}


## **Comment importer des données dans Excel à partir d'un tableau**

Pour importer des données dans une feuille de calcul à partir d'un tableau, appelez la méthode [**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index) de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Il existe de nombreuses versions surchargées de la méthode [**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index) mais une surcharge typique prend les paramètres suivants:

- **Tableau**, l'objet tableau à partir duquel vous importez le contenu.
- **Numéro de ligne**, le numéro de ligne de la première cellule dans laquelle les données seront importées.
- **Numéro de colonne**, le numéro de colonne de la première cellule dans laquelle les données seront importées.
- **Est vertical**, une valeur booléenne qui spécifie si les données doivent être importées verticalement ou horizontalement.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArray-1.cs" >}}

## **Comment importer des données dans Excel à partir d'un ArrayList**

Pour importer des données d'un *ArrayList* dans des feuilles de calcul, appelez la méthode [**ImportArrayList**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarraylist) de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). La méthode ImportArray prend les paramètres suivants:

- **Liste de tableaux**, représente l'objet *ArrayList* que vous importez.
- **Numéro de ligne**, représente le numéro de ligne de la première cellule dans laquelle les données seront importées.
- **Numéro de colonne**, représente le numéro de colonne de la première cellule dans laquelle les données seront importées.
- **Est vertical**, une valeur booléenne qui spécifie si les données doivent être importées verticalement ou horizontalement.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArrayList-1.cs" >}}

## **Comment importer des données dans Excel à partir d'objets personnalisés**

Pour importer des données à partir d'une collection d'objets dans une feuille de calcul, utilisez [**ImportCustomObjects**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importcustomobjects/index). Fournissez une liste de colonnes/propriétés à la méthode pour afficher la liste d'objets souhaitée.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromCustomObject-1.cs" >}}

## **Comment importer des données dans Excel à partir d'objets personnalisés et vérifier la zone fusionnée**

Pour importer des données à partir d'une collection d'objets dans une feuille de calcul contenant des cellules fusionnées, utilisez la propriété [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells). Si le modèle Excel comporte des cellules fusionnées, définissez la valeur de la propriété [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) sur vrai. Transmettez l'objet [**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) avec la liste de colonnes/propriétés à la méthode pour afficher la liste d'objets souhaitée. L'exemple de code suivant montre l'utilisation de la propriété [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) pour importer des données à partir d'objets personnalisés dans des cellules fusionnées. Veuillez consulter le fichier Excel source (90112033.xlsx) et le fichier Excel de sortie (90112034.xlsx) pour référence.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportCustomObjectsToMergedArea-1.cs" >}}

## **Comment importer des données dans Excel à partir d'un DataTable**

Pour importer des données à partir d'un *DataTable*, appelez la méthode [**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index) de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Il existe de nombreuses versions surchargées de la méthode [**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index), mais une surcharge typique prend les paramètres suivants :

- **Data table**, l'objet *DataTable* à partir duquel vous importez le contenu.
- **Is field name shown**, spécifie si les noms des colonnes du *DataTable* doivent être importés dans la feuille de calcul en tant que première ligne ou non.
- **Start cell**, représente le nom de la cellule de départ (par exemple "A1") à partir de laquelle importer le contenu du *DataTable*.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataTable-1.cs" >}}

## **Comment importer des données dans Excel à partir d'un objet dynamique en tant que source de données**

Aspose.Cells fournit des fonctionnalités pour travailler avec des objets dynamiques en tant que source de données. Cela aide à utiliser une source de données où les propriétés sont ajoutées dynamiquement aux objets. Une fois que les propriétés sont ajoutées à l'objet, Aspose.Cells considère la première entrée comme le modèle et gère le reste en conséquence. Cela signifie que si une propriété dynamique est ajoutée à un seul élément et pas aux autres objets, Aspose.Cells considère que tous les éléments de la collection doivent être identiques.

Dans cet exemple, un modèle de formulaire est utilisé qui contient initialement uniquement deux variables. Cette liste est convertie en liste d'objets dynamiques. Ensuite, un champ supplémentaire y est ajouté et finalement chargé dans le classeur. Le classeur ne prend que les valeurs qui se trouvent dans le fichier XLSX modèle. Ce classeur modèle utilise des marqueurs intelligents qui contiennent également des paramètres. Les paramètres vous permettent de modifier la disposition des informations. Des détails sur les marqueurs intelligents peuvent être obtenus dans l'article suivant :

[Utilisation des marqueurs intelligents](/cells/fr/net/using-smart-markers/)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDynamicDataTable-1.cs" >}}

## **Comment importer DataColumn dans Excel**

Un objet *DataTable* ou *DataView* est composé d'une ou plusieurs colonnes. Les développeurs peuvent également importer des données de n'importe quelle colonne/des colonnes du *DataTable* ou *DataView* en appelant la méthode [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). La méthode [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) accepte un paramètre de type [**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions). La classe [**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) fournit une propriété [**ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes) qui accepte un tableau d'index de colonnes.

Le code d'exemple ci-dessous démontre l'utilisation de [**ImportTableOptions.ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes) pour importer des colonnes sélectives.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataColumn-1.cs" >}}

## **Comment importer DataView dans Excel**

Pour importer des données à partir d'un *DataView*, appelez la méthode [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Il existe de nombreuses versions surchargées de la méthode [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index), mais celle pour le DataView prend les paramètres suivants :

- **DataView:** L'objet *DataView* à partir duquel vous êtes sur le point d'importer le contenu.
- **First Row:** le numéro de ligne de la première cellule où les données seront importées.
- **First Column:** le numéro de colonne de la première cellule où les données seront importées.
- **ImportTableOptions:** Les options d'importation.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataView-1.cs" >}}

## **Comment importer DataGrid dans Excel**

Il est possible d'importer des données à partir d'un *DataGrid* en appelant la méthode [**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index) de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Il existe de nombreuses versions surchargées de la méthode [**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index), mais une surcharge typique prend les paramètres suivants :

- **Data grid**, l'objet *DataGrid* à partir duquel vous importez le contenu.
- **Numéro de ligne**, le numéro de ligne de la première cellule dans laquelle les données seront importées.
- **Numéro de colonne**, le numéro de colonne de la première cellule dans laquelle les données seront importées.
- **Insérer des lignes**, une propriété booléenne qui indique si des lignes supplémentaires doivent être ajoutées à la feuille de calcul pour ajuster les données ou non.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataGrid-1.cs" >}}

## **Comment importer GridView dans Excel**

Pour importer des données à partir d'un contrôle *GridView*, appelez la méthode [**ImportGridView**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importgridview) de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells).

Aspose.Cells nous permet de conserver les valeurs formatées en HTML lors de l'importation des données dans la feuille de calcul. Lorsque l'analyse HTML est activée lors de l'importation des données, Aspose.Cells convertit le HTML en formatage de cellule correspondant.

## **Comment importer des données au format HTML dans Excel**

Aspose.Cells fournit une classe [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) qui propose des méthodes très utiles pour importer des données à partir de sources de données externes. Cet article montre comment analyser du texte formaté en HTML lors de l'importation des données et convertir le HTML en valeurs de cellule formatées.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportHtmlFormattedData-1.cs" >}}

## **Comment importer des données dans Excel à partir de JSON**

Aspose.Cells fournit une classe [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) pour le traitement JSON. La classe [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) dispose d'une méthode [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata) pour l'importation de données JSON. Aspose.Cells fournit également une classe [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) qui représente les options de la disposition JSON. La méthode [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata) accepte [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) en tant que paramètre. La classe [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) propose les propriétés suivantes.

- [**ArrayAsTable**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable) : Indique si le tableau doit être traité comme un tableau ou non.
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/convertnumericordate) : Obtient ou définit une valeur qui indique si la chaîne en JSON doit être convertie en numérique ou en date.
- [**DateFormat**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/dateformat) : Obtient et définit le format de la valeur de date.
- [**IgnoreArrayTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle) : Indique s'il faut ignorer le titre si la propriété de l'objet est un tableau.
- [**IgnoreNull**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorenull) : Indique si la valeur nulle doit être ignorée ou non.
- [**IgnoreObjectTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignoreobjecttitle) : Indique s'il faut ignorer le titre si la propriété de l'objet est un objet.
- [**NumberFormat**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/numberformat): Obtient et définit le format de la valeur numérique.
- [**TitleStyle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/titlestyle): Obtient et définit le style du titre.

Le code d'exemple ci-dessous démontre l'utilisation des classes [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) et [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) pour importer des données JSON.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromJson-1.cs" >}}

## **Sujets avancés**
- [Spécifier les champs de formule lors de l'importation de données dans la feuille de calcul](/cells/fr/net/specify-formula-fields-while-importing-data-to-worksheet/)
- [Décaler la première ligne vers le bas lors de l'insertion de lignes de tableau de données de cellules](/cells/fr/net/shift-first-row-down-when-inserting-cells-data-table-rows/)
{{< app/cells/assistant language="csharp" >}}
