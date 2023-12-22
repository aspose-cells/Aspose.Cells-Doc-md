---
title: Excel データを書式設定せずに DataTable にエクスポート
type: docs
weight: 280
url: /ja/net/export-excel-data-to-datatable-without-any-formatting/
description: Aspose.Cells for .NET API を通じて、書式設定を行わずに Excel データを DataTable にエクスポートする方法を学びます。
keywords: Export Excel Data to DataTable without any Formatting, Specify Cell Value Format Strategy, Add Format Strategy When Exporting Data to DataTable. 
---
{{% alert color="primary" %}}

ユーザーは、Excel データを書式設定せずにデータ テーブルにエクスポートしたい場合があります。たとえば、あるセルの値が 0.012345 で、小数点以下 2 桁を表示するように書式設定されている場合、ユーザーが Excel データをデータ テーブルにエクスポートすると、0.012345 ではなく 0.01 としてエクスポートされます。この問題に対処するために、Aspose.Cells は次のサービスを提供しています。[**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy)これら 3 つの値のいずれかを取れるプロパティ

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

に設定する場合は、[**CellValueFormatStrategy.None**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy)を指定すると、書式設定なしでデータがエクスポートされます。

{{% /alert %}}

## サンプルコード

次のサンプルは、の使用法を説明しています。[**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy)Excel データを書式付きまたは書式なしでエクスポートするためのプロパティ。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ExportExcelDataToDataTableWithoutFormatting-ExportExcelDataToDataTableWithoutFormatting.cs" >}}

##  **コンソール出力**

以下は、上記のサンプル コードのコンソール デバッグ出力です。

{{< highlight "java" >}}

Cell String Value: 0.01

Cell String Value without Format: 0.012345

Export Data Table with Format Strategy as Cell Style: 0.01

Export Data Table with Format Strategy as None: 0.012345

{{< /highlight >}}
