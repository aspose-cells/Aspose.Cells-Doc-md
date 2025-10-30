---
title: 集計の作成
type: docs
weight: 800
url: /ja/nodejs-cpp/creating-subtotals/
description: スプレッドシート内の繰り返し値に対して小計を作成する方法を、Aspose.Cells for Node.js via C++ APIを使って学びます。
keywords: サブトータルの追加、サブトータルの設定、サブトータルの追加、サブトータルの作成、ワークシートにサブトータルを追加する方法 
---

{{% alert color="primary" %}}

スプレッドシートの繰り返し値に対して自動的に小計を作成できます。Aspose.Cells for Node.js via C++は、スプレッドシートに小計をプログラム的に追加するのに役立つAPI機能を提供します。

{{% /alert %}}

## **Microsoft Excel の使用**

Microsoft Excel でサブトータルを追加する方法:

1. ブック1.xlsとして保存、ブックの最初のワークシートに簡単なデータリストを作成します（以下の図を参照）。
1. リスト内の任意のセルを選択します。
1. **データ** メニューから、**サブトータル** を選択します。サブトータルのダイアログが表示されます。使用する関数とサブトータルを配置する場所を定義します。

## **Aspose.Cells for Node.js via C++ APIを使用する**

Aspose.Cells for Node.js via C++は、Microsoft Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)を提供します。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)コレクションが含まれています。

ワークシートは [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) クラスによって表されます。このクラスはワークシートや他のオブジェクトの管理に幅広いプロパティとメソッドを提供します。各ワークシートには [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) コレクションが含まれています。ワークシートにサブトータルを追加するには、[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) クラスの [**subtotal**](https://reference.aspose.com/cells/nodejs-cpp/cells/#subtotal-cellarea-number-consolidationfunction-numberarray-) メソッドを使用します。メソッドにパラメータ値を指定して、サブトータルの計算方法と配置を指定します。

以下の例では、Aspose.Cells for Node.js via C++ APIを使用して[テンプレートファイル](book1.xlsx)の最初のワークシートに小計を追加しました。コードを実行すると、小計を含むワークシートが作成されます。

以下のコードスニペットは、Aspose.Cells for Node.js via C++を使用してワークシートに小計を追加する方法を示しています。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CreatingSubtotals-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
