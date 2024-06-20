---
title: 共有式数式の設定
type: docs
weight: 10
url: /ja/net/setting-shared-formula/
---

{{% alert color="primary" %}}

ワークシートに計算を行う関数を追加したい場合があります。この記事では、Aspose.Cellsを使用してこのタスクを達成する方法について説明します。

{{% /alert %}}

## Aspose.Cellsを使用した共有式の設定

次のサンプルワークシートのようなデータで満たされたワークシートがあるとします。

|**1 列またはデータを持つ入力ファイル**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

B2に関数を追加し、最初のデータ行の売上税を計算したいとします。税金は9%です。売上税を計算する式は次のとおりです:"=A2*0.09"。この記事では、Aspose.Cellsでこの式を適用する方法について説明します。

Aspose.Cellsを使用すると、[**Cell.Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) プロパティを使用して式を指定できます。その他のセル（B3、B4、B5など）に式を追加するためには、2つのオプションがあります。

最初のセルに対して行ったことを他のセルに対しても行い、セル参照を適切に更新することによって、各セルのために式を設定します（A3*0.09、A4*0.09、A5*0.09など）。これには各行のセル参照を更新する必要があります。また、Aspose.Cellsはそれぞれの式を個別に解析する必要がありますが、これは大規模なスプレッドシートや複雑な式に対して時間がかかる場合があります。また、余分な行数が追加されますが、ループを使用することでそれらを削減することができます。

もう1つの方法は、**共有式**を使用することです。共有式を使用すると、式は各行のセル参照に自動的に更新されるため、税金が正しく計算されます。[**Cell.SetSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setsharedformula/index) メソッドは、最初の方法よりも効率的です。

次の例では、その使用方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingSharedFormula-1.cs" >}}
