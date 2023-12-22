---
title: .NET のワークシートからデータをエクスポート
linktitle: ワークシートからデータをエクスポート
type: docs
weight: 180
url: /ja/net/export-data-from-worksheet/
description: この記事では、C# を使用してワークシートからデータテーブルにデータをエクスポートまたはインポートする方法について説明します。
keywords: C# Export Data from Worksheet, C# Export Data to DataTable, Columns Containing Strongly Typed Data, Columns Containing Non-Strongly Typed Data, C# Export Range with flag to skip column name
---
## 概要

この記事では、C# を使用してワークシート データを DataTable にエクスポートする方法について説明します。内容は次のトピックです。

 _フォーマット_：**エクセル**
- [C# Excel から DataTable へ](#csharp-excel-to-datatable)
- [C# Excel を DataTable に変換](#csharp-convert-excel-to-datatable)
- [C# Excel を DataTable にインポート](#csharp-import-excel-to-datatable)
- [C# Excel から DataTable にエクスポート](#csharp-export-to-datatable-from-excel)

 _フォーマット_：**XLS**
- [C# XLS データテーブルへ](#csharp-xls-to-datatable)
- [C# XLS をデータテーブルに変換します](#csharp-convert-xls-to-datatable)
- [C# XLS を DataTable にインポート](#csharp-import-xls-to-datatable)
- [C# XLS から DataTable にエクスポート](#csharp-export-to-datatable-from-xls)

 _フォーマット_：**XLSX**
- [C# XLSX データテーブルへ](#csharp-xlsx-to-datatable)
- [C# XLSX をデータテーブルに変換します](#csharp-convert-xlsx-to-datatable)
- [C# XLSX を DataTable にインポート](#csharp-import-xlsx-to-datatable)
- [C# XLSX から DataTable にエクスポート](#csharp-export-to-datatable-from-xlsx)

 _フォーマット_：**ODS**
- [C# ODS データテーブルへ](#csharp-ods-to-datatable)
- [C# ODS をデータテーブルに変換します](#csharp-convert-ods-to-datatable)
- [C# ODS を DataTable にインポート](#csharp-import-ods-to-datatable)
- [C# ODS から DataTable にエクスポート](#csharp-export-to-datatable-from-ods)

##  **C# を使用して Excel データをエクスポートする方法**

{{% alert color="primary" %}}

この記事では、開発者が Aspose.Cells を通じてアクセスできるいくつかのデータ エクスポート テクニックについて説明します。

{{% /alert %}}

##  **ワークシートからデータをエクスポートする方法**

Aspose.Cells により、ユーザーは外部データ ソースからワークシートにデータをインポートできるだけでなく、ワークシート データを[**データ表**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)。私たちが知っているように、[**データ表**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)これは ADO.NET の一部であり、データを保持するために使用されます。データが保存されると、[**データ表**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) 、ユーザーの要件に応じて任意の方法で使用できます。開発者は、このデータを保存することもできます（次の場所に保存されます）。[**データ表**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) ) 必要に応じて、データベースに直接アクセスします。したがって、ワークシート データをエクスポートすると、開発者にとってワークシート データの操作が容易になることがわかります。[**データ表**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8).

##  **Aspose.Cells を使用してデータを DataTable にエクスポートする方法**

開発者はワークシート データを簡単にエクスポートできます。[**データ表**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)いずれかを呼び出してオブジェクトをオブジェクト化する[**データテーブルのエクスポート**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)または[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index)の方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)クラス。どちらの方法もさまざまなシナリオで使用されます。これについては、以下で詳しく説明します。

##  **厳密に型指定されたデータを含む列**

スプレッドシートにはデータが一連の行と列として格納されることがわかっています。ワークシートの列内のすべての値が厳密に型指定されている場合 (つまり、列内のすべての値が同じデータ型を持つ必要がある)、次のメソッドを呼び出してワークシートのコンテンツをエクスポートできます。[**データテーブルのエクスポート**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)の方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)クラス。[**データテーブルのエクスポート**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)このメソッドは、ワークシート データを次の形式でエクスポートするために次のパラメータを受け取ります。[**データ表**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)物体：

- *行番号**、エクスポートされる最初のセルの行番号。
- *列番号**、データのエクスポート元の最初のセルの列番号。
- *行数**、エクスポートする行数。
- *列の数**、エクスポートする列の数。
- *列名をエクスポート**。ワークシートの最初の行のデータをワークシートの列名としてエクスポートするかどうかを示すブール型プロパティです。[**データ表**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)か否か。

_手順: DataTable へのデータのエクスポート_

- <a name="csharp-excel-to-datatable" id="csharp-excel-to-datatable"><strong><em>手順:</em> C# の Excel から DataTable</strong></a>
  - <a name="csharp-xls-to-datatable" id="csharp-xls-to-datatable"><strong><em>手順:</em> XLS の DataTable へ</strong></a>
  - <a name="csharp-xlsx-to-datatable" id="csharp-xlsx-to-datatable"><strong><em>手順:</em> XLSX の DataTable へ</strong></a>
  - <a name="csharp-ods-to-datatable" id="csharp-ods-to-datatable"><strong><em>手順:</em> ODS の DataTable へ</strong></a>
- <a name="csharp-convert-excel-to-datatable" id="csharp-convert-excel-to-datatable"><strong><em>手順:</em>C# で Excel を DataTable に変換</strong></a>
  - <a name="csharp-convert-xls-to-datatable" id="csharp-convert-xls-to-datatable"><strong><em>手順:</em>XLS を C# の DataTable に変換します</strong></a>
  - <a name="csharp-convert-xlsx-to-datatable" id="csharp-convert-xlsx-to-datatable"><strong><em>手順:</em>XLSX を C# の DataTable に変換します</strong></a>
  - <a name="csharp-convert-ods-to-datatable" id="csharp-convert-ods-to-datatable"><strong><em>手順:</em>ODS を C# の DataTable に変換します</strong></a>
- <a name="csharp-import-excel-to-datatable" id="csharp-import-excel-to-datatable"><strong><em>手順:</em>C# の DataTable に Excel をインポート</strong></a>
  - <a name="csharp-import-xls-to-datatable" id="csharp-import-xls-to-datatable"><strong><em>手順:</em>XLS を C# の DataTable にインポートします</strong></a>
  - <a name="csharp-import-xlsx-to-datatable" id="csharp-import-xlsx-to-datatable"><strong><em>手順:</em>XLSX を C# の DataTable にインポートします</strong></a>
  - <a name="csharp-import-ods-to-datatable" id="csharp-import-ods-to-datatable"><strong><em>手順:</em>ODS を C# の DataTable にインポートします</strong></a>
- <a name="csharp-export-to-datatable-from-excel" id="csharp-export-to-datatable-from-excel"><strong><em>手順:</em>C# の Excel から DataTable にエクスポート</strong></a>
  - <a name="csharp-export-to-datatable-from-xls" id="csharp-export-to-datatable-from-xls"><strong><em>手順:</em>C# の XLS から DataTable にエクスポート</strong></a>
  - <a name="csharp-export-to-datatable-from-xlsx" id="csharp-export-to-datatable-from-xlsx"><strong><em>手順:</em>C# の XLSX から DataTable にエクスポート</strong></a>
  - <a name="csharp-export-to-datatable-from-ods" id="csharp-export-to-datatable-from-ods"><strong><em>手順:</em>C# の ODS から DataTable にエクスポート</strong></a>

_コードの手順:_

1.  Excelファイルをロードします[ワークブック](https://reference.aspose.com/cells/net/aspose.cells/workbook/)物体。
   - [ワークブック](https://reference.aspose.com/cells/net/aspose.cells/workbook/)オブジェクトは Excel ファイル形式 (例: XLS、XLSX、XLSM、ODS など) をロードできます。
 3. 最初にアクセスします[ワークシート](https://reference.aspose.com/cells/net/aspose.cells/worksheet/)Excel ファイル内。
4. エクスポート領域を選択します (例: *DataTable** の 1 番目のセルから始まる 7 行 2 列)。
 5. 使用する[データテーブルのエクスポート](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/)データを DataTable にエクスポートするメソッド。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingStronglyTypedData-1.cs" >}}

##  **厳密に型指定されていないデータを含む列**

ワークシートの列のすべての値が厳密に型指定されていない場合 (つまり、列の値が異なるデータ型を持つ可能性がある)、次のメソッドを呼び出してワークシートのコンテンツをエクスポートできます。[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index)の方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)クラス。[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index)メソッドは、メソッドと同じパラメータのセットを受け取ります。[**データテーブルのエクスポート**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)ワークシート データを[**データ表**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)物体。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingNonStronglyTypedData-1.cs" >}}

##  **列名をスキップするフラグを付けて範囲をエクスポートする方法**

ある範囲のデータは次の場所にエクスポートできます[**データ表**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)ここで、エクスポートされたデータのヘッダー行をスキップするためのフラグを使用できます。次のコードは、さまざまなデータをエクスポートします。[**データ表**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)引数付き[**エクスポートテーブルオプション**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions)を含む[**エクスポート列名**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/exportcolumnname)フラグ。に設定されています**真実**ヘッダー情報が存在する場合、それはデータには含まれず、に設定されます。**間違い**ヘッダーがなく、すべての行がデータと見なされる場合。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportRangeWithFlagToSkipColumnHeader-1.cs" >}}

##  **アドバンストトピック**
- [Excel データを書式設定せずに DataTable にエクスポート](/cells/ja/net/export-excel-data-to-datatable-without-any-formatting/)
- [HTML の HTML 文字列値を DataTable にエクスポートします](/cells/ja/net/export-html-string-value-of-the-cells-to-the-datatable/)
- [表示されている行データをワークシートからエクスポート](/cells/ja/net/export-visible-rows-data-from-worksheet/)
- [ワークシート データをデータ テーブルにエクスポートするときに非表示の列を無視する](/cells/ja/net/ignore-hidden-columns-while-exporting-worksheet-data-to-data-table/)
- [ワークシート データのエクスポート中に重複する列の名前を自動的に変更する](/cells/ja/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/)
