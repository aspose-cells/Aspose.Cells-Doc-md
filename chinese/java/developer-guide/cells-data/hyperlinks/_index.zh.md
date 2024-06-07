---
title: 在 Excel 或 OpenOffice 中插入超链接
linktitle: 管理超链接
type: docs
weight: 160
url: /zh/java/insert-hyperlinks-to-excel/
---

## **添加超链接以链接数据**
{{% alert color="primary" %}} 

超链接用于在两个实体之间创建链接。每个人都熟悉超链接的使用，特别是在网站上。

使用 Aspose.Cells，开发人员可以在 Microsoft Excel 文件中创建不同类型的超链接。本主题讨论了 Aspose.Cells 支持哪些类型的超链接以及如何在 Excel 文件中使用它们。

{{% /alert %}} 
## **添加超链接**
使用Aspose.Cells可以向单元格添加三种类型的超链接:

- [添加到URL的链接](/cells/zh/java/working-with-hyperlinks-to-link-data/)
- [添加到同一文件中的另一个单元格的链接](/cells/zh/java/working-with-hyperlinks-to-link-data/)
- [添加到外部文件的链接](/cells/zh/java/working-with-hyperlinks-to-link-data/)

Aspose.Cells允许开发人员通过使用API或[设计器电子表格](/cells/zh/java/what-is-a-designer-spreadsheet/)（手动创建超链接并使用Aspose.Cells将其导入其他电子表格）向Excel文件添加超链接。

Aspose.Cells提供了一个表示Microsoft Excel文件的[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)，允许访问Excel文件中的每个工作表。工作表由[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类表示。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类提供不同的方法来向Excel文件添加不同的超链接。
## **添加超链接到URL**
[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类包含一个[Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection)集合。[Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection)集合中的每个项目表示一个[Hyperlink](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink)。通过调用[Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Hyperlinks)集合的[Add ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\))方法向URL添加超链接。[Add ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\))方法的参数如下

- 单元格名称，将要添加超链接的单元格名称。
- 行数，此超链接范围中的行数。
- 列数，此超链接范围的列数
- URL，URL 地址。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURL-AddingLinkToURL.java" >}}


在上面的示例中，向空单元格**A1**添加了一个超链接。在这种情况下，如果单元格为空，则URL地址也将作为其值添加到该空单元格中。如果单元格不为空且添加了超链接，则单元格的值看起来像纯文本。为使其看起来像超链接，请在该单元格上应用适当的格式设置。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURLNotEmpty-AddingLinkToURLNotEmpty.java" >}}



## **将链接添加到同一文件中的单元格**
可以通过调用[Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection)集合的[Add ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\))方法在同一Excel文件中向单元格添加超链接。[Add ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\))方法适用于内部和外部超链接。重载方法的一个版本需要以下参数

- 单元格名称，将要添加超链接的单元格名称。
- 行数，此超链接范围中的行数。
- 列数，此超链接范围中的列数。
- URL，目标单元格的地址。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToAnotherCell-AddingLinkToAnotherCell.java" >}}



## **将链接添加到外部文件**
可以通过通过调用[Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection)集合的[Add ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\))方法向外部Excel文件添加超链接。[Add ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\))方法接受以下参数

- 单元格名称，将要添加超链接的单元格名称。
- 行数，此超链接范围中的行数。
- 列数，此超链接范围中的列数。
- URL，目标的地址，外部 Excel 文件。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToExternalFile-AddingLinkToExternalFile.java" >}}

## **高级主题**
- [添加图像超链接](/cells/zh/java/add-image-hyperlinks/)
- [检测超链接类型](/cells/zh/java/detect-hyperlink-type/)
- [编辑工作表的超链接](/cells/zh/java/editing-hyperlinks-of-worksheet/)
- [获取范围内的超链接](/cells/zh/java/get-hyperlinks-in-range/)


