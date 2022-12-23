---
title: .NET のワークシートからデータをエクスポート
linktitle: ワークシートからデータをエクスポート
type: docs
weight: 180
url: /ja/net/export-data-from-worksheet/
description: この記事では、C# を使用してワークシートからデータテーブルにデータをエクスポートまたはインポートする方法について説明します。
---
## 概要

この記事では、C# を使用して Worksheet データを DataTable にエクスポートする方法について説明します。次のトピックについて説明します。

_フォーマット_: **エクセル**
- [C# Excel から DataTable](#csharp-excel-to-datatable)
- [C# Excel を DataTable に変換](#csharp-convert-excel-to-datatable)
- [C# Excel を DataTable にインポート](#csharp-import-excel-to-datatable)
- [C# Excel から DataTable にエクスポート](#csharp-export-to-datatable-from-excel)

_フォーマット_: **XLS**
- [C# XLS データテーブルへ](#csharp-xls-to-datatable)
- [C# XLS を DataTable に変換](#csharp-convert-xls-to-datatable)
- [C# XLS を DataTable にインポート](#csharp-import-xls-to-datatable)
- [C# XLS から DataTable にエクスポート](#csharp-export-to-datatable-from-xls)

_フォーマット_: **XLSX**
- [C# XLSX データテーブルへ](#csharp-xlsx-to-datatable)
- [C# XLSX を DataTable に変換](#csharp-convert-xlsx-to-datatable)
- [C# XLSX を DataTable にインポート](#csharp-import-xlsx-to-datatable)
- [C# XLSX から DataTable にエクスポート](#csharp-export-to-datatable-from-xlsx)

_フォーマット_: **ODS**
- [C# ODS データテーブルへ](#csharp-ods-to-datatable)
- [C# ODS を DataTable に変換](#csharp-convert-ods-to-datatable)
- [C# ODS を DataTable にインポート](#csharp-import-ods-to-datatable)
- [C# ODS から DataTable にエクスポート](#csharp-export-to-datatable-from-ods)

## **C# Excel データのエクスポート**

{{% alert color="primary" %}}

この記事では、開発者が Aspose.Cells を通じてアクセスできるいくつかのデータ エクスポート手法について説明します。

{{% /alert %}}

## **ワークシートからデータをエクスポート**

 Aspose.Cells は、ユーザーが外部データ ソースからワークシートにデータをインポートできるようにするだけでなく、ワークシート データを[**データ表**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8).私たちが知っているように[**データ表**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)ADO.NET の一部であり、データを保持するために使用されます。データが[**データ表**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)、ユーザーの要件に応じて任意の方法で使用できます。開発者は、このデータを保存することもできます ([**データ表**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) ）必要に応じてデータベースに直接。したがって、ワークシート データを[**データ表**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8).

## **Aspose.Cells を使用してデータを DataTable にエクスポートする**

開発者は、ワークシート データを簡単にエクスポートできます。[**データ表**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)いずれかを呼び出してオブジェクト[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)また[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index)の方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)クラス。どちらの方法も、以下で詳しく説明するさまざまなシナリオで使用されます。

## **厳密に型指定されたデータを含む列**

スプレッドシートはデータを一連の行と列として保存することがわかっています。ワークシートの列のすべての値が厳密に型指定されている場合 (つまり、列のすべての値が同じデータ型である必要があることを意味します)、[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)の方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)クラス。[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)メソッドは、次のパラメーターを使用して、ワークシート データを次のようにエクスポートします。[**データ表**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)物体：

- **行番号**からエクスポートされる最初のセル データの行番号。
- **列番号**、データがエクスポートされる最初のセルの列番号。
- **行の数**、エクスポートする行数。
- **列の数**、エクスポートする列の数。
- **列名のエクスポート**、ワークシートの最初の行のデータを列名としてエクスポートする必要があるかどうかを示すブール型プロパティ[**データ表**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)か否か。

_手順: データを DataTable にエクスポートする_

- <a name="csharp-excel-to-datatable" id="csharp-excel-to-datatable"><strong><em>手順:</em> C# の Excel から DataTable へ</strong></a>
  - <a name="csharp-xls-to-datatable" id="csharp-xls-to-datatable"><strong><em>手順:</em>XLS から C# の DataTable へ</strong></a>
  - <a name="csharp-xlsx-to-datatable" id="csharp-xlsx-to-datatable"><strong><em>手順:</em>XLSX から C# の DataTable へ</strong></a>
  - <a name="csharp-ods-to-datatable" id="csharp-ods-to-datatable"><strong><em>手順:</em>ODS から C# の DataTable へ</strong></a>
- <a name="csharp-convert-excel-to-datatable" id="csharp-convert-excel-to-datatable"><strong><em>手順:</em>C# で Excel を DataTable に変換する</strong></a>
  - <a name="csharp-convert-xls-to-datatable" id="csharp-convert-xls-to-datatable"><strong><em>手順:</em>XLS を C# の DataTable に変換します</strong></a>
  - <a name="csharp-convert-xlsx-to-datatable" id="csharp-convert-xlsx-to-datatable"><strong><em>手順:</em>XLSX を C# の DataTable に変換します</strong></a>
  - <a name="csharp-convert-ods-to-datatable" id="csharp-convert-ods-to-datatable"><strong><em>手順:</em>ODS を C# の DataTable に変換します</strong></a>
- <a name="csharp-import-excel-to-datatable" id="csharp-import-excel-to-datatable"><strong><em>手順:</em>Excel を C# の DataTable にインポートする</strong></a>
  - <a name="csharp-import-xls-to-datatable" id="csharp-import-xls-to-datatable"><strong><em>手順:</em>C# の DataTable に XLS をインポートします。</strong></a>
  - <a name="csharp-import-xlsx-to-datatable" id="csharp-import-xlsx-to-datatable"><strong><em>手順:</em>C# の DataTable に XLSX をインポートします。</strong></a>
  - <a name="csharp-import-ods-to-datatable" id="csharp-import-ods-to-datatable"><strong><em>手順:</em>C# の DataTable に ODS をインポートします。</strong></a>
- <a name="csharp-export-to-datatable-from-excel" id="csharp-export-to-datatable-from-excel"><strong><em>手順:</em> C# の Excel から DataTable にエクスポート</strong></a>
  - <a name="csharp-export-to-datatable-from-xls" id="csharp-export-to-datatable-from-xls"><strong><em>手順:</em>C# の XLS から DataTable にエクスポート</strong></a>
  - <a name="csharp-export-to-datatable-from-xlsx" id="csharp-export-to-datatable-from-xlsx"><strong><em>手順:</em>C# の XLSX から DataTable にエクスポート</strong></a>
  - <a name="csharp-export-to-datatable-from-ods" id="csharp-export-to-datatable-from-ods"><strong><em>手順:</em>C# の ODS から DataTable にエクスポート</strong></a>

_コードステップ:_

1.  Excelファイルをロードします[ワークブック](https://reference.aspose.com/cells/net/aspose.cells/workbook/)物体。
   - [ワークブック](https://reference.aspose.com/cells/net/aspose.cells/workbook/)オブジェクトは、XLS、XLSX、XLSM、ODS などの Excel ファイル形式をロードできます。
 3. 最初にアクセスする[ワークシート](https://reference.aspose.com/cells/net/aspose.cells/worksheet/)エクセルファイルで。
 4. エクスポート領域を選択します (例: 1 番目のセルから始まる 7 行 2 列)。**データ表**.
 5.使用[ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/)データを DataTable にエクスポートするメソッド。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingStronglyTypedData-1.cs" >}}

## **厳密に型指定されていないデータを含む列**

ワークシートの列のすべての値が厳密に型指定されていない場合 (つまり、列の値のデータ型が異なる可能性があることを意味します)、[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index)の方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)クラス。[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index)メソッドは、[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)ワークシート データを[**データ表**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)物体。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingNonStronglyTypedData-1.cs" >}}

## **列名をスキップするフラグ付きのエクスポート範囲**

範囲からのデータをエクスポートできます[**データ表**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)エクスポートされたデータのヘッダー行をスキップするフラグが利用可能です。次のコードは、データの範囲をにエクスポートします[**データ表**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)引数付き[**ExportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions)を含む[**エクスポート列名**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/exportcolumnname)国旗。に設定されています**真実**ヘッダー情報がある場合、それはデータに含まれず、に設定されます**間違い**ヘッダーがなく、すべての行がデータと見なされる場合。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportRangeWithFlagToSkipColumnHeader-1.cs" >}}

## **先行トピック**
- [書式設定なしで Excel データを DataTable にエクスポートする](/cells/ja/net/export-excel-data-to-datatable-without-any-formatting/)
- [HTML Cells の文字列値を DataTable にエクスポートします](/cells/ja/net/export-html-string-value-of-the-cells-to-the-datatable/)
- [ワークシートからの可視行データのエクスポート](/cells/ja/net/export-visible-rows-data-from-worksheet/)
- [ワークシート データをデータ テーブルにエクスポートする際に非表示の列を無視する](/cells/ja/net/ignore-hidden-columns-while-exporting-worksheet-data-to-data-table/)
- [ワークシート データのエクスポート中に重複する列の名前を自動的に変更する](/cells/ja/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/)
