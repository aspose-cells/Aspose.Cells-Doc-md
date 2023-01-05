---
title: 公共 API Aspose.Cells 8.5.1 的变化
type: docs
weight: 170
url: /zh/net/public-api-changes-in-aspose-cells-8-5-1/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.5.0 到 8.5.1 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法，[添加类等](/cells/zh/net/public-api-changes-in-aspose-cells-8-5-1/)还描述了 Aspose.Cells 中幕后行为的任何变化。

{{% /alert %}} 
## **添加的 API**
### **方法 Workbook.Dispose 添加**
Workbook 对象现在实现了 System.IDisposable 接口，该接口只有一个 Dispose 方法。您可以直接调用 Workbook.Dispose 方法，也可以在 Using 结构中创建一个 Workbook 对象以自动调用此方法。

**C#**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook book = new Workbook();

//Call Dispose method

book.Dispose();

//Call Dispose method via Using statement

using (Workbook book = new Workbook())

{

    //do processing

}

{{< /highlight >}}


### **添加方法 Cell.GetHeightOfValue**
 Aspose.Cells for .NET 8.5.1暴露了Cell.GetHeightOfValue方法获取单元格高度值。通过使用此方法，您可以计算单元格值的高度，然后分别设置该单元格的行高。查看详细文章[如何计算单元格的高度和宽度](/cells/zh/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/).
### **添加了枚举 TableDataSourceType**
Aspose.Cells for .NET 8.5.1 公开了枚举 Aspose.Cells.Tables.TableDataSourceType 以检索 ListObject 的数据源类型。 TableDataSourceType 枚举如下字段。

1. TableDataSourceType.QueryTable
1. TableDataSourceType.SharePoint
1. TableDataSourceType.工作表
1. 表数据源类型.XML
### **添加了属性 ListObject.DataSourceType**
随着v8.5.1的发布，Aspose.Cells API 公开了readonly ListObject.DataSourceType属性，可以用来检测ListObject的数据源类型。

这里是最简单的使用场景。

**C#**

{{< highlight "csharp" >}}

 Workbook book = new Workbook("D:/book1.xlsx");

Worksheet sheet = book.Worksheets[0];

ListObject listObject = sheet.ListObjects[0];

if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.QueryTable)

{

    Console.WriteLine("Data Source Type is Query Table");

}

else if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.SharePoint)

{

    Console.WriteLine("Data Source Type is SharePoint Linked List");

}

else if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.Worksheet)

{

    Console.WriteLine("Data Source Type is Excel Worksheet Table");

}

else if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.XML)

{

    Console.WriteLine("Data Source Type is XML");

}

{{< /highlight >}}
