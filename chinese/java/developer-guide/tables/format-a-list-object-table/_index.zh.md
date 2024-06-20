---
title: 格式化列表对象  表格
type: docs
weight: 50
url: /zh/java/format-a-list-object-table/
---

{{% alert color="primary" %}}

要管理和分析一组相关数据，可以将一系列单元格转换为列表对象（也称为Excel表格）。 表格是包含相关数据的一系列行和列，独立于其他行和列中的数据。 默认情况下，表中的每一列都在标题行中启用了过滤器，这样您就可以快速过滤或排序列表对象数据。 您可以向列表对象添加一个总行（列表中的特殊行，为使用数字数据工作提供了一系列有用的聚合函数）。 Aspose.Cells提供了创建和管理列表（或表格）的选项。

{{% /alert %}}

## **格式化列表对象**

Aspose.Cells提供了一个表示Microsoft Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)。 [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)集合，允许访问Excel文件中的每个工作表。

工作表由[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类表示。 [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类提供了广泛的属性和方法，用于管理工作表。 要在工作表中创建[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)，请使用[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类的[**ListObjects**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects)集合属性。 每个[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)实际上是[**ListObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/listobjectcollection)类的对象，后者进一步提供了添加列表对象并指定应涵盖的单元格范围的add方法。 根据指定的单元格范围，Aspose.Cells在工作表中创建了一个[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)。 使用[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)类的属性（例如[**TableStyleType**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#TableStyleType)）为您的要求格式化表。

下面的示例将示例数据添加到工作表中，添加一个[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)并应用默认样式。 Microsoft Excel 2007/2010支持[**ListObject**](https://reference.aspose.com/cells/java/com.aspose.cells/ListObject)样式。

执行代码时生成以下输出。

**在工作表中创建了格式化的表** 

![todo:image_alt_text](format-a-list-object-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FormataListObject-FormataListObject.java" >}}
