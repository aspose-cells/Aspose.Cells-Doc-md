---
title: ワークシートに条件付き書式設定を適用する
type: docs
weight: 40
url: /ja/java/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

この記事では、ワークシートのセル範囲に条件付き書式設定を追加する方法について詳しく説明しています。

条件付き書式設定は、Microsoft Excelの高度な機能であり、セルの値や数式の値に応じて書式を適用し、その書式を変更することを可能にします。たとえば、セルの背景が赤くなるとマイナスの値が強調表示されたり、テキストの色が緑色になるとプラスの値が強調表示されます。セルの値が条件を満たしている場合、書式が適用されます。セルの値が条件を満たしていない場合、セルのデフォルトの書式が使用されます。

Microsoft Office Automationで条件付き書式設定を適用することは可能ですが、その欠点があります。たとえば、セキュリティ、安定性、拡張性、速度などの理由や問題が存在します。他のソリューションを探す主な理由は、Microsoft自体がソフトウェアソリューション向けにOffice Automationを強く推奨していないことです。

この記事では、Aspose.Cells APIを使用して、わずか数行のコードでセルに条件付き書式設定を追加するコンソールアプリケーションを作成する方法を示しています。

{{% /alert %}}

## **条件付き書式を使用する**

この記事は、以下のタスクを実行します：

1. [Aspose.Cellsを使用してセルの値に基づいて条件付き書式を適用する](/cells/ja/java/apply-conditional-formatting-in-worksheets/#task-1-using-asposecells-to-apply-conditional-formatting-based-on-cell-value)。
1. [Aspose.Cellsを使用して数式に基づいて条件付き書式を適用する](/cells/ja/java/apply-conditional-formatting-in-worksheets/#task-2-using-asposecells-to-apply-conditional-formatting-based-on-a-formula)。

### **タスク1: Aspose.Cellsを使用してセルの値に基づいて条件付き書式を適用する**

1. **Aspose.Cells.zipをダウンロードしてインストールします**：
   1. [ダウンロード](https://downloads.aspose.com/cells/java) Aspose.Cells for Java。
   1. 開発コンピュータにそれを解凍します。
      全てのAsposeコンポーネントは、インストールされると評価モードで動作します。評価モードには時間制限はなく、生成されたドキュメントにウォーターマークが挿入されます。
1. **プロジェクトを作成します**。
   EclipseなどのJavaエディタを使用してプロジェクトを作成するか、テキストエディタを使用してシンプルなプログラムを作成します。
1. **クラスパスを追加します**。
   Eclipseを使用してクラスパスを設定するには、次の手順を実行します。
   1. Aspose.Cells.zipからAspose.Cells.jarとdom4j_1.6.1.jarを抽出します。
   1. Eclipseでプロジェクトのクラスパスを設定します。
      1. Eclipseでプロジェクトを選択し、**Project**メニューから**Properties**を選択します。
      1. ダイアログの左側で **Java Build Path** を選択します。
      1. **Libraries**タブで、**Add JARs** または **Add External JARs** を選択して、Aspose.Cells.jar と dom4j_1.6.1.jar を選択し、ビルドパスに追加します。
   1. AsposeのコンポーネントのAPIを呼び出すアプリケーションを作成します。
      または、WindowsのDOSプロンプトで実行時にパスを設定することもできます。

{{< highlight java >}}

  javac -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName  

{{< /highlight >}}

1. セルの値に基づいて条件付き書式を適用します**。
   以下は、コンポーネントがタスクを達成するために使用したコードです。それはセルに条件付き書式を適用します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingOnCellValue-ApplyConditionalFormattingOnCellValue.java" >}}

上記のコードを実行すると、出力ファイル（output.xls）の最初のワークシートのA1セルに条件付き書式が適用されます。A1のセル値に依存して条件付き書式が適用されます。A1のセル値が50から100の間である場合、条件付き書式により背景色が赤になります。生成されたXLSファイルのスクリーンショットを参照してください。

**A1の値が50未満の出力Excelファイル**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_1.png)

**A1が50から100の間の出力Excelファイル**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_2.png)

### **タスク2: Aspose.Cellsを使用して数式に基づいて条件付き書式を適用する**

1. **数式に応じて条件付き書式を適用します**。
   以下は、コンポーネントがタスクを達成するために使用した実際のコードです。それは「B3」に条件付き書式を適用します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingBasedOnFormula-ConditionalFormattingBasedOnFormula.java" >}}

上記のコードを実行すると、出力ファイル（output.xls）の最初のワークシートのB3セルに条件付き書式が適用されます。適用される条件付き書式は、B1とB2の合計を計算する数式に依存します。生成されたXLSファイルのスクリーンショットをご覧ください。

**B3の値が100未満の出力Excelファイル**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_3.png)

**B3が100を超える出力Excelファイル**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_4.png)

### **結論**

{{% alert color="primary" %}}

この記事では、Aspose.Cells APIを使用してワークシート内のセルに条件付き書式を適用する方法を示しています。おそらく、自分自身のシナリオでこれらのオプションを使用できるようになる洞察を得ることができるでしょう。

Aspose.Cellsは解決策に対する大きな柔軟性を提供し、特定のビジネスアプリケーションの要件を満たすための優れた速度、効率、信頼性を提供しています。Aspose.Cellsは、長年の研究、設計、慎重な調整から利益を得ています。

Aspose.Cellsフォーラムでのお問い合わせ、コメント、提案を歓迎します。迅速な回答を保証します。[Aspose.Cells Forum](https://forum.aspose.com/c/cells/9)

{{% /alert %}}
