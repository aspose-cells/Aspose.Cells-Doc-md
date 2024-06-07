---
title: 更改行或列的字体和颜色
type: docs
weight: 110
url: /zh/net/aspose-cells-griddesktop/change-the-font-and-color-of-a-row-or-column/
keywords: GridDesktop，字体，颜色
description: 本文介绍如何在GridDesktop中更改行或列中的字体和颜色。
---

{{% alert color="primary" %}} 

在本主题中，我们将讨论如何更改工作表的行和列的字体和字体颜色。这是Aspose.Cells.GridDesktop提供的一项基本格式功能，使开发人员可以自定义工作表的视图，使其更具展示性。

{{% /alert %}} 
## **更改列的字体和颜色**
要使用Aspose.Cells.GridDesktop更改列的字体和颜色，请按照以下步骤操作：

- 访问任何所需的**工作表**
- 访问要更改字体和颜色的**列**
- 创建自定义**字体**
- 将**列**的**字体**设置为自定义的字体
- 最后，将**列**的**字体颜色**设置为任何所需的**颜色**



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
## **更改行的字体和颜色**
- 访问任何所需的**工作表**
- 访问要更改字体和颜色的**行**
- 创建自定义**字体**
- 将**行**的**字体**设置为自定义的字体
- 最后，将**行**的**字体颜色**设置为任何所需的**颜色**



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
