---
title: ワークシートに条件付き書式を適用する
type: docs
weight: 40
url: /ja/cpp/apply-conditional-formatting-in-worksheet/
---
## **考えられる使用シナリオ**
Aspose.Cells では、数式、平均以上、カラー スケール、データ バー、アイコン セット、Top10 など、あらゆる種類の条件付き書式を追加できます。[IFormatCondition](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition)選択した条件付き書式を適用するために必要なすべてのメソッドを持つクラス。 Get メソッドのいくつかのリストを次に示します。

- [GetIAboveAverage()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#aff550fd834cd78967ec440492ff012d5)
- [GetIColorScale()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a3348a7c447dc564ceabc22c9c89bd6f5)
- [GetIDataBar()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a4415a87833c41386ed1595e742485e07)
- [GetIIconSet()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a011b2c7dbaaf671819d09f5d1df865e3)
- [GetITop10()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a64388aaf1b43811f5ee1ee3090c9bd4a)
## **ワークシートに条件付き書式を適用する**
次のサンプル コードは、セル A1 と B2 に Cell 値の条件付き書式を追加する方法を示しています。をご覧ください[出力エクセルファイル](23167004.xlsx)コードによって生成された、および次のスクリーンショットは、コードが[出力エクセルファイル](23167004.xlsx).セル A2 と B2 に 100 より大きい値を入力すると、セル A1 と B2 の赤の塗りつぶし色が消えます。

![todo:画像_代替_文章](apply-conditional-formatting-in-worksheet_1.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ApplyConditionalFormattingInWorksheet.cpp" >}}
