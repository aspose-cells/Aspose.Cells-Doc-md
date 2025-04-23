---
title: 在Excel或OpenOffice中插入超链接
linktitle: 管理超链接
type: docs
weight: 45
url: /zh/net/insert-hyperlinks-to-excel/
description: 如何在不使用 MS Excel 的情况下，使用 Aspose.Cells 库将超链接插入 Excel 文件
keywords: 在 Excel 中插入超链接，添加或插入超链接，添加或插入到 URL 的链接，在单元格中添加或插入链接，向外部文件添加链接
---

{{% alert color="primary" %}} 

超链接用于在两个实体之间创建链接。每个人都熟悉超链接的使用，特别是在网站上。
使用Aspose.Cells，开发人员可以在Microsoft Excel文件中创建不同类型的超链接。本主题讨论了Aspose.Cells支持哪些类型的超链接以及如何在我们的Excel文件中使用它们。

{{% /alert %}} 
## **添加超链接**
Aspose.Cells 允许开发人员使用 API 或设计者电子表格（手动创建超链接，然后使用 Aspose.Cells 将它们导入其他电子表格）向 Excel 文件添加超链接。

Aspose.Cells 提供了一个代表 Microsoft Excel 文件的 [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类。[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类包含了一个 [WorksheetCollection](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) 用于访问 Excel 文件中的每个工作表。工作表由 [Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类表示。[Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类提供了向 Excel 文件中添加不同超链接的不同方法。
## **添加指向URL的链接**
[Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类包含一个 [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) 集合。 [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) 集合中的每个项表示一个 [Hyperlink](https://reference.aspose.com/cells/net/aspose.cells/hyperlink)。通过调用 [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) 集合的 [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) 方法，可以向 URL 添加超链接。 [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) 方法采用以下参数:

- 单元格名称，超链接将添加到的单元格的名称。
- 行数，超链接范围中的行数。
- 列数，该超链接范围的列数
- URL，URL地址。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToURL-1.cs" >}}

{{% alert color="primary" %}} 

在上述示例中，在空单元格**A1**中添加了一个超链接。在这种情况下，如果单元格为空，则URL地址也会作为其值添加到该空单元格。如果单元格不为空并添加了超链接，则单元格的值看起来像普通文本。要使其看起来像超链接，请在该单元格上应用适当的格式设置。

{{% /alert %}} 
## **将链接添加到同一文件中的单元格**
通过调用 [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) 集合的 [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) 方法，可以向同一 Excel 文件的单元格添加超链接。 [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) 方法适用于内部和外部超链接。重载方法的一个版本采用以下参数:

- 单元格名称，将要添加超链接的单元格名称。
- 行数，超链接范围中的行数。
- 列数，超链接范围中的列数。
- URL，目标单元格的地址。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToAnotherCell-1.cs" >}}
## **向外部文件添加链接**
通过调用 [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) 集合的 [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) 方法，可以向外部 Excel 文件添加超链接。[Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) 方法采用以下参数:

- 单元格名称，超链接将添加到的单元格的名称。
- 行数，超链接范围中的行数。
- 列数，超链接范围中的列数。
- URL，目标外部Excel文件的地址。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToExternalFile-1.cs" >}}

## **高级主题**
- [添加图像超链接](/cells/zh/net/add-image-hyperlinks/)
- [检测超链接类型](/cells/zh/net/detect-hyperlink-type/)
- [编辑工作表的超链接](/cells/zh/net/editing-hyperlinks-of-worksheet/)
- [获取范围内的超链接](/cells/zh/net/get-hyperlinks-in-range/)

{{< app/cells/assistant language="csharp" >}}
