---
title: 访问GridWeb单元格的超链接对象
type: docs
weight: 60
url: /zh/java/access-hyperlink-object-of-the-gridweb-cell/
---

## **可能的使用场景**
您可以使用以下两种方法来检查单元格是否包含超链接。如果单元格不包含超链接，这些方法将返回null；如果包含超链接，则会返回GridHyperlink对象。

- GridHyperlinkCollection.getHyperlink(GridCell cell)
- GridHyperlinkCollection.getHyperlink(int row,int column)
## **在新窗口或现有窗口中打开超链接**
If your excel file contains hyperlink which links to some URL like <http://wwww.aspose.com/> and you load it in GridWeb then the hyperlinks will be rendered with target attribute set to _blank. It means, when you will click the hyperlink in a GridWeb cell, it will open up in a new window instead of the existing window. Besides, if you want to open the hyperlink in the existing window, then please set the GridHyperlink.Target to _self.
## **访问GridWeb Cell的超链接对象**
以下示例代码访问A1单元格的超链接。如果A1单元格包含超链接，则会返回GridHyperlink对象；否则将返回null。
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessHyperlinkobjectofGridWebCell-AccessHyperlinkobjectofGridWebCell.jsp" >}}
