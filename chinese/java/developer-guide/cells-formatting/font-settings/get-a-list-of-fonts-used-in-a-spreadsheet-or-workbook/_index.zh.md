---
title: 获取电子表格或工作簿中使用的字体列表
type: docs
weight: 20
url: /zh/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---
## **可能的使用场景**

通常需要了解工作簿中用于呈现目的的字体。当您将工作簿转换为 PDF 或图像时，Aspose.Cells 要求所有需要的字体都安装在您的系统上或出现在您的**字体目录**.如果 Aspose.Cells 找不到所需的字体，它会尝试用系统或字体目录中存在的其他合适的字体替换它，并且可以替换您的实际字体。这不仅会导致 PDF 或图像出现不需要的渲染，而且会花费处理时间来寻找合适的字体。

为了处理这种情况，您应该知道您的工作簿使用的是什么字体，然后在 Windows 环境的情况下在您的系统上安装这些字体，或者在 Windows 或 Linux 环境的情况下将它们放在您的字体目录中。

Aspose.Cells 提供了[工作簿.getFonts()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#getFonts()) 方法返回工作簿或电子表格中使用的所有字体的列表。

## **获取电子表格或工作簿中使用的字体列表**

以下示例代码加载源 excel 文件并检索其中使用的字体列表。它有一个虚拟工作表，其中添加了一些用于说明目的的虚拟字体。当代码打印工作簿中的所有字体时，它还会打印那些虚拟字体。以下屏幕截图显示了[示例 excel 文件](sampleGetFonts.xlsx)以及如何列出虚拟字体。

![待办事项：图片_替代_文本](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetFontsUsedinWorkbook-GetFontsUsedinWorkbook.java" >}}

## **控制台输出**

这是使用给定的执行时上述示例代码的控制台输出[示例 excel 文件](sampleGetFonts.xlsx).

{{< highlight "java" >}}

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Arial; 10.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Calibri; 10.0; Bold; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Calibri; 10.0; Regular; com.aspose.cells.Color@ff808080 ]Aspose.Cells.Font [ Calibri; 10.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Bold; com.aspose.cells.Color@ffffffff ]Aspose.Cells.Font [ Calibri; 36.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 20.0; Bold; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ffffffff ]Aspose.Cells.Font [ Calibri; 11.0; Italic; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Bold; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff294a4e ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff294a4e ]Aspose.Cells.Font [ Calibri; 12.0; Regular; com.aspose.cells.Color@ff294a4e ]Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff294a4e ]Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ffffffff ]Aspose.Cells.Font [ Dummy-Arial-X; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Arial-Y; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Arial-Z; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Times-I; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Times-II; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Times-III; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Calibri; 10.5; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 20.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff376268 ]{{< /highlight >}}
