---
title: Golang経由のC++でタイムラインを挿入
linktitle: タイムライン
type: docs
weight: 170
url: /ja/go-cpp/create-timeline/
description: Aspose.Cellsを使用してC++でタイムラインを作成する方法を学びましょう。
---

## **可能な使用シナリオ**

フィルターを調整して日付を表示する代わりに、ピボットテーブルのタイムライン——日付/時間で簡単にフィルタリングし、スライダーコントロールで期間をズームインできる動的フィルターオプションを使用できます。Microsoft Excelでは、ピボットテーブルを選択してから *挿入 > タイムライン* をクリックすることでタイムラインを作成できます。Aspose.Cells も [**Worksheet.Timelines.Add()**](https://reference.aspose.com/cells/go-cpp/timelinecollection/add_pivottable_int_int_string/) メソッドを使用してタイムラインを作成できます。

## **ピボットテーブルにタイムラインを作成する**

次のサンプルコードを参照してください。ピボットテーブルを含む[サンプルExcelファイル](input.xlsx)をロードし、最初の基本ピボットフィールドに基づいてタイムラインを作成します。最後に、[出力XLSX](output.xlsx)形式でワークブックを保存します。次のスクリーンショットは、Aspose.Cellsによって出力されたExcelファイル内のタイムラインを示しています。

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Timelines.go" >}}
