---
title: Aspose.Cells 8.5.1中的公共API更改
type: docs
weight: 180
url: /zh/java/public-api-changes-in-aspose-cells-8-5-1/
---

{{% alert color="primary" %}} 

描述了Aspose.Cells API从版本8.5.0到8.5.1的更改，这些更改可能对模块/应用程序开发人员感兴趣。其中包括新的和更新的公共方法，[添加的类等](/cells/zh/java/public-api-changes-in-aspose-cells-8-5-1/)，以及Aspose.Cells背后的行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **添加了Workbook.Dispose方法**
Aspose.Cells for Java 8.5.1已经暴露出Workbook.dispose方法，用于释放Workbook对象的非托管资源。Dispose模式仅适用于访问非托管资源的对象，如文件和管道句柄、注册表句柄、等待句柄或指向非托管内存块的指针。这是因为垃圾回收器非常有效地回收未使用的托管对象，但无法回收非托管对象。

Java

{{< highlight csharp >}}

 //Create workbook object

Workbook book = new Workbook();

//Call dispose method

book.dispose();

{{< /highlight >}}
### **添加了Cell.getHeightOfValue方法**
Aspose.Cells for Java 8.5.1已经暴露出Cell.getHeightOfValue方法，用于获取单元格值的高度。通过使用该方法，您可以计算单元格值的高度，然后相应地设置该单元格的行高。查看有关[如何计算单元格高度和宽度](/cells/zh/java/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)的详细文章。
### **添加了枚举TableDataSourceType**
Aspose.Cells for Java 8.5.1已经暴露出com.aspose.cells.TableDataSourceType枚举，以检索ListObject的数据源类型。TableDataSourceType枚举如下字段。 

1. TableDataSourceType.QUERY_TABLE
1. TableDataSourceType.SHARE_POINT
1. TableDataSourceType.WORKSHEET
1. TableDataSourceType.XML
### **添加了ListObject.DataSourceType属性**
随着v8.5.1的发布，Aspose.Cells API公开了只读的ListObject.DataSourceType属性，用于检测ListObject的数据源类型。

这是最简单的使用场景。

Java

{{< highlight csharp >}}

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
