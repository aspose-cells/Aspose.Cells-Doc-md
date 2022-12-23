---
title: Importer des données dans la feuille de calcul
type: docs
weight: 170
url: /fr/net/import-data-into-worksheet/
---
{{% alert color="primary" %}}

Cet article traite de certaines techniques d'importation de données auxquelles les développeurs ont accès via Aspose.Cells.

{{% /alert %}}

## **Importer des données dans la feuille de calcul**

Lorsque vous ouvrez un fichier Excel avec Aspose.Cells, toutes les données du fichier sont automatiquement importées. Aspose.Cells peut également importer des données à partir d'autres sources de données.

Aspose.Cells fournit un[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook)classe qui représente un fichier Excel Microsoft. Le[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook)classe contient un[**Feuilles de travail**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe offre une[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)le recueil.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)La collection fournit des méthodes utiles pour importer des données à partir de différentes sources de données. Cet article explique comment ces méthodes peuvent être utilisées.

## **Importation de données dans Excel avec l'interface ICellsDataTable**
 Mettre en œuvre[ICellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable) pour envelopper vos différentes sources de données, puis utilisez[Cells.ImportData()](https://reference.aspose.com/cells/net/aspose.cells/cells/importdata/#importdata) pour importer des données dans une feuille de calcul Excel.
### **Exemple de code**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "ImportICellsDataTableIntoWorksheet.cs" >}}

L'implémentation de*CustomerDataSource*, *Client*, et*Liste de clients* les cours sont donnés ci-dessous

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}


## **Importation à partir d'un tableau**

 Pour importer des données dans une feuille de calcul à partir d'un tableau, appelez le[**ImporterTableau**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index) méthode de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) le recueil. Il existe de nombreuses versions surchargées du[**ImporterTableau**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index)mais une surcharge typique prend les paramètres suivants :

- **Déployer**, l'objet tableau à partir duquel vous importez le contenu.
- **Numéro de ligne**le numéro de ligne de la première cellule dans laquelle les données seront importées.
- **Numéro de colonne**, le numéro de colonne de la première cellule dans laquelle les données seront importées.
- **Est vertical**, une valeur booléenne qui spécifie s'il faut importer les données verticalement ou horizontalement.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArray-1.cs" >}}

## **Importation depuis ArrayList**

 Pour importer des données d'un*Liste des tableaux* aux feuilles de travail, appelez le[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) de la collection[**ImportArrayListImportArrayListImportArrayList**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarraylist)méthode. La méthode ImportArray prend les paramètres suivants :

- **Liste des tableaux** , représente le*Liste des tableaux*objet que vous importez.
- **Numéro de ligne**, représente le numéro de ligne de la première cellule dans laquelle les données seront importées.
- **Numéro de colonne**, représente le numéro de colonne de la première cellule dans laquelle les données seront importées.
- **Est vertical**, une valeur booléenne qui spécifie s'il faut importer les données verticalement ou horizontalement.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArrayList-1.cs" >}}

## **Importation à partir d'objets personnalisés**

 Pour importer des données d'une collection d'objets dans une feuille de calcul, utilisez[**ImportCustomObjects**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importcustomobjects/index). Fournissez une liste de colonnes/propriétés à la méthode pour afficher la liste d'objets souhaitée.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromCustomObject-1.cs" >}}

## **Importation d'objets personnalisés vers une zone fusionnée**

Pour importer des données d'une collection d'objets vers une feuille de calcul contenant des cellules fusionnées, utilisez[**ImportTableOptions.CheckMergedCellsImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) la propriété. Si le modèle Excel contient des cellules fusionnées, définissez la valeur de[**ImportTableOptions.CheckMergedCellsImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells)propriété à vrai. Passe le[**ImportTableOptionsImportTableOptionsImportTableOptionsImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) objet avec la liste des colonnes/propriétés de la méthode pour afficher la liste d'objets souhaitée. L'exemple de code suivant illustre l'utilisation de[**ImportTableOptions.CheckMergedCellsImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) propriété pour importer des données d'objets personnalisés vers des cellules fusionnées. Veuillez regarder la pièce jointe[source Excel](90112033.xlsx) dossier et le[sortie Excel](90112034.xlsx) fichier pour référence.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportCustomObjectsToMergedArea-1.cs" >}}

## **Importation depuis DataTable**

 Pour importer des données d'un*Tableau de données* , appeler le[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) de la collection[**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index) méthode. Il existe de nombreuses versions surchargées du[**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index)mais une surcharge typique prend les paramètres suivants :

- **Tableau de données** , le*Tableau de données* objet dont vous importez le contenu.
- **Le nom du champ est-il affiché** , spécifie si les noms des*Tableau de données*les colonnes doivent être importées dans la feuille de calcul en tant que première ligne ou non.
- **Cellule de départ** , représente le nom de la cellule de départ (par exemple "A1") à partir de laquelle importer le contenu de la*Tableau de données*.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataTable-1.cs" >}}

## **Importation à partir d'un objet dynamique en tant que source de données**

Aspose.Cells fournit des fonctionnalités permettant de travailler avec des objets dynamiques en tant que source de données. Cela aide à utiliser la source de données où les propriétés sont ajoutées dynamiquement aux objets. Une fois les propriétés ajoutées à l'objet, Aspose.Cells considère la première entrée comme modèle et gère le reste en conséquence. Cela signifie que si une propriété dynamique est ajoutée à un premier élément uniquement et non à d'autres objets, Aspose.Cells considère que tous les éléments de la collection doivent être identiques.

Dans cet exemple, un modèle de modèle est utilisé qui ne contient initialement que deux variables. Cette liste est convertie en liste d'objets dynamiques. Ensuite, un champ supplémentaire y est ajouté et finalement chargé dans le classeur. Le classeur sélectionne uniquement les valeurs qui se trouvent dans le fichier de modèle XLSX. Ce modèle de classeur utilise des marqueurs intelligents qui contiennent également des paramètres. Les paramètres permettent de modifier la présentation des informations. Des détails sur les marqueurs intelligents peuvent être obtenus à partir de l'article suivant :

[Utiliser des marqueurs intelligents](/cells/fr/net/using-smart-markers/)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDynamicDataTable-1.cs" >}}

## **Importation depuis DataColumn (.NET)**

UNE*Tableau de données*ou alors*Affichage des données*objet est composé d'une ou plusieurs colonnes. Les développeurs peuvent également importer des données à partir de n'importe quelle colonne/colonnes du*Tableau de données*ou alors*Affichage des données*en appelant le[**Importer des données**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) méthode de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)le recueil. Le[**Importer des données**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)la méthode accepte un paramètre de type[**ImportTableOptionsImportTableOptionsImportTableOptionsImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions). Le[**ImportTableOptionsImportTableOptionsImportTableOptionsImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) la classe offre une[**Index de colonne**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)propriété qui accepte un tableau d'index de colonnes.

L'exemple de code ci-dessous illustre l'utilisation de[**ImportTableOptions.ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes) pour importer des colonnes sélectives.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataColumn-1.cs" >}}

## **Importation depuis DataView (.NET)**

 Pour importer des données d'un*Affichage des données* , appeler le[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) de la collection[**Importer des données**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) méthode. Il existe de nombreuses versions surchargées du[**Importer des données**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)mais celle de DataView prend les paramètres suivants :

- **Affichage des données :** Le*Affichage des données*objet dont vous êtes sur le point d'importer le contenu.
- **Première rangée:**le numéro de ligne de la première cellule dans laquelle les données seront importées.
- **Première colonne :**le numéro de colonne de la première cellule dans laquelle les données seront importées.
- **Options d'importation de table :**Les options d'importation.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataView-1.cs" >}}

## **Importation depuis DataGrid (.NET)**

 Il est possible d'importer des données à partir d'un*Grille de données* en appelant le[**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index) méthode de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) le recueil. Il existe de nombreuses versions surchargées du[**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index)mais une surcharge typique prend les paramètres suivants :

- **Grille de données** , le*Grille de données*objet à partir duquel vous importez du contenu.
- **Numéro de ligne**le numéro de ligne de la première cellule dans laquelle les données seront importées.
- **Numéro de colonne**, le numéro de colonne de la première cellule dans laquelle les données seront importées.
- **Insérer des lignes**, une propriété booléenne qui indique si des lignes supplémentaires doivent être ajoutées à la feuille de calcul pour ajuster les données ou non.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataGrid-1.cs" >}}

## **Importation depuis GridView**

 Pour importer des données d'un*GridView* contrôle, appeler le[**ImportGridView**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importgridview) méthode de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)le recueil.

Aspose.Cells nous permet de respecter les valeurs formatées HTML lors de l'importation de données dans la feuille de calcul. Lorsque l'analyse HTML est activée lors de l'importation de données, Aspose.Cells convertit le HTML dans le format de cellule correspondant.

## **Importation de données au format HTML**

 Aspose.Cells fournit un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)classe qui fournit des méthodes très utiles pour importer des données à partir de sources de données externes. Cet article montre comment analyser le texte formaté HTML lors de l'importation de données et convertir le HTML en valeurs de cellule formatées.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportHtmlFormattedData-1.cs" >}}

## **Importation de données depuis JSON**

Aspose.Cells fournit un[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) classe de traitement JSON.[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) la classe a un[**Importer des données**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata) méthode d'importation des données JSON. Aspose.Cells fournit également un[**JsonLayoutOptionsJsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) classe qui représente les options de mise en page JSON. Le[**Importer des données**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata)la méthode accepte[**JsonLayoutOptionsJsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)comme paramètre. Le[**JsonLayoutOptionsJsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)classe fournit les propriétés suivantes.

- [**TableauCommeTable**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable): Indique dans le tableau qu'il doit être traité ou non comme une table.
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/convertnumericordate): Obtient ou définit une valeur qui indique si la chaîne dans JSON doit être convertie en numérique ou en date.
- [**Format de date**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/dateformat): Obtient et définit le format de la valeur de date.
- [**IgnoreArrayTitleIgnoreArrayTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle): Indique s'il faut ignorer le titre si la propriété de l'objet est un tableau
- [**IgnorerNull**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorenull): Indique si la valeur nulle doit être ignorée ou non.
- [**IgnoreObjectTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignoreobjecttitle): Indique s'il faut ignorer le titre si la propriété de l'objet est un objet.
- [**Format de nombre**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/numberformat): Obtient et définit le format de la valeur numérique.
- [**Style de titre**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/titlestyle): Obtient et définit le style du titre.

L'exemple de code ci-dessous illustre l'utilisation du[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) et[**JsonLayoutOptionsJsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) classes pour importer les données JSON.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromJson-1.cs" >}}

## **Sujets avancés**
- [Spécifier les champs de formule lors de l'importation de données dans la feuille de calcul](/cells/fr/net/specify-formula-fields-while-importing-data-to-worksheet/)
- [Décaler la première ligne vers le bas lors de l'insertion de lignes de table de données Cells](/cells/fr/net/shift-first-row-down-when-inserting-cells-data-table-rows/)
