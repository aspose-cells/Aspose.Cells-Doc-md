---
title: 共有式の設定
type: docs
weight: 10
url: /ja/net/setting-shared-formula/
---
{{% alert color="primary" %}}

いくつかの計算を行う関数をワークシートに追加したい場合。この記事では、Aspose.Cells を使用してこのタスクを達成する方法について説明します。

{{% /alert %}}

## Aspose.Cells を使用して共有数式を設定する

次のサンプル ワークシートのような形式のデータが入力されたワークシートがあるとします。

|**1 つの列またはデータを含む入力ファイル**|
|:- |
|![todo:画像_代替_文章](setting-shared-formula_1.png)|

データの最初の行の消費税を計算する関数を B2 に追加します。税金は**9%**.売上税を計算する式は次のとおりです。**「=A2*0.09」**.この記事では、この式を Aspose.Cells に適用する方法について説明します。

 Aspose.Cells を使用すると、式を指定できます[**Cell.Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula)財産。列の他のセル (B3、B4、B5 など) に数式を追加するには、2 つのオプションがあります。

最初のセルに対して行ったことを実行し、各セルの数式を効果的に設定し、それに応じてセル参照を更新します (A3*0.09、A4*0.09、A5*0.09 など)。これには、各行のセル参照を更新する必要があります。また、各数式を個別に解析するには Aspose.Cells が必要です。これは、大規模なスプレッドシートや複雑な数式では時間がかかる可能性があります。また、コードの余分な行を追加しますが、ループを使用すると多少削減できます。

別のアプローチは、**共有式**.共有数式を使用すると、税金が適切に計算されるように、各行のセル参照の数式が自動的に更新されます。の[**Cell.SetSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setsharedformula/index)この方法は、最初の方法よりも効率的です。

次の例は、その使用方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingSharedFormula-1.cs" >}}
