---
title: Cells フォーマット
type: docs
weight: 50
url: /ja/cpp/cells-formatting/
---
## **フォーマット Cell または範囲 Cells**
セルまたはセルの範囲をフォーマットする場合は、Aspose.Cells を指定します。[IStyle](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_style)クラス。このクラスを使用して、セルまたはセル範囲のすべての書式設定を実行できます。 IStyle クラスで実現できる書式設定に関連するもののいくつかは次のとおりです。

- セルの塗りつぶし色を設定する
- セルのテキスト ラップを設定する
- 上、左、下、右の境界線などのセルの境界線を設定します。
- フォントの色、フォントサイズ、フォント名、ストライク、ボールド、イタリック、アンダーラインなどを設定します。
- テキストの水平方向または垂直方向の配置を、右、左、上、下、中央などに設定します。

単一のセルのスタイルを設定する場合は、使用してください[ICell->SetIStyle()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#afa3d5b2aa5e90b286effc9e92de59dd5)メソッドを使用し、セル範囲のスタイルを設定する場合は、使用してください[IRange->ApplyIStyle()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_range#aaad6703b803565b674999bbaf5eed3a0)方法。
## **サンプルコード**
次のサンプル コードは、ワークシートのセル C4 をさまざまな方法で書式設定します。スクリーンショットは、[出力エクセルファイル](21266438.xlsx)参照用にそれによって生成されます。

![todo:画像_代替_文章](cells-formatting_1.png)



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CellsFormatting-FormatCellOrRangeOfCells.cpp" >}}
