---
title: 更改行或列的字体和颜色
type: docs
weight: 110
url: /zh/net/changing-the-font-and-color-of-a-row-or-column/
---
{{% alert color="primary" %}} 

在本主题中，我们将讨论如何更改工作表的行和列的字体和字体颜色。这是 Aspose.Cells.GridDesktop 提供的基本级别的格式化功能，它使开发人员能够自定义工作表的视图，使其更易于呈现。

{{% /alert %}} 
## **更改列的字体和颜色**
要使用 Aspose.Cells.GridDesktop 更改列的字体和颜色，请按照以下步骤操作：

- 访问任何想要的**工作表**
- 访问一个**柱子**要更改其字体和颜色
- 创建自定义**字体**
- 设置**字体**的**柱子**到定制的
- 最后，设置**字体颜色**的**柱子**任何想要的**颜色**



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
## **更改行的字体和颜色**
- 访问任何想要的**工作表**
- 访问一个**排**要更改其字体和颜色
- 创建自定义**字体**
- 设置**字体**的**排**到定制的
- 最后，设置**字体颜色**的**排**任何想要的**颜色**



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
