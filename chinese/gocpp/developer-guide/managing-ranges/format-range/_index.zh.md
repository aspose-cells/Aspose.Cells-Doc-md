---
title: 用Golang通过C++设置范围格式
linktitle: 格式化范围
type: docs
weight: 105
url: /zh/go-cpp/how-to-format-a-range/
description: 学习如何使用Aspose.Cells结合Golang通过C++对Excel中的范围进行格式化。以编程方式应用样式、字体和颜色到单元格范围。
---

## **可能的使用场景**
当您需要对一组范围应用样式时，可以使用范围格式化。

## **如何在Excel中格式化范围**

要在Excel中格式化一系列单元格，您可以使用Excel提供的内置格式选项。以下是如何直接在Excel中格式化一系列单元格的方法：

1. 打开Excel并打开包含要格式化的范围的工作簿。

2. 选择您要格式化的单元格范围。您可以单击并拖动以选择范围，或者您可以使用诸如Shift+箭头键之类的键盘快捷键来扩展选择。

3. 选择范围后，右键单击所选范围，然后从上下文菜单中选择“格式单元格”。或者，您可以转到ExcelRibbon中的“主页”选项卡，在“单元格”组中的“格式”下拉菜单中单击“格式单元格”进行选择。

4. “格式单元格”对话框将会出现。在这里，您可以选择各种格式选项来应用于所选范围。例如，您可以更改字体样式、字体大小、字体颜色、数字格式、边框、背景颜色等。在对话框中探索不同的标签以访问各种格式选项。

5. 在进行所需的格式更改后，单击“确定”按钮以将格式应用于所选范围。

## **如何使用C++格式化范围**

使用Aspose.Cells格式化范围，可以使用以下方法：
1. [Range.ApplyStyle(Style style, StyleFlag flag)](https://reference.aspose.com/cells/go-cpp/range/applystyle/)
2. [Range.SetStyle(Style style)](https://reference.aspose.com/cells/go-cpp/range/setstyle_style_bool/)

## **示例代码**
在此示例中，我们创建了一个Excel工作簿，添加了一些示例数据，访问第一个工作表，并定义了两个范围（"A1:C3" 和 "A4:C5"）。然后，我们创建新的样式，设置各种格式选项（如字体颜色、加粗），并将样式应用到范围。最后，将工作簿保存到新文件中。
<br>
![todo:image_alt_text](format-range.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormatRange.go" >}}
