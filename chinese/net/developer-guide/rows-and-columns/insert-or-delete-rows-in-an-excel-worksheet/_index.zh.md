---
title: 在Excel工作表中插入或删除行
type: docs
weight: 20
url: /zh/net/insert-or-delete-rows-in-an-excel-worksheet/
description: 本文提供了在Excel工作表中插入和删除行的C#代码
keywords: c#在Excel工作表中插入或删除行，c#在Excel工作表中插入或删除行，c#在Excel中插入行，c#删除Excel中的行，在c#中使用的Excel工作表中插入或删除行，使用c#在Excel中插入或删除行，使用c#在Excel中插入行，使用c#在Excel中删除行
---

{{% alert color="primary" %}}

在创建新工作表或处理现有工作表时，您可能需要添加额外的行或列以容纳数据。其他时候，您可能需要从工作表中指定位置删除行或列。

{{% /alert %}}

Aspose.Cells提供了两种用于插入和删除行的方法:[**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index)和[**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index)。这些方法经过优化以提高性能，并且可以快速完成任务。

为了插入或移除一些行，我们建议您始终使用[**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index)和[**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index)方法，而不要在循环中使用[**Cells.InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow)或[**DeleteRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterow)方法。

Aspose.Cells的工作方式与Microsoft Excel相同。添加行或列时，工作表内容会向下和向右移动。删除行或列时，工作表内容会向上或向左移动。当添加或删除行时，其他工作表和单元格中的引用会更新。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertDeleteRows-1.cs" >}}
