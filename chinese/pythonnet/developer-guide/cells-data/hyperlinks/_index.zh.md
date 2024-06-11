---
title: 在Excel或OpenOffice中插入超链接
linktitle: 管理超链接
type: docs
weight: 45
url: /zh/python-net/insert-hyperlinks-to-excel/
description: 如何使用Aspose.Cells for Python via .NET库在Excel文件中插入超链接而无需MS Excel。
keywords: Python Excel库, Python在Excel中插入超链接, Python添加或插入超链接, Python添加或插入到URL的链接, Python向单元格添加或插入链接, Python向外部文件添加链接
---

{{% alert color="primary" %}} 

超链接用于在两个实体之间创建链接。每个人都熟悉超链接的使用，特别是在网站上。
使用Aspose.Cells for Python via .NET，开发人员可以在Microsoft Excel文件中创建不同类型的超链接。本主题讨论了Aspose.Cells for Python via .NET支持哪些类型的超链接以及如何在我们的Excel文件中使用它们。

{{% /alert %}} 
## **如何添加超链接**
Aspose.Cells for Python via .NET允许开发人员使用API或设计者电子表格（手动创建超链接并使用Aspose.Cells for Python via .NET将它们导入其他电子表格）向Excel文件添加超链接。

Aspose.Cells for Python via .NET提供了一个类[Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)，表示Microsoft Excel文件。[Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类包含一个[WorksheetCollection](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection)，允许访问Excel文件中的每个工作表。工作表由[Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类表示。[Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类提供不同方法来向Excel文件添加不同的超链接。

## **如何添加到URL的链接**
[Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类包含[hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/)集合。[hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/)集合中的每个项目表示[Hyperlink](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink)。通过调用[hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/)集合的[add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str)方法向URL添加超链接。[add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str)方法需要以下参数：

- 单元格名称，超链接将添加到的单元格的名称。
- 行数，超链接范围中的行数。
- 列数，该超链接范围的列数
- URL，URL地址。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToURL-1.py" >}}

{{% alert color="primary" %}} 

在上述示例中，在空单元格**A1**中添加了一个超链接。在这种情况下，如果单元格为空，则URL地址也会作为其值添加到该空单元格。如果单元格不为空并添加了超链接，则单元格的值看起来像普通文本。要使其看起来像超链接，请在该单元格上应用适当的格式设置。

{{% /alert %}} 

## **如何添加到同一文件中某单元格的链接**
通过调用[hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/)集合的[add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str)方法，可以将超链接添加到同一Excel文件中的单元格。[add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str)方法适用于内部和外部超链接。重载方法的一个版本需要以下参数：

- 单元格名称，将要添加超链接的单元格名称。
- 行数，超链接范围中的行数。
- 列数，超链接范围中的列数。
- URL，目标单元格的地址。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToAnotherCell-1.py" >}}

## **如何添加到外部文件的链接**
通过调用[hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/)集合的[add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str)方法，可以将超链接添加到外部Excel文件。[add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str)方法需要以下参数：

- 单元格名称，超链接将添加到的单元格的名称。
- 行数，超链接范围中的行数。
- 列数，超链接范围中的列数。
- URL，目标外部Excel文件的地址。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToExternalFile-1.py" >}}

## **高级主题**
- [添加图像超链接](/cells/zh/python-net/add-image-hyperlinks/)
- [检测超链接类型](/cells/zh/python-net/detect-hyperlink-type/)
- [编辑工作表的超链接](/cells/zh/python-net/editing-hyperlinks-of-worksheet/)
- [获取范围内的超链接](/cells/zh/python-net/get-hyperlinks-in-range/)

