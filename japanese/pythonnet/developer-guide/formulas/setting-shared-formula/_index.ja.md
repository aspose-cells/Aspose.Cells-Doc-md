---
title: 共有式数式の設定
type: docs
weight: 10
url: /ja/python-net/setting-shared-formula/
---

{{% alert color="primary" %}}

ワークシートに計算を行う関数を追加したい場合に、この方法をAspose.Cells for Python via .NETを使って実現する方法を説明します。

{{% /alert %}}

## Aspose.Cells for Python via .NET を使った共有式の設定

次のサンプルワークシートのようなデータで満たされたワークシートがあるとします。

|**1 列またはデータを持つ入力ファイル**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

B2に関数を追加して、最初のデータ行の売上税を計算したい場合。税率は**9%**です。売上税を計算する式は：**"=A2*0.09"**です。この方法をAspose.Cells for Python via .NETを使って適用する方法を説明します。

Aspose.Cells for Python via .NETでは、[**Cell.formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/formula)プロパティを使用して式を指定できます。他のセル（B3、B4、B5など）に式を追加する2つの方法があります。

最初のセルに対して行った方法と同様に、各セルに式を設定し、セル参照を適宜更新します（A3*0.09、A4*0.09、A5*0.09など）。これには各行のセル参照を更新する必要があります。また、Aspose.Cells for Python via .NETは各式を個別に解析する必要があり、特に大規模なスプレッドシートや複雑な式の場合、時間がかかることがあります。ループを使えばある程度短縮できますが、コードが増えます。

もう1つの方法は、**共有式**を使用することです。共有式を使用すると、式は各行のセル参照に自動的に更新されるため、税金が正しく計算されます。[**Cell.set_shared_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_shared_formula) メソッドは、最初の方法よりも効率的です。

次の例では、その使用方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SettingSharedFormula-1.py" >}}

