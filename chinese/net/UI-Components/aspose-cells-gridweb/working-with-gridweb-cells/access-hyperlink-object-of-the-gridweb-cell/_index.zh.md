---
title: 访问GridWeb单元格的超链接对象
type: docs
weight: 100
url: /zh/net/aspose-cells-gridweb/access-hyperlink-object-of-the-gridweb-cell/
keywords: GridWeb, 超链接
description: 本文介绍了如何在GridWeb中处理超链接。
---

## **可能的使用场景**
您可以使用以下两种方法检查单元格是否包含超链接。如果单元格不包含超链接，这些方法将返回null；如果包含超链接，则会返回GridHyperlink对象。

- GridHyperlinkCollection.GetHyperlink(GridCell cell)
- GridHyperlinkCollection.GetHyperlink(int row, int column)
## **在新窗口或现有窗口中打开超链接**
If your excel file contains hyperlink which links to some URL like <http://wwww.aspose.com/> and you load it in GridWeb then the hyperlinks will be rendered with target attribute set to _blank. It means, when you will click the hyperlink in a GridWeb cell, it will open up in a new window instead of existing window. Please check the GridHyperlink.Target property in the following debug window. Besides, if you want to open the hyperlink in the existing window, then please set the GridHyperlink.Target to _self.

![todo:image_alt_text](access-hyperlink-object-of-the-gridweb-cell_1.png)
## **访问GridWeb单元格的超链接对象**
以下示例代码访问单元格A1的超链接。如果单元格A1包含超链接，则会返回GridHyperlink对象；否则，将返回null。
### **示例代码**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCellHyperlink.aspx-AccessHyperlink.cs" >}}
