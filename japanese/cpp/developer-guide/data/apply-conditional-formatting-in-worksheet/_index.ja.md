---
title: ワークシートに条件付き書式を適用する
type: docs
weight: 40
url: /ja/cpp/apply-conditional-formatting-in-worksheet/
---
##  **考えられる使用シナリオ**
Aspose.Cells を使用すると、あらゆる種類の条件付き書式設定 (数式、平均以上、カラー スケール、データ バー、アイコン セット、トップ 10 など) を追加できます。[フォーマット条件](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/)このクラスには、選択した条件付き書式設定を適用するために必要なメソッドがすべて含まれています。 Get メソッドのいくつかのリストを次に示します。

- [GetAboveAverage()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getaboveaverage/)
- [GetColorScale()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getcolorscale)
- [GetDataBar()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getdatabar)
- [GetIconSet()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/geticonset)
- [GetTop10()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/gettop10)
##  **ワークシートに条件付き書式を適用する**
次のサンプル コードは、セル A1 と B2 に Cell 値の条件付き書式を追加する方法を示しています。をご覧ください。[Excelファイルを出力する](23167004.xlsx)コードによって生成されたものと、コードが に及ぼす影響を説明する次のスクリーンショット。[Excelファイルを出力する](23167004.xlsx)。セル A2 と B2 に 100 より大きい値を入力すると、セル A1 と B2 の赤色の塗りつぶし色が消えます。

![todo:image_alt_text](apply-conditional-formatting-in-worksheet_1.png)
##  **サンプルコード**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ApplyConditionalFormattingInWorksheet-new.cpp" >}}
