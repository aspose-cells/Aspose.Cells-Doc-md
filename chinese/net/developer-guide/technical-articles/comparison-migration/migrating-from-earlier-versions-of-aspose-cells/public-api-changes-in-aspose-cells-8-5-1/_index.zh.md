---
title: Aspose.Cells 8.5.1中的公共API更改
type: docs
weight: 170
url: /zh/net/public-api-changes-in-aspose-cells-8-5-1/
---

{{% alert color="primary" %}} 

本文描述了Aspose.Cells API从版本8.5.0到8.5.1的更改，这些更改可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法、[新增的类等](/cells/zh/net/public-api-changes-in-aspose-cells-8-5-1/)，还描述了Aspose.Cells在幕后行为的任何更改。

{{% /alert %}} 
## **添加的 API**
### **添加了Workbook.Dispose方法**
Workbook对象现在实现了System.IDisposable接口，该接口具有一个Dispose方法。您可以直接调用Workbook.Dispose方法，或者在Using结构中创建一个Workbook对象来自动调用此方法。

**C#**

{{< highlight csharp >}}

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


### **添加了Cell.GetHeightOfValue方法**
Aspose.Cells for .NET 8.5.1已公开了Cell.GetHeightOfValue方法，用于获取单元格值的高度。通过使用此方法，您可以计算单元格值的高度，然后相应地设置该单元格的行高度。查看[如何计算单元格高度和宽度](/cells/zh/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)的详细文章。
### **添加了TableDataSourceType枚举**
Aspose.Cells for .NET 8.5.1已公开了Aspose.Cells.Tables.TableDataSourceType枚举，用于检索ListObject的数据源类型。TableDataSourceType枚举具有以下字段。

1. TableDataSourceType.QueryTable
1. TableDataSourceType.SharePoint
1. TableDataSourceType.Worksheet
1. TableDataSourceType.XML
### **添加了ListObject.DataSourceType属性**
随着v8.5.1的发布，Aspose.Cells API公开了只读的ListObject.DataSourceType属性，用于检测ListObject的数据源类型。

这是最简单的使用场景。

**C#**

{{< highlight csharp >}}

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
{{< app/cells/assistant language="csharp" >}}
