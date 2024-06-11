---
title: 在Excel或OpenOffice中插入超链接
linktitle: 管理超链接
type: docs
weight: 160
url: /zh/java/insert-hyperlinks-to-excel/
---

## **添加超链接以链接数据**
{{% alert color="primary" %}} 

超链接用于在两个实体之间创建链接。每个人都熟悉超链接的使用，特别是在网站上。

使用Aspose.Cells，开发人员可以在Microsoft Excel文件中创建不同类型的超链接。本主题讨论了Aspose.Cells支持哪些类型的超链接以及如何在我们的Excel文件中使用它们。

{{% /alert %}} 
## **添加超链接**
使用Aspose.Cells可以向单元格添加三种类型的超链接：

- [添加指向URL的链接](/cells/zh/java/working-with-hyperlinks-to-link-data/).
- [添加指向同一文件中其他单元格的链接](/cells/zh/java/working-with-hyperlinks-to-link-data/).
- [添加指向外部文件的链接](/cells/zh/java/working-with-hyperlinks-to-link-data/).

Aspose.Cells允许开发人员通过使用API或[设计者电子表格](/cells/zh/java/what-is-a-designer-spreadsheet/)（手动创建超链接，并使用Aspose.Cells将它们导入其他电子表格）向Excel文件中添加超链接。

Aspose.Cells提供一个表示Microsoft Excel文件的类，即[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)，[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)，它允许访问Excel文件中的每个工作表。工作表由[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类表示。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类提供了向Excel文件添加不同超链接的不同方法。
## **添加指向URL的链接**
[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类包含一个[Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection)集合。[Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection)集合中的每一项都代表一个[Hyperlink](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink)。通过调用[Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Hyperlinks)集合的[Add ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\))方法可以向URL添加超链接。[Add ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\))方法接受以下参数：

- 单元格名称，超链接将添加到的单元格的名称。
- 行数，超链接范围中的行数。
- 列数，此超链接范围的列数
- URL，URL地址。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURL-AddingLinkToURL.java" >}}


在上面的示例中，将超链接添加到一个空单元格**A1**的URL。在这种情况下，如果单元格为空，则URL地址也作为其值添加到该空单元格。如果单元格不为空且添加了超链接，则单元格的值看起来像纯文本。要使其看起来像超链接，请对该单元格应用适当的格式设置。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURLNotEmpty-AddingLinkToURLNotEmpty.java" >}}



## **将链接添加到同一文件中的单元格**
可以通过调用 [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) 集合的 [Add ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\))方法向同一 Excel 文件中的单元格添加超链接。Add 方法适用于内部和外部超链接。其中一个重载的方法版本接受以下参数:

- 单元格名称，超链接将添加到的单元格的名称。
- 行数，超链接范围中的行数。
- 列数，超链接范围中的列数。
- URL，目标单元格的地址。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToAnotherCell-AddingLinkToAnotherCell.java" >}}



## **向外部文件添加链接**
可以通过调用 [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) 集合的 [Add ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\))方法向外部 Excel 文件添加超链接。Add 方法接受以下参数:

- 单元格名称，超链接将添加到的单元格的名称。
- 行数，超链接范围中的行数。
- 列数，超链接范围中的列数。
- URL，目标外部Excel文件的地址。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToExternalFile-AddingLinkToExternalFile.java" >}}

## **高级主题**
- [添加图像超链接](/cells/zh/java/add-image-hyperlinks/)
- [检测超链接类型](/cells/zh/java/detect-hyperlink-type/)
- [编辑工作表的超链接](/cells/zh/java/editing-hyperlinks-of-worksheet/)
- [获取范围内的超链接](/cells/zh/java/get-hyperlinks-in-range/)


