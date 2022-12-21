---
title: 名前付き範囲の数式の設定
type: docs
weight: 20
url: /ja/net/setting-formula-for-named-range/
---
## **名前付き範囲の数式の設定**
Excel アプリケーションと同様に、Aspose.Cells API は、名前付き範囲の数式を指定する機能を提供します。[参照先](https://reference.aspose.com/cells/net/aspose.cells/range/properties/refersto)財産。この機能には多数のユーザビリティ シナリオが考えられますが、そのうちのいくつかを以下に詳しく説明します。
### **名前付き範囲の単純な式の設定**
単純な数式は、同じ (または異なる) ワークシート内の別のセルへの参照である可能性があります。次の例では、新しいスプレッドシートに名前付き範囲を作成し、その参照を別のセルに設定します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingSimpleFormula-SettingSimpleFormulaForNamedRanges.cs" >}}
### **名前付き範囲の複雑な数式の設定**
複雑な数式は、ダイナミック レンジや、異なるワークシートの複数のセルにまたがる数式など、あらゆるものである可能性があります。次の例では、INDEX 関数を使用して動的範囲を作成し、その場所に基づいてリストから値を取得します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingComplexFormula-SettingComplexFormulaNamedRange.cs" >}}



名前付き範囲を使用して、異なるワークシートの 2 つのセルの値を合計する別の例を次に示します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CalculatingSumUsingNamedRange-CalculatingSumUsingNamedRangeOnDifferentSheets.cs" >}}
