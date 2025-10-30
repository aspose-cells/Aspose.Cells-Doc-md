---
title: GolangとC++を使用してピボットテーブルのDataFieldのデータ表示形式を操作
linktitle: ピボットテーブルのDataFieldのデータ表示形式を操作
type: docs
weight: 140
url: /ja/go-cpp/working-with-data-display-formats-of-datafield-in-pivot-table/
description: Aspose.Cells for C++を使用して、ピボットテーブルのDataFieldのデータ表示形式の操作方法を学びます。
---

{{% alert color="primary" %}}

Aspose.Cellsは、データフィールドのすべての表示形式をサポートしています。

{{% /alert %}}

## **"最小から最大までの順位付け"および"最大から最小までの順位付け"表示形式オプション**

Aspose.Cellsは、ピボットフィールドの表示形式オプションを設定する機能を提供します。これには、[**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/go-cpp/pivotshowvaluessetting/getcalculationtype/)プロパティを使用します。最大から最小までランク付けする場合は、[**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/go-cpp/pivotshowvaluessetting/getcalculationtype/)プロパティを[**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfielddatadisplayformat/)に設定できます。以下のコードスニペットは、表示形式オプションの設定例です。

サンプルソースと出力ファイルは、テスト用のサンプルコードをダウンロードできます:

[ソースExcelファイル](101089332.xlsx)

[出力Excelファイル](101089333.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithDataDisplayFormatsOfDatafieldInPivotTable.go" >}}
