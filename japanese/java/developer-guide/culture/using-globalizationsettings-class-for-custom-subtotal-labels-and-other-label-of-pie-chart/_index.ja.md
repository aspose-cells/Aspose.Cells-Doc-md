---
title: ピーグラフのカスタムサブトータルラベルおよびその他のラベル用のGlobalizationSettingsクラスの使用
type: docs
weight: 50
url: /ja/java/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---

## **可能な使用シナリオ**
Aspose.CellsのAPIは、スプレッドシートでサブトータルのカスタムラベルを使用したい場合に[GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings)クラスを公開しています。さらに、[GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings)クラスを使用して、ワークシートやグラフで**Other**ラベルを変更することもできます。
## **GlobalizationSettingsクラスの紹介**
[GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings)クラスは現在、以下の3つのメソッドを提供しており、これらはカスタムクラスでオーバーライドし、サブトータルのために望ましいラベルを取得するために使用することができます。また、円グラフの**Other**ラベルに対してカスタムテキストをレンダリングすることもできます。

1. [GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName\(int\)): 関数の合計名を取得します。
1. [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName\(int\)): 関数の総合計名を取得します。
1. [GlobalizationSettings.getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\)): 円グラフの「その他」ラベルの名前を取得します。
### **サブトータルのカスタムラベル**
[GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) クラスを使用して、[GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName\(int\)) と [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName\(int\)) メソッドを上書きして小計のラベルをカスタマイズできます。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


カスタムラベルを追加するには、小計をワークシートに追加する前に、[WorkbookSettings.GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) プロパティに先ほど定義した *CustomSettings* クラスのインスタンスを割り当てる必要があります。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomLabelsforSubtotals-CustomLabelsforSubtotals.java" >}}

{{% alert color="primary" %}} 

小計を追加する際にのみ、既存のスプレッドシートに小計が含まれている場合、そのラベルを変更することはできません。

{{% /alert %}} 
### **円グラフの他のラベルのカスタムテキスト**
[GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) クラスは、円グラフの「その他」ラベルにカスタム値を与えるのに役立つ [getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\)) メソッドを提供します。以下のスニペットは、デフォルトの言語設定に基づいてカスタムラベルを取得するために、カスタムクラスを定義し [getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\)) メソッドを上書きしています。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


既存のスプレッドシートを読み込み、*CustomSettings* クラスを利用してワークブックの [WorkbookSettings.GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) プロパティに割り当て、円グラフを画像としてレンダリングする以下のスニペットです。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomTextforOtherLabelofPieChart-CustomTextforOtherLabelofPieChart.java" >}}


マシンのロケールがフランスに設定されている場合の結果画像は以下の通りです。*CustomSettings* クラスで定義したように、「その他」ラベルは「Autre」に翻訳されていることがわかります。

![todo:image_alt_text](using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart_1.png)
