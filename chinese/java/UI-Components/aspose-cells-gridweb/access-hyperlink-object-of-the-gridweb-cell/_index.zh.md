---
title: 访问 GridWeb 的超链接对象 Cell
type: docs
weight: 60
url: /zh/java/access-hyperlink-object-of-the-gridweb-cell/
---
##  **可能的使用场景**
您可以使用以下两种方法检查单元格是否包含超链接。如果单元格不包含超链接，这些方法将返回 null；如果单元格包含超链接，则将返回 GridHyperlink 对象。

- GridHyperlinkCollection.getHyperlink(GridCell 单元格)
- GridHyperlinkCollection.getHyperlink(int 行,int 列)
##  **在新窗口或现有窗口中打开超链接**
如果您的 Excel 文件包含链接到某些 URL 的超链接，例如<http://wwww.aspose.com/>然后将其加载到 GridWeb 中，然后将呈现超链接，并将目标属性设置为 _blank。这意味着，当您单击 GridWeb 单元格中的超链接时，它将在新窗口而不是现有窗口中打开。另外，如果您想在现有窗口中打开超链接，请将GridHyperlink.Target设置为_self。
##  **访问 GridWeb 的超链接对象 Cell**
以下示例代码访问单元格 A1 的超链接。如果单元格 A1 包含超链接，则返回 GridHyperlink 对象，否则返回 null。
##  **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessHyperlinkobjectofGridWebCell-AccessHyperlinkobjectofGridWebCell.jsp" >}}
