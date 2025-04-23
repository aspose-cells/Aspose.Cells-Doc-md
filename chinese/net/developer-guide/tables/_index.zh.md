---
title: 创建和管理Microsoft Excel文件的表格。
linktitle: 表格
type: docs
weight: 150
url: /zh/net/create-and-format-table/
description: 使用Aspose.Cells库插入、调整大小、编辑、删除和格式化Excel文件的表格。
---

## **创建表**

电子表格的优点之一是它们允许您创建不同类型的列表，例如电话列表、任务列表、交易列表、资产或负债列表。多个用户可以共同使用、创建和维护各种列表。

Aspose.Cells支持创建和管理列表。

### **列表对象的优点**

当您将数据列表转换为实际列表对象时，会有相当多的优点

- 新行和列会自动包括在内。
- 列表底部可以轻松添加总计行来显示求和、平均、计数等信息。
- 添加在右侧的列会自动并入列表对象中。
- 基于行和列的图表会自动扩展。
- 分配给行和列的命名范围将自动扩展。
列表受到意外行和列删除的保护。

### **在 Microsoft Excel 中创建列表对象**

- 选择用于创建列表对象的数据范围
- 这将显示创建列表对话框。
- 为数据实现列表对象，并指定总行（选择**数据**，然后**列表**，再**总行**）。

### **使用 Aspose.Cells API**

Aspose.Cells提供了一个表示Microsoft Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)。 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)集合，允许访问Excel文件中的每个工作表。

工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了广泛的属性和方法来管理工作表。要在工作表中创建一个[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)，请使用[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类的[**ListObjects**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects)集合属性。实际上，每个[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)都是[**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection)类的对象，后者进一步提供[**Add**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index)方法以添加列表对象并指定列表的单元格范围。

根据指定的单元格范围，Aspose.Cells创建列表对象。使用[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)类的属性（例如[**ShowTotals**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/showtotals)，[**ListColumns**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/listcolumns)等）来控制列表。

在下面的示例中，我们使用Aspose.Cells API创建了与前面在Microsoft Excel中创建相同的[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-CreatingListObject-1.cs" >}}

## **格式化表**

要管理和分析一组相关数据，可以将一系列单元格转换为列表对象（也称为Excel表格）。 表格是包含相关数据的一系列行和列，独立于其他行和列中的数据。 默认情况下，表中的每一列都在标题行中启用了过滤器，这样您就可以快速过滤或排序列表对象数据。 您可以向列表对象添加一个总行（列表中的特殊行，为使用数字数据工作提供了一系列有用的聚合函数）。 Aspose.Cells提供了创建和管理列表（或表格）的选项。

### **格式化列表对象**

Aspose.Cells提供了一个表示Microsoft Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)。 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)集合，允许访问Excel文件中的每个工作表。

工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了广泛的属性和方法来管理工作表。要在工作表中创建一个[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)，请使用[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类的[**ListObjects**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects)集合属性。实际上，每个[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)都是[**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection)类的对象，后者进一步提供[**Add**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index)方法以添加列表对象并指定它应包含的单元格范围。根据指定的单元格范围，Aspose.Cells在工作表中创建一个[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)。使用[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)类的属性（例如[**TableStyleType**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/tablestyletype)）来按照您的要求格式化表格。

以下示例向工作表添加示例数据，添加[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)并对其应用默认样式。Microsoft Excel 2007/2010支持[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)样式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-FormataListObject-1.cs" >}}

## **高级主题**
- [将表格转换为ODS](/cells/zh/net/convert-table-to-ods/)
- [查找与外部数据连接相关的查询表和列表对象](/cells/zh/net/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [读取和写入带有查询表数据源的表格](/cells/zh/net/read-and-write-table-with-query-table-data-source/)
- [设置工作表内表格或列表对象的批注](/cells/zh/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [表格和区域](/cells/zh/net/tables-and-ranges/)

{{< app/cells/assistant language="csharp" >}}
