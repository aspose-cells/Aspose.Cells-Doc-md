---
title: 日付軸
description: Aspose.Cells for Javaで日付軸を管理する方法を学びます。当社のガイドを参照して、さまざまな日付形式、時間軸、目盛りラベル頻度との作業方法を理解してください。
keywords: Aspose.Cells for Java、日付軸、管理、日付形式、時間軸、目盛りラベル頻度。
type: docs
weight: 200
url: /ja/java/date-axis/
---

## **可能な使用シナリオ**
ワークシートデータからチャートを作成し、そのデータに日付が使用されており、チャートの水平（カテゴリ）軸に日付がプロットされている場合、Aspose.cellsは自動的にカテゴリ軸を日付（時間軸）軸に変更します。
日付軸は、特定の間隔や基本単位（日数、月、年など）で、ワークシートの日付を年代順に表示します。ワークシート上の日付が順次に並んでいない場合や基本単位が同じでない場合でも、表示されます。
デフォルトでは、Aspose.cellsは、ワークシートデータの任意の2つの日付間の最小の差に基づいて、日付軸の基本単位を決定します。たとえば、株価のデータがあり、日付間の最小の差が7日の場合、Excelは基本単位を日に設定しますが、株のパフォーマンスをより長い期間で見たい場合は、基本単位を月や年に変更することができます。
## **Microsoft Excelのように日付軸を処理する**
以下のサンプルコードを参照して、新しいExcelファイルを作成し、チャートの値を最初のワークシートに配置します。 
その後、チャートを追加し、[**Axis**](https://reference.aspose.com/cells/java/com.aspose.cells/axis/)の種類を設定します。 
[**TimeScale**](https://reference.aspose.com/cells/java/com.aspose.cells/categorytype/#TIME-SCALE)のタイプを設定し、その後基本単位を日に設定します。

![todo:image_alt_text](excel.png)

次のサンプルコードは、[出力Excelファイル](DateAxis.xlsx)を生成します。

## **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DateAxis.java" >}}
