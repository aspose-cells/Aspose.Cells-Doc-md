---
title: 插入数据透视表
linktitle: 数据透视表
type: docs
weight: 160
url: /zh/python-net/create-pivot-table/
description: 使用Aspose.Cells for Python via .NET创建和格式化数据透视表。
keywords: 创建数据透视表，插入数据透视表，格式化数据透视表。
---

## **创建数据透视表**

可以使用Aspose.Cells for Python via .NET以程序方式向电子表格添加数据透视表。

### **数据透视表对象模型**

Aspose.Cells for Python via .NET在[**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/)命名空间中提供了一组特殊的类，用于创建和控制数据透视表。这些类用于创建和设置[**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/)对象，数据透视表的构建模块。对象包括：

- [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) 代表 [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/) 中的一个字段。
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) 代表 [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) 中的所有 [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield) 对象的集合。
- [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) 代表工作表上的数据透视表。
- [**PivotTableCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) 代表工作表上的所有 [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) 对象的集合。

### **使用 Aspose.Cells 创建一个简单的数据透视表**

1. 使用 [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) 对象的 [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str) 方法向工作表添加数据。
   这些数据将被用作数据透视表的数据源。
1. 通过调用 [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) 集合的 [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str) 方法（封装在工作表对象中）向工作表添加一个数据透视表。
1. 通过传递数据透视表索引从 [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) 集合中访问新的 [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) 对象。
1. 使用上面解释的任何 [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) 对象来管理数据透视表。

执行示例代码后，数据透视表将被添加到工作表中。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-CreatePivotTable-1.py" >}}

{{% alert color="primary" %}}

当将一系列单元格指定为数据源时，该范围必须从左上到右下。例如，“A1:C3”是有效的，但“C3:A1”是无效的。

{{% /alert %}}

## **高级主题**
- [合并功能](/cells/zh/python-net/consolidation-function/)
- [数据透视表中的自定义排序](/cells/zh/python-net/custom-sorting-in-pivot-table/)
- [自定义数据透视表的全球化设置](/cells/zh/python-net/customize-globalization-settings-for-pivot-table/)
- [禁用数据透视表功能区](/cells/zh/python-net/disable-pivot-table-ribbons/)
- [查找并刷新父数据透视表的嵌套或子数据透视表](/cells/zh/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/)
- [格式化数据透视表](/cells/zh/python-net/formatting-pivot-table/)
- [获取数据透视表的外部连接数据源](/cells/zh/python-net/get-external-connection-data-source-of-pivot-table/)
- [获取数据透视表刷新日期和刷新者信息](/cells/zh/python-net/get-pivot-table-refresh-date-and-refresh-by-who-information/)
- [在透视表中对透视字段进行分组](/cells/zh/python-net/group-pivot-fields-in-the-pivot-table/)
- [在加载Excel文件时解析透视缓存记录](/cells/zh/python-net/parsing-pivot-cached-records-while-loading-excel-file/)
- [数据透视表和源数据](/cells/zh/python-net/pivot-table-and-source-data/)
- [数据透视表隐藏和排序数据](/cells/zh/python-net/pivot-table-hide-and-sort-data/)
- [刷新和计算包含计算项的数据透视表](/cells/zh/python-net/refresh-and-calculate-pivot-table-having-calculated-items/)
- [将数据透视表保存为 ODS 文件](/cells/zh/python-net/save-pivot-table-in-ods-file/)
- [显示报表筛选页选项](/cells/zh/python-net/show-report-filter-pages-option/)
- [在数据透视表的DataField中使用数据显示格式](/cells/zh/python-net/working-with-data-display-formats-of-datafield-in-pivot-table/)
