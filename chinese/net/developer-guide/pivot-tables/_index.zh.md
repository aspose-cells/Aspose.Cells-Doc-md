---
title: 插入数据透视表
linktitle: 数据透视表
type: docs
weight: 160
url: /zh/net/create-pivot-table/
description: 创建和格式化 Excel 电子表格文件的数据透视表。
---
## **创建数据透视表**

可以使用 Aspose.Cells 以编程方式将数据透视表添加到电子表格。

### **数据透视表对象模型**

Aspose.Cells 提供了一组特殊的类[**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot)用于创建和控制数据透视表的名称空间。这些类用于创建和设置[**数据透视表**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)对象，数据透视表的构建块。这些对象是：

- [**数据透视表**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield)代表一个字段[**数据透视表**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**数据透视字段集合**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection)代表所有的集合[**数据透视表**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield)中的对象[**数据透视表**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**数据透视表**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)代表工作表上的数据透视表。
- [**数据透视表集合**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection)代表所有的集合[**数据透视表**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)工作表上的对象。

### **使用 Aspose.Cells 创建一个简单的数据透视表**

1. 使用[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)对象的[**认沽价值**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)方法。
此数据将用作数据透视表的数据源。
1. 通过调用将数据透视表添加到工作表[**数据透视表**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection)收藏的[**添加**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index)方法，该方法封装在 Worksheet 对象中。
1. 访问新的[**数据透视表**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)对象来自[**数据透视表**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection)通过传递数据透视表索引进行收集。
1. 使用任何[**数据透视表**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)对象（如上所述）来管理数据透视表。

执行示例代码后，数据透视表将添加到工作表中。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CreatePivotTable-1.cs" >}}

{{% alert color="primary" %}}

将单元格区域指定为数据源时，该区域必须从左上角到右下角。例如，“A1:C3”有效，但“C3:A1”无效。

{{% /alert %}}

## **推进主题**
- [整合功能](/cells/zh/net/consolidation-function/)
- [数据透视表中的自定义排序](/cells/zh/net/custom-sorting-in-pivot-table/)
- [自定义数据透视表的全球化设置](/cells/zh/net/customize-globalization-settings-for-pivot-table/)
- [禁用数据透视表功能区](/cells/zh/net/disable-pivot-table-ribbons/)
- [查找并刷新父数据透视表的嵌套或子数据透视表](/cells/zh/net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/)
- [格式化数据透视表](/cells/zh/net/formatting-pivot-table/)
- [获取数据透视表的外部连接数据源](/cells/zh/net/get-external-connection-data-source-of-pivot-table/)
- [获取数据透视表刷新日期和刷新者信息](/cells/zh/net/get-pivot-table-refresh-date-and-refresh-by-who-information/)
- [数据透视表中的分组数据透视字段](/cells/zh/net/group-pivot-fields-in-the-pivot-table/)
- [加载 Excel 文件时解析数据透视缓存记录](/cells/zh/net/parsing-pivot-cached-records-while-loading-excel-file/)
- [数据透视表和源数据](/cells/zh/net/pivot-table-and-source-data/)
- [数据透视表隐藏和排序数据](/cells/zh/net/pivot-table-hide-and-sort-data/)
- [刷新并计算具有计算项的数据透视表](/cells/zh/net/refresh-and-calculate-pivot-table-having-calculated-items/)
- [将数据透视表保存在 ODS 文件中](/cells/zh/net/save-pivot-table-in-ods-file/)
- [显示报告筛选页面选项](/cells/zh/net/show-report-filter-pages-option/)
- [使用数据透视表中DataField的数据显示格式](/cells/zh/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
