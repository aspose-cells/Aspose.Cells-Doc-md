---
title: セルの形式を変更する
description: C# の Aspose.Cells ライブラリを使用して、フォント、色、境界線などのセルの書式設定を変更する方法。これらのプロパティを調整することで、セルの外観と表示方法をより詳細に制御できます。
keywords: Aspose.Cells, cell formatting, C#, font, color, border
type: docs
weight: 105
url: /ja/net/how-to-change-format-of-cell/
---
##  **考えられる使用シナリオ**
特定のデータを強調表示したい場合は、セルのスタイルを変更できます。

##  **Excelでセルの書式を変更する方法**

Excel で単一のセルの形式を変更するには、次の手順に従います。

1. Excel を開き、書式設定するセルが含まれるブックを開きます。

2. 書式設定するセルを見つけます。

3. セルを右クリックし、コンテキスト メニューから「Format Cells」を選択します。または、セルを選択して Excel リボンの [ホーム] タブに移動し、[Cells] グループの [書式] ドロップダウンをクリックして、[Cells の書式設定] を選択することもできます。

4. 「Cellsのフォーマット」ダイアログボックスが表示されます。ここでは、選択したセルに適用するさまざまな書式設定オプションを選択できます。たとえば、フォント スタイル、フォント サイズ、フォントの色、数値形式、枠線、背景色などを変更できます。ダイアログ ボックスのさまざまなタブを参照して、さまざまな書式設定オプションにアクセスします。

5. 必要な書式変更を行った後、[OK] ボタンをクリックして、選択したセルに書式を適用します。


##  **C#を使用してセルの形式を変更する方法**

Aspose.Cells を使用してセルの形式を変更するには、次の方法を使用できます。
1. [Cell.SetStyle(スタイルスタイル)](https://reference.aspose.com/cells/net/aspose.cells/cell/setstyle/#setstyle)
2. [Cell.SetStyle(スタイル スタイル、ブール明示フラグ)](https://reference.aspose.com/cells/net/aspose.cells/cell/setstyle/#setstyle_2)
3. [Cell.SetStyle(スタイルスタイル、StyleFlagフラグ)](https://reference.aspose.com/cells/net/aspose.cells/cell/setstyle/#setstyle_1)


##  **サンプルコード**
この例では、Excel ワークブックを作成し、サンプル データを追加し、最初のワークシートにアクセスして、2 つのセル (「A2」と「B3」) を取得します。次に、セルのスタイルを取得し、さまざまな書式設定オプション (フォントの色、太字など) を設定し、セルの書式を変更します。最後に、ワークブックを新しいファイルに保存します。
![todo:image_alt_text](change-format.png)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-change-format.cs" >}}
