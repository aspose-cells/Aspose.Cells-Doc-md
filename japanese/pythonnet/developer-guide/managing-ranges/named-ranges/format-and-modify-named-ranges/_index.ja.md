---
title: 名前付き範囲の書式および変更
type: docs
weight: 85
url: /ja/python-net/format-and-modify-named-ranges/
description: この記事では、Aspose.Cells for Python via .NET APIを使用して、名前付き範囲の書式設定と変更方法が示されています。
keywords: Python Excelライブラリ、Pythonフォーマットおよび名前付き範囲の変更、名前付き範囲に背景色とフォント属性を設定するPython、名前付き範囲に境界線を追加するPython、名前付き範囲の名前変更Python、範囲のユニオンPython、範囲の交差Python、名前付き範囲でセルを結合するPython。
---

## **範囲の書式設定**

### **名前付き範囲に背景色とフォント属性を設定する方法**

書式を適用するには、[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) オブジェクトを定義してスタイル設定を指定し、そのスタイルを[**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) オブジェクトに適用します。

次の例では範囲に実線の塗りつぶし色（シェーディング色）とフォント設定を設定する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-FormatRanges1-1.py" >}}

### **名前付き範囲に境界線を追加する方法**

単一のセルではなく、セルの範囲に境界線を追加することが可能です。[**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) オブジェクトには、次のパラメータを取る[**set_outline_border**](https://reference.aspose.com/cells/python-net/aspose.cells/range/set_outline_border/#aspose.cells.BorderType-aspose.cells.CellBorderType-aspose.cells.CellsColor) メソッドが提供され、セルの範囲に境界線を追加することができます：

- 境界線の種類、[**BorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/bordertype) 列挙型から選択される境界線の種類。
- ライン スタイル は [**CellBorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellbordertype) 列挙体から選択されます。
- カラー は Color 列挙体から選択されます。

次の例では、範囲にアウトラインボーダーを設定する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-FormatRanges2-1.py" >}}


## **名前付き範囲の名前変更方法**

Aspose.Cellsを使用して、必要に応じて名前付き範囲の名前を変更できます。名前付き範囲を取得して、[**Name.text**](https://reference.aspose.com/cells/python-net/aspose.cells/name/text) 属性を使用して名前を変更する方法を次の例で示します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-RenameNamedRange-1.py" >}}

## **範囲のユニオン方法**

Aspose.Cellsは範囲のユニオンを取るための[**Range.union**](https://reference.aspose.com/cells/python-net/aspose.cells/range/union/#aspose.cells.Range)メソッドを提供します。次の例は、範囲のユニオンを取る方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-UnionOfRanges-1.py" >}}

## **範囲の交差方法**

Aspose.Cells は 2 つの範囲の交差を求めるための [**Range.intersect**](https://reference.aspose.com/cells/python-net/aspose.cells/range/intersect/#aspose.cells.Range) メソッドを提供しており、このメソッドは [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) オブジェクトを返します。範囲が他の範囲と交差するかどうかを確認するには、ブール値を返す [**Range.intersect**](https://reference.aspose.com/cells/python-net/aspose.cells/range/intersect/#aspose.cells.Range) メソッドを使用します。次の例では、範囲の交差方法を示します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-IntersectionofRanges-1.py" >}}

## **名前付き範囲でセルを結合する方法**

Aspose.Cells は範囲内のセルを結合するための [**Range.merge()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/merge/#) メソッドを提供しています。次の例では、名前付き範囲内の個々のセルを結合する方法を示します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-MergeCellsInNamedRange-1.py" >}}
