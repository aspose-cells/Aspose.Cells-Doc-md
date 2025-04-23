---
title: 在Excel或OpenOffice中插入超链接
linktitle: 管理超链接
type: docs
weight: 45
url: /zh/nodejs-cpp/insert-hyperlinks-to-excel/
description: 如何使用Node.js通过C++在没有MS Excel的情况下将超链接插入Excel文件中。
keywords: 将超链接插入Excel，通过C++的Node.js中添加或插入超链接，添加或插入指向URL的超链接，添加或插入到单元格的链接，添加一个指向外部文件的链接。
---

{{% alert color="primary" %}} 

超链接用于在两个实体之间创建链接。每个人都熟悉超链接的使用，特别是在网站上。
使用Aspose.Cells，开发人员可以在Microsoft Excel文件中创建不同类型的超链接。本主题讨论了Aspose.Cells支持哪些类型的超链接以及如何在我们的Excel文件中使用它们。

{{% /alert %}} 

## **添加超链接**
Aspose.Cells允许开发者使用API或设计表格（手动创建超链接并由Aspose.Cells导入到其他表格中）向Excel文件中添加超链接。

Aspose.Cells提供了一个类[Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook)，它代表一个Microsoft Excel文件。[Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook)类包含一个[WorksheetCollection](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection)，可以访问Excel文件中的每个工作表。一个工作表由[Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet)类表示。[Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet)类提供了不同的方法，用于向Excel文件添加不同的超链接。
## **添加指向URL的链接**
[Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet)类包含一个[getHyperlinks()](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHyperlinks--)集合。每个[getHyperlinks()](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHyperlinks--)中的项目代表一个[Hyperlink](https://reference.aspose.com/cells/nodejs-cpp/hyperlink)。通过调用[Hyperlinks](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection)集合的[add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-)方法，可以将超链接添加到URL。该[add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-)方法参数如下：

- 单元格名称，超链接将添加到的单元格的名称。
- 行数，超链接范围中的行数。
- 列数，超链接范围中的列数。
- URL，URL地址。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-AddLinkToURL.js" >}}


{{% alert color="primary" %}} 

在上述示例中，在空单元格**A1**中添加了一个超链接。在这种情况下，如果单元格为空，则URL地址也会作为其值添加到该空单元格。如果单元格不为空并添加了超链接，则单元格的值看起来像普通文本。要使其看起来像超链接，请在该单元格上应用适当的格式设置。

{{% /alert %}} 
## **将链接添加到同一文件中的单元格**
可以通过调用[Hyperlinks](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection)集合的[add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-)方法，在同一个Excel文件中的单元格添加超链接。[add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-)方法适用于内部和外部超链接。重载方法之一的参数如下：

- 单元格名称，超链接将添加到的单元格的名称。
- 行数，超链接范围中的行数。
- 列数，超链接范围中的列数。
- URL，目标单元格的地址。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-AddLinkToCell.js" >}}


## **向外部文件添加链接**
可以通过调用[Hyperlinks](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection)集合的[add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-)方法，为外部Excel文件添加超链接。其参数如下：

- 单元格名称，超链接将添加到的单元格的名称。
- 行数，超链接范围中的行数。
- 列数，超链接范围中的列数。
- URL，目标外部Excel文件的地址。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-AddLinkToExternalFile.js" >}}



## **高级主题**
- [添加图像超链接](/cells/zh/nodejs-cpp/add-image-hyperlinks/)
- [检测超链接类型](/cells/zh/nodejs-cpp/detect-hyperlink-type/)
- [编辑工作表的超链接](/cells/zh/nodejs-cpp/editing-hyperlinks-of-worksheet/)
- [获取范围内的超链接](/cells/zh/nodejs-cpp/get-hyperlinks-in-range/)

