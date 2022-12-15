---
title: 格式化列表对象 - 表格
type: docs
weight: 50
url: /zh/java/format-a-list-object-table/
---
{{% alert color="primary" %}}

要管理和分析一组相关数据，可以将一系列单元格转换为列表对象（也称为 Excel 表格）。表是一系列行和列，其中包含独立于其他行和列中的数据管理的相关数据。默认情况下，表格中的每一列都在标题行中启用了筛选，以便您可以快速筛选或排序列表对象数据。您可以将总计行（列表中的特殊行，提供对处理数字数据有用的聚合函数选择）添加到列表对象，该列表对象为每个总计行单元格提供聚合函数的下拉列表。 Aspose.Cells 提供用于创建和管理列表（或表格）的选项。

{{% /alert %}}

## **格式化列表对象**

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)，代表一个 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)允许访问 Excel 文件中每个工作表的集合。

工作表由[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类提供了广泛的属性和方法来管理工作表。创建一个[**列表对象**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)在工作表中，使用[**列表对象**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects)的集合属性[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级。每个[**列表对象**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)实际上是[**列表对象集合**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection)类，它进一步提供了添加方法来添加一个 List 对象并指定它应该包含的单元格范围。根据指定的单元格范围，一个[**列表对象**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)由 Aspose.Cells 在工作表中创建。使用属性（例如，[**表格样式类型**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#TableStyleType)） 的[**列表对象**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)类来根据您的要求格式化表格。

下面的示例将样本数据添加到工作表，添加[**列表对象**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)并将默认样式应用于它。[**列表对象**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)Microsoft Excel 2007/2010 支持样式。

执行代码时会生成以下输出。

**在工作表中创建格式化表格** 

![待办事项：图像_替代_文本](format-a-list-object-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FormataListObject-FormataListObject.java" >}}
