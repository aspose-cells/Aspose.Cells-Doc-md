---
title: 插入数据透视表
linktitle: 数据透视表
type: docs
weight: 160
url: /zh/net/create-pivot-table/
description: 创建并格式化Excel电子表格文件的数据透视表。
---

## **创建数据透视表**

可以使用Aspose.Cells来编程方式向电子表格添加数据透视表。

### **数据透视表对象模型**

Aspose.Cells提供了一组特殊的类，位于[**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot) 命名空间中，用于创建和控制数据透视表。 这些类用于创建和设置数据透视表的构建块对象。 这些对象包括：

- [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) 代表[**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)中的一个字段。
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) 代表[**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)中所有[**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield)对象的集合。
- [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) 代表工作表上的一个数据透视表。
- [**PivotTableCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) 代表工作表上所有[**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)对象的集合。

### **使用Aspose.Cells创建简单数据透视表**

1. 使用[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)对象的[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)方法向工作表添加数据。
   这些数据将用作数据透视表的数据源。
1. 通过调用[**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection)集合的[**add**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index)方法向工作表添加数据透视表，该方法封装在工作表对象中。
1. 通过传递数据透视表索引从[**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection)集合中访问新的[**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)对象。
1. 使用上述任何[**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)对象来管理数据透视表。

执行示例代码后，工作表上将添加一个数据透视表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CreatePivotTable-1.cs" >}}

{{% alert color="primary" %}}

将一系列单元格指定为数据源时，该范围必须从左上角到右下角。 例如，“A1:C3”是有效的，但“C3:A1”是无效的。

{{% /alert %}}

## **高级主题**
- [汇总函数](/cells/zh/net/consolidation-function/)
- [数据透视表中的自定义排序](/cells/zh/net/custom-sorting-in-pivot-table/)
- [自定义数据透视表的全球化设置](/cells/zh/net/customize-globalization-settings-for-pivot-table/)
- [禁用数据透视表功能区](/cells/zh/net/disable-pivot-table-ribbons/)
- [查找和刷新父数据透视表的嵌套或子数据透视表](/cells/zh/net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/)
- [格式化数据透视表](/cells/zh/net/formatting-pivot-table/)
- [获取数据透视表的外部连接数据源](/cells/zh/net/get-external-connection-data-source-of-pivot-table/)
- [获取数据透视表刷新日期和刷新者信息](/cells/zh/net/get-pivot-table-refresh-date-and-refresh-by-who-information/)
- [在数据透视表中对数据透视字段进行分组](/cells/zh/net/group-pivot-fields-in-the-pivot-table/)
- [在加载Excel文件时解析数据透视缓存记录](/cells/zh/net/parsing-pivot-cached-records-while-loading-excel-file/)
- [数据透视表和源数据](/cells/zh/net/pivot-table-and-source-data/)
- [数据透视表隐藏和排序数据](/cells/zh/net/pivot-table-hide-and-sort-data/)
- [刷新和计算包含计算项的数据透视表](/cells/zh/net/refresh-and-calculate-pivot-table-having-calculated-items/)
- [将数据透视表保存为ODS文件](/cells/zh/net/save-pivot-table-in-ods-file/)
- [显示报表筛选页面选项](/cells/zh/net/show-report-filter-pages-option/)
- [工作中使用数据透视表中 DataField 的数据显示格式](/cells/zh/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
