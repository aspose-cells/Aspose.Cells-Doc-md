---
title: 在用Golang通过C++保存为HTML时，使用CrossHideRight隐藏叠加内容
linktitle: 使用 CrossHideRight 在保存为 HTML 时隐藏重叠内容
type: docs
weight: 100
url: /zh/go-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
description: 使用Aspose.Cells在C++中通过CrossHideRight隐藏覆盖内容以保存为HTML。
---

## **可能的使用场景**

将Excel文件保存为HTML时，可以为单元格字符串指定不同的交叉类型。默认情况下，Aspose.Cells根据微软Excel生成HTML，但当你将交叉类型更改为[**CrossHideRight**](https://reference.aspose.com/cells/go-cpp/htmlcrosstype)时，它会隐藏所有在单元格右侧被覆盖或重叠的字符串。

## **在保存为Html时使用CrossHideRight隐藏重叠内容**

以下示例代码加载[样本Excel文件](64716894.xlsx)，并在将[**HtmlSaveOptions.GetHtmlCrossStringType()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/gethtmlcrossstringtype/)设置为[**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype)后将其保存为[输出HTML](64716893.zip)。截图说明了[**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype)如何影响默认输出的HTML。

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HidingOverlaidContentWithCrosshiderightWhileSavingToHtml.go" >}}
