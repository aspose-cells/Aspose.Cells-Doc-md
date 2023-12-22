---
title: GridWeb ワークシートの Cell データをパーセント形式で入力します
type: docs
weight: 1010
url: /ja/java/enter-cell-data-of-gridweb-worksheet-in-percentage-format/
---
##  **考えられる使用シナリオ**
GridWeb では、ユーザーがセル データを 3% などのパーセント形式で入力できるようになりました。セル内のデータは自動的に 3.00% として形式設定されます。ただし、セル スタイルを Percentage Format (GridTableItemStyle.NumberType の 9 または 10) に設定する必要があります。数値 9 は 3% を 3% としてフォーマットしますが、数値 10 は 3% を 3.00% としてフォーマットします。

{{% alert color="primary" %}} 

セル スタイルをパーセント形式に設定していない場合、入力データ 3% は 0.03 として表示されます。

{{% /alert %}} 
##  **GridWeb ワークシートの Cell データをパーセント形式で入力します**
次のサンプル コードでは、セル A1 GridTableItemStyle.NumberType を 10 に設定します。したがって、スクリーンショットに示すように、入力データ 3% は自動的に 3.00% として書式設定されます。

![todo:image_alt_text](enter-cell-data-of-gridweb-worksheet-in-percentage-format_1.png)
##  **サンプルコード**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}






