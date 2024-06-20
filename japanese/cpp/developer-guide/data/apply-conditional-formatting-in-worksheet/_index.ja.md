---
title: ワークシートへの条件付き書式を適用する
type: docs
weight: 40
url: /ja/cpp/apply-conditional-formatting-in-worksheet/
---

## **可能な使用シナリオ**
Aspose.Cellsでは、式、平均以上、カラースケール、データバー、アイコンセット、Top10など、さまざまな条件付き書式を追加できます。選択した条件付き書式を適用するために必要なメソッドをすべて備えた[FormatCondition](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/)クラスを提供しています。次に示すのは、いくつかのGetメソッドのリストです。

- [GetAboveAverage()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getaboveaverage/)
- [GetColorScale()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getcolorscale)
- [GetDataBar()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getdatabar)
- [GetIconSet()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/geticonset)
- [GetTop10()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/gettop10)
## **ワークシートへの条件付き書式を適用する**
以下のサンプルコードは、セルA1およびB2にセル値の条件付き書式を追加する方法を示しています。このコードで生成された[出力エクセルファイル](23167004.xlsx)と、[出力エクセルファイル](23167004.xlsx)へのコードの効果を説明する次のスクリーンショットをご覧ください。セルA2およびB2に100より大きい値を入力すると、セルA1およびB2の赤色の塗りつぶしが消えます。

![todo:image_alt_text](apply-conditional-formatting-in-worksheet_1.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ApplyConditionalFormattingInWorksheet-new.cpp" >}}
