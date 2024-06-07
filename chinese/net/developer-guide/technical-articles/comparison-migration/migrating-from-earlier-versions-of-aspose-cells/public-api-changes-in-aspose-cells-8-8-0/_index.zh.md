---
title: Aspose.Cells 8.8.0版本的公共API更改
type: docs
weight: 260
url: /zh/net/public-api-changes-in-aspose-cells-8-8-0/
---

{{% alert color="primary" %}} 

此文档描述了从版本8.7.2到8.8.0的Aspose.Cells API的更改，这可能会对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还包括对Aspose.Cells后台行为的任何更改的描述。

{{% /alert %}} 
## **已添加API**
### **获取外部连接的单元引用**
Aspose.Cells for .NET 8.8.0已公开了以下新属性，有助于检索存储在电子表格中的外部连接的目标和输出单元引用。

1. QueryTable.ConnectionId: 获取查询表的连接ID。
1. ExternalConnection.Id: 获取外部连接的ID。
1. ListObject.QueryTable: 获取链接的查询表。

{{% alert color="primary" %}} 

有关此功能的更多详情，请查看关于查找与外部数据连接相关的查询表和列表对象的详细文章。

{{% /alert %}} 
### **已添加HTMLLoadOptions.KeepPrecision属性**
Aspose.Cells for .NET 8.8.0已添加HTMLLoadOptions.KeepPrecision属性，以便在导入HTML文件时控制长数字值转换为指数符号。默认情况下，如果从HTML字符串或文件导入数据，则长度超过15位的任何值都会转换为指数符号。然而，现在用户可以通过HTMLLoadOptions.KeepPrecision属性 控制此行为。如果将该属性设置为true，则值将按照源中的值导入。

{{% alert color="primary" %}} 

有关此功能的更多详情，请查看关于避免将大数值转换为指数表示法的详细文章。

{{% /alert %}} 

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

 string html = @" 

<table data-cache=""not-cached"" class=""sortable""> 

   <tbody> 

    <tr> 

     <td class=""even"">9999999999999999</td> 

     <td class=""odd"">10.8%</td> 

    </tr> 

   </tbody> 

</table> 

";

byte[] byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.KeepPrecision = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

Worksheet sheet = workbook.Worksheets[0];

sheet.AutoFitColumns();

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **已添加HTMLLoadOptions.DeleteRedundantSpaces属性**
Aspose.Cells for .NET 8.8.0 has exposed the HTMLLoadOptions.DeleteRedundantSpaces property in order to keep or delete the extra spaces after the line break tag (<br> Tag) while importing the data from the HTML string or file. The HTMLLoadOptions.DeleteRedundantSpaces property has the default value as false that means, all extra spaces will be preserved and imported to the Workbook object, however, when set to true, the API will delete all the redundant spaces coming after the line break tag.

{{% alert color="primary" %}} 

有关此功能的更多详情，请查看关于从HTML中删除多余空格的详细文章。

{{% /alert %}} 

简单的使用场景如下。

**C#**

{{< highlight csharp >}}

 string html = @" 

<html>

    <body>

        <table>

            <tr>

                <td>

                    <br>    This is sample data 

                    <br>    This is sample data

                    <br>    This is sample data

                </td>

            </tr>

        </table>

    </body>

</html>

";

byte[] byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.DeleteRedundantSpaces = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **已添加Style.QuotePrefix属性**
Aspose.Cells for .NET 8.8.0已公开了Style.QuotePrefix属性，以检测单元格值是否以单引号符号开头。

{{% alert color="primary" %}} 

有关此功能的更多详情，请查看检测单元格值是否以单引号开头的详细文章。

{{% /alert %}} 

简单的使用场景如下。

**C#**

{{< highlight csharp >}}

 Workbook book = new Workbook();

Worksheet sheet = book.Worksheets[0];

Cell a1 = sheet.Cells["A1"];

Cell a2 = sheet.Cells["A2"];

a1.PutValue("sample");

a2.PutValue("'sample");

Console.WriteLine("String value of A1: " + a1.StringValue);

Console.WriteLine("String value of A2: " + a2.StringValue);

Style s1 = a1.GetStyle();

Style s2 = a2.GetStyle();

Console.WriteLine("A1 has a quote prefix: " + s1.QuotePrefix);

Console.WriteLine("A2 has a quote prefix: " + s2.QuotePrefix);

{{< /highlight >}}
## **已废弃的API**
### **已废弃LoadOptions.ConvertNumericData属性**
Aspose.Cells 8.8.0已标记LoadOptions.ConvertNumericData属性为废弃。请使用HTMLLoadOptions或TxtLoadOptions类中相应的属性。
