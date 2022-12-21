---
title: 行または列にスタイルを適用する
type: docs
weight: 50
url: /ja/net/applying-style-on-a-row-or-column/
---
{{% alert color="primary" %}} 

このトピックでは、ワークシートの行と列のフォントとフォントの色の変更について説明します。これは、Aspose.Cells.GridDesktop によって提供される基本レベルの書式設定機能であり、開発者がワークシートのビューをカスタマイズして見やすくすることができます。

{{% /alert %}} 
## **列にスタイルを適用する**
Aspose.Cells.GridDesktop を使用して列にカスタム スタイルを適用するには、次の手順に従ってください。

- 任意のアクセス**ワークシート**
- アクセス**桁**適用したい**スタイル**
- 取得する**スタイル**の**桁**
- セットする**スタイル**カスタムニーズに応じたプロパティ
- 最後に、設定**スタイル**の**桁**更新されたもので

によって提供される多くの便利なプロパティとメソッドがあります。**スタイル**開発者が要件に応じてスタイルをカスタマイズするために使用できるオブジェクト。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ApplyingStyleOnRowColumn-AddingColumnStyle.cs" >}}
## **行にスタイルを適用する**
Aspose.Cells.GridDesktop を使用して行にカスタム スタイルを適用するには、次の手順に従ってください。

- 任意のアクセス**ワークシート**
- アクセス**行**適用したい**スタイル**
- 取得する**スタイル**の**行**
- セットする**スタイル**カスタムニーズに応じたプロパティ
- 最後に、設定**スタイル**の**行**更新されたもので

によって提供される多くの便利なプロパティとメソッドがあります。**スタイル**開発者が要件に応じてスタイルをカスタマイズするために使用できるオブジェクト。



{{< highlight "csharp" >}}

 // Accessing the worksheet of the Grid that is currently active

Worksheet sheet = gridDesktop1.GetActiveWorksheet();

// Accessing the first row of the worksheet

Aspose.Cells.GridDesktop.Data.GridRow row = sheet.Rows[0];

// Getting the Style object for the row

Style style = row.GetStyle();

// Setting Style properties i.e. border, color, alignment, background color etc.

style.SetBorderLine(BorderType.Right, BorderLineType.Thick);

style.SetBorderColor(BorderType.Right, Color.Blue);

style.HAlignment = HorizontalAlignmentType.Centred;

style.Color = Color.Yellow;

// Setting the style of the row with the customized Style object

row.SetStyle(style);

{{< /highlight >}}
