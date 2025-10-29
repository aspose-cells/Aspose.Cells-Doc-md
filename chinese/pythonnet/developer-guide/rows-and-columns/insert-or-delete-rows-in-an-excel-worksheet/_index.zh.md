---
title: 在Excel工作表中插入或删除行
type: docs
weight: 20
url: /zh/python-net/insert-or-delete-rows-in-an-excel-worksheet/
description: 本文提供了在 Excel 工作表中使用 Aspose.Cells for Python via .NET 库插入和删除行的 Python 代码。
keywords: Python Excel库，Python在Excel工作表中插入或删除行，Python在Excel中插入或删除行，Python在Excel中插入行，Python在Excel中删除行，使用Python在Excel工作表中插入或删除行，在Excel中使用Python插入或删除行，在Excel中使用Python插入行，在Excel中使用Python删除行
---

{{% alert color="primary" %}}

在创建新工作表或处理现有工作表时，您可能需要添加额外的行或列以容纳数据。其他时候，您可能需要从工作表中指定位置删除行或列。

{{% /alert %}}

Aspose.Cells for Python via .NET提供了两种插入和删除行的方法：[**Cells.insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/)和[**Cells.delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/)。这些方法经过了性能优化，可以非常快速地完成任务。

要插入或删除多行，我们建议始终使用[**Cells.insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/)和[**Cells.delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/)方法，而不是在循环中使用[**Cells.insert_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_row)或[**delete_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_row)方法。

Aspose.Cells for Python via .NET的工作方式与Microsoft Excel相同。当添加行或列时，工作表内容会向下和向右移动。当移除行或列时，工作表内容会向上或向左移动。在添加或删除行时，其他工作表和单元格中的引用会得到更新。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertDeleteRows-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
