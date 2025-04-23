---
title: 名前付き範囲の式の設定
type: docs
weight: 20
url: /ja/python-net/setting-formula-for-named-range/
---

## **名前付き範囲の式の設定**
Excelアプリケーションと同様に、Aspose.Cells for Python via .NET APIは、名前付き範囲に対して式を指定する機能を提供します。これは[**Range.refers_to**](https://reference.aspose.com/cells/python-net/aspose.cells/range/refers_to)プロパティを使用します。多くの利用シナリオが考えられ、その一部を以下に示します。
### **名前付き範囲に簡単な式を設定する**
簡単な式は、同じワークシート（または異なるワークシート）内の別のセルへの参照である場合があります。次の例は、新しいスプレッドシートで名前付き範囲を作成し、その参照先を別のセルに設定します。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SettingSimpleFormulaForNamedRanges.py" >}}
### **名前付き範囲に複雑な式を設定する**
複雑な式は、動的な範囲や異なるワークシートの複数のセルにまたがる式など、さまざまなものになります。次の例は、INDEX 関数を使用して、リスト内の位置に基づいて値を取得する動的な範囲を作成します。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SettingComplexFormulaNamedRange.py" >}}



異なるワークシートの2つのセルから値を合計する名前付き範囲を使用するもう1つの例がこちら



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-CalculatingSumUsingNamedRangeOnDifferentSheets.py" >}}
