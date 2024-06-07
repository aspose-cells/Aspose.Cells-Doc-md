---
title: 创建和管理Microsoft Excel文件的表。
linktitle: 表格
type: docs
weight: 150
url: /zh/net/create-and-format-table/
description: 使用Aspose.Cells库插入，调整大小，编辑，删除，格式化Excel文件的表。
---

## **创建表**

电子表格的优点之一是它允许您创建不同类型的列表，例如电话列表、任务列表、交易列表、资产或负债列表。多个用户可以共同使用、创建和维护各种列表。

Aspose.Cells支持创建和管理列表。

### **列表对象的优点**

将数据列表转换为实际列表对象时有很多优点

- 新行和列会自动包含其中。
- 可轻松添加位于列表底部的总行，以显示 SUM、AVERAGE、COUNT 等。
- 添加到右侧的列会自动合并到列表对象中。
- 基于行和列的图表将自动扩展。
- 针对行和列分配的命名范围将自动扩展。
- 列表受到意外删除的保护。

### **使用Microsoft Excel创建列表对象**

- 选择用于创建List对象的数据范围
- 显示创建List对话框。
- 为数据实现List对象并指定总行（选择**数据**，然后**列表**，然后**总行**）。

### **使用Aspose.Cells API**

Aspose.Cells提供了一个类，[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，代表一个微软Excel文件。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)集合，允许访问Excel文件中的每个工作表。

工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了广泛的属性和方法，用于管理工作表。要在工作表中创建一个[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)，使用[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类的[**ListObjects**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects)集合属性。[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)的每个对象实际上是[**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection)类的对象，后者提供了[**Add**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index)方法来添加一个List对象，并指定列表中的单元格范围。

根据指定的单元格范围，Aspose.Cells创建一个List对象。使用[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)类的属性（例如[**ShowTotals**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/showtotals)、[**ListColumns**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/listcolumns)等）来控制列表。

在下面给出的示例中，我们使用Aspose.Cells API创建了一个与上述部分中使用Microsoft Excel创建的相同的[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-CreatingListObject-1.cs" >}}

## **格式化表**

要管理和分析一组相关数据，可以将一系列单元格转换为列表对象（也称为Excel表）。表是包含相关数据的一系列行和列，独立于其他行和列中的数据进行管理。默认情况下，表中的每列在标题行中启用了过滤器，以便您可以快速过滤或对列表对象数据进行排序。您可以向列表对象添加一个总行（列表中的特殊行，为处理数字数据提供了一组聚合函数的选择）,为列表对象的每个总行单元格提供一个聚合函数的下拉列表。Aspose.Cells提供了创建和管理列表（或表）的选项。

### **格式化列表对象**

Aspose.Cells提供了一个类，[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，代表一个微软Excel文件。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)集合，允许访问Excel文件中的每个工作表。

工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了广泛的属性和方法，用于管理工作表。要在工作表中创建一个[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)，使用[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类的[**ListObjects**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/listobjects)集合属性。[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)的每个对象实际上是[**ListObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection)类的对象，后者提供了[**Add**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobjectcollection/methods/add/index)方法来添加一个List对象，并指定列表中的单元格范围。根据指定的单元格范围，Aspose.Cells在工作表中创建一个[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)。使用[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)类的属性（例如[**TableStyleType**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/properties/tablestyletype)）来根据您的需求格式化表。

下面的示例向工作表添加了示例数据，并添加了一个[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)，并应用了默认样式。Microsoft Excel 2007/2010支持[**ListObject**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject)样式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-FormataListObject-1.cs" >}}

## **高级主题**
- [将表格转换为ODS](/cells/zh/net/convert-table-to-ods/)
- [查找与外部数据连接相关的查询表和列表对象](/cells/zh/net/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [读取并写入包含查询表数据源的表格](/cells/zh/net/read-and-write-table-with-query-table-data-source/)
- [设置工作表内表格或列表对象的注释](/cells/zh/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [表和范围](/cells/zh/net/tables-and-ranges/)

