---
title: 使用 Golang 通过 C++ 获取电子表格或工作簿中使用的字体列表
linktitle: 获取字体列表
description: Aspose.Cells 是一个用于操作电子表格文件的 C++ 库。它支持获取在电子表格或工作簿中使用的字体列表，允许用户获取文档中所用字体信息。本文将介绍如何使用 Aspose.Cells 库获取字体列表。
keywords: Aspose.Cells，电子表格，工作簿，字体，列表
type: docs
weight: 20
url: /zh/go-cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **可能的使用场景**

通常需要知道工作簿中使用的字体，以便进行呈现。当您将工作簿转换为PDF或图像时，Aspose.Cells要求系统中安装了或者位于您的**字体目录**中存在所有需要的字体。如果Aspose.Cells无法找到需要的字体，它将尝试用系统中存在或者位于您的字体目录中的其他合适的字体替代您的实际字体。这不仅导致PDF或图像呈现不理想，还需要处理时间来找到合适的字体。

为了处理这种情况，您应该知道工作簿中使用的字体，然后在Windows环境中安装这些字体，或者在Windows或Linux环境中将其放置在您的字体目录中。

Aspose.Cells 提供了 [**Workbook.GetFonts**](https://reference.aspose.com/cells/go-cpp/workbook/getfonts/) 方法，用于返回工作簿或电子表格中使用的所有字体列表。

## **获取电子表格或工作簿中使用的字体列表**

以下示例代码加载源Excel文件并检索其中使用的字体列表。其中有一个虚拟工作表，用于说明目的而添加了一些虚拟字体。当代码打印工作簿中的所有字体时，它还会打印这些虚拟字体。以下屏幕截图显示了[示例Excel文件](25395211.xlsx)以及虚拟字体的列表。

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetAListOfFontsUsedInASpreadsheetOrWorkbook.go" >}}
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
