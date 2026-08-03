---
title: 插入数据透视表
linktitle: 数据透视表
type: docs
weight: 160
url: /zh/net/pivot-tables/
description: 创建和格式化Excel电子表格文件的数据透视表。
keywords: 创建数据透视表，插入数据透视表，格式化数据透视表。
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **创建数据透视表**

可以使用Aspose.Cells在程序中向电子表格添加数据透视表。

### **数据透视表对象模型**

Aspose.Cells提供了一组特殊的类在[**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot)命名空间中，用于创建和控制数据透视表。这些类用于创建和设置[**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)对象，数据透视表的构建块。这些对象包括:

- [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) 代表 [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) 中的一个字段。
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) 代表 [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) 中的所有 [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) 对象的集合。
- [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) 代表工作表上的数据透视表。
- [**PivotTableCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) 代表工作表上的所有 [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) 对象的集合。

### **使用 Aspose.Cells 创建一个简单的数据透视表**

1. 使用 [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) 对象的 [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) 方法向工作表添加数据。这些数据将被用作数据透视表的数据源。
2. 通过调用 [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) 集合的 [**add**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index) 方法（封装在工作表对象中）向工作表添加一个数据透视表。
3. 通过传递数据透视表索引从 [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) 集合中访问新的 [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) 对象。
4. 使用上面解释的任何 [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) 对象来管理数据透视表。

执行示例代码后，数据透视表将被添加到工作表中。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CreatePivotTable-1.cs" >}}

{{% alert color="primary" %}}

当将一系列单元格指定为数据源时，该范围必须从左上到右下。例如，“A1:C3”是有效的，但“C3:A1”是无效的。

{{% /alert %}}

{{< app/cells/assistant language="csharp" >}}
