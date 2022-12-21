---
title: ワークシートに条件付き書式を適用する
type: docs
weight: 40
url: /ja/java/apply-conditional-formatting-in-worksheets/
---
{{% alert color="primary" %}}

この記事は、ワークシートのセル範囲に条件付き書式を追加する方法を詳しく説明することを目的としています。

条件付き書式は Microsoft Excel の高度な機能で、セルの範囲に書式を適用し、セルの値または数式の値に応じて書式を変更できます。たとえば、セルの背景を赤色にして負の値を強調したり、テキストの色を緑色にして正の値にしたりすることができます。セルの値がフォーマット条件を満たしている場合、フォーマットが適用されます。セルの値がフォーマット条件を満たさない場合、セルのデフォルトのフォーマットが使用されます。

Microsoft Office Automation で条件付き書式を適用することは可能ですが、これには欠点があります。関連する理由と問題はいくつかあります。たとえば、セキュリティ、安定性、スケーラビリティ、速度などです。別のソリューションを見つける主な理由は、Microsoft 自身がソフトウェア ソリューションに Office Automation を使用しないことを強く推奨しているためです。

この記事では、コンソール アプリケーションを作成し、Aspose.Cells API.

{{% /alert %}}

## **条件付き書式の操作**

この記事では、次のタスクを実行します。

1. [Aspose.Cells を使用して、セル値に基づいて条件付き書式を適用する](/cells/ja/java/apply-conditional-formatting-in-worksheets/#task-1-using-asposecells-to-apply-conditional-formatting-based-on-cell-value).
1. [Aspose.Cells を使用して、数式に基づいて条件付き書式を適用する](/cells/ja/java/apply-conditional-formatting-in-worksheets/#task-2-using-asposecells-to-apply-conditional-formatting-based-on-a-formula).

### **タスク 1: Aspose.Cells を使用して、Cell の値に基づいて条件付き書式を適用する**

1. **Aspose.Cells.zip をダウンロードしてインストールします**:
   1. [ダウンロード](https://downloads.aspose.com/cells/java) Aspose.Cells for Java.
1. 開発用コンピューターで解凍します。
 Aspose コンポーネントはすべて、インストールすると評価モードで動作します。評価モードには時間制限がなく、生成されたドキュメントに透かしを挿入するだけです。
1. **プロジェクトを作成する**.
Eclipse などの Java エディターを使用してプロジェクトを作成するか、テキスト エディターを使用して簡単なプログラムを作成します。
1. **クラスパスを追加**.
Eclipse を使用してクラス パスを設定するには、次の手順を実行してください。
1. Aspose.Cells.zip から Aspose.Cells.jar と dom4j_1.6.1.jar を抽出します。
 1. Eclipse でプロジェクトのクラスパスを設定します。
 1. Eclipse でプロジェクトを選択し、**プロパティ**から**計画**メニュー。
1. ダイアログの左側にある [Java Build Path] を選択します。
 1.**ライブラリ**タブ、選択**JAR を追加する**また**外部 JAR を追加する**Aspose.Cells.jar と dom4j_1.6.1.jar を選択してビルド パスに追加します。
 1. Aspose のコンポーネントの API を呼び出すアプリケーションを作成します。
または、Windows の DOS プロンプトで実行時にパスを設定することもできます。

{{< highlight "java" >}}

  javac -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName  

{{< /highlight >}}

1. **セル値に基づいて条件付き書式を適用する**.
以下は、タスクを実行するためにコンポーネントによって使用されるコードです。セルに条件付き書式を適用します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingOnCellValue-ApplyConditionalFormattingOnCellValue.java" >}}

上記のコードを実行すると、出力ファイル (output.xls) の最初のワークシートのセル「A1」に条件付き書式が適用されます。 A1 に適用される条件付き書式は、セルの値によって異なります。 A1 のセル値が 50 ～ 100 の場合、条件付き書式が適用されているため、背景色は赤になります。生成された XLS ファイルの次のスクリーンショットを参照してください。

**A1 値が 50 未満の Excel ファイルを出力する**

![todo:画像_代替_文章](apply-conditional-formatting-in-worksheets_1.png)

**A1 が 50 ～ 100 の Excel ファイルを出力する**

![todo:画像_代替_文章](apply-conditional-formatting-in-worksheets_2.png)

### **タスク 2: Aspose.Cells を使用して、数式に基づいて条件付き書式を適用する**

1. **数式に応じて条件付き書式を適用する**.
以下は、コンポーネントがタスクを実行するために使用する実際のコードです。 「B3」に条件付き書式を適用します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingBasedOnFormula-ConditionalFormattingBasedOnFormula.java" >}}

上記のコードを実行すると、出力ファイル（output.xls）の最初のワークシートのセル「B3」に条件付き書式が適用されます。適用される条件付き書式は、「B3」の値を B1 と B2 の合計として計算する式によって異なります。生成された XLS ファイルの次のスクリーンショットを参照してください。

**B3 値が 100 未満の Excel ファイルを出力する**

![todo:画像_代替_文章](apply-conditional-formatting-in-worksheets_3.png)

**B3 が 100 より大きい出力 Excel ファイル**

![todo:画像_代替_文章](apply-conditional-formatting-in-worksheets_4.png)

### **結論**

{{% alert color="primary" %}}

この記事では、Aspose.Cells API を使用してワークシート内のセルに条件付き書式を適用する方法を示します。これらのオプションを独自のシナリオで使用できるようになることを願っています。

Aspose.Cells は、ソリューションに優れた柔軟性を提供し、特定のビジネス アプリケーション要件を満たす卓越した速度、効率、および信頼性を提供します。 Aspose.Cells は、長年にわたる研究、設計、慎重なチューニングの恩恵を受けています。

ご質問、ご意見、ご提案は、[Aspose.Cells フォーラム](https://forum.aspose.com/c/cells/9).迅速な返信をお約束します。

{{% /alert %}}
