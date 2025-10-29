---
title: 创建和管理Microsoft Excel文件的表格。
linktitle: 表格
type: docs
weight: 150
url: /zh/python-net/create-and-format-table/
description: 使用Aspose.Cells库插入、调整大小、编辑、删除和格式化Excel文件的表格。
---

## **创建表**

电子表格的优点之一是它们允许您创建不同类型的列表，例如电话列表、任务列表、交易列表、资产或负债列表。多个用户可以共同使用、创建和维护各种列表。

Aspose.Cells for Python via .NET支持创建和管理列表。

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

### **使用Aspose.Cells for Python via .NET API**

Aspose.Cells for Python via .NET提供一个类 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)，代表一个Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类包含一个集合，允许访问Excel文件中的每个工作表。

工作表由[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类提供了广泛的属性和方法来管理工作表。要在工作表中创建一个[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)，请使用[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类的[**list_objects**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/list_objects)集合属性。实际上，每个[**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject)都是[**add**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection/add/#int-int-int-int-bool)类的对象，后者进一步提供[**add**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection/add/#int-int-int-int-bool)方法以添加列表对象并指定列表的单元格范围。

根据指定的单元格范围，Aspose.Cells for Python via .NET将创建List对象。使用[**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject)类的属性（例如 [**show_totals**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/show_totals)、[**ListColumns**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/list_columns) 等）控制列表。

在下面的示例中，我们使用Aspose.Cells for Python via .NET API创建了与上节所用Microsoft Excel创建的相同 [**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject)。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-CreatingListObject-1.py" >}}

## **格式化表**

为了管理和分析一组相关数据，可以将单元格范围转换为列表对象（也称为Excel表格）。表格是一系列包含相关数据的行和列，独立于其他行和列进行管理。默认情况下，表中的每一列在标题行启用过滤，可以快速筛选或排序列表数据。您还可以为列表添加总行（一个特殊的列表行，提供一些汇总函数，便于处理数值数据），每个总行单元格都可以提供一个下拉列表，显示各种汇总函数。Aspose.Cells for Python via .NET 提供创建和管理列表（或表格）的方法。

### **格式化列表对象**

Aspose.Cells for Python via .NET提供一个类 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)，代表一个Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类包含一个 [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) 集合，允许访问Excel文件中的每个工作表。

工作表由[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类提供了广泛的属性和方法来管理工作表。要在工作表中创建一个[**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject)，请使用[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类的[**list_objects**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/list_objects)集合属性。实际上，每个[**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject)都是[**ListObjectCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection)类的对象，后者进一步提供[**add**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobjectcollection/add/#int-int-int-int-bool)方法以添加列表对象并指定它应包含的单元格范围。根据指定的单元格范围，Aspose.Cells在工作表中创建一个[**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject)。使用[**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject)类的属性（例如[**table_style_type**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/table_style_type)）来按照您的要求格式化表格。

以下示例向工作表添加示例数据，添加[**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject)并对其应用默认样式。Microsoft Excel 2007/2010支持[**ListObject**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject)样式。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-FormataListObject-1.py" >}}

## **高级主题**
- [将表格转换为ODS](/cells/zh/python-net/convert-table-to-ods/)
- [查找与外部数据连接相关的查询表和列表对象](/cells/zh/python-net/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [读取和写入带有查询表数据源的表格](/cells/zh/python-net/read-and-write-table-with-query-table-data-source/)
- [设置工作表内表格或列表对象的批注](/cells/zh/python-net/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [表格和区域](/cells/zh/python-net/tables-and-ranges/)


{{< app/cells/assistant language="python-net" >}}
