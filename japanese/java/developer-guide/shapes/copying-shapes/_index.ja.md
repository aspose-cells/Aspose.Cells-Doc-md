---
title: ワークシート間で図形をコピーする
type: docs
weight: 250
url: /ja/java/copy-shapes-between-worksheets/
---
{{% alert color="primary" %}}

必要に応じて、さまざまな画像、チャート、その他の描画オブジェクトをさまざまなワークシートにコピーする必要がある場合があります。 Aspose.Cells は、ワークシート間での図形のコピーをサポートしています。チャート、画像、その他のオブジェクトは、最高の精度でコピーされます。

Office オートメーションを試すこともできますが、それには欠点があります。関連するいくつかの理由と問題があります。たとえば、セキュリティ、安定性、スケーラビリティ、速度、価格、および機能です。簡単に言えば、多くの理由がありますが、一番の理由は、Microsoft 自身がソフトウェア ソリューションによる Office オートメーションを強く推奨していないことです。

この記事では、コンソール アプリケーションを作成し、Aspose.Cells を使用した数行の最も単純なコードで、ワークブックのワークシート間で画像、グラフ、およびその他の描画オブジェクトのコピーを実行します。

このドキュメントは、開発者がワークシート間で図形 (画像、グラフ、コントロール、およびその他の描画オブジェクト) をコピーする方法を詳細に理解できるようにすることを目的としています。

{{% /alert %}}

## **形状のコピー**

この記事では、次の方法について説明します。

- [あるワークシートから別のワークシートに画像をコピーする](/cells/ja/java/copy-shapes-between-worksheets/#copying-a-picture-from-one-worksheet-to-another).
- [あるワークシートから別のワークシートにグラフをコピーする](/cells/ja/java/copy-shapes-between-worksheets/#task-2-copying-a-chart-from-one-worksheet-to-another).
- [あるワークシートから別のワークシートにコントロールやその他の描画オブジェクトをコピーする](/cells/ja/java/copy-shapes-between-worksheets/#task-3-copying-controls-and-other-drawing-objects-from-one-worksheet-to-another).

### **あるワークシートから別のワークシートに画像をコピーする**

#### **ステップ 1: Microsoft Excel で画像とグラフを含むワークブックを作成する**

1. Microsoft Excel で新しいブックを作成しました。
1. 最初のワークシートに画像を追加し、2 番目のワークシートにグラフを追加します。

次のスクリーンショットは、Microsoft Excel で作成された 2 つのテンプレート ワークシートを示しています。

   **チャート付きワークシート「Chart」**

![todo:画像_代替_文章](copy-shapes-between-worksheets_1.png)

**絵入りワークシート「絵」**

![todo:画像_代替_文章](copy-shapes-between-worksheets_2.png)

ここで、「Picture」という名前のワークシートの画像を最後のワークシート「Result」にコピーします。

#### **ステップ 2: Aspose.Cells.Zip をダウンロードする**

1. [ダウンロード Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. 開発用コンピューターで解凍します。

全て[Aspose](http://www.aspose.com/)コンポーネントがインストールされると、評価モードで動作します。評価モードには時間制限がなく、生成されたドキュメントに透かしを挿入するだけです。

#### **ステップ 3: プロジェクトを作成する**

Eclipse などの Java エディターを使用してプロジェクトを作成するか、メモ帳を使用して簡単なプログラムを作成することができます。

#### **ステップ 4: クラスパスを追加する**

Eclipse を使用してクラス パスを設定するには、次の手順を実行してください。

1. Aspose.Cells.zip から Aspose.Cells.jar と dom4j_1.6.1.jar を抽出します。
1. Eclipse でプロジェクトのクラスパスを設定します。
1. Eclipse でプロジェクトを選択し、メニューの Project-Properties をクリックします。
1. ポップアップ ウィンドウの左側で [Java Build Path] を選択し、[Libraries] タブを選択し、[Add JARs] または [Add External JARs] をクリックして Aspose.Cells.jar と dom4j_1.6.1.jar を選択し、ビルドに追加します。パス。
1. Aspose のコンポーネントの API を呼び出すアプリケーションを作成します。

または、実行時に Windows の DOS プロンプトで設定することもできます。例:

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar;クラス名

#### **ステップ 5: あるワークシートから別のワークシートに画像をコピーする**

以下は、タスクを実行するためのコードです。 「Picture」という名前のワークシートからワークシート「Result」に画像をコピーします。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyPicturefromOneWorksheetToAnother-CopyPicturefromOneWorksheetToAnother.java" >}}

#### **結果 タスク 1:**

上記のコードを実行すると、ワークシート「Picture」の画像が最後のワークシート「Result」にコピーされます。

**ワークシート「結果」とコピーした写真**

![todo:画像_代替_文章](copy-shapes-between-worksheets_3.png)

### **タスク 2: あるワークシートから別のワークシートにグラフをコピーする**

#### **手順 1: あるワークシートから別のワークシートにグラフをコピーする**

以下は、コンポーネントがタスクを実行するために使用する実際のコードです。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyChartFromOneWorksheetToAnother-CopyChartFromOneWorksheetToAnother.java" >}}

#### **結果 タスク 2**

上記のコードを実行すると、ワークシート「Chart」のチャートがワークシート「Result」にコピーされます。結果のワークシートの次のスナップ ショットを参照してください。

**コピーした写真とチャートを含むワークシート「結果」**

![todo:画像_代替_文章](copy-shapes-between-worksheets_4.png)

### **タスク 3: あるワークシートから別のワークシートへのコントロールおよびその他の描画オブジェクトのコピー**

**テキストボックスと楕円形のワークシート「コントロール」**

![todo:画像_代替_文章](copy-shapes-between-worksheets_5.png)

目的の結果を得るために実行する必要がある次の簡単な手順を参照してください。

#### **ステップ 1: ワークブック間でワークシートをコピーする**

以下は、タスクを実行するためにコンポーネントによって使用されるコードです。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyWorksheetBetweenWorkbooks-CopyWorksheetBetweenWorkbooks.java" >}}

#### **結果 タスク 3**

上記のコードを実行すると、ワークシート「Control」のコントロールがワークシート「Result」にコピーされます。以下の「結果」のスナップショットをご覧ください。

**コピーされたテキストボックスと楕円形のワークシート「結果」**

![todo:画像_代替_文章](copy-shapes-between-worksheets_6.png)

## **結論**

この記事では、Aspose.Cells を使用して、写真、チャート、その他の描画オブジェクトなどのさまざまな図形をコピーする方法を示しました。うまくいけば、いくつかの洞察が得られ、さまざまなシナリオに従ってこれらのオプションを利用できるようになります。

Aspose.Cells は、他のソリューションよりも柔軟性が高く、特定のビジネス アプリケーション要件を満たすための卓越した速度、効率性、および信頼性を提供します。結果は、Aspose.Cells が何年にもわたる研究、設計、および慎重な調整の恩恵を受けていることを示しています。

ご質問、ご意見、ご提案をお待ちしております。[Aspose.Cells フォーラム](https://forum.aspose.com/c/cells/9).
