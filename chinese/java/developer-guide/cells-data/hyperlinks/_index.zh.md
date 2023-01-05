---
title: 将超链接插入 Excel 或 OpenOffice
linktitle: 管理超链接
type: docs
weight: 160
url: /zh/java/insert-hyperlinks-to-excel/
---
## **添加超链接到链接数据**
{{% alert color="primary" %}} 

超链接用于在两个实体之间创建链接。每个人都熟悉超链接的使用，尤其是在网站上。

使用 Aspose.Cells，开发人员可以在 Microsoft Excel 文件中创建不同种类的超链接。本主题讨论 Aspose.Cells 支持哪些类型的超链接以及如何在我们的 Excel 文件中使用它们。

{{% /alert %}} 
## **添加超链接**
使用 Aspose.Cells 可以将三种类型的超链接添加到单元格：

- [添加指向 URL 的链接](/cells/zh/java/working-with-hyperlinks-to-link-data/).
- [添加指向同一文件中另一个单元格的链接](/cells/zh/java/working-with-hyperlinks-to-link-data/).
- [添加指向外部文件的链接](/cells/zh/java/working-with-hyperlinks-to-link-data/).

Aspose.Cells 允许开发人员使用 API 或[设计师电子表格](/cells/zh/java/what-is-a-designer-spreadsheet/)（手动创建超链接并使用 Aspose.Cells 将它们导入其他电子表格的电子表格）。

Aspose.Cells提供了一个类，[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)表示 Microsoft Excel 文件。这[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[工作表集合](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)允许访问 Excel 文件中的每个工作表。工作表由[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级。这[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类提供了向 Excel 文件添加不同超链接的不同方法。
## **将链接添加到 URL**
这[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类包含一个[超级链接](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection)收藏。中的每一项[超级链接](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection)集合代表一个[超级链接](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink).通过调用[超级链接](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Hyperlinks)收藏的[添加](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)）方法。这[添加](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\))方法采用以下参数：

- Cell name，超链接将添加到的单元格的名称。
- Number of rows，这个超链接范围内的行数。
- Number of columns，这个超链接范围的列数
- 网址，网址地址。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURL-AddingLinkToURL.java" >}}


在上面的示例中，超链接被添加到空单元格中的 URL，**A1**.在这种情况下，如果单元格为空，则 URL 地址也会作为其值添加到该空单元格中。如果单元格不为空并且添加了超链接，则单元格的值看起来像纯文本。要使其看起来像超链接，请在该单元格上应用适当的格式设置。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURLNotEmpty-AddingLinkToURLNotEmpty.java" >}}



## **在同一文件中添加指向 Cell 的链接**
可以通过调用[超级链接](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection)收藏的[添加](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)）方法。这[添加](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)方法适用于内部和外部超链接。重载方法的一种版本采用以下参数：

- Cell name，超链接将添加到的单元格的名称。
- Number of rows，这个超链接范围内的行数。
- Number of columns，这个超链接范围内的列数。
- URL，目标单元格的地址。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToAnotherCell-AddingLinkToAnotherCell.java" >}}



## **添加指向外部文件的链接**
可以通过调用[超级链接](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection)收藏的[添加](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)）方法。这[添加](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\))方法采用以下参数：

- Cell name，超链接将添加到的单元格的名称。
- Number of rows，这个超链接范围内的行数。
- Number of columns，这个超链接范围内的列数。
- URL，目标地址，外部Excel文件。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToExternalFile-AddingLinkToExternalFile.java" >}}

## **推进主题**
- [添加图像超链接](/cells/zh/java/add-image-hyperlinks/)
- [检测超链接类型](/cells/zh/java/detect-hyperlink-type/)
- [编辑工作表的超链接](/cells/zh/java/editing-hyperlinks-of-worksheet/)
- [获取范围内的超链接](/cells/zh/java/get-hyperlinks-in-range/)


