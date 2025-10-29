---
title: 获取电子表格或工作簿中使用的字体列表
description: Aspose.Cells 是一个用于处理电子表格文件的 Python 库。它支持获取电子表格或工作簿中使用的字体列表，让用户可以获取文档中的字体信息。本文将介绍如何使用 Aspose.Cells for Python via .NET 库获取字体列表。
keywords: Aspose.Cells for Python via .NET，电子表格，工作簿，字体，列表
type: docs
weight: 20
url: /zh/python-net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **可能的使用场景**

通常需要知道您的工作簿中使用了哪些字体以供渲染。当您将工作簿转换为PDF或图像时，Aspose.Cells for Python via .NET 要求系统中已安装所有所需字体或存放在您的**字体目录**中。如果 Aspose.Cells for Python via .NET 无法找到所需字体，它会尝试用系统或字体目录中存在的其他合适字体替代您的实际字体。这不仅会导致PDF或图像渲染效果不理想，还会增加查找合适字体的处理时间。

为了处理这种情况，您应该知道工作簿中使用的字体，然后在Windows环境中安装这些字体，或者在Windows或Linux环境中将其放置在您的字体目录中。

Aspose.Cells for Python via .NET 提供 [**Workbook.get_fonts**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/get_fonts) 方法，可返回工作簿或电子表格中使用的所有字体列表。

## **获取电子表格或工作簿中使用的字体列表**

以下示例代码加载源Excel文件并检索其中使用的字体列表。其中有一个虚拟工作表，用于说明目的而添加了一些虚拟字体。当代码打印工作簿中的所有字体时，它还会打印这些虚拟字体。以下屏幕截图显示了[示例Excel文件](25395211.xlsx)以及虚拟字体的列表。

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-GetListOfFontsUsedInSpreadsheetOrWorkbook.py" >}}

## **控制台输出**

以下是执行给定[示例Excel文件](25395211.xlsx)时上述示例代码的控制台输出。

{{< highlight java >}}

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

{{< app/cells/assistant language="python-net" >}}
