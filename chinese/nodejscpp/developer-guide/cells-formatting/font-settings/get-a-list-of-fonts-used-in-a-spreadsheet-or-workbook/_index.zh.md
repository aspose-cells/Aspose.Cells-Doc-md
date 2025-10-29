---
title: 获取电子表格或工作簿中使用的字体列表
linktitle: 获取电子表格或工作簿中使用的字体列表
description: 学习如何使用 Aspose.Cells for Node.js via C++ 获取电子表格或工作簿中使用的字体列表。本文将展示如何从文档中检索字体信息。
keywords: Aspose.Cells，Node.js 通过 C++，电子表格，工作簿，字体，列表
type: docs
weight: 20
url: /zh/nodejs-cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **可能的使用场景**

通常需要知道工作簿中使用的字体，以便进行呈现。当您将工作簿转换为PDF或图像时，Aspose.Cells要求系统中安装了或者位于您的**字体目录**中存在所有需要的字体。如果Aspose.Cells无法找到需要的字体，它将尝试用系统中存在或者位于您的字体目录中的其他合适的字体替代您的实际字体。这不仅导致PDF或图像呈现不理想，还需要处理时间来找到合适的字体。

为了处理这种情况，你应该了解你的工作簿使用了哪些字体，然后在 Windows 环境下将这些字体安装到系统中，或者在 Windows 或 Linux 环境中将字体放置到你的字体目录中。

 Aspose.Cells for Node.js via C++ 提供 [**Workbook.getFonts**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getFonts--) 方法，返回工作簿或电子表格中使用的所有字体列表。

## **获取电子表格或工作簿中使用的字体列表**

以下示例代码加载源Excel文件并检索其中使用的字体列表。其中有一个虚拟工作表，用于说明目的而添加了一些虚拟字体。当代码打印工作簿中的所有字体时，它还会打印这些虚拟字体。以下屏幕截图显示了[示例Excel文件](25395211.xlsx)以及虚拟字体的列表。

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-GetFontsListUsedInWorkbook.js" >}}


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
{{< app/cells/assistant language="nodejs-cpp" >}}
