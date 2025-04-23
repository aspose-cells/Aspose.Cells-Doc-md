---
title: ExcelデータをDataTableにエクスポートして任意の書式なしで確認
type: docs
weight: 280
url: /ja/net/export-excel-data-to-datatable-without-any-formatting/
description: Aspose.Cells for .NET APIを介してExcelデータをDataTableにエクスポートして任意の書式なしで確認する方法を学びます。
keywords: ExcelデータをDataTableに任意の書式なしでエクスポートし、セルの値のフォーマット戦略を指定し、データをDataTableにエクスポートする際にフォーマット戦略を追加します。 
---

{{% alert color="primary" %}}

ユーザーは、Excelデータを書式なしのデータテーブルにエクスポートすることがあります。たとえば、セルに値0.012345があり、小数点以下2桁にフォーマットされている場合、ユーザーがExcelデータをデータテーブルにエクスポートすると、0.01としてエクスポートされます。この問題に対処するために、Aspose.Cellsは[**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy)プロパティを提供しており、これは次の3つの値のいずれかを取ることができます

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

それを[**CellValueFormatStrategy.None**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy)に設定すると、フォーマットなしでデータがエクスポートされます。

{{% /alert %}}

## サンプルコード

次のサンプルは、[**ExportTableOptions.FormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/formatstrategy)プロパティを使用してExcelデータをフォーマットありおよびなしでエクスポートする方法を説明しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ExportExcelDataToDataTableWithoutFormatting-ExportExcelDataToDataTableWithoutFormatting.cs" >}}

## **コンソール出力**

上記サンプルコードのコンソールデバッグ出力は次のとおりです

{{< highlight java >}}

Cell String Value: 0.01

Cell String Value without Format: 0.012345

Export Data Table with Format Strategy as Cell Style: 0.01

Export Data Table with Format Strategy as None: 0.012345

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
