---
title: 行または列にスタイルを適用
type: docs
weight: 50
url: /ja/net/aspose-cells-griddesktop/apply-style-on-a-row-or-column/
keywords: GridDesktop、スタイル、行、列
description: この記事では、GridDesktopで行や列にスタイルを適用する方法について紹介します。
---

{{% alert color="primary" %}} 

このトピックでは、Aspose.Cells.GridDesktop が提供する基本的なフォーマット機能であるワークシートの行や列のフォントとフォントの色を変更する方法について説明します。

{{% /alert %}} 
## **列にスタイルを適用する**
Aspose.Cells.GridDesktopを使用して列にカスタムスタイルを適用するには、以下の手順に従ってください：

- 任意の **Worksheet** にアクセスします
- 適用したい **スタイル** を適用する **列** にアクセス
- **列** の **スタイル** を取得
- カスタムの必要に応じて **スタイル** プロパティを設定
- 最後に、更新されたもので **列** の **スタイル** を設定

**Style** オブジェクトが提供する多くの便利なプロパティとメソッドを使用して、開発者が要件に応じてスタイルをカスタマイズできます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ApplyingStyleOnRowColumn-AddingColumnStyle.cs" >}}
## **行にスタイルを適用**
Aspose.Cells.GridDesktop を使用して行にカスタムスタイルを適用するには、以下の手順に従ってください

- 任意の **Worksheet** にアクセスします
- 適用したい **スタイル** を適用する **行** にアクセス
- **行** の **スタイル** を取得
- カスタムの必要に応じて **スタイル** プロパティを設定
- 最後に、更新されたもので **行** の **スタイル** を設定

**Style** オブジェクトが提供する多くの便利なプロパティとメソッドを使用して、開発者が要件に応じてスタイルをカスタマイズできます。



{{< highlight csharp >}}

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
