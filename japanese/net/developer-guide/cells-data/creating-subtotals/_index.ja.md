---
title: 集計の作成
type: docs
weight: 800
url: /ja/net/creating-subtotals/
description: Aspose.Cells for .NET APIを使用して、スプレッドシート内の繰り返し値に対して小計を作成する方法について学びます。
keywords: サブトータルの追加、サブトータルの設定、サブトータルの追加、サブトータルの作成、ワークシートにサブトータルを追加する方法 
---

{{% alert color="primary" %}}

スプレッドシート内の繰り返し値に自動的に小計を作成できます。Aspose.Cellsには、スプレッドシートに小計をプログラムで追加するのに役立つAPI機能が備わっています。

{{% /alert %}}

## **Microsoft Excel の使用**

Microsoft Excel でサブトータルを追加する方法:

1. ブック1.xlsとして保存、ブックの最初のワークシートに簡単なデータリストを作成します（以下の図を参照）。
1. リスト内の任意のセルを選択します。
1. **データ** メニューから、**サブトータル** を選択します。サブトータルのダイアログが表示されます。使用する関数とサブトータルを配置する場所を定義します。

## **Aspose.Cells APIの使用**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスするための[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)コレクションが含まれています。

ワークシートは [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) クラスによって表されます。このクラスはワークシートや他のオブジェクトの管理に幅広いプロパティとメソッドを提供します。各ワークシートには [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) コレクションが含まれています。ワークシートにサブトータルを追加するには、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) クラスの [**Subtotal**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index) メソッドを使用します。メソッドにパラメータ値を指定して、サブトータルの計算方法と配置を指定します。

以下の例では、Aspose.Cells APIを使用してテンプレートファイル（Book1.xls）の最初のワークシートにサブトータルを追加しました。コードを実行すると、サブトータルが含まれるワークシートが作成されます。

以下のコードスニペットは、Aspose.Cells for .NETを使用してワークシートにサブトータルを追加する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-CreatingSubtotals-1.cs" >}}

## **高度なトピック**
- [サブトータルの適用と概要の方向を詳細の下に変更](/cells/ja/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
