---
title: ExcelデータをDataTableにエクスポートして混合データ型を確認
type: docs
weight: 280
url: /ja/net/export-excel-data-to-datatable-and-check-mixed-data-type/
description: Aspose.Cells for .NET APIを介してExcelデータをDataTableにエクスポートし、混合データ型を確認する方法を学びます。
keywords: ExcelデータをDataTableにエクスポートして混合データ型を確認し、WorkbookデータをDataTableにエクスポートして混合データ型を確認し、データをDataTableにエクスポートして混合データ型を確認します、ExcelデータをDataTableにエクスポートし、ワークシートデータをDataTableにエクスポートして混合データ型を確認します。
---

## **可能な使用シナリオ**
列にさまざまなタイプのデータが含まれている場合、データをDataTableにエクスポートする際にタイプエラーが発生します。データテーブルをエクスポートする場合、Aspose.Cellsはデフォルトで、列の最初の値に基づいて値のデータ型を評価します。そのため、値が数値であれば、その列のデータ型は数値になります。これは合理的なことです。最初の値が数値ではあるが列には数字と文字列のデータや値がある場合、文字列のデータ型が割り当てられるべきです。この問題に対処するには、[ExportDataTableオーバーロード](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/#exportdatatable_1)と[ExportDataTableOptions](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/)を使用し、[ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/)ブール属性を「true」に設定してください。

## **ExcelデータをDataTableにエクスポートして混合データ型をチェック**

以下のサンプルは、[ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/)プロパティを使用してExcelデータをデータテーブルにエクスポートする方法を説明しています。参考のために、[サンプルExcelファイル](sample.xlsx)、そのスクリーンショット、およびコンソールの出力をご覧ください。

### **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-ExportDataAndCheckMixedType.cs" >}}

### **スクリーンショット**
<br>
<image src="1.png" width="70%" />
<br>
<image src="2.png" width="70%" />
<br>

### **コンソール出力**

上記サンプルコードのコンソールデバッグ出力は次のとおりです

{{< highlight java >}}

Column1 = System.String
Column2 = System.String
Column3 = System.Double
Column4 = System.Double
Column5 = System.String

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
