---
title: 空のワークシートを検出する
type: docs
weight: 710
url: /ja/java/detecting-empty-worksheets/
---

## **空の初期化されたセルのチェック**
ワークシートには、値が入力されたセルが1つ以上含まれることがあります。値は単純なもの（テキスト、数値、日付/時刻）または式、または式に基づく値であることがあります。このような場合、与えられたワークシートが空かどうかを検出するのは簡単です。確認する必要があるのは[Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow)または[Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn)プロパティだけです。前述のプロパティがゼロまたは正の値を返す場合、1つ以上のセルが入力されていることを意味し、これらのプロパティのいずれかが-1を返す場合、与えられたワークシートにセルが入力されていないことを示します。

{{% alert color="primary" %}} 

行と列のコレクションにはゼロベースのインデックスがあります。そのため、行0および列0のセルはワークシートの最初のセルであり、A1を意味します。

{{% /alert %}} 
## **空の初期化されたセルのチェック**
値が入力されたすべてのセルは自動的に初期化されますが、ワークシートにはフォーマットのみが適用されたセルがある可能性があります。このようなシナリオでは、[Cells.MaxDataRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataRow)または[Cells.MaxDataColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDataColumn)プロパティは-1を返し、入力値は存在しないがセルの初期化が行われていることが検出できません。ワークシートに空の初期化されたセルがあるかどうかを確認するには、Cellsコレクションから取得したイテレーターに対して*Iterator.hasNext* メソッドを使用することをお勧めします。*iterator.hasNext* メソッドがtrueを返す場合、与えられたワークシートに1つ以上の初期化されたセルがあることを意味します。

{{% alert color="primary" %}} 

詳細は[イテレータの使用法と場所](/cells/ja/java/how-and-where-to-use-iterators/)に記載されています。

{{% /alert %}} 
## **図形のチェック**
特定のワークシートに入力されたセルが存在しない可能性がありますが、コントロール、チャート、画像などの図形やオブジェクトが含まれていることがあります。ワークシートに図形が含まれているかどうかを確認するには、[ShapeCollection.Count](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#Count)プロパティを検査します。正の値はワークシートに図形が存在することを示します。
## **プログラミングサンプル**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CheckForShapes-1.java" >}}
{{< app/cells/assistant language="java" >}}
