---
title: 公共 API Aspose.Cells 8.5.1 的变化
type: docs
weight: 180
url: /zh/java/public-api-changes-in-aspose-cells-8-5-1/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.5.0 到 8.5.1 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法，[添加类等](/cells/zh/java/public-api-changes-in-aspose-cells-8-5-1/)还描述了 Aspose.Cells 中幕后行为的任何变化。

{{% /alert %}} 
## **添加的 API**
### **方法 Workbook.Dispose 添加**
Aspose.Cells for Java 8.5.1暴露了Workbook.dispose方法释放Workbook对象的非托管资源。 dispose 模式仅用于访问非托管资源的对象，例如文件和管道句柄、注册表句柄、等待句柄或指向非托管内存块的指针。这是因为垃圾收集器在回收未使用的托管对象方面非常有效，但无法回收非托管对象。

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook book = new Workbook();

//Call dispose method

book.dispose();

{{< /highlight >}}
### **添加方法 Cell.getHeightOfValue**
 Aspose.Cells for Java 8.5.1暴露了Cell.getHeightOfValue方法获取单元格高度值。通过使用此方法，您可以计算单元格值的高度，然后分别设置该单元格的行高。查看详细文章[如何计算单元格的高度和宽度](/cells/zh/java/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/).
### **添加了枚举 TableDataSourceType**
Aspose.Cells for Java 8.5.1 公开了枚举 com.aspose.cells.TableDataSourceType 以检索 ListObject 的数据源类型。 TableDataSourceType 枚举如下字段。

1. TableDataSourceType.QUERY_TABLE
1. TableDataSourceType.SHARE_POINT
1. TableDataSourceType.WORKSHEET
1. 表数据源类型.XML
### **添加了属性 ListObject.DataSourceType**
随着v8.5.1的发布，Aspose.Cells API 公开了readonly ListObject.DataSourceType属性，可以用来检测ListObject的数据源类型。

这里是最简单的使用场景。

**Java**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("D:/book1.xlsx");

Worksheet sheet = book.getWorksheets().get(0);

ListObject listObject = sheet.getListObjects().get(0);

if (listObject.getDataSourceType() == com.aspose.cells.TableDataSourceType.QUERY_TABLE)

{

	System.out.println("Data Source Type is Query Table");

}

else if (listObject.getDataSourceType() == com.aspose.cells.TableDataSourceType.SHARE_POINT)

{

	System.out.println("Data Source Type is SharePoint Linked List");

}

else if (listObject.getDataSourceType() == com.aspose.cells.TableDataSourceType.WORKSHEET)

{

	System.out.println("Data Source Type is Excel Worksheet Table");

}

else if (listObject.getDataSourceType() == com.aspose.cells.TableDataSourceType.XML)

{

	System.out.println("Data Source Type is XML");

}

{{< /highlight >}}
