---
title: 格式化列表对象 - 表
type: docs
weight: 50
url: /zh/java/format-a-list-object-table/
---

{{% alert color="primary" %}}

要管理和分析一组相关数据，可以将一系列单元格转换为列表对象（也称为Excel表）。表是包含相关数据的一系列行和列，独立于其他行和列中的数据进行管理。默认情况下，表中的每列在标题行中启用了过滤器，以便您可以快速过滤或对列表对象数据进行排序。您可以向列表对象添加一个总行（列表中的特殊行，为处理数字数据提供了一组聚合函数的选择）,为列表对象的每个总行单元格提供一个聚合函数的下拉列表。Aspose.Cells提供了创建和管理列表（或表）的选项。

{{% /alert %}}

## **格式化列表对象**

Aspose.Cells提供了一个类，[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)，代表一个微软Excel文件。[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)集合，允许访问Excel文件中的每个工作表。

工作表由 [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类提供了用于管理工作表的各种属性和方法。要在工作表中创建一个 [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)，请使用 [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类的 [**ListObjects**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects) 集合属性。实际上，每个 [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) 都是 [**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection) 类的对象，后者还提供了添加列表对象和指定应包含范围单元格的 add 方法。根据指定的单元格范围，在工作表中创建了Aspose.Cells的 [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)。使用 [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) 类的属性 (例如，[**TableStyleType**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#TableStyleType)) 格式化表格以满足您的需求。

以下示例向工作表添加了样本数据，添加了一个 [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) 并应用了默认样式。Microsoft Excel 2007/2010支持 [**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject) 样式。

执行代码时生成以下输出。

**在工作表中创建了格式化表格** 

![todo:image_alt_text](format-a-list-object-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FormataListObject-FormataListObject.java" >}}
