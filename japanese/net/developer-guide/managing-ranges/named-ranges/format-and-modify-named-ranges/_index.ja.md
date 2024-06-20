---
title: 名前付き範囲の書式および変更
type: docs
weight: 85
url: /ja/net/format-and-modify-named-ranges/
---

## **範囲の書式設定**

### **指定した範囲に背景色とフォント属性を設定する**

書式を適用するには、[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) オブジェクトを定義してスタイル設定を指定し、そのスタイルを[**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) オブジェクトに適用します。

次の例では範囲に実線の塗りつぶし色（シェーディング色）とフォント設定を設定する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges1-1.cs" >}}

### **名前付き範囲に境界線を追加する**

単一のセルではなく、セルの範囲に境界線を追加することが可能です。[**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) オブジェクトには、次のパラメータを取る[**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder) メソッドが提供され、セルの範囲に境界線を追加することができます：

- 境界線の種類、[**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype) 列挙型から選択される境界線の種類。
- ライン スタイル は [**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype) 列挙体から選択されます。
- カラー は Color 列挙体から選択されます。

次の例では、範囲にアウトラインボーダーを設定する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges2-1.cs" >}}

次の例では、範囲内の各セルに境界線を設定する方法を示します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SetBorderAroundEachCell-1.cs" >}}

## **名前付き範囲の名前を変更する**

Aspose.Cellsを使用して、必要に応じて名前付き範囲の名前を変更できます。名前付き範囲を取得して、[**Name.Text**](https://reference.aspose.com/cells/net/aspose.cells/name/properties/text) 属性を使用して名前を変更する方法を次の例で示します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RenameNamedRange-1.cs" >}}

## **範囲の合併**

Aspose.Cells は範囲の合併に使用する [**Range.Union**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/union) メソッドを提供しており、このメソッドは [*ArrayList*](https://docs.microsoft.com/en-gb/dotnet/api/system.collections.arraylist?view=netframework-4.8) オブジェクトを返します。次の例では、範囲の合併方法を示します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-UnionOfRanges-1.cs" >}}

## **範囲の交差**

Aspose.Cells は 2 つの範囲の交差を求めるための [**Range.Intersect**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect) メソッドを提供しており、このメソッドは [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) オブジェクトを返します。範囲が他の範囲と交差するかどうかを確認するには、ブール値を返す [**Range.Intersect**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect) メソッドを使用します。次の例では、範囲の交差方法を示します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IntersectionofRanges-1.cs" >}}

## **名前付き範囲内のセルの結合**

Aspose.Cells は範囲内のセルを結合するための [**Range.Merge()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge) メソッドを提供しています。次の例では、名前付き範囲内の個々のセルを結合する方法を示します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-MergeCellsInNamedRange-1.cs" >}}

## **ネームド レンジの削除**

Aspose.Cells は範囲の名前を消去するための [**NameCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/namecollection/methods/removeat) メソッドを提供しています。範囲の内容をクリアするには、[**Cells.ClearRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/clearrange/index) メソッドを使用します。次の例では、名前付き範囲とその内容を削除する方法を示します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RemoveANamedRange-1.cs" >}}
