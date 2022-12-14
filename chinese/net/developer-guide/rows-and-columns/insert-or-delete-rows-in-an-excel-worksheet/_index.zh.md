---
title: 在 Excel 工作表中插入或删除行
type: docs
weight: 20
url: /zh/net/insert-or-delete-rows-in-an-excel-worksheet/
description: 本文提供C#代码在Excel工作表中插入和删除行
keywords: c# insert or delete rows in excel worksheet, c# insert or delete rows in excel, c# insert rows in excel, c# delete rows in excel, insert or delete rows in excel worksheet with c#, insert or delete rows in excel with c#, insert rows in excel with c#, delete rows in excel with c#
---
{{% alert color="primary" %}}

创建新工作表或使用现有工作表时，您可能需要添加额外的行或列以容纳数据。在其他时候，您可能需要从工作表中的指定位置删除行或列。

{{% /alert %}}

 Aspose.Cells 提供了两种插入和删除行的方法：[**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index)和[**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index).这些方法针对性能进行了优化，可以非常快速地完成工作。

要插入或删除多行，我们建议您始终使用[**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index)和[**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index)方法而不是使用[**Cells.InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow)或者[**删除行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterow)循环中的方法。

Aspose.Cells 与 Microsoft Excel 的工作方式相同。添加行或列时，工作表内容会向下和向右移动。删除行或列时，工作表内容会向上或向左移动。添加或删除行时，其他工作表和单元格中的任何引用都会更新。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertDeleteRows-1.cs" >}}
