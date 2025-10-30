---
title: 日付軸
description: Aspose.Cells for Python via .NETを使用した日付軸の管理方法について学びます。ガイドでは、さまざまな日時形式や時間スケール、目盛りラベルの頻度の調整方法を理解できます。
keywords: Aspose.Cells for Python via .NET、日付軸、管理、日付フォーマット、時間スケール、目盛りラベルの頻度。
type: docs
weight: 200
url: /ja/python-net/date-axis/
---

## **可能な使用シナリオ**
ワークシートデータからチャートを作成し、そのデータに日付が使用されており、チャートの水平（カテゴリ）軸に日付がプロットされている場合、Aspose.cellsは自動的にカテゴリ軸を日付（時間軸）軸に変更します。
日付軸は、特定の間隔や基本単位（日数、月、年など）で、ワークシートの日付を年代順に表示します。ワークシート上の日付が順次に並んでいない場合や基本単位が同じでない場合でも、表示されます。
デフォルトでは、Aspose.cellsは、ワークシートデータの任意の2つの日付間の最小の差に基づいて、日付軸の基本単位を決定します。たとえば、株価のデータがあり、日付間の最小の差が7日の場合、Excelは基本単位を日に設定しますが、株のパフォーマンスをより長い期間で見たい場合は、基本単位を月や年に変更することができます。

## **Microsoft Excelのように日付軸を処理する**
以下のサンプルコードを参照して、新しいExcelファイルを作成し、チャートの値を最初のワークシートに配置します。 
その後、チャートを追加し、[**Axis**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/axis)の種類を設定します。 
[**TIME_SCALE**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/categorytype/)のタイプを設定し、その後基本単位を日に設定します。

![todo:image_alt_text](excel.png)

## **サンプルコード**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-DateAxis.py" >}}
{{< app/cells/assistant language="python-net" >}}
