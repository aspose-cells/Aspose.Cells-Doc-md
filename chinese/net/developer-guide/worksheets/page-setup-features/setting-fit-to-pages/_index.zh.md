---
title: 如何将Excel打印为宽度和高度适应的页面
type: docs
weight: 200
url: /zh/net/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: 本文将展示如何使用Aspose.Cells库设置 FitToPagesWide 和 FitToPagesTall。
keywords: 在C#中如何设置FitToPagesWide和FitToPagesTall，如何在C#中添加FitToPagesWide和FitToPagesTall，如何在Excel中设置FitToPagesWide和FitToPagesTall，如何清除Excel中的FitToPagesWide和FitToPagesTall，如何将Excel打印为宽和高适应的页面，如何将工作表作为一页打印，如何在一页中打印工作表的所有列。
---

## **介绍**

FitToPagesWide和FitToPagesTall设置用于电子表格应用（如Microsoft Excel），用于控制打印时电子表格的缩放方式。这些设置确保你的打印输出在水平和垂直方向上都在指定的页数内。以下是每个设置的详细说明：

1. FitToPagesWide：此设置指定打印输出应适合的页宽。例如，将FitToPagesWide设置为1，表示内容缩放至适合一页宽，无论电子表格有多宽。
1. 适合页面高度：该设置指定打印输出应适应的页面总数。例如，将适合页面高度设置为1意味着内容将缩放以适应单个页面高度，无论行数多少。

## **为什么使用适合页面宽度和高度**
以下是设置适合页面宽度和高度的一些原因：
1. 控制打印布局：通过指定页面宽度和高度的页数，可以确保打印的文档易于阅读且布局合理，没有列或行被尴尬地拆分到不同的页面上。
1. 一致性：如果你需要打印多个工作表或报告，使用这些设置可以帮助保持格式一致，使打印的文档更易于比较和分析。
1. 专业呈现：正确缩放和适应内容到指定页面数可以使你的数据呈现更专业、更精致。

## **如何在Excel中将文件打印为宽度和高度都适合的页面**

要在Microsoft Excel中设置适合页面宽度和高度的设置，请按照以下步骤操作：

1. 打开你的Excel工作簿，转到你想打印的工作表。
1. 转到功能区上的页面布局标签。
1. 在页面设置组中，点击右下角的小箭头以打开页面设置对话框。
1. 在页面设置对话框中，转到页面标签。
1. 在缩放部分，选择“适合”选项，然后指定你想要的宽度和高度的页面数：在第一个框中输入你想要的宽度页面数（适合x页宽），在第二个框中输入你想要的高度页面数（适合y页高）。
<br>
<img src="2.png" width=60% />

1. 点击确定以应用设置。


## **如何使用Aspose.Cells将Excel的宽度和高度适合页面打印**

要在指定工作表中设置FitToPagesWide和FitToPagesTall：首先加载[示例文件](input.xlsx)，然后修改[**Worksheet.PageSetup.FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/fittopagestall/)和[**Worksheet.PageSetup.FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/fittopageswide/)属性的[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/)对象以实现目标工作表。以下是C#示例：

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-PageSetup-set-FitToPagesWide-FitToPagesTall.cs" >}}

输出结果：
<br>
<img src="1.png" width=60% />


## **如何使用Aspose.Cells将工作表打印为一页**

要打印工作表为一页：首先加载[示例文件](sample.xlsx)，然后设置[**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/)对象的[**PdfSaveOptions.OnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/onepagepersheet/)属性。以下是C#示例：

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-PageSetup-OnePagePerSheet.cs" >}}

输出结果：
<br>
<img src="3.png" width=60% />


## **如何使用Aspose.Cells将工作表的所有列打印在一页中**

要在一页中打印工作表所有列：首先加载[示例文件](sample.xlsx)，然后设置[**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/)对象的[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/allcolumnsinonepagepersheet/)属性。以下是C#示例：

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-PageSetup-AllColumnsInOnePagePerSheet.cs" >}}

输出结果：
<br>
<img src="4.png" width=60% />
{{< app/cells/assistant language="csharp" >}}
