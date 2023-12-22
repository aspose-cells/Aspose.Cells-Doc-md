---
title: 调整行高和列宽
type: docs
weight: 10
url: /zh/cpp/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}} 

使用电子表格并向行或列添加数据时，您可能需要更改行高或列宽。有时，在行或列上应用格式意味着需要更改当前高度或宽度才能显示数据。通常，用户使用 Microsoft Excel 在所见即所得环境中调整行高和列宽。但是，使用 Aspose.Cells 开发人员可以在运行时执行这些操作。

{{% /alert %}} 
##  **使用行**
###  **调整行高**
Aspose.Cells提供一堂课，[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)代表 Microsoft Excel 文件。这[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含一个[工作表集合](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)允许访问 Excel 文件中的每个工作表。工作表由以下形式表示[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)班级。这[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供了一个[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)代表工作表中所有单元格的集合。这[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合提供了多种管理工作表中的行或列的方法。下面将更详细地讨论其中一些。
####  **设置行的高度**
可以通过调用来设置单行的高度[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)收藏的[设置行高](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/)方法。这[设置行高](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/)方法采用以下参数：

- *行索引**，您要更改其高度的行的索引。
- *行高**，应用于行的行高。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfRow-new.cpp" >}}


####  **设置工作表中所有行的高度**
如果开发人员需要为工作表中的所有行设置相同的行高，他们可以使用[设置标准高度](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardheight/)的方法[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)收藏。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfAllRowsInWorksheet-new.cpp" >}}
##  **使用列**
###  **设置列的宽度**
通过调用设置列的宽度[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)收藏的[设置列宽](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/)方法。这[设置列宽](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/)方法采用以下参数：

- *列索引**，您要更改宽度的列的索引。
- *列宽**，所需的列宽。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfColumn-new.cpp" >}}
###  **设置工作表中所有列的宽度**
要为工作表中的所有列设置相同的列宽，请使用[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)收藏的[设置标准宽度](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardwidth/)方法。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfAllColumnsInWorksheet-new.cpp" >}}
