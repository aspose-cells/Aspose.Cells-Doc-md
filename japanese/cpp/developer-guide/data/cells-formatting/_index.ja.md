---
title: セルの書式設定
type: docs
weight: 50
url: /ja/cpp/cells-formatting/
---

## **セルまたはセル範囲の書式設定**
セルまたはセル範囲の書式設定を行いたい場合、Aspose.Cellsは[Style](https://reference.aspose.com/cells/cpp/aspose.cells/style/)クラスを提供しています。このクラスを使用して、セルやセル範囲の書式設定をすべて行うことができます。IStyleクラスを使用して達成できる書式設定に関連するいくつかのことは以下の通りです

- セルの塗りつぶしの色を設定する
- セルのテキスト折り返しを設定する
- セルの上部、左部、下部、右側の境界など、セルの境界線を設定する
- フォントの色、サイズ、名前、取り消し線、太字、斜体、下線などを設定します。
- テキストの水平または垂直配置を右、左、上、下、中央などに設定します。

個々のセルのスタイルを設定する場合は、[Cell->SetStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) メソッドを使用し、セルの範囲のスタイルを設定する場合は、[Range->ApplyStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/) メソッドを使用してください。
## **サンプルコード**
以下のサンプルコードは、ワークシートのセルC4の書式をさまざまな方法で設定し、それによって生成された [出力エクセルファイル](21266438.xlsx) を参照してください。

![todo:image_alt_text](cells-formatting_1.png)



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CellsFormatting-FormatCellOrRangeOfCells-new.cpp" >}}
