---
title: 在 Excel 或 OpenOffice 中插入超链接
linktitle: 管理超链接
type: docs
weight: 45
url: /zh/net/insert-hyperlinks-to-excel/
description: 如何使用 Aspose.Cells 库在 Excel 文件中插入超链接，而不使用 MS Excel。
keywords: 在 Excel 中插入超链接，添加或插入超链接，添加或插入到 URL 的链接，添加或插入到单元格的链接，添加到外部文件的链接
---

{{% alert color="primary" %}} 

超链接用于在两个实体之间创建链接。每个人都熟悉超链接的使用，特别是在网站上。
使用 Aspose.Cells，开发人员可以在 Microsoft Excel 文件中创建不同类型的超链接。本主题讨论了 Aspose.Cells 支持哪些类型的超链接以及如何在 Excel 文件中使用它们。

{{% /alert %}} 
## **添加超链接**
Aspose.Cells 允许开发人员通过 API 或设计人员电子表格（手动创建超链接并使用 Aspose.Cells 将它们导入到其他电子表格）将超链接添加到 Excel 文件中。

Aspose.Cells 提供一个表示 Microsoft Excel 文件的 [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类。[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类包含一个允许访问 Excel 文件中每个工作表的 [WorksheetCollection](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)。工作表由 [Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类表示。[Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类提供了将不同类型的超链接添加到 Excel 文件中的不同方法。
## **添加超链接到URL**
Worksheet 类包含 Hyperlinks 集合。 Hyperlinks 集合中的每个项表示一个超链接。通过调用 Hyperlinks 集合的 Add 方法可以将超链接添加到 URL。Add 方法接受以下参数:

- 单元格名称，将要添加超链接的单元格名称。
- 行数，此超链接范围中的行数。
- 列数，此超链接范围中的列数。
- URL，URL 地址。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToURL-1.cs" >}}

{{% alert color="primary" %}} 

在上面的示例中，在空单元格**A1** 中添加了一个超链接。在这种情况下，如果一个单元格为空，则 URL 地址也会作为其值添加到该空单元格中。如果单元格不为空并添加了超链接，则单元格的值会显示为普通文本。要使其看起来像超链接，请在该单元格上应用适当的格式设置。

{{% /alert %}} 
## **将链接添加到同一文件中的单元格**
可以通过调用 Hyperlinks 集合的 Add 方法在同一 Excel 文件中的单元格中添加超链接。Add 方法适用于内部和外部超链接。重载方法的一个版本接受以下参数:

- 单元格名称，将要添加超链接的单元格名称。
- 行数，此超链接范围中的行数。
- 列数，此超链接范围中的列数。
- URL，目标单元格的地址。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToAnotherCell-1.cs" >}}
## **将链接添加到外部文件**
可以通过调用 Hyperlinks 集合的 Add 方法将超链接添加到外部 Excel 文件中。Add 方法接受以下参数:

- 单元格名称，将要添加超链接的单元格名称。
- 行数，此超链接范围中的行数。
- 列数，此超链接范围中的列数。
- URL，目标的地址，外部 Excel 文件。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToExternalFile-1.cs" >}}

## **高级主题**
- [添加图像超链接](/cells/zh/net/add-image-hyperlinks/)
- [检测超链接类型](/cells/zh/net/detect-hyperlink-type/)
- [编辑工作表的超链接](/cells/zh/net/editing-hyperlinks-of-worksheet/)
- [获取范围内的超链接](/cells/zh/net/get-hyperlinks-in-range/)

