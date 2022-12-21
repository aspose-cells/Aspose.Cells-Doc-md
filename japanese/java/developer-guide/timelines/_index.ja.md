---
title: タイムラインを挿入
linktitle: タイムライン
type: docs
weight: 170
url: /ja/java/create-timeline/
description: Aspose.Cells For java でタイムラインを作成する方法を学びます。
---
## **考えられる使用シナリオ**

フィルターを調整して日付を表示する代わりに、ピボットテーブル タイムラインを使用できます。これは、日付/時刻で簡単にフィルター処理し、スライダー コントロールで必要な期間を拡大できる動的フィルター オプションです。 Microsoft Excel では、ピボット テーブルを選択してから、*挿入 > タイムライン*Java の Aspose.Cells では、[**Worksheet.getTimelines.add()**] メソッドを使用してタイムラインを作成することもできます。

## **ピボット テーブルにタイムラインを作成する**

以下のサンプルコードをご覧ください。それは[サンプル Excel ファイル](input.xlsx)ピボットテーブルが含まれています。次に、最初のベース ピボット フィールドに基づいてタイムラインを作成します。最後に、ワークブックを[出力XLSX](output.xlsx)フォーマット。次のスクリーンショットは、出力 Excel ファイルで Aspose.Cells によって作成されたタイムラインを示しています。

<img src="create-timeline-to-a-pivot-table_1.png" width="60%">

### **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Timelines-CreateTimelineToPivotTable.java" >}}

