---
title: 使用HtmlCrossType指定输出HTML中如何交叉字符串
type: docs
weight: 140
url: /zh/net/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---

## **可能的使用场景**

当单元格包含文本或字符串但大于单元格宽度时, 如果下一列中的单元格为空或空白, 则字符串将溢出. 将Excel文件保存为HTML时, 您可以使用[**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype)枚举来控制此溢出. 具有以下值:

- **HtmlCrossType.Default**: 与MS Excel显示类似, 取决于下一个单元格. 如果下一个单元格为空, 字符串将跨越或被截断.

- **HtmlCrossType.MSExport**: 以MS Excel导出HTML的方式显示字符串.

- **HtmlCrossType.Cross**: 显示HTML交叉字符串, 对于创建大型HTML文件性能要比将值设置为Default或FitToCell快十倍以上.

- **HtmlCrossType.FitToCell**: 仅在单元格宽度内显示字符串.

## **使用HtmlCrossType指定输出HTML中如何交叉字符串**

以下示例代码加载了[sample Excel file](51740732.xlsx)并通过指定不同的[**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype)将其保存为HTML格式。请下载使用该代码生成的[output HTMLs](51740734.zip)。示例Excel文件包含了带有红色边框的图片，如此屏幕截图所示，展示出输出HTML上[**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype)值的效果。

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.cs" >}}
{{< app/cells/assistant language="csharp" >}}
