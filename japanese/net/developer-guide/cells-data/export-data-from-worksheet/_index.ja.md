---
title: .NETでワークシートからデータをエクスポートする方法
linktitle: ワークシートからデータをエクスポートする方法
type: docs
weight: 180
url: /ja/net/export-data-from-worksheet/
description: この記事では、C#を使用してワークシートからデータをDataTableにエクスポートまたはインポートする方法について説明しています。
keywords: C#でのワークシートからのデータエクスポート、C#でのDataTableへのデータエクスポート、強く型付けされたデータを含む列、弱く型付けされたデータを含む列、列名をスキップするためのフラグを持つ範囲のエクスポート方法、ヘッダー付きの範囲のエクスポート方法
---

## 概要

この記事では、C#を使用してワークシートデータをDataTableにエクスポートする方法について説明します。以下のトピックをカバーしています

_フォーマット_: **Excel**
- [C# ExcelからDataTableへ](#csharp-excel-to-datatable)
- [C# ExcelをDataTableに変換](#csharp-convert-excel-to-datatable)
- [C# ExcelをDataTableにインポート](#csharp-import-excel-to-datatable)
- [C# ExcelからDataTableにエクスポート](#csharp-export-to-datatable-from-excel)

_フォーマット_: **XLS**
- [C# XLSをDataTableに](#csharp-xls-to-datatable)
- [C#でXLSをDataTableに変換する](#csharp-convert-xls-to-datatable)
- [C#でXLSをDataTableにインポートする](#csharp-import-xls-to-datatable)
- [C#でXLSからDataTableにエクスポートする](#csharp-export-to-datatable-from-xls)

_フォーマット_: **XLSX**
- [C# XLSXをDataTableに変換する](#csharp-xlsx-to-datatable)
- [C#でXLSXをDataTableに変換する](#csharp-convert-xlsx-to-datatable)
- [C#でXLSXをDataTableにインポートする](#csharp-import-xlsx-to-datatable)
- [C#でXLSXからDataTableにエクスポートする](#csharp-export-to-datatable-from-xlsx)

_フォーマット_: **ODS**
- [C# ODSをDataTableに変換する](#csharp-ods-to-datatable)
- [C#でODSをDataTableに変換する](#csharp-convert-ods-to-datatable)
- [C#でODSをDataTableにインポートする](#csharp-import-ods-to-datatable)
- [C#でODSからDataTableにエクスポートする](#csharp-export-to-datatable-from-ods)

## **C#を使用したExcelデータのエクスポート方法**

{{% alert color="primary" %}}

この記事では、Aspose.Cellsを介して開発者がアクセスできるデータエクスポート技術について説明します。

{{% /alert %}}

## **ワークシートからデータをエクスポートする方法**

Aspose.Cellsは、ワークシートに外部データソースからデータをインポートするだけでなく、ワークシートデータを[**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)  にエクスポートすることも可能です。[**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)  はADO.NETの一部であり、データを保持するために使用されます。データが[**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)に保存されると、ユーザーの要件に応じていつでも使用できます。開発者は、必要に応じて（[**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)で保存された）このデータを直接データベースに保存することもできます。したがって、ワークシートデータを[**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)にエクスポートすると、開発者がワークシートデータを操作することが容易になります。

## **Aspose.Cellsを使用してデータをDataTableにエクスポートする方法**

開発者は、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)クラスの[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)メソッドまたは[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index)メソッドを呼び出すことで、簡単にワークシートデータを[**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)オブジェクトにエクスポートできます。いずれのメソッドも、異なるシナリオで使用され、以下で詳しく説明されています。

## **型指定データを含む列**

スプレッドシートはデータを行と列の連続として保存していることを知っています。ワークシートの列のすべての値が強く型付けされている場合（つまり、列のすべての値が同じデータ型である場合）、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)クラスの[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)メソッドを呼び出すことでワークシートの内容を[**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)オブジェクトとしてエクスポートできます。[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)メソッドは、ワークシートデータを[**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)オブジェクトとしてエクスポートするために次のパラメータを取ります:

- **行番号**： データをエクスポートする最初のセルの行番号。
- **列番号**： データをエクスポートする最初のセルの列番号。
- **行数**： エクスポートする行数。
- **列数**： エクスポートする列数。
- **列名をエクスポート**： ワークシートの最初の行のデータを[**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)の列名としてエクスポートするかどうかを示すブール値プロパティ。

_手順：DataTableにデータをエクスポート_

- <a name="csharp-excel-to-datatable" id="csharp-excel-to-datatable"><strong><em>手順：</em> Excel to DataTable in C#</strong></a>
  - <a name="csharp-xls-to-datatable" id="csharp-xls-to-datatable"><strong><em>手順：</em> XLS to DataTable in C#</strong></a>
  - <a name="csharp-xlsx-to-datatable" id="csharp-xlsx-to-datatable"><strong><em>手順：</em> XLSX to DataTable in C#</strong></a>
  - <a name="csharp-ods-to-datatable" id="csharp-ods-to-datatable"><strong><em>手順：</em> ODS to DataTable in C#</strong></a>
- <a name="csharp-convert-excel-to-datatable" id="csharp-convert-excel-to-datatable"><strong><em>手順：</em> Convert Excel to DataTable in C#</strong></a>
  - <a name="csharp-convert-xls-to-datatable" id="csharp-convert-xls-to-datatable"><strong><em>手順：</em> Convert XLS to DataTable in C#</strong></a>
  - <a name="csharp-convert-xlsx-to-datatable" id="csharp-convert-xlsx-to-datatable"><strong><em>手順：</em> Convert XLSX to DataTable in C#</strong></a>
  - <a name="csharp-convert-ods-to-datatable" id="csharp-convert-ods-to-datatable"><strong><em>手順：</em> Convert ODS to DataTable in C#</strong></a>
- <a name="csharp-import-excel-to-datatable" id="csharp-import-excel-to-datatable"><strong><em>手順：</em> Import Excel to DataTable in C#</strong></a>
  - <a name="csharp-import-xls-to-datatable" id="csharp-import-xls-to-datatable"><strong><em>手順：</em> Import XLS to DataTable in C#</strong></a>
  - <a name="csharp-import-xlsx-to-datatable" id="csharp-import-xlsx-to-datatable"><strong><em>手順：</em> Import XLSX to DataTable in C#</strong></a>
  - <a name="csharp-import-ods-to-datatable" id="csharp-import-ods-to-datatable"><strong><em>手順：</em> Import ODS to DataTable in C#</strong></a>
- <a name="csharp-export-to-datatable-from-excel" id="csharp-export-to-datatable-from-excel"><strong><em>手順：</em> Export to DataTable from Excel in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xls" id="csharp-export-to-datatable-from-xls"><strong><em>手順：</em> Export to DataTable from XLS in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xlsx" id="csharp-export-to-datatable-from-xlsx"><strong><em>手順：</em> Export to DataTable from XLSX in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-ods" id="csharp-export-to-datatable-from-ods"><strong><em>手順：</em> Export to DataTable from ODS in C#</strong></a>

_コードの手順:_

1. [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook/)オブジェクトにExcelファイルをロードします。
   - [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook/)オブジェクトは、XLS、XLSX、XLSM、ODSなどのExcelファイル形式を読み込むことができます。
3. Excelファイル内の最初の[Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet/)にアクセスします。
4. 1番目の**DataTable**のセルから始まる7行2列など、エクスポートするエリアを選択します。
5. [ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/)メソッドを使用してデータをDataTableにエクスポートします。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingStronglyTypedData-1.cs" >}}

## **非型指定データを含む列**

ワークシートの列のすべての値が強く型指定されていない場合（つまり、列の値には異なるデータ型がある可能性がある）、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)クラスの[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index)メソッドを呼び出すことによってワークシートのコンテンツをエクスポートすることができます。[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index)メソッドは、ワークシートデータを[**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)オブジェクトとしてエクスポートするために[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)メソッドと同じセットのパラメータを受け取ります。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingNonStronglyTypedData-1.cs" >}}

## **ヘッダー付きの範囲のエクスポート方法**

範囲からのデータは、[**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)にエクスポートできます。[**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)にはエクスポートされたデータでヘッダー行をスキップするフラグが含まれています。次のコードは、データの範囲を[**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)にエクスポートし、ヘッダー情報がある場合には**true**に設定される[**ExportColumnName**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/exportcolumnname)含む引数[**ExportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions)を使用します。そのため、データが含まれていない場合は**false**に設定され、すべての行がデータとして考慮されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportRangeWithFlagToSkipColumnHeader-1.cs" >}}

## **高度なトピック**
- [書式設定なしでExcelデータをDataTableにエクスポート](/cells/ja/net/export-excel-data-to-datatable-without-any-formatting/)
- [セルのHTML文字列値をDataTableにエクスポート](/cells/ja/net/export-html-string-value-of-the-cells-to-the-datatable/)
- [ワークシートから表示される行のデータをエクスポート](/cells/ja/net/export-visible-rows-data-from-worksheet/)
- [ワークシートデータをデータテーブルにエクスポートする際に非表示の列を無視](/cells/ja/net/ignore-hidden-columns-while-exporting-worksheet-data-to-data-table/)
- [ワークシートデータをエクスポートする際に重複する列の名前を自動的に変更する](/cells/ja/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/)
