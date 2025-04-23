---
title: タイムラインを挿入
linktitle: タイムライン
type: docs
weight: 170
url: /ja/java/create-timeline/
description: Aspose.Cells for Javaでタイムラインを作成する方法を学びます。
---

## **可能な使用シナリオ**

日付を表示するためにフィルタを調整する代わりに、PivotTableタイムラインを使用できます。これは、日付/時刻でフィルタリングすることが容易になり、スライダー コントロールで望む期間にズームインできるダイナミックフィルタオプションです。Microsoft Excelでは、ピボットテーブルを選択して*挿入 > タイムライン*をクリックしてタイムラインを作成できます。Aspose.Cells for Javaでは、[**Worksheet.getTimelines.add()**]メソッドを使用してタイムラインを作成することができます。

## **ピボットテーブルにタイムラインを作成する**

次のサンプルコードを参照してください。ピボットテーブルを含む[サンプルExcelファイル](input.xlsx)をロードし、最初の基本ピボットフィールドに基づいてタイムラインを作成します。最後に、[出力XLSX](output.xlsx)形式でワークブックを保存します。次のスクリーンショットは、Aspose.Cellsによって出力されたExcelファイル内のタイムラインを示しています。

<img src="create-timeline-to-a-pivot-table_1.png" width="60%">

### **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Timelines-CreateTimelineToPivotTable.java" >}}

{{< app/cells/assistant language="java" >}}
