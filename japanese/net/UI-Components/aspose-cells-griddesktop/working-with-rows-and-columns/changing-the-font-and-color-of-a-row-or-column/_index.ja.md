---
title: 行または列のフォントと色の変更
type: docs
weight: 110
url: /ja/net/changing-the-font-and-color-of-a-row-or-column/
---
{{% alert color="primary" %}} 

このトピックでは、ワークシートの行と列のフォントとフォントの色の変更について説明します。これは、Aspose.Cells.GridDesktop によって提供される基本レベルの書式設定機能であり、開発者がワークシートのビューをカスタマイズして見やすくすることができます。

{{% /alert %}} 
## **列のフォントと色の変更**
Aspose.Cells.GridDesktop を使用して列のフォントと色を変更するには、次の手順に従ってください。

- 任意のアクセス**ワークシート**
- アクセス**桁**フォントと色を変更する
- カスタマイズされた**フォント**
- をセットする**フォント**の**桁**カスタマイズされたものに
- 最後に、設定**フォントの色**の**桁**任意に**色**



{{< highlight "csharp" >}}

 //Accessing the worksheet of the Grid that is currently active

Worksheet sheet = gridDesktop1.GetActiveWorksheet();

//Accessing the first column of the worksheet

GridColumn column = sheet.Columns[0];

//Creating a customized Font object

Font font = new Font("Arial", 10, FontStyle.Bold);

//Setting the font of the column to the customized Font object

column.SetFont(font);

//Setting the font color of the column to Blue

column.SetFontColor(Color.Blue);

{{< /highlight >}}
## **行のフォントと色を変更する**
- 任意のアクセス**ワークシート**
- アクセス**行**フォントと色を変更する
- カスタマイズされた**フォント**
- をセットする**フォント**の**行**カスタマイズされたものに
- 最後に、設定**フォントの色**の**行**任意に**色**



{{< highlight "csharp" >}}

 //Accessing the worksheet of the Grid that is currently active

Worksheet sheet = gridDesktop1.GetActiveWorksheet();

//Accessing the first row of the worksheet

GridRow row = sheet.Rows[0];

//Creating a customized Font object

Font font = new Font("Arial", 10, FontStyle.Underline);

//Setting the font of the column to the customized Font object

row.SetFont(font);

//Setting the font color of the column to Green

row.SetFontColor(Color.Green);

{{< /highlight >}}
