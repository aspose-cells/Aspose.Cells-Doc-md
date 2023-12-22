---
title: 获取电子表格或工作簿中使用的字体列表
description: Aspose.Cells 是一个用于处理电子表格文件的 .NET 库。它支持获取电子表格或工作簿中使用的字体列表，允许用户获取文档中使用的字体信息。本文将向您展示如何使用 Aspose.Cells 库来获取字体列表。
keywords: Aspose.Cells, Spreadsheet, Workbook, Font, List
type: docs
weight: 20
url: /zh/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---
##  **可能的使用场景**

通常有必要了解工作簿中用于渲染目的的字体。当您将工作簿转换为 PDF 或图像时，Aspose.Cells 要求所有需要的字体都安装在您的系统上或存在于您的*字体目录**中。如果 Aspose.Cells 无法找到所需的字体，它会尝试将其替换为您的系统或字体目录中存在的其他合适的字体，并且可以替换您的实际字体。这不仅会导致 PDF 或图像出现不需要的渲染，而且还会花费处理时间来查找合适的字体。

为了处理这种情况，您应该知道您的工作簿正在使用哪些字体，然后在 Windows 环境中将这些字体安装在您的系统上，或者在 Windows 或 Linux 环境中将其放置在您的字体目录中。

 Aspose.Cells 提供**[Workbook.GetFonts](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getfonts)**返回工作簿或电子表格中使用的所有字体的列表的方法。

##  **获取电子表格或工作簿中使用的字体列表**

以下示例代码加载源 Excel 文件并检索其中使用的字体列表。它有一个虚拟工作表，其中添加了一些用于说明目的的虚拟字体。当代码打印工作簿中的所有字体时，它还会打印这些虚拟字体。下面的屏幕截图显示了[示例 Excel 文件](25395211.xlsx)以及如何列出虚拟字体。

![待办事项：图像_替代_文本](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

##  **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-GetListOfFontsUsedInSpreadsheetOrWorkbook.cs" >}}

##  **控制台输出**

这是使用给定的命令执行上述示例代码时的控制台输出[示例 Excel 文件](25395211.xlsx).

{{< highlight "java" >}}

Aspose.Cells.Font [ Calibri; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Arial; 10; Regular; Color [A=255, R=0, G=0, B=0] ]

Aspose.Cells.Font [ Calibri; 10; Bold; Color [Black] ]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=128, G=128, B=128] ]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Calibri; 36; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 20; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Calibri; 11; Italic; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [Black] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 12; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Dummy-Arial-X; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Arial-Y; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Arial-Z; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-I; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-II; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-III; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Calibri; 10.5; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 20; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104] ]

{{< /highlight >}}
