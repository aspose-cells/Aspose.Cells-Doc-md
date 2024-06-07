---
title: 获取电子表格或工作簿中使用的字体列表
description: Aspose.Cells是一个用于处理电子表格文件的.NET库。它支持获取电子表格或工作簿中使用的字体列表，使用户能够获取文档中使用的字体信息。本文将展示如何使用Aspose.Cells库获取字体列表。
keywords: Aspose.Cells、电子表格、工作簿、字体、列表
type: docs
weight: 20
url: /zh/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **可能的使用场景**

通常需要了解工作簿中使用的字体以进行呈现。当您将工作簿转换为PDF或图像时，Aspose.Cells要求系统中安装所有所需的字体，或者位于您的**fonts目录**中。如果Aspose.Cells无法找到所需的字体，则会尝试用系统中存在的其他适当的字体替换您的实际字体。这不仅会导致PDF或图像的不良呈现，还会花费时间查找合适的字体。

为应对这种情况，您应该知道工作簿中使用的字体，然后在Windows环境下安装这些字体，或者在Windows或Linux环境下将其放在您的字体目录中。

Aspose.Cells提供了**[Workbook.GetFonts](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getfonts)** 方法，该方法返回工作簿或电子表格中使用的所有字体的列表。

## **获取电子表格或工作簿中使用的字体列表**

以下示例代码加载源Excel文件并检索其中使用的字体列表。其中包含一个虚拟工作表，用于说明目的添加了一些虚拟字体。当代码打印工作簿中所有字体时，还会打印这些虚拟字体。以下截图显示了[示例Excel文件](25395211.xlsx)及虚拟字体的列表。

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-GetListOfFontsUsedInSpreadsheetOrWorkbook.cs" >}}

## **控制台输出**

执行上述示例代码并使用给定的[样本Excel文件](25395211.xlsx)时，以下是控制台的输出。

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
