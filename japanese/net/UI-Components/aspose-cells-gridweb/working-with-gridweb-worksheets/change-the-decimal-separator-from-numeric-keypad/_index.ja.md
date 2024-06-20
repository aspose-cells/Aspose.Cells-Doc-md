---
title: 10進記号の変更を数字キーパッドから変更する
type: docs
weight: 150
url: /ja/net/aspose-cells-gridweb/change-the-decimal-separator-from-numeric-keypad/
keywords: GridWeb、10進数、10進数の記号
description: この記事では、GridWebで10進数の記号を変更する方法について紹介します。
---

## **可能な使用シナリオ**
Aspose.Cells.GridWebは、デフォルトでは、機械のロケール/地域設定に基づいて数値データを表示します。Aspose.Cells.GridWeb APIを使用して、Numericパッドからの小数点セパレータをプログラムで変更することができます。したがって、ファイルをGridWebマトリックスにインポートするか、新しいワークシートセルに数値データ（Numericパッドから）を入力すると、望ましい小数点セパレータが視覚的に設定されます。 
## **Numericパッドからの小数点セパレータを変更する**
**GridWorksheetCollection.NumberDecimalSeparator**プロパティを使用して、Numericパッドからの小数点セパレータをプログラムで変更することができます。その動作については、スクリーンショットを参照してください。

![todo:image_alt_text](change-the-decimal-separator-from-numeric-keypad_1.png)

![todo:image_alt_text](change-the-decimal-separator-from-numeric-keypad_2.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Worksheets-ChangeDecimalSeparatorFromNumericKeypad.aspx.cs" >}}

{{% alert color="primary" %}} 

小数点セパレータの変更は、GridWeb上のユーザーの視覚的な体験のためのものです。ワークブックを編集して保存する際、スプレッドシート内の数値は引き続きロケール/地域の小数点セパレータに基づいて格納されます。

{{% /alert %}}
