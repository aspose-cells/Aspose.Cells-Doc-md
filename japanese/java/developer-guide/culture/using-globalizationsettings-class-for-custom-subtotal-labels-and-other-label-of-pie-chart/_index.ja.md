---
title: カスタム小計ラベルおよび円グラフのその他のラベルに GlobalizationSettings クラスを使用する
type: docs
weight: 50
url: /ja/java/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---
## **考えられる使用シナリオ**
 Aspose.Cells API が[グローバリゼーション設定](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings)クラスを使用して、ユーザーがスプレッドシートの小計にカスタム ラベルを使用したいシナリオに対処します。さらに、[グローバリゼーション設定](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings)クラスを使用して変更することもできます**他の**ワークシートまたはグラフのレンダリング中の円グラフのラベル。
## **GlobalizationSettings クラスの紹介**
の[グローバリゼーション設定](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings)クラスは現在、カスタム クラスでオーバーライドして、小計の目的のラベルを取得したり、**他の**円グラフのラベル。

1. [GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName\(int\)): 関数の完全な名前を取得します。
1. [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName\(int\)): 関数の総計名を取得します。
1. [GlobalizationSettings.getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\)): 円グラフの「その他」ラベルの名前を取得します。
### **小計のカスタム ラベル**
の[グローバリゼーション設定](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings)クラスをオーバーライドして、小計ラベルをカスタマイズするために使用できます。[GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName\(int\)) & [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName\(int\)) メソッドは先に示したとおりです。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


カスタム ラベルを挿入するには、[WorkbookSettings.GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings)のインスタンスへのプロパティ*カスタム設定*小計をワークシートに追加する前に、上で定義したクラス。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomLabelsforSubtotals-CustomLabelsforSubtotals.java" >}}

{{% alert color="primary" %}} 

の[グローバリゼーション設定](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings)クラスは、新しい小計を追加する場合にのみ機能します。スプレッドシートにすでに小計が含まれている場合、そのラベルは変更できません。

{{% /alert %}} 
### **円グラフの他のラベルのカスタム テキスト**
の[グローバリゼーション設定](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings)クラスが提供する[getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\) ) 円グラフの「その他」ラベルにカスタム値を与えるのに役立つメソッド。次のスニペットは、カスタム クラスを定義し、[getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\)) メソッドを使用して、JVM のデフォルト言語セットに基づいてカスタム ラベルを取得します。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


次のスニペットは、円グラフを含む既存のスプレッドシートを読み込み、グラフを画像にレンダリングします。*カスタム設定*上記で作成したクラス。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomTextforOtherLabelofPieChart-CustomTextforOtherLabelofPieChart.java" >}}


以下は、マシンのロケールがフランスに設定されている場合の結果のイメージです。で定義されているように、ラベル「Other」が「Autre」に変換されていることがわかります。*カスタム設定*クラス。

![todo:画像_代替_文章](using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart_1.png)
