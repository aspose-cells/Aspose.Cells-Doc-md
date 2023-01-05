---
title: 書式設定なしで Excel データを DataTable にエクスポートする
type: docs
weight: 280
url: /ja/net/export-excel-data-to-datatable-without-any-formatting/
---
{{% alert color="primary" %}}

書式設定なしで Excel データをデータ テーブルにエクスポートしたい場合があります。たとえば、一部のセルの値が 0.012345 で、小数点以下 2 桁を表示するように書式設定されている場合、ユーザーが Excel データをデータ テーブルにエクスポートすると、0.012345 ではなく 0.01 としてエクスポートされます。この問題に対処するために、Aspose.Cells が提供しています。[**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy)これらの 3 つの値のいずれかを取ることができるプロパティ

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

に設定する場合[**CellValueFormatStrategy.None**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy)、フォーマットなしでデータをエクスポートします。

{{% /alert %}}

## サンプルコード

次のサンプルでは、[**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy)書式設定の有無にかかわらず Excel データをエクスポートするプロパティ。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ExportExcelDataToDataTableWithoutFormatting-ExportExcelDataToDataTableWithoutFormatting.cs" >}}

## **コンソール出力**

以下は、上記のサンプル コードのコンソール デバッグ出力です。

{{< highlight "java" >}}

Cell String Value: 0.01

Cell String Value without Format: 0.012345

Export Data Table with Format Strategy as Cell Style: 0.01

Export Data Table with Format Strategy as None: 0.012345

{{< /highlight >}}
