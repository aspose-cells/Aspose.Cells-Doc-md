---
title: 行または列のフォントと色を変更する
type: docs
weight: 110
url: /ja/net/aspose-cells-griddesktop/change-the-font-and-color-of-a-row-or-column/
keywords: GridDesktop で行または列のフォント、色を変更する
description: この記事では、GridDesktop で行または列のフォントと色を変更する方法について紹介します。
---

{{% alert color="primary" %}} 

このトピックでは、Aspose.Cells.GridDesktop が提供する基本的なフォーマット機能であるワークシートの行や列のフォントとフォントの色を変更する方法について説明します。

{{% /alert %}} 
## **列のフォントと色を変更する**
Aspose.Cells.GridDesktop を使用して列のフォントと色を変更するには、以下の手順に従ってください

- 任意の **Worksheet** にアクセスします
- フォントと色を変更したい **列** にアクセス
- カスタムの **フォント** を作成
- **列** の **フォント** をカスタマイズしたものに設定
- 最後に、任意の **色** で **列** の **フォントの色** を設定



{{< highlight csharp >}}

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
- 任意の **Worksheet** にアクセスします
- フォントと色を変更したい **行** にアクセス
- カスタムの **フォント** を作成
- **行** の **フォント** をカスタマイズしたものに設定
- 最後に、**行**の**フォントカラー**を任意の**カラー**に設定します



{{< highlight csharp >}}

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
