---
title: Aspose.Cells 8.5.1 中的公共 API 更改
type: docs
weight: 170
url: /zh/net/public-api-changes-in-aspose-cells-8-5-1/
---

{{% alert color="primary" %}} 

本文描述了从版本8.5.0到8.5.1的Aspose.Cells API的更改，可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，添加的类等，还包括Aspose.Cells幕后行为中的任何更改的描述。

{{% /alert %}} 
## **已添加API**
### **新增 Workbook.Dispose 方法**
Workbook 对象现在实现了 System.IDisposable 接口，其中包含一个 Dispose 方法。您可以直接调用 Workbook.Dispose 方法，或者在 Using 结构中创建一个 Workbook 对象以自动调用该方法。

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


### **新增 Cell.GetHeightOfValue 方法**
Aspose.Cells for .NET 8.5.1已公开了Cell.GetHeightOfValue方法，用于获取单元格值的高度。通过使用此方法，您可以计算单元格值的高度，然后相应地设置该单元格所在行的高度。查看关于如何计算单元格高度和宽度的详细文章。
### **新增 TableDataSourceType 枚举**
Aspose.Cells for .NET 8.5.1 暴露了枚举 Aspose.Cells.Tables.TableDataSourceType，用于检索 ListObject 的数据源类型。TableDataSourceType 枚举具有以下字段。

1. TableDataSourceType.QueryTable
1. TableDataSourceType.SharePoint
1. TableDataSourceType.Worksheet
1. TableDataSourceType.XML
### **新增 ListObject.DataSourceType 属性**
随着 v8.5.1 的发布，Aspose.Cells API 暴露了 ListObject.DataSourceType 只读属性，用于检测 ListObject 的数据源类型。

这里是最简单的使用场景。

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
