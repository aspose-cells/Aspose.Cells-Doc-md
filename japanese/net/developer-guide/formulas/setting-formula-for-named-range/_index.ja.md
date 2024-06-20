---
title: 名前付き範囲の式の設定
type: docs
weight: 20
url: /ja/net/setting-formula-for-named-range/
---

## **名前付き範囲の式の設定**
Aspose.CellsのAPIは、参照先プロパティを使用して、名前付き範囲の式を指定する機能を提供します。この機能には多くの使用シナリオがあり、そのうちのいくつかは以下に詳細に記載されています。
### **名前付き範囲に簡単な式を設定する**
簡単な式は、同じワークシート（または異なるワークシート）内の別のセルへの参照である場合があります。次の例は、新しいスプレッドシートで名前付き範囲を作成し、その参照先を別のセルに設定します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingSimpleFormula-SettingSimpleFormulaForNamedRanges.cs" >}}
### **名前付き範囲に複雑な式を設定する**
複雑な式は、動的な範囲や異なるワークシートの複数のセルにまたがる式など、さまざまなものになります。次の例は、INDEX 関数を使用して、リスト内の位置に基づいて値を取得する動的な範囲を作成します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingComplexFormula-SettingComplexFormulaNamedRange.cs" >}}



異なるワークシートの2つのセルから値を合計する名前付き範囲を使用するもう1つの例がこちら



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CalculatingSumUsingNamedRange-CalculatingSumUsingNamedRangeOnDifferentSheets.cs" >}}
