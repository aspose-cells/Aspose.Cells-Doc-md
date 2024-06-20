---
title: GridWebワークシートのセルデータをパーセント形式で入力します
type: docs
weight: 80
url: /ja/net/aspose-cells-gridweb/enter-cell-data-in-percentage-format/
keywords: GridWeb,percentage,format
description: この記事では、GridWebでパーセント形式でセルデータを入力する方法について紹介します。
---


## **可能な使用シナリオ**
GridWebは今、ユーザーが3%などのパーセント形式でセルデータを入力できるようにサポートしており、セルのデータは自動的に3.00%のようにフォーマットされます。しかし、セルスタイルをパーセンテージ形式に設定する必要があります。これはGridTableItemStyle.NumberTypeの9または10です。数字9は3%を3%としてフォーマットしますが、数字10は3%を3.00%としてフォーマットします。

{{% alert color="primary" %}} 

セルスタイルをパーセント形式に設定していない場合、入力データ3%は0.03として表示されます。

{{% /alert %}} 
## **GridWebワークシートのセルデータをパーセント形式で入力する**
次のサンプルコードはセルA1のGridTableItemStyle.NumberTypeを10に設定しています。したがって、入力データ3%は自動的に3.00%としてフォーマットされます（スクリーンショットを参照）。

![todo:image_alt_text](enter-cell-data-of-gridweb-worksheet-in-percentage-format_1.png)
### **サンプルコード**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SetCellPercentageFormat.aspx-SetCellPercentageFormat.cs" >}}
