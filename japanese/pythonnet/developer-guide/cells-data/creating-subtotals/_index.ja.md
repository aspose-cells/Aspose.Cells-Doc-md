---
title: 集計の作成
type: docs
weight: 800
url: /ja/python-net/creating-subtotals/
description: スプレッドシート内の繰り返し値の任意の部分合計を、Aspose.Cells for Python via .NET APIを使用して作成する方法について学んでください。
keywords: Python Excelライブラリ、サブトータルの適用、サブトータルの設定、サブトータルの追加、ワークシートにサブトータルを追加する方法 
---

{{% alert color="primary" %}}

スプレッドシート内の繰り返し値の任意の部分合計を自動的に作成することができます。Aspose.Cells for Python via .NETは、スプレッドシートに部分合計をプログラムで追加するのに役立つAPI機能を提供しています。

{{% /alert %}}

## **Microsoft Excel の使用**

Microsoft Excel でサブトータルを追加する方法:

1. ブック1.xlsとして保存、ブックの最初のワークシートに簡単なデータリストを作成します（以下の図を参照）。
1. リスト内の任意のセルを選択します。
1. **データ** メニューから、**サブトータル** を選択します。サブトータルのダイアログが表示されます。使用する関数とサブトータルを配置する場所を定義します。

## **Aspose.Cells for Python via .NET APIを使用する**

Aspose.Cells for Python via .NET は、Microsoft Excelファイルを表す [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) クラスには、Excelファイル内の各ワークシートにアクセスできる [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) コレクションが含まれています。

ワークシートは [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) クラスによって表されます。このクラスはワークシートや他のオブジェクトの管理に幅広いプロパティとメソッドを提供します。各ワークシートには [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) コレクションが含まれています。ワークシートにサブトータルを追加するには、[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) クラスの [**subtotal**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/subtotal/#aspose.cells.CellArea-int-aspose.cells.ConsolidationFunction-list) メソッドを使用します。メソッドにパラメータ値を指定して、サブトータルの計算方法と配置を指定します。

以下の例では、Aspose.Cells for Python via .NET APIを使用して、テンプレートファイル (Book1.xls) の最初のワークシートにサブトータルを追加しました。コードを実行すると、サブトータルが含まれるワークシートが作成されます。

以下のコードスニペットは、Aspose.Cells for Python via .NETでワークシートにサブトータルを追加する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CreatingSubtotals-1.py" >}}

## **高度なトピック**
- [サブトータルの適用と概要の方向を詳細の下に変更](/cells/ja/python-net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
