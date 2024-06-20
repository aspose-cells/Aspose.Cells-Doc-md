---
title: タイムラインを挿入
linktitle: タイムライン
type: docs
weight: 170
url: /ja/net/create-timeline/
description: Aspose.Cellsでタイムラインを作成する方法について学びます。
---

## **可能な使用シナリオ**

日付を表示するためにフィルタを調整する代わりに、PivotTableタイムラインを使用できます。これは、日付/時刻で簡単にフィルタリングを行い、スライダーで希望する期間をズームインできる動的フィルタオプションです。マイクロソフトエクセルでは、ピボットテーブルを選択して*挿入 > タイムライン*をクリックすることでタイムラインを作成できます。Aspose.Cellsでは、[**Worksheet.Timelines.Add()**](https://reference.aspose.com/cells/net/aspose.cells.timelines/timelinecollection/methods/index)メソッドを使用してタイムラインを作成できます。

## **ピボットテーブルにタイムラインを作成する**

次のサンプルコードを参照してください。ピボットテーブルを含む[サンプルExcelファイル](input.xlsx)をロードし、最初の基本ピボットフィールドに基づいてタイムラインを作成します。最後に、[出力XLSX](output.xlsx)形式でワークブックを保存します。次のスクリーンショットは、Aspose.Cellsによって出力されたExcelファイル内のタイムラインを示しています。

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Timelines-CreateTimelineToPivotTable.cs" >}}

