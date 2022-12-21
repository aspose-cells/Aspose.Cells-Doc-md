---
title: 共有式の設定
type: docs
weight: 10
url: /ja/java/setting-shared-formula/
---
{{% alert color="primary" %}} 

次のサンプル ワークシートのような形式のデータが入力されたワークシートがあるとします。

**1 つの列またはデータを含む入力ファイル** 

![todo:画像_代替_文章](setting-shared-formula_1.png)

データの最初の行の消費税を計算する関数を B2 に追加します。税金は**9%**.売上税を計算する式は次のとおりです。**「=A2*0.09」**.この記事では、この式を Aspose.Cells に適用する方法について説明します。

{{% /alert %}} 

 Aspose.Cells を使用すると、式を指定できます[Cell.Formula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)プロパティ、具体的には[Cell.set式()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)と[Cell.get式()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula).

列の他のセル (B3、B4、B5 など) に数式を追加するには、2 つのオプションがあります。

最初のセルに対して行ったことを実行し、各セルの数式を効果的に設定し、それに応じてセル参照を更新します (A3*0.09、A4*0.09、A5*0.09 など)。これには、各行のセル参照を更新する必要があります。また、各数式を個別に解析するには Aspose.Cells が必要です。これは、大規模なスプレッドシートや複雑な数式では時間がかかる可能性があります。また、コードの余分な行を追加しますが、ループを使用すると多少削減できます。

別のアプローチは、**共有式**.共有数式を使用すると、税金が適切に計算されるように、各行のセル参照の数式が自動的に更新されます。の[Cell.setSharedFormula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setSharedFormula\(java.lang.String,%20int,%20int\)メソッドは、最初のメソッドよりも効率的です。

次の例は、その使用方法を示しています。以下のスクリーンショットは、出力ファイルを示しています。

**出力ファイル: 共有数式を適用** 

![todo:画像_代替_文章](setting-shared-formula_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingSharedFormula-SettingSharedFormula.java" >}}
