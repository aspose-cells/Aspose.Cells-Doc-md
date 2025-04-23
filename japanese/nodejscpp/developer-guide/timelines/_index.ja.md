---
title: タイムラインを挿入
linktitle: タイムライン
type: docs
weight: 170
url: /ja/nodejs-cpp/create-timeline/
description: Aspose.Cells for Node.js via C++を使ったタイムラインの作成方法を学びましょう。
---

## **可能な使用シナリオ**

フィルターを調整して日付を表示する代わりに、ピボットテーブルのタイムラインを使用できます。これは、日付や時間で簡単にフィルタリングでき、スライダーコントロールを使用して期間をズームインできる動的なフィルターオプションです。Microsoft Excelでは、ピボットテーブルを選択し、「挿入」>「タイムライン」をクリックすることでタイムラインを作成できます。Aspose.Cells for Node.js via C++では、[**Worksheet.getTimelines().add()**](https://reference.aspose.com/cells/nodejs-cpp/timelinecollection/#add-pivottable-number-number-string-)メソッドを使用してタイムラインを作成することも可能です。

## **ピボットテーブルにタイムラインを作成する**

以下のサンプルコードを参照してください。これにより、ピボットテーブルを含む[サンプルExcelファイル](input.xlsx)が読み込まれます。その後、最初の基本ピボットフィールドに基づいてタイムラインが作成され、最後にワークブックが[出力 XLSX](output.xlsx)形式で保存されます。以下のスクリーンショットは、Aspose.Cells for Node.js via C++が作成したタイムラインを出力Excelファイルに示しています。

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **サンプルコード**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Timelines-CreateTimelineToPivotTable.js" >}}

