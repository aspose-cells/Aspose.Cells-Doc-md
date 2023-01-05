---
title: Exporter les données de la feuille de calcul dans .NET
linktitle: Exporter les données de la feuille de calcul
type: docs
weight: 180
url: /fr/net/export-data-from-worksheet/
description: Cet article explique comment exporter ou importer des données d'une feuille de calcul dans une table de données à l'aide de C#.
---
## Aperçu

Cet article explique comment exporter vos données de feuille de calcul vers DataTable à l'aide de C#. Il couvre les sujets suivants

_Format_: **Exceller**
- [C# Excel vers DataTable](#csharp-excel-to-datatable)
- [C# Convertir Excel en DataTable](#csharp-convert-excel-to-datatable)
- [C# Importer Excel dans DataTable](#csharp-import-excel-to-datatable)
- [C# Exporter vers DataTable à partir d'Excel](#csharp-export-to-datatable-from-excel)

_Format_: **XLS**
- [C# XLS à DataTable](#csharp-xls-to-datatable)
- [C# Convertir XLS en DataTable](#csharp-convert-xls-to-datatable)
- [C# Importer XLS dans DataTable](#csharp-import-xls-to-datatable)
- [C# Exporter vers DataTable à partir de XLS](#csharp-export-to-datatable-from-xls)

_Format_: **XLSX**
- [C# XLSX à DataTable](#csharp-xlsx-to-datatable)
- [C# Convertir XLSX en DataTable](#csharp-convert-xlsx-to-datatable)
- [C# Importer XLSX dans DataTable](#csharp-import-xlsx-to-datatable)
- [C# Exporter vers DataTable à partir de XLSX](#csharp-export-to-datatable-from-xlsx)

_Format_: **ODS**
- [C# ODS à DataTable](#csharp-ods-to-datatable)
- [C# Convertir ODS en DataTable](#csharp-convert-ods-to-datatable)
- [C# Importer ODS dans DataTable](#csharp-import-ods-to-datatable)
- [C# Exporter vers DataTable à partir de ODS](#csharp-export-to-datatable-from-ods)

## **C# Exporter des données Excel**

{{% alert color="primary" %}}

Cet article traite de certaines techniques d'exportation de données auxquelles les développeurs ont accès via Aspose.Cells.

{{% /alert %}}

## **Exporter les données de la feuille de calcul**

 Aspose.Cells permet non seulement à ses utilisateurs d'importer des données dans des feuilles de calcul à partir de sources de données externes, mais leur permet également d'exporter leurs données de feuille de calcul vers un[**Tableau de données**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) . Comme nous savons que[**Tableau de données**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) fait partie de ADO.NET et est utilisé pour stocker des données. Une fois les données stockées dans un[**Tableau de données**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) , il peut être utilisé de n'importe quelle manière selon les exigences des utilisateurs. Les développeurs peuvent également stocker ces données (stockées dans[**Tableau de données**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) ) directement dans une base de données s'ils le souhaitent. Ainsi, nous pouvons voir qu'il devient plus facile pour les développeurs de manipuler les données de la feuille de calcul si elles sont exportées vers un[**Tableau de données**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8).

## **Exportation de données vers DataTable à l'aide de Aspose.Cells**

 Les développeurs peuvent facilement exporter leurs données de feuille de calcul vers un[**Tableau de données**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) objet en appelant soit[**ExporterTableDeDonnées**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) ou alors[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) méthode de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)classe. Les deux méthodes sont utilisées dans différents scénarios, qui sont discutés ci-dessous plus en détail.

## **Colonnes contenant des données fortement typées**

Nous savons qu'une feuille de calcul stocke les données sous la forme d'une séquence de lignes et de colonnes. Si toutes les valeurs des colonnes d'une feuille de calcul sont fortement typées (cela signifie que toutes les valeurs d'une colonne doivent avoir le même type de données), nous pouvons exporter le contenu de la feuille de calcul en appelant le[**ExporterTableDeDonnées**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) méthode de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) classe.[**ExporterTableDeDonnées**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) prend les paramètres suivants pour exporter les données de la feuille de calcul en tant que[**Tableau de données**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)objet:

- **Numéro de ligne**, le numéro de ligne des premières données de cellule sera exporté à partir de.
- **Numéro de colonne**, le numéro de colonne de la première cellule à partir de laquelle les données seront exportées.
- **Nombre de rangées**, le nombre de lignes à exporter.
- **Le nombre de colonnes**, le nombre de colonnes à exporter.
- **Exporter les noms de colonne** , une propriété booléenne qui indique si les données de la première ligne de la feuille de calcul doivent être exportées en tant que noms de colonne du[**Tableau de données**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)ou non.

_Étapes : exporter des données vers DataTable_

- <a name="csharp-excel-to-datatable" id="csharp-excel-to-datatable"><strong><em>Pas:</em> Excel vers DataTable en C#</strong></a>
  - <a name="csharp-xls-to-datatable" id="csharp-xls-to-datatable"><strong><em>Pas:</em> XLS à DataTable dans C#</strong></a>
  - <a name="csharp-xlsx-to-datatable" id="csharp-xlsx-to-datatable"><strong><em>Pas:</em> XLSX à DataTable dans C#</strong></a>
  - <a name="csharp-ods-to-datatable" id="csharp-ods-to-datatable"><strong><em>Pas:</em> ODS à DataTable dans C#</strong></a>
- <a name="csharp-convert-excel-to-datatable" id="csharp-convert-excel-to-datatable"><strong><em>Pas:</em> Convertir Excel en DataTable en C#</strong></a>
  - <a name="csharp-convert-xls-to-datatable" id="csharp-convert-xls-to-datatable"><strong><em>Pas:</em>Convertir XLS en DataTable en C#</strong></a>
  - <a name="csharp-convert-xlsx-to-datatable" id="csharp-convert-xlsx-to-datatable"><strong><em>Pas:</em>Convertir XLSX en DataTable en C#</strong></a>
  - <a name="csharp-convert-ods-to-datatable" id="csharp-convert-ods-to-datatable"><strong><em>Pas:</em>Convertir ODS en DataTable en C#</strong></a>
- <a name="csharp-import-excel-to-datatable" id="csharp-import-excel-to-datatable"><strong><em>Pas:</em> Importer Excel vers DataTable dans C#</strong></a>
  - <a name="csharp-import-xls-to-datatable" id="csharp-import-xls-to-datatable"><strong><em>Pas:</em> Importer XLS dans DataTable dans C#</strong></a>
  - <a name="csharp-import-xlsx-to-datatable" id="csharp-import-xlsx-to-datatable"><strong><em>Pas:</em> Importer XLSX dans DataTable dans C#</strong></a>
  - <a name="csharp-import-ods-to-datatable" id="csharp-import-ods-to-datatable"><strong><em>Pas:</em> Importer ODS dans DataTable dans C#</strong></a>
- <a name="csharp-export-to-datatable-from-excel" id="csharp-export-to-datatable-from-excel"><strong><em>Pas:</em> Exporter vers DataTable à partir d'Excel en C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xls" id="csharp-export-to-datatable-from-xls"><strong><em>Pas:</em> Exporter vers DataTable de XLS à C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xlsx" id="csharp-export-to-datatable-from-xlsx"><strong><em>Pas:</em> Exporter vers DataTable de XLSX à C#</strong></a>
  - <a name="csharp-export-to-datatable-from-ods" id="csharp-export-to-datatable-from-ods"><strong><em>Pas:</em> Exporter vers DataTable de ODS à C#</strong></a>

_Étapes de code :_

1.  Chargez votre fichier Excel dans[Cahier](https://reference.aspose.com/cells/net/aspose.cells/workbook/) objet.
   - [Cahier](https://reference.aspose.com/cells/net/aspose.cells/workbook/) l'objet peut charger des formats de fichier Excel, par exemple XLS, XLSX, XLSM, ODS, etc.
 3. Accéder au premier[Feuille de travail](https://reference.aspose.com/cells/net/aspose.cells/worksheet/) dans le fichier Excel.
 4. Choisissez votre zone d'exportation, par exemple 7 lignes et 2 colonnes à partir de la 1ère cellule de**Tableau de données**.
 5. Utilisez[ExporterTableDeDonnées](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/) méthode pour exporter les données dans DataTable.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingStronglyTypedData-1.cs" >}}

## **Colonnes contenant des données non fortement typées**

 Si toutes les valeurs des colonnes d'une feuille de calcul ne sont pas fortement typées (cela signifie que les valeurs d'une colonne peuvent avoir des types de données différents), nous pouvons exporter le contenu de la feuille de calcul en appelant le[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) méthode de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) classe.[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index)prend le même jeu de paramètres que celui de la[**ExporterTableDeDonnées**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)méthode pour exporter des données de feuille de calcul en tant que[**Tableau de données**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)objet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingNonStronglyTypedData-1.cs" >}}

## **Exporter la plage avec un indicateur pour ignorer le nom de la colonne**

Les données d'une plage peuvent être exportées vers[**Tableau de données**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) où un indicateur est disponible pour ignorer la ligne d'en-tête dans les données exportées. Le code suivant exporte une plage de données vers[**Tableau de données**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) avec une argumentation[**ExportTableOptionsExportTableOptionsExportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions) qui contient[**ExportColumnNameExportColumnNameExportColumnName**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/exportcolumnname) drapeau. Il est fixé à**vrai** si les informations d'en-tête sont présentes, elles ne seront donc pas incluses dans les données et définies sur**faux** s'il n'y a pas d'en-tête et que toutes les lignes doivent être considérées comme des données.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportRangeWithFlagToSkipColumnHeader-1.cs" >}}

## **Sujets avancés**
- [Exporter des données Excel vers DataTable sans aucun formatage](/cells/fr/net/export-excel-data-to-datatable-without-any-formatting/)
- [Exporter la valeur de chaîne HTML du Cells vers le DataTable](/cells/fr/net/export-html-string-value-of-the-cells-to-the-datatable/)
- [Exporter les données des lignes visibles à partir de la feuille de calcul](/cells/fr/net/export-visible-rows-data-from-worksheet/)
- [Ignorer les colonnes masquées lors de l'exportation des données de la feuille de calcul vers la table de données](/cells/fr/net/ignore-hidden-columns-while-exporting-worksheet-data-to-data-table/)
- [Renommer automatiquement les colonnes en double lors de l'exportation des données de la feuille de calcul](/cells/fr/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/)
