---
title: 数値キーパッドから小数点記号を変更する
type: docs
weight: 150
url: /ja/net/change-the-decimal-separator-from-numeric-keypad/
---
## **考えられる使用シナリオ**
デフォルトでは、Aspose.Cells.GridWeb は、マシンのロケール/地域設定に応じて数値データを表示します。 Aspose.Cells.GridWeb API を使用して、数値キーパッドから小数点記号をプログラムで変更できます。そのため、ファイルを GridWeb マトリックスにインポートするか、(数値キーパッドから) 数値データを新しいワークシート セルに入力すると、目的の小数点を持つ必要があります。セパレーターを視覚的に設定します。
## **数値キーパッドから小数点記号を変更する**
を使用して**GridWorksheetCollection.NumberDecimalSeparator**プロパティを使用すると、数値キーパッドからプログラムで小数点記号を変更できます。それがどのように機能するかを示すスクリーンショットをご覧ください

![todo:画像_代替_文章](change-the-decimal-separator-from-numeric-keypad_1.png)

![todo:画像_代替_文章](change-the-decimal-separator-from-numeric-keypad_2.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Worksheets-ChangeDecimalSeparatorFromNumericKeypad.aspx.cs" >}}

{{% alert color="primary" %}} 

小数点記号の変更は、GridWeb でのユーザーの視覚的な経験のためだけのものであることに注意してください。ワークブックを編集して保存すると、ロケール/地域の小数点記号に従って数値が (スプレッドシートに) 保存されます。

{{% /alert %}}
