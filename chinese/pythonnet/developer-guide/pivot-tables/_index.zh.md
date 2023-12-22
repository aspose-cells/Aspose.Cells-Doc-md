---
title: 插入数据透视表
linktitle: 数据透视表
type: docs
weight: 160
url: /zh/python-net/create-pivot-table/
description: 使用 Aspose.Cells for Python via .NET 创建数据透视表并设置其格式。
keywords: Create Pivot Table, Insert Pivot Table, Format Pivot Table.
---
##  **创建数据透视表**

可以使用 Aspose.Cells for Python via .NET 以编程方式将数据透视表添加到电子表格中。

###  **数据透视表对象模型**

Aspose.Cells for Python via .NET 提供了一组特殊的类[**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/)用于创建和控制数据透视表的命名空间。这些类用于创建和设置[**数据透视表**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/)对象，数据透视表的构建块。这些对象是：

- [**数据透视字段**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/)代表a中的一个字段[**数据透视表**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/).
- [**数据透视字段集合**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection)代表所有的集合[**数据透视字段**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield)中的物体[**数据透视表**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable).
- [**数据透视表**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)表示工作表上的数据透视表。
- [**数据透视表集合**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection)代表所有的集合[**数据透视表**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)工作表上的对象。

###  **使用 Aspose.Cells 创建简单的数据透视表**

1. 使用以下命令将数据添加到工作表[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)对象的[**看跌期权价值**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str)方法。
该数据将用作数据透视表的数据源。
1. 通过调用将数据透视表添加到工作表[**数据透视表**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection)收藏的[**添加**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str)方法，该方法封装在 Worksheet 对象中。
1. 访问新的[**数据透视表**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)对象从[**数据透视表**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection)通过传递数据透视表索引进行集合。
1. 使用任何[**数据透视表**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)对象（如上所述）来管理数据透视表。

执行示例代码后，数据透视表将添加到工作表中。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-CreatePivotTable-1.py" >}}

{{% alert color="primary" %}}

将单元格范围指定为数据源时，该范围必须从左上角到右下角。例如，“A1:C3”有效，但“C3:A1”无效。

{{% /alert %}}

##  **高级主题**
- [合并功能](/cells/zh/python-net/consolidation-function/)
- [数据透视表中的自定义排序](/cells/zh/python-net/custom-sorting-in-pivot-table/)
- [自定义数据透视表的全球化设置](/cells/zh/python-net/customize-globalization-settings-for-pivot-table/)
- [禁用数据透视表功能区](/cells/zh/python-net/disable-pivot-table-ribbons/)
- [查找并刷新父数据透视表的嵌套或子数据透视表](/cells/zh/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/)
- [设置数据透视表格式](/cells/zh/python-net/formatting-pivot-table/)
- [获取数据透视表的外部连接数据源](/cells/zh/python-net/get-external-connection-data-source-of-pivot-table/)
- [获取数据透视表刷新日期和刷新者信息](/cells/zh/python-net/get-pivot-table-refresh-date-and-refresh-by-who-information/)
- [对数据透视表中的数据透视字段进行分组](/cells/zh/python-net/group-pivot-fields-in-the-pivot-table/)
- [加载 Excel 文件时解析数据透视表缓存记录](/cells/zh/python-net/parsing-pivot-cached-records-while-loading-excel-file/)
- [数据透视表和源数据](/cells/zh/python-net/pivot-table-and-source-data/)
- [数据透视表隐藏和排序数据](/cells/zh/python-net/pivot-table-hide-and-sort-data/)
- [刷新并计算具有计算项目的数据透视表](/cells/zh/python-net/refresh-and-calculate-pivot-table-having-calculated-items/)
- [将数据透视表保存在 ODS 文件中](/cells/zh/python-net/save-pivot-table-in-ods-file/)
- [显示报告过滤页面选项](/cells/zh/python-net/show-report-filter-pages-option/)
- [使用数据透视表中 DataField 的数据显示格式](/cells/zh/python-net/working-with-data-display-formats-of-datafield-in-pivot-table/)
