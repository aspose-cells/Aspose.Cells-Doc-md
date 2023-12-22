---
title: Importer des données dans une feuille de calcul
type: docs
weight: 170
url: /fr/net/import-data-into-worksheet/
description: Découvrez comment importer des données dans Worksheet via le Aspose.Cells for .NET API.
keywords: C# Import Data into Worksheet, Import data into Excel with ICellsDataTable interface, Import data from Array, Import Data from ArrayList, Import Data from Custom Objects, Import Data from Custom Objects to merged area, Import Data from DataTable, Import Data from dynamic object as data source, Import Data from DataColumn, Import Data from DataView, Import Data from DataGrid, Import Data from GridView, Import HTML formatted data, Import Data Data from JSON
---
{{% alert color="primary" %}}

Cet article traite de certaines techniques d'importation de données auxquelles les développeurs ont accès via le Aspose.Cells.

{{% /alert %}}

##  **Comment importer des données dans une feuille de calcul**

Lorsque vous ouvrez un fichier Excel avec Aspose.Cells, toutes les données du fichier sont automatiquement importées. Aspose.Cells peut également importer des données provenant d'autres sources de données.

Aspose.Cells fournit un[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook)classe qui représente un fichier Excel Microsoft. Le[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook)la classe contient un[**Des feuilles de calcul**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fournit un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collection.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)La collecte fournit des méthodes utiles pour importer des données à partir de différentes sources de données. Cet article explique comment ces méthodes peuvent être utilisées.

##  **Comment importer des données dans Excel avec l'interface ICellsDataTable**
 Mettre en œuvre[ICellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable) pour envelopper vos différentes sources de données, puis utilisez[Cells.ImportData()](https://reference.aspose.com/cells/net/aspose.cells/cells/importdata/#importdata) pour importer des données dans une feuille de calcul Excel.
###  **Exemple de code**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "ImportICellsDataTableIntoWorksheet.cs" >}}

L'implémentation de*CustomerDataSource*, *Customer* et *CustomerList* les cours sont donnés ci-dessous

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}


##  **Comment importer des données dans Excel à partir d'un tableau**

 Pour importer des données dans une feuille de calcul à partir d'un tableau, appelez le[**Importerun tableau**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index) méthode du[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collection. Il existe de nombreuses versions surchargées du[**Importerun tableau**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index)méthode mais une surcharge typique prend les paramètres suivants :

- *Array**, l'objet tableau à partir duquel vous importez du contenu.
- *Numéro de ligne**, le numéro de ligne de la première cellule dans laquelle les données seront importées.
- *Numéro de colonne**, le numéro de colonne de la première cellule dans laquelle les données seront importées.
- *Est vertical**, une valeur booléenne qui spécifie s'il faut importer les données verticalement ou horizontalement.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArray-1.cs" >}}

##  **Comment importer des données dans Excel à partir d'ArrayList**

 Pour importer des données depuis un*Liste des tableaux* aux feuilles de calcul, appelez le[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) la collection[**ImportArrayList**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarraylist)méthode. La méthode ImportArray prend les paramètres suivants :

-  *Liste de tableaux**, représente le*Liste des tableaux*objet que vous importez.
- *Numéro de ligne** représente le numéro de ligne de la première cellule dans laquelle les données seront importées.
- *Numéro de colonne**, représente le numéro de colonne de la première cellule dans laquelle les données seront importées.
- *Est vertical**, une valeur booléenne qui spécifie s'il faut importer les données verticalement ou horizontalement.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArrayList-1.cs" >}}

##  **Comment importer des données dans Excel à partir d'objets personnalisés**

 Pour importer des données d'une collection d'objets vers une feuille de calcul, utilisez[**Importer des objets personnalisés**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importcustomobjects/index). Fournissez une liste de colonnes/propriétés à la méthode pour afficher la liste d’objets souhaitée.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromCustomObject-1.cs" >}}

##  **Comment importer des données dans Excel à partir d'objets personnalisés vers une zone fusionnée**

Pour importer des données d'une collection d'objets vers une feuille de calcul contenant des cellules fusionnées, utilisez[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) propriété. Si le modèle Excel a fusionné des cellules, définissez la valeur de[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells)propriété à vrai. Passe le[**Options d'importation de table**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) object avec la liste des colonnes/propriétés à la méthode pour afficher la liste d’objets souhaitée. L'exemple de code suivant illustre l'utilisation de[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) propriété pour importer des données d’objets personnalisés vers des cellules fusionnées. Veuillez regarder la pièce jointe[sourceExcel](90112033.xlsx) fichier et le[sortie Excel](90112034.xlsx) fichier pour référence.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportCustomObjectsToMergedArea-1.cs" >}}

##  **Comment importer des données dans Excel à partir de DataTable**

Pour importer des données depuis un *DataTable*, appelez le[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) la collection[**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index) méthode. Il existe de nombreuses versions surchargées du[**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index)méthode mais une surcharge typique prend les paramètres suivants :

-  *Tableau de données**, le*Table de données* objet à partir duquel vous importez le contenu.
-  *Le nom du champ est-il affiché**, précise si les noms des*Table de données*les colonnes doivent être importées dans la feuille de calcul en tant que première ligne ou non.
- *Cellule de départ**, représente le nom de la cellule de départ (par exemple "A1") à partir de laquelle importer le contenu du *DataTable*.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataTable-1.cs" >}}

##  **Comment importer des données dans Excel à partir d'un objet dynamique comme source de données**

Aspose.Cells fournit des fonctionnalités permettant de travailler avec des objets dynamiques comme source de données. Cela aide à utiliser une source de données où les propriétés sont ajoutées dynamiquement aux objets. Une fois les propriétés ajoutées à l'objet, Aspose.Cells considère la première entrée comme modèle et gère le reste en conséquence. Cela signifie que si une propriété dynamique est ajoutée à un premier élément uniquement et non aux autres objets, Aspose.Cells considère que tous les éléments de la collection doivent être identiques.

Dans cet exemple, un modèle modèle est utilisé qui contient initialement deux variables uniquement. Cette Liste est convertie en Liste d'objets dynamiques. Ensuite, un champ supplémentaire y est ajouté et finalement chargé dans le classeur. Le classeur sélectionne uniquement les valeurs qui se trouvent dans le fichier modèle XLSX. Ce classeur modèle utilise des marqueurs intelligents qui contiennent également des paramètres. Les paramètres vous permettent de modifier la façon dont les informations sont présentées. Des détails sur les marqueurs intelligents peuvent être obtenus dans l’article suivant :

[Utiliser des marqueurs intelligents](/cells/fr/net/using-smart-markers/)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDynamicDataTable-1.cs" >}}

##  **Comment importer des données dans Excel à partir de DataColumn (.NET)**

A *Table de données*ou*Vue de données*L'objet est composé d'une ou plusieurs colonnes. Les développeurs peuvent également importer des données à partir de n'importe quelle colonne/colonne du*Table de données*ou*Vue de données*en appelant le[**Importer des données**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) méthode du[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collection. Le[**Importer des données**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)la méthode accepte un paramètre de type[**Options d'importation de table**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions). Le[**Options d'importation de table**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) la classe fournit un[**Index de colonnes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)propriété qui accepte un tableau d’index de colonnes.

L'exemple de code ci-dessous démontre l'utilisation de[**ImportTableOptions.ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)pour importer des colonnes sélectives.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataColumn-1.cs" >}}

##  **Comment importer des données dans Excel à partir de DataView (.NET)**

 Pour importer des données depuis un *DataView*, appelez le[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) la collection[**Importer des données**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) méthode. Il existe de nombreuses versions surchargées du[**Importer des données**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)méthode mais celle de DataView prend les paramètres suivants :

- **Vue de données :** Le*Vue de données*objet à partir duquel vous êtes sur le point d’importer du contenu.
- **Première rangée:**le numéro de ligne de la première cellule dans laquelle les données seront importées.
- **Première colonne :**le numéro de colonne de la première cellule dans laquelle les données seront importées.
- **Options d'importation de table :**Les options d'importation.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataView-1.cs" >}}

##  **Comment importer des données dans Excel à partir de DataGrid (.NET)**

 Il est possible d'importer des données depuis un*Grille de données* en appelant le[**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index) méthode du[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collection. Il existe de nombreuses versions surchargées du[**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index)méthode mais une surcharge typique prend les paramètres suivants :

-  *Grille de données**, la*Grille de données*objet à partir duquel vous importez du contenu.
- *Numéro de ligne**, le numéro de ligne de la première cellule dans laquelle les données seront importées.
- *Numéro de colonne**, le numéro de colonne de la première cellule dans laquelle les données seront importées.
- *Insérer des lignes**, une propriété booléenne qui indique si des lignes supplémentaires doivent être ajoutées à la feuille de calcul pour ajuster les données ou non.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataGrid-1.cs" >}}

##  **Comment importer des données dans Excel à partir de GridView**

 Pour importer des données depuis un*Vue Grille* contrôle, appelez le[**ImporterGridView**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importgridview) méthode du[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collection.

Aspose.Cells nous permet de respecter les valeurs formatées HTML lors de l'importation de données dans la feuille de calcul. Lorsque l'analyse HTML est activée lors de l'importation de données, Aspose.Cells convertit le HTML dans le formatage de cellule correspondant.

##  **Comment importer des données au format HTML dans Excel**

 Aspose.Cells fournit un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)classe qui fournit des méthodes très utiles pour importer des données à partir de sources de données externes. Cet article montre comment analyser le texte formaté HTML lors de l'importation de données et convertir le HTML en valeurs de cellule formatées.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportHtmlFormattedData-1.cs" >}}

##  **Comment importer des données dans Excel à partir du JSON**

Aspose.Cells fournit un[**JsonUtilitaire**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) classe de traitement JSON.[**JsonUtilitaire**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) la classe a un[**Importer des données**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata) méthode d'importation des données JSON. Aspose.Cells fournit également un[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) classe qui représente les options de mise en page JSON. Le[**Importer des données**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata)la méthode accepte[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)comme paramètre. Le[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)La classe fournit les propriétés suivantes.

- [**TableauEn tant queTable**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable): Indique dans le tableau qu'il doit être traité comme un tableau ou non.
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/convertnumericordate): obtient ou définit une valeur qui indique si la chaîne dans JSON doit être convertie en numérique ou en date.
- [**Format de date**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/dateformat): obtient et définit le format de la valeur de date.
- [**IgnorerArrayTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle): Indique s'il faut ignorer le titre si la propriété de l'objet est un tableau
- [**IgnorerNull**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorenull): Indique si la valeur nulle doit être ignorée ou non.
- [**Ignorer le titre de l'objet**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignoreobjecttitle): Indique s'il faut ignorer le titre si la propriété de l'objet est un objet.
- [**Format de nombre**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/numberformat): Obtient et définit le format de la valeur numérique.
- [**Style de titre**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/titlestyle): Obtient et définit le style du titre.

L'exemple de code ci-dessous démontre l'utilisation du[**JsonUtilitaire**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) et[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)classes pour importer les données JSON.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromJson-1.cs" >}}

##  **Sujets avancés**
- [Spécifier les champs de formule lors de l'importation de données dans une feuille de calcul](/cells/fr/net/specify-formula-fields-while-importing-data-to-worksheet/)
- [Décaler la première ligne vers le bas lors de l'insertion des lignes du tableau de données Cells](/cells/fr/net/shift-first-row-down-when-inserting-cells-data-table-rows/)
