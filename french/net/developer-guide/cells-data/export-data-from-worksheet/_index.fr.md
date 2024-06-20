---
title: Exporter des données à partir de la feuille de calcul en .NET
linktitle: Exporter des données à partir de la feuille de calcul
type: docs
weight: 180
url: /fr/net/export-data-from-worksheet/
description: Cet article explique comment exporter ou importer des données de la feuille de calcul dans un datatable en utilisant C#.
keywords: Exporter des données de la feuille de calcul en C#, Exporter des données vers DataTable en C#, Colonnes contenant des données fortement typées, Colonnes contenant des données non fortement typées, Exporter une plage en C# avec un indicateur pour sauter le nom de la colonne, Comment exporter une plage avec en tête en C#.
---

## Aperçu

Cet article explique comment exporter les données de votre feuille de calcul vers DataTable en utilisant C#. Il couvre les sujets suivants

_Format_: **Excel**
- [C# Excel to DataTable](#csharp-excel-to-datatable)
- [C# Convert Excel to DataTable](#csharp-convert-excel-to-datatable)
- [C# Importez Excel vers DataTable](#csharp-import-excel-to-datatable)
- [C# Exporter vers DataTable à partir d'Excel](#csharp-export-to-datatable-from-excel)

_Format_: **XLS**
- [C# XLS vers DataTable](#csharp-xls-to-datatable)
- [C# Convertir XLS en DataTable](#csharp-convert-xls-to-datatable)
- [C# Importez XLS vers DataTable](#csharp-import-xls-to-datatable)
- [C# Exporter vers DataTable à partir de XLS](#csharp-export-to-datatable-from-xls)

_Format_: **XLSX**
- [C# XLSX vers DataTable](#csharp-xlsx-to-datatable)
- [C# Convertir XLSX en DataTable](#csharp-convert-xlsx-to-datatable)
- [C# Importez XLSX vers DataTable](#csharp-import-xlsx-to-datatable)
- [C# Exporter vers DataTable à partir de XLSX](#csharp-export-to-datatable-from-xlsx)

_Format_: **ODS**
- [C# ODS vers DataTable](#csharp-ods-to-datatable)
- [C# Convertir ODS en DataTable](#csharp-convert-ods-to-datatable)
- [C# Importez ODS vers DataTable](#csharp-import-ods-to-datatable)
- [C# Exporter vers DataTable à partir de ODS](#csharp-export-to-datatable-from-ods)

## **Comment exporter des données Excel à l'aide de C#**

{{% alert color="primary" %}}

Cet article traite de quelques techniques d'exportation de données auxquelles les développeurs ont accès via Aspose.Cells.

{{% /alert %}}

## **Comment exporter des données de la feuille de calcul**

Aspose.Cells non seulement facilite ses utilisateurs pour importer des données vers des feuilles de calcul à partir de sources de données externes mais leur permet également d'exporter leurs données de feuilles de calcul vers une [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8). Comme nous le savons que [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) fait partie d'ADO.NET et est utilisé pour contenir des données. Une fois les données stockées dans un [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8), elles peuvent être utilisées de n'importe quelle manière selon les besoins des utilisateurs. Les développeurs peuvent également stocker ces données (stockées dans [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)) directement dans une base de données s'ils le souhaitent. Ainsi, nous pouvons voir qu'il devient plus facile pour les développeurs de manipuler les données de feuille de calcul si elles sont exportées vers un [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8).

## **Comment exporter des données vers un DataTable en utilisant Aspose.Cells**

Les développeurs peuvent facilement exporter leurs données de feuille de calcul vers un objet [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) en appelant soit la méthode [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) soit [**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) de la classe [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Les deux méthodes sont utilisées dans différents scénarios, qui sont discutés ci-dessous de manière plus détaillée.

## **Colonnes contenant des données fortement typées**

Nous savons qu'une feuille de calcul stocke des données sous forme d'une séquence de lignes et de colonnes. Si toutes les valeurs dans les colonnes d'une feuille de calcul sont fortement typées (cela signifie que toutes les valeurs d'une colonne doivent avoir le même type de données), alors nous pouvons exporter le contenu de la feuille de calcul en appelant la méthode [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) de la classe [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). La méthode [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) prend les paramètres suivants pour exporter les données de la feuille de calcul en tant qu'objet [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) :

- **Numéro de ligne**, le numéro de la première donnée de cellule sera exporté à partir de.
- **Numéro de colonne**, le numéro de colonne de la première donnée de cellule sera exporté à partir de.
- **Nombre de lignes**, le nombre de lignes à exporter.
- **Nombre de colonnes**, le nombre de colonnes à exporter.
- **Exporter les noms de colonne**, une propriété booléenne qui indique si les données dans la première ligne de la feuille de calcul doivent être exportées en tant que noms de colonnes du [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) ou non.

Étapes : Exporter des données vers un DataTable

- <a name="csharp-excel-to-datatable" id="csharp-excel-to-datatable"><strong><em>Étapes :</em> Excel to DataTable in C#</strong></a>
  - <a name="csharp-xls-to-datatable" id="csharp-xls-to-datatable"><strong><em>Étapes :</em> XLS to DataTable in C#</strong></a>
  - <a name="csharp-xlsx-to-datatable" id="csharp-xlsx-to-datatable"><strong><em>Étapes :</em> XLSX to DataTable in C#</strong></a>
  - <a name="csharp-ods-to-datatable" id="csharp-ods-to-datatable"><strong><em>Étapes :</em> ODS to DataTable in C#</strong></a>
- <a name="csharp-convert-excel-to-datatable" id="csharp-convert-excel-to-datatable"><strong><em>Étapes :</em> Convert Excel to DataTable in C#</strong></a>
  - <a name="csharp-convert-xls-to-datatable" id="csharp-convert-xls-to-datatable"><strong><em>Étapes :</em> Convert XLS to DataTable in C#</strong></a>
  - <a name="csharp-convert-xlsx-to-datatable" id="csharp-convert-xlsx-to-datatable"><strong><em>Étapes :</em> Convert XLSX to DataTable in C#</strong></a>
  - <a name="csharp-convert-ods-to-datatable" id="csharp-convert-ods-to-datatable"><strong><em>Étapes :</em> Convert ODS to DataTable in C#</strong></a>
- <a name="csharp-import-excel-to-datatable" id="csharp-import-excel-to-datatable"><strong><em>Étapes :</em> Import Excel to DataTable in C#</strong></a>
  - <a name="csharp-import-xls-to-datatable" id="csharp-import-xls-to-datatable"><strong><em>Étapes :</em> Import XLS to DataTable in C#</strong></a>
  - <a name="csharp-import-xlsx-to-datatable" id="csharp-import-xlsx-to-datatable"><strong><em>Étapes :</em> Import XLSX to DataTable in C#</strong></a>
  - <a name="csharp-import-ods-to-datatable" id="csharp-import-ods-to-datatable"><strong><em>Étapes :</em> Import ODS to DataTable in C#</strong></a>
- <a name="csharp-export-to-datatable-from-excel" id="csharp-export-to-datatable-from-excel"><strong><em>Étapes :</em> Export to DataTable from Excel in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xls" id="csharp-export-to-datatable-from-xls"><strong><em>Étapes :</em> Export to DataTable from XLS in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xlsx" id="csharp-export-to-datatable-from-xlsx"><strong><em>Étapes :</em> Export to DataTable from XLSX in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-ods" id="csharp-export-to-datatable-from-ods"><strong><em>Étapes :</em> Export to DataTable from ODS in C#</strong></a>

_Étapes du code :_

1. Chargez votre fichier Excel dans l'objet [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook/).
   - L'objet [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook/) peut charger des formats de fichiers Excel tels que XLS, XLSX, XLSM, ODS, etc.
3. Accédez à la première [Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet/) dans le fichier Excel.
4. Choisissez votre zone d'exportation p. ex. 7 lignes et 2 colonnes à partir de la 1ère cellule de **DataTable**.
5. Utilisez la méthode [ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/) pour exporter les données dans DataTable.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingStronglyTypedData-1.cs" >}}

## **Colonnes contenant des données non fortement typées**

Si toutes les valeurs dans les colonnes d'une feuille de calcul ne sont pas fortement typées (cela signifie que les valeurs dans une colonne peuvent avoir des types de données différents), nous pouvons exporter le contenu de la feuille de calcul en appelant la méthode [**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) de la classe [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). La méthode [**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) prend le même ensemble de paramètres que la méthode [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) pour exporter les données de la feuille de calcul en tant qu'objet [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingNonStronglyTypedData-1.cs" >}}

## **Comment exporter une plage avec en-tête**

Les données d'une plage peuvent être exportées vers [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) où un indicateur est disponible pour ignorer la ligne d'en-tête dans les données exportées. Le code suivant exporte une plage de données vers [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) avec un argument [**ExportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions) qui contient un drapeau [**ExportColumnName**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/exportcolumnname). Il est défini sur **true** s'il y a des informations d'en-tête, donc il ne seront pas incluses dans les données et défini sur **false** s'il n'y a pas d'en-tête et que toutes les lignes doivent être considérées comme des données.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportRangeWithFlagToSkipColumnHeader-1.cs" >}}

## **Sujets avancés**
- [Exporter les données Excel dans un DataTable sans aucun formatage](/cells/fr/net/export-excel-data-to-datatable-without-any-formatting/)
- [Exporter la valeur de chaîne HTML des cellules dans le DataTable](/cells/fr/net/export-html-string-value-of-the-cells-to-the-datatable/)
- [Exporter les données des lignes visibles de la feuille de calcul](/cells/fr/net/export-visible-rows-data-from-worksheet/)
- [Ignorer les colonnes masquées lors de l'exportation des données de la feuille de calcul dans un DataTable](/cells/fr/net/ignore-hidden-columns-while-exporting-worksheet-data-to-data-table/)
- [Renommer automatiquement les colonnes en double lors de l'exportation des données de la feuille de calcul](/cells/fr/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/)
