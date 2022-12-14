---
title: 创建和管理 Microsoft Excel 文件的表格。
linktitle: 表
type: docs
weight: 150
url: /zh/net/create-and-format-table/
description: 使用 Aspose.Cells 库插入、调整大小、编辑、删除、格式化 Excel 文件表格。
---
## **创建表**

电子表格的优点之一是它们允许您创建不同类型的列表，例如电话列表、任务列表、交易列表、资产或负债。多个用户可以一起使用、创建和维护各种列表。

Aspose.Cells 支持创建和管理列表。

### **列表对象的优点**

将数据列表转换为实际列表对象时有很多优点

- 自动包含新行和新列。
- 列表底部的总计行可以轻松添加以显示 SUM、AVERAGE、COUNT 等。
- 添加到右侧的列会自动合并到 List 对象中。
- 基于行和列的图表将自动展开。
- 分配给行和列的命名范围将自动扩展。
- 该列表受到保护，不会意外删除行和列。

### **使用 Microsoft Excel 创建列表对象**

- 选择用于创建列表对象的数据范围
- 这将显示“创建列表”对话框。
- 为数据实现列表对象并指定合计行（选择**数据**， 然后**列表**， 其次是**总行数**).

### **使用 Aspose.Cells API**

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，代表一个 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中每个工作表的集合。

工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了广泛的属性和方法来管理工作表。创建一个[**列表对象**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)在工作表中，使用[**列表对象**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects)的集合属性[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。每个[**列表对象**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)实际上是[**列表对象集合**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection)类，它进一步提供了[**添加**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index)添加 List 对象并为列表指定单元格范围的方法。

Aspose.Cells根据指定范围的单元格，创建List对象。使用属性（例如，[**显示总计**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/showtotals), [**列表列**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/listcolumns)等）的[**列表对象**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)控制列表的类。

在下面给出的示例中，我们创建了相同的[**列表对象**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)使用我们在上一节中使用 Microsoft Excel 创建的 Aspose.Cells API。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-CreatingListObject-1.cs" >}}

## **格式化表格**

要管理和分析一组相关数据，可以将一系列单元格转换为列表对象（也称为 Excel 表格）。表是一系列行和列，其中包含独立于其他行和列中的数据管理的相关数据。默认情况下，表格中的每一列都在标题行中启用了筛选，以便您可以快速筛选或排序列表对象数据。您可以将总计行（列表中的特殊行，提供对处理数字数据有用的聚合函数选择）添加到列表对象，该列表对象为每个总计行单元格提供聚合函数的下拉列表。 Aspose.Cells 提供用于创建和管理列表（或表格）的选项。

### **格式化列表对象**

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，代表一个 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中每个工作表的集合。

工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了广泛的属性和方法来管理工作表。创建一个[**列表对象**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)在工作表中，使用[**列表对象**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects)的集合属性[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。每个[**列表对象**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)实际上是[**列表对象集合**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection)类，它进一步提供了[**添加**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index)添加 List 对象并指定它应包含的单元格范围的方法。根据指定的单元格范围，一个[**列表对象**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)由 Aspose.Cells 在工作表中创建。使用属性（例如，[**表格样式类型**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/tablestyletype)） 的[**列表对象**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)类来根据您的要求格式化表格。

下面的示例将样本数据添加到工作表，添加[**列表对象**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)并对其应用默认样式。[**列表对象**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)Microsoft Excel 2007/2010 支持样式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-FormataListObject-1.cs" >}}

## **推进主题**
- [将表转换为 ODS](/cells/zh/net/convert-table-to-ods/)
- [查找与外部数据连接相关的查询表和列表对象](/cells/zh/net/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [使用查询表数据源读写表](/cells/zh/net/read-and-write-table-with-query-table-data-source/)
- [在工作表中设置表格或列表对象的注释](/cells/zh/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [表格和范围](/cells/zh/net/tables-and-ranges/)

