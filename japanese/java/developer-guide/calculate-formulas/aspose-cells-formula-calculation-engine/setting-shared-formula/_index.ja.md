---
title: 共有式数式の設定
type: docs
weight: 10
url: /ja/java/setting-shared-formula/
---

{{% alert color="primary" %}} 

次のサンプルワークシートのようなデータで満たされたワークシートがあるとします。

1列分またはデータを含んだ入力ファイル 

![todo:image_alt_text](setting-shared-formula_1.png)

B2に関数を追加し、最初のデータ行の売上税を計算したいとします。税金は9%です。売上税を計算する式は次のとおりです:"=A2*0.09"。この記事では、Aspose.Cellsでこの式を適用する方法について説明します。

{{% /alert %}} 

Aspose.Cellsを使用すると、[Cell.Formula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)プロパティを使用して式を指定できます。具体的には、[Cell.setFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)および[Cell.getFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)を使用します。

列の他のセル（B3、B4、B5など）に数式を追加するための2つのオプションがあります。

最初のセルに対して行ったことをその他のセル（A3*0.09、A4*0.09、A5*0.09など）に対して行い、それぞれの行のセル参照を更新するという方法があります。これには各行のセル参照の更新が必要です。また、Aspose.Cellsは個々の数式を解析する必要があり、大きなスプレッドシートや複雑な数式の場合には時間がかかる可能性があります。また、ループを使用してコード行を削減できますが、追加のコード行が追加されます。

別のアプローチとして、**共有式**を使用する方法があります。共有式を使用すると、各行のセル参照に対して数式が自動的に更新されるため、税金が適切に計算されます。[Cell.setSharedFormula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setSharedFormula\(java.lang.String,%20int,%20int\))メソッドは、最初の方法よりも効率的です。

次の例では、その使用方法を示しています。スクリーンショットは、出力ファイルを示しています。

出力ファイル：共有式が適用された 

![todo:image_alt_text](setting-shared-formula_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingSharedFormula-SettingSharedFormula.java" >}}
