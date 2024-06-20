---
title: 集計の作成
type: docs
weight: 50
url: /ja/java/creating-subtotals/
---

{{% alert color="primary" %}}

スプレッドシートに繰り返し値のサブトータルを自動的に作成できます。Aspose.Cellsは、プログラムでサブトータルを追加するのに役立つAPI機能を提供しています。

{{% /alert %}}

## **Microsoft Excel の使用**

Microsoft Excelでサブトータルを作成するには：

1. ブック1.xlsとして保存、ブックの最初のワークシートに簡単なデータリストを作成します（以下の図を参照）。
1. リスト内の任意のセルを選択します。
1. **データ** メニューから **集計** を選択します。
   サブトータルダイアログが表示されます。使用する機能やサブトータルを配置する場所を定義します。

   **サブトータルを追加するデータ範囲を選択**

![todo:image_alt_text](creating-subtotals_1.png)

**サブトータルダイアログ** 

![todo:image_alt_text](creating-subtotals_2.png)

## **Aspose.Cells APIを使用する**

Aspose.Cellsには、Microsoft Excelファイルを表すクラス [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) が提供されています。 [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) クラスには、Excelファイル内の各ワークシートにアクセスするのを可能にする [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) が含まれています。

ワークシートは [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) クラスで表されます。このクラスはワークシートや他のオブジェクトを管理するための多くのプロパティやメソッドを提供します。各ワークシートは [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) コレクションで構成されます。ワークシートでサブトータルを作成するには、[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) クラスのsubtotal メソッドを使用します。メソッドのパラメーターに適切な値を指定して、望む結果を得るために使用します。

以下の例は、Aspose.Cells APIを使用してテンプレートファイル（Book1.xls）の最初のワークシートにサブトータルを作成する方法を示しています。

コードを実行すると、サブトータルが追加されたワークシートが作成されます。

**サブトータルを適用** 

![todo:image_alt_text](creating-subtotals_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreatingSubtotals-CreatingSubtotals.java" >}}
