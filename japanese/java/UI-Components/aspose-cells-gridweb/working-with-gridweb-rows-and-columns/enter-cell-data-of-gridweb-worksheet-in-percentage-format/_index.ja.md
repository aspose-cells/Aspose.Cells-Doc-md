---
title: GridWebワークシートのセルデータをパーセント形式で入力します
type: docs
weight: 1010
url: /ja/java/enter-cell-data-of-gridweb-worksheet-in-percentage-format/
---

## **可能な使用シナリオ**
GridWebは今、ユーザーが3%などのパーセント形式でセルデータを入力できるようにサポートしており、セルのデータは自動的に3.00%のようにフォーマットされます。しかし、セルスタイルをパーセンテージ形式に設定する必要があります。これはGridTableItemStyle.NumberTypeの9または10です。数字9は3%を3%としてフォーマットしますが、数字10は3%を3.00%としてフォーマットします。

{{% alert color="primary" %}} 

セルスタイルをパーセント形式に設定していない場合、入力データ3%は0.03として表示されます。

{{% /alert %}} 
## **GridWebワークシートのセルデータをパーセント形式で入力する**
次のサンプルコードはセルA1のGridTableItemStyle.NumberTypeを10に設定しています。したがって、入力データ3%は自動的に3.00%としてフォーマットされます（スクリーンショットを参照）。

![todo:image_alt_text](enter-cell-data-of-gridweb-worksheet-in-percentage-format_1.png)
## **サンプルコード**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}






