---
title: セルの書式設定
type: docs
weight: 40
url: /ja/net/aspose-cells-gridweb/format-grid-cell/
keywords: GridWeb、書式、スタイル
description: この記事では、GridWebのセル（GridCell）にスタイル書式を設定する方法について紹介します。
---

{{% alert color="primary" %}} 

このトピックでは、セルの書式設定について詳しく説明します。

Aspose.Cells.GridWebコントロールのスタイルダイアログを使用してGUIモードでのセルの書式設定をカバーしています。また、プログラムでセルの書式を設定する方法も示しています。フォント、罫線、および数値書式などのさまざまな書式設定が例を交えて説明されています。

{{% /alert %}} 
## **スタイルダイアログを使用してセルの書式を設定する**
セルの書式設定は[プログラム](/cells/ja/net/aspose-cells-gridweb/format-cells/)で行うこともできますが、Aspose.Cells.GridWebコントロールでセルの書式設定をWYSIWYGな方法で行うには、スタイルダイアログを使用するのが最も簡単です。

スタイルダイアログの使用方法：
セルの範囲を選択して右クリックし、**セルの書式設定**を選択します。 

**セルの書式設定を選択** 

![todo:image_alt_text](format-cells_1.png)



スタイルダイアログが表示されます。 

**セルの書式を設定するためにスタイルダイアログが使用されます** 

![todo:image_alt_text](format-cells_2.png)

スタイルダイアログを使用すると、ユーザーはフォントや罫線の設定をカスタマイズしてセルの書式を設定できます。
### **フォント設定のカスタマイズ**
スタイルダイアログを使用して、以下のフォント設定をカスタマイズできます:

- フォント名、リストから希望のフォントを選択します。
- フォントスタイル、太字、斜体などのフォントスタイルを適用します。
- フォントサイズ、ポイントでフォントサイズを選択します。
- 下線、テキストに下線を引きます。
- 取り消し線、テキストに取り消し線の効果を適用します。
- 水平配置、水平配置を選択します。
- 垂直配置、垂直配置を選択します。
- フォントの色、フォントの色を選択します。
- 背景、背景の色を選択します。

選択したフォント設定を小さなプレビューエリアで確認できます。

**カスタマイズされたフォント設定** 

![todo:image_alt_text](format-cells_3.png)
### **境界線設定のカスタマイズ**
スタイルダイアログで境界線設定をカスタマイズすることで、セルの周囲に境界線を描画することも可能です。

境界線に関連するオプションを表示するには:
スタイルダイアログで**境界線**をクリックします。
境界線に関連するオプションが表示されます。 

**スタイルダイアログ内の境界線オプション** 

![todo:image_alt_text](format-cells_4.png)

スタイルダイアログから以下の境界線オプションを選択できます:

- 境界線スタイル、実線、点線などの境界線スタイルを選択します。
- 境界線の幅、ピクセル単位で境界線の幅を選択します。
- 境界線の色、線の色を選択します。
- 境界線、境界線の番号付けと配置を選択します。

**カスタマイズされた境界線設定** 

![todo:image_alt_text](format-cells_5.png)
### **設定の適用**
変更を適用するには、スタイルダイアログで**OK**をクリックします。

**フォントおよび境界線設定が適用されました** 

![todo:image_alt_text](format-cells_6.png)


## **APIを使用したセルの書式設定**
Aspose.Cells.GridWeb APIを使用して、プログラムでセルの書式設定も可能です。各セルにはStyleプロパティがあり、これはGridTableItemStyleオブジェクトを表します。フォントおよび境界線設定をカスタマイズするには、Styleプロパティを使用します。
### **フォントの設定**
プログラムでフォント設定をカスタマイズするには:

1. Web フォームに Aspose.Cells.GridWeb コントロールを追加します。
1. ワークシートにアクセスします。
1. フォーマットするセルにアクセスします。
1. セルのスタイルにアクセスします。
1. フォントサイズをポイントで設定します。
1. フォントスタイルを設定します。
1. 前景色と背景色を設定します。
1. 水平および垂直の配置を設定します。
1. スタイルをセルに戻します。

**出力: A1に表示されるカスタマイズされたフォント設定** 

![todo:image_alt_text](format-cells_7.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyFontStyles.cs" >}}
### **境界線の設定**
境界線は個々のセルまたは範囲に適用できます。
#### **個々のセル**
個々のセルの境界線を設定するには:

1. Web フォームに Aspose.Cells.GridWeb コントロールを追加します。
1. ワークシートにアクセスします。
1. フォーマットするセルにアクセスします。
1. セルのスタイルオブジェクトにアクセスします。
1. 境界スタイルを設定します。
1. 境界の幅をピクセルで設定します。
1. 境界線の色を設定します。
1. セルにスタイルを設定します。

**個々のセルのカスタマイズされた境界設定** 

![todo:image_alt_text](format-cells_8.png)

{{% alert color="primary" %}} 

セルのStyle.TopBorderStyle、Style.BottomBorderStyle、Style.LeftBorderStyle、Style.RightBorderStyleプロパティを使用して、各境界線に異なるスタイルを設定することができます。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyBorderStyles.cs" >}}
#### **セルの範囲**
セルの範囲に境界線を設定するには:

1. Web フォームに Aspose.Cells.GridWeb コントロールを追加します
1. 希望のワークシートにアクセスします
1. WebBorderStyle クラスのオブジェクトをインスタンス化します
1. 境界線のスタイルをソリッドまたはダッシュなどに設定します
1. 境界線の幅をピクセル単位で設定します
1. 境界線の色を設定します
1. WebBorderStyle オブジェクトに格納された境界線の設定を特定のセル範囲に適用します

**カスタマイズされた境界線設定のセル範囲** 

![todo:image_alt_text](format-cells_9.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyRangeBorderStyles.cs" >}}
### **数値形式の設定**
Aspose.Cells.GridWeb は数値形式の設定をサポートしています。59 個の組み込み数値形式があります。これらを表示するには、[サポートされている数値形式の一覧](/cells/ja/net/aspose-cells-gridweb/list-of-supported-number-formats/) を参照してください。

すべての組み込み数値形式は NumberType 列挙型に含まれています。組み込みの数値形式を使用するには、セルのオブジェクトの SetNumberType メソッドを使用して、NumberType 列挙型から数値形式を設定します。

カスタム数値形式を設定するには、セルの SetCustom メソッドを使用します。

**B1 と B2 に適用された数値形式設定** 

![todo:image_alt_text](format-cells_10.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyNumberFormats.cs" >}}
