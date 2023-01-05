---
title: Cell GridWebワークシートのデータをパーセンテージ形式で入力
type: docs
weight: 80
url: /ja/net/enter-cell-data-of-gridweb-worksheet-in-percentage-format/
---
## **考えられる使用シナリオ**
GridWeb では、ユーザーが 3% などのパーセンテージ形式でセル データを入力できるようになり、セル内のデータは自動的に 3.00% としてフォーマットされます。ただし、セル スタイルをパーセンテージ形式に設定する必要があります。これは GridTableItemStyle.NumberType が 9 または 10 のいずれかです。数値 9 は 3% を 3% として書式設定しますが、数値 10 は 3% を 3.00% として書式設定します。

{{% alert color="primary" %}} 

セル スタイルをパーセント形式に設定していない場合、入力データ 3% は 0.03 として表示されます。

{{% /alert %}} 
## **Cell GridWebワークシートのデータをパーセンテージ形式で入力**
次のサンプル コードは、セル A1 GridTableItemStyle.NumberType を 10 に設定するため、スクリーンショットに示すように、入力データ 3% は自動的に 3.00% としてフォーマットされます。

![todo:画像_代替_文章](enter-cell-data-of-gridweb-worksheet-in-percentage-format_1.png)
### **サンプルコード**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SetCellPercentageFormat.aspx-SetCellPercentageFormat.cs" >}}
