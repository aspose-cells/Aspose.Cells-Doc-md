---
title: 在 Excel 或 OpenOffice 中插入超链接
linktitle: 管理超链接
type: docs
weight: 45
url: /zh/python-net/insert-hyperlinks-to-excel/
description: 如何在不使用MS Excel的情况下使用Aspose.Cells for Python通过.NET库向Excel文件插入超链接。
keywords: Python Excel库，Python在Excel中插入超链接，Python添加或插入超链接，Python添加或插入URL的链接，Python添加或插入链接到单元格，Python添加链接到外部文件。
---

{{% alert color="primary" %}} 

超链接用于在两个实体之间创建链接。每个人都熟悉超链接的使用，特别是在网站上。
使用Aspose.Cells for Python通过.NET，开发人员可以在Microsoft Excel文件中创建不同类型的超链接。本主题讨论了Aspose.Cells for Python通过.NET支持哪些类型的超链接以及如何在Excel文件中使用它们。

{{% /alert %}} 
## **如何添加超链接**
通过Aspose.Cells for Python通过.NET可以使用API或设计师表格（手动创建超链接的电子表格，然后使用Aspose.Cells for Python通过.NET将它们导入其他电子表格）向Excel表格添加超链接。

Aspose.Cells for Python通过.NET提供一个类，[工作簿](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)，表示Microsoft Excel文件。[工作簿](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类包含一个[WorksheetCollection](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection)，允许访问Excel文件中的每个工作表。工作表由[Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类表示。[Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类提供不同的方法来向Excel文件添加不同类型的超链接。

## **如何添加链接到URL**
[Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类包含[超链接](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/)集合。 [超链接](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/)集合中的每个项目表示一个[超链接](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink)。通过调用 [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str)方法，可以向URL添加超链接。[add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str)方法接受以下参数：

- 单元格名称，将要添加超链接的单元格名称。
- 行数，此超链接范围中的行数。
- 列数，此超链接范围中的列数。
- URL，URL 地址。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToURL-1.py" >}}

{{% alert color="primary" %}} 

在上面的示例中，在空单元格**A1** 中添加了一个超链接。在这种情况下，如果一个单元格为空，则 URL 地址也会作为其值添加到该空单元格中。如果单元格不为空并添加了超链接，则单元格的值会显示为普通文本。要使其看起来像超链接，请在该单元格上应用适当的格式设置。

{{% /alert %}} 

## **如何向同一文件的单元格添加链接**
通过调用[超链接](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/)集合的[add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str)方法，可以在同一Excel文件中向单元格添加超链接。 [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str)方法针对内部和外部超链接均有效。重载方法的一个版本接受以下参数：

- 单元格名称，将要添加超链接的单元格名称。
- 行数，此超链接范围中的行数。
- 列数，此超链接范围中的列数。
- URL，目标单元格的地址。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToAnotherCell-1.py" >}}

## **如何向外部文件添加链接**
通过调用[超链接](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/)集合的[add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str)方法，可以向外部Excel文件添加超链接。 [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str)方法接受以下参数：

- 单元格名称，将要添加超链接的单元格名称。
- 行数，此超链接范围中的行数。
- 列数，此超链接范围中的列数。
- URL，目标的地址，外部 Excel 文件。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToExternalFile-1.py" >}}

## **高级主题**
- [添加图像超链接](/cells/zh/python-net/add-image-hyperlinks/)
- [检测超链接类型](/cells/zh/python-net/detect-hyperlink-type/)
- [编辑工作表的超链接](/cells/zh/python-net/editing-hyperlinks-of-worksheet/)
- [获取范围内的超链接](/cells/zh/python-net/get-hyperlinks-in-range/)

