---
title: Cells フォーマット中
type: docs
weight: 50
url: /ja/cpp/cells-formatting/
---
##  **形式 Cell または Cells の範囲**
セルまたはセル範囲の書式を設定する場合、Aspose.Cells は[スタイル](https://reference.aspose.com/cells/cpp/aspose.cells/style/)クラス。このクラスを使用して、セルまたはセル範囲のすべての書式設定を実行できます。 IStyle クラスを使用して実行できる書式設定に関連するいくつかのことは次のとおりです。

- セルの塗りつぶし色を設定する
- セルのテキストの折り返しを設定する
- 上、左、下、右の境界線などのセルの境界線を設定します。
- 文字色、文字サイズ、フォント名、取り消し線、太字、斜体、下線などを設定します。
- テキストの水平方向または垂直方向の配置を右、左、上、下、中央などに設定します。

単一セルのスタイルを設定したい場合は、次を使用してください。[Cell->SetStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/)メソッドを使用し、セル範囲のスタイルを設定したい場合は、を使用してください。[範囲 ->ApplyStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/)方法。
##  **サンプルコード**
次のサンプル コードでは、ワークシートのセル C4 をさまざまな方法で書式設定します。スクリーンショットは、[Excelファイルを出力する](21266438.xlsx)参考のためにそれによって生成されました。

![todo:image_alt_text](cells-formatting_1.png)



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CellsFormatting-FormatCellOrRangeOfCells-new.cpp" >}}
