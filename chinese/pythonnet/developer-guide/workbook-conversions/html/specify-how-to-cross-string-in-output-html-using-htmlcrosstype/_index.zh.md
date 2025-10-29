---
title: 使用HtmlCrossType指定输出HTML中如何交叉字符串
type: docs
weight: 140
url: /zh/python-net/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---

## **可能的使用场景**

当单元格包含文本或字符串但大于单元格宽度时, 如果下一列中的单元格为空或空白, 则字符串将溢出. 将Excel文件保存为HTML时, 您可以使用[**HtmlCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype)枚举来控制此溢出. 具有以下值:

- **HtmlCrossType.DEFAULT**：显示方式类似MS Excel，取决于下一个单元格。如果下一个单元格为空，则字符串会交叉或被截断。

- **HtmlCrossType.MS_EXPORT**：显示方式类似MS Excel导出HTML的方式。

- **HtmlCrossType.CROSS**：显示HTML交叉字符串，创建大型HTML文件的性能比设置为 Default 或 FitToCell 快十倍以上。

- **HtmlCrossType.CROSS_HIDE_RIGHT**：显示HTML交叉字符串，隐藏右侧的字符串，适用于文本重叠的情况。

- **HtmlCrossType.FIT_TO_CELL**：只显示单元格宽度内的字符串。

## **使用HtmlCrossType指定输出HTML中如何交叉字符串**

以下示例代码加载了[sample Excel file](51740732.xlsx)并通过指定不同的[**HtmlCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype)将其保存为HTML格式。请下载使用该代码生成的[output HTMLs](51740734.zip)。示例Excel文件包含了带有红色边框的图片，如此屏幕截图所示，展示出输出HTML上[**HtmlCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype)值的效果。

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-SpecifyHtmlCrossTypeInOutputHTML.py" >}}
{{< app/cells/assistant language="python-net" >}}
