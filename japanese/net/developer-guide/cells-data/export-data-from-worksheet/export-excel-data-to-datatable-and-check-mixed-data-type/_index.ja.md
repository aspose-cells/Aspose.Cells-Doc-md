---
title: Excel データを DataTable にエクスポートし、混合データ型をチェックする
type: docs
weight: 280
url: /ja/net/export-excel-data-to-datatable-and-check-mixed-data-type/
description: Excel データを DataTable にエクスポートし、Aspose.Cells for .NET API を通じて混合データ型を確認する方法を学びます。
keywords: Export Excel Data to DataTable and Check Mixed Data Type, Export Workbook Data to DataTable and Check Mixed Data Type, Export Data to DataTable and Check Mixed Data Type, Export Worksheet Data to DataTable and Check Mixed Data Type.
---
##  **考えられる使用シナリオ**
列にさまざまな型のデータが含まれている場合、プログラムはデータを DataTable にエクスポートするときに型例外をスローします。データテーブルをエクスポートする場合、デフォルトでは、Aspose.Cells は列の最初の (セル) 値に基づいて値のデータ型を評価します。したがって、値が数値であれば、列のデータ型が数値であることを意味しており、これは妥当です。一番最初の値が数値であっても、列に英数字データまたは値がある場合は、文字列データ型を割り当てる必要があります。それに対処するには、を使用してください[ExportDataTable のオーバーロード](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/#exportdatatable_1)それには[データテーブルのエクスポートオプション](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/)そして設定してみてください[ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/)列に数値と文字列の両方の値がある場合、エラーを回避するためにブール属性を「true」に設定します。

##  **Excel データを DataTable にエクスポートし、混合データ型をチェックする**

次のサンプルは、の使用法を説明しています。[ExportTableOptions.CheckMixedValueType](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/checkmixedvaluetype/)Excel データをデータ テーブルにエクスポートするプロパティ。をご覧ください。[サンプル Excel ファイル](sample.xlsx)、そのスクリーンショット、および参考用のコンソール出力。

###  **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-ExportDataAndCheckMixedType.cs" >}}

###  **スクリーンショット**
<br>
<image src="1.png" width="70%" />
<br>
<image src="2.png" width="70%" />
<br>

###  **コンソール出力**

以下は、上記のサンプル コードのコンソール デバッグ出力です。

{{< highlight "java" >}}

Column1 = System.String
Column2 = System.String
Column3 = System.Double
Column4 = System.Double
Column5 = System.String

{{< /highlight >}}
