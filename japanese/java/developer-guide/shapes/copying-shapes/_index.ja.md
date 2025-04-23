---
title: ワークシート間でシェイプをコピーする
type: docs
weight: 250
url: /ja/java/copy-shapes-between-worksheets/
---

{{% alert color="primary" %}}

時には、異なる画像やチャート、およびその他の図形をワークシート間で必要に応じてコピーする必要があります。Aspose.Cellsは、ワークシート間で図形をコピーする機能をサポートしています。チャート、画像、およびその他のオブジェクトは、最高水準の精度でコピーされます。

Office Automationを試してみることもできますが、それには独自の欠点があります。たとえば、セキュリティ、安定性、スケーラビリティ、速度、価格、機能など、さまざまな理由や問題が関与しています。要するに、Microsoft自体もOfficeの自動化を強く推奨していません。

この記事では、Aspose.Cellsを使用して数行の簡単なコードで、ワークブックのワークシート間で画像やチャート、およびその他の図形をコピーする方法について説明します。

この文書は、開発者に対して、ワークシート間で図形（画像、チャート、コントロール、およびその他の図形オブジェクト）をコピーする方法について詳細に理解を提供するように設計されています。

{{% /alert %}}

## **図形のコピー**

この記事では以下の方法について説明します:

- [ワークシートから別のワークシートへの画像のコピー](/cells/ja/java/copy-shapes-between-worksheets/#copying-a-picture-from-one-worksheet-to-another)。
- [ワークシートから別のワークシートへのチャートのコピー](/cells/ja/java/copy-shapes-between-worksheets/#task-2-copying-a-chart-from-one-worksheet-to-another)。
- [ワークシートから別のワークシートへのコントロールやその他の図形オブジェクトのコピー](/cells/ja/java/copy-shapes-between-worksheets/#task-3-copying-controls-and-other-drawing-objects-from-one-worksheet-to-another)。

### **ワークシート間での画像のコピー**

#### **ステップ1: Microsoft Excelで画像とチャートが含まれたワークブックの作成**

1. Microsoft Excelで新しいワークブックを作成しました。
1. 最初のワークシートに写真を追加し、2番目のワークシートにグラフを追加します。

   次のスクリーンショットは、Microsoft Excelで作成された2つのテンプレートワークシートを示しています。

   **グラフがある「チャート」というワークシート**

![todo:image_alt_text](copy-shapes-between-worksheets_1.png)

**写真がある「ピクチャ」というワークシート**

![todo:image_alt_text](copy-shapes-between-worksheets_2.png)

そして、ワークシート「ピクチャ」から写真を最後のワークシート「結果」にコピーします。

#### **ステップ2：Aspose.Cells.Zipとしてダウンロード**

1. [Aspose.Cells for Javaをダウンロード](https://downloads.aspose.com/cells/java)します。
1. 開発コンピュータにそれを解凍します。

   すべての[Aspose](http://www.aspose.com/)コンポーネントは、インストールされると評価モードで動作します。評価モードには時間制限がなく、生成された文書にウォーターマークしか挿入されません。

#### **ステップ3：プロジェクトの作成**

たとえばEclipseのようなJavaエディタを使用してプロジェクトを作成するか、NotePadを使用して簡単なプログラムを作成することができます。

#### **ステップ4：クラスパスの追加**

Eclipseを使用してクラスパスを設定するには、次の手順を実行します。

1. Aspose.Cells.zipからAspose.Cells.jarとdom4j_1.6.1.jarを抽出します。
1. Eclipseでプロジェクトのクラスパスを設定します。
1. Eclipseでプロジェクトを選択し、[プロジェクト] - [プロパティ]メニューをクリックします。
1. ポップアップウィンドウの左側で「Javaビルドパス」を選択し、[ライブラリ]タブを選択し、「JARの追加」または「外部JARの追加」をクリックして、Aspose.Cells.jarおよびdom4j_1.6.1.jarを選択し、それらをビルドパスに追加します。
1. AsposeのコンポーネントのAPIを呼び出すアプリケーションを作成します。

または、WindowsのDOSプロンプトで実行時に設定することもできます。たとえば：

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; ClassName

#### **ステップ5：ワークシート間での写真のコピー**

次に示すコードは、タスクを達成するためのものです。これにより、「ピクチャ」というワークシートから「結果」というワークシートに写真がコピーされます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyPicturefromOneWorksheetToAnother-CopyPicturefromOneWorksheetToAnother.java" >}}

#### **タスク1の結果：**

上記のコードを実行した後、ワークシート「ピクチャ」から写真が最後のワークシート「結果」にコピーされます。

**コピーされた写真がある「結果」というワークシート**

![todo:image_alt_text](copy-shapes-between-worksheets_3.png)

### **タスク2：ワークシート間でのグラフのコピー**

#### **ステップ1：ワークシート間でグラフをコピー**

次に示すのは、コンポーネントがタスクを達成するために使用した実際のコードです。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyChartFromOneWorksheetToAnother-CopyChartFromOneWorksheetToAnother.java" >}}

#### **タスク2の結果**

上記のコードを実行した後、ワークシート「チャート」からグラフが「結果」というワークシートにコピーされます。結果のワークシートのスナップショットは以下の通りです。

**コピーされた写真とグラフがある「結果」というワークシート**

![todo:image_alt_text](copy-shapes-between-worksheets_4.png)

### **タスク3：ワークシート間のコントロールやその他の図形オブジェクトのコピー**

**テキストボックスと楕円形がある「コントロール」というワークシート**

![todo:image_alt_text](copy-shapes-between-worksheets_5.png)

以下は、望ましい結果を得るために実行する必要がある簡単な手順です。

#### **ステップ1：ワークブック間でワークシートをコピー**

次に示すのは、コンポーネントがタスクを達成するために使用したコードです。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyWorksheetBetweenWorkbooks-CopyWorksheetBetweenWorkbooks.java" >}}

#### **タスク3の結果**

上記のコードを実行した後、ワークシート「Control」からコントロールがワークシート「Result」にコピーされました。「Result」のスナップショットを以下にご覧ください。

コピーされたテキストボックスと楕円がある「Result」というワークシート

![todo:image_alt_text](copy-shapes-between-worksheets_6.png)

## **結論**

この記事では、Aspose.Cellsを使用して画像、グラフ、およびその他の図形オブジェクトをコピーする方法を示しました。おそらく、これによりいくつかの洞察を得て、さまざまなシナリオに応じてこれらのオプションを利用することができるでしょう。

Aspose.Cellsは解決策に対して他よりも柔軟性を提供し、特定のビジネスアプリケーション要件を満たすために優れた速度、効率性、信頼性を提供します。結果は、Aspose.Cellsが長年の研究、設計、注意深い調整の成果を得たことを示しています。

[Aspose.Cellsフォーラム](https://forum.aspose.com/c/cells/9)でのお問い合わせ、コメント、提案を心より歓迎します。
{{< app/cells/assistant language="java" >}}
