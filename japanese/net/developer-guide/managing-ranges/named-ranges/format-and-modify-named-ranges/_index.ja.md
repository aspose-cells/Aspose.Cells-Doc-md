---
title: 名前付き範囲の書式設定と変更
type: docs
weight: 85
url: /ja/net/format-and-modify-named-ranges/
---
## **フォーマット範囲**

### **背景色とフォント属性を名前付き範囲に設定する**

フォーマットを適用するには、[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)オブジェクトを使用してスタイル設定を指定し、[**範囲**](https://reference.aspose.com/cells/net/aspose.cells/range)物体。

次の例は、フォント設定で塗りつぶしの塗りつぶし色 (シェーディング色) を範囲に設定する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges1-1.cs" >}}

### **名前付き範囲に境界線を追加する**

 つのセルだけでなく、セル範囲に罫線を追加することもできます。の[**範囲**](https://reference.aspose.com/cells/net/aspose.cells/range)オブジェクトは[**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder)次のパラメーターを使用して、セル範囲に境界線を追加するメソッド:

- 枠線の種類、枠線の種類で、[**ボーダータイプ**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)列挙。
- ライン スタイル、ライン スタイル、から選択[**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)列挙。
- Color 列挙体から選択された色、線の色。

次の例は、アウトラインの境界線を範囲に設定する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges2-1.cs" >}}

次の例は、範囲内の各セルの周囲に境界線を設定する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SetBorderAroundEachCell-1.cs" >}}

## **名前付き範囲の名前を変更する**

Aspose.Cells を使用すると、必要に応じて名前付き範囲の名前を変更できます。名前付き範囲を取得し、名前を変更するには、[**名前.テキスト**](https://reference.aspose.com/cells/net/aspose.cells/name/properties/text)属性。次の例は、名前付き範囲の名前を変更する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RenameNamedRange-1.cs" >}}

## **範囲の連合**

Aspose.Cells提供[**範囲.ユニオン**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/union)メソッドが範囲の結合を取る場合、メソッドは[*配列リスト*](https://docs.microsoft.com/en-gb/dotnet/api/system.collections.arraylist?view=netframework-4.8)物体。次の例は、範囲のユニオンを取る方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-UnionOfRanges-1.cs" >}}

## **範囲の交差**

Aspose.Cells は[**Range.Intersect**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect) 2 つの範囲を交差させる方法。メソッドは[**範囲**](https://reference.aspose.com/cells/net/aspose.cells/range)物体。範囲が別の範囲と交差するかどうかを確認するには、[**Range.Intersect**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect)ブール値を返すメソッド。次の例は、範囲を交差させる方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IntersectionofRanges-1.cs" >}}

## **名前付き範囲で Cells をマージします**

Aspose.Cells提供[**Range.Merge()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge)範囲内のセルを結合するメソッド。次の例は、名前付き範囲の個々のセルを結合する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-MergeCellsInNamedRange-1.cs" >}}

## **名前付き範囲を削除する**

Aspose.Cells は[**NameCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/namecollection/methods/removeat)範囲の名前を消去するメソッド。範囲の内容をクリアするには、次を使用します[**Cells.ClearRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/clearrange/index)方法。次の例は、名前付き範囲とその内容を削除する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RemoveANamedRange-1.cs" >}}
