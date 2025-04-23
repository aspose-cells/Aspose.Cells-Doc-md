---
title: Aspose.Cells 8.8.0中的公共API更改
type: docs
weight: 260
url: /zh/net/public-api-changes-in-aspose-cells-8-8-0/
---

{{% alert color="primary" %}} 

本文档描述了从版本8.7.2到8.8.0的Aspose.Cells API的更改，这可能会对模块/应用程序开发人员感兴趣。它不仅包括新和更新的公共方法、添加和删除的类等，还描述了Aspose.Cells背后的行为中的任何变化。

{{% /alert %}} 
## **添加的 API**
### **获取外部连接的单元引用**
Aspose.Cells for .NET 8.8.0已公开了以下新属性，有助于检索存储在电子表格中的外部连接的目标和输出单元引用。

1. QueryTable.ConnectionId: 获取查询表的连接ID。
1. ExternalConnection.Id: 获取外部连接的ID。
1. ListObject.QueryTable: 获取关联的QueryTable。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看 [查找与外部数据连接相关的查询表和列表对象](/cells/zh/net/find-query-tables-and-list-objects-related-to-external-data-connections/) 的详细文章。

{{% /alert %}} 
### **添加了HTMLLoadOptions.KeepPrecision属性。**
Aspose.Cells for .NET 8.8.0已添加了HTMLLoadOptions.KeepPrecision属性，以控制在导入HTML文件时将长数字值转换为指数符号的行为。默认情况下，如果数据是从HTML字符串或文件导入，并且值超过15位，则任何值都会被转换为指数符号。然而，现在用户可以通过HTMLLoadOptions.KeepPrecision属性来控制此行为。如果设置为true，则值将按原样导入。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看[避免大数值转换为指数符号](/cells/zh/net/avoid-exponential-notation-of-large-numbers-while-importing-from/)的详细文章。

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


### **添加了HTMLLoadOptions.DeleteRedundantSpaces属性。**
Aspose.Cells for .NET 8.8.0 has exposed the HTMLLoadOptions.DeleteRedundantSpaces property in order to keep or delete the extra spaces after the line break tag (<br> Tag) while importing the data from the HTML string or file. The HTMLLoadOptions.DeleteRedundantSpaces property has the default value as false that means, all extra spaces will be preserved and imported to the Workbook object, however, when set to true, the API will delete all the redundant spaces coming after the line break tag.

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看[从HTML删除冗余空格](/cells/zh/net/delete-redundant-spaces-after-line-break-while-importing/)的详细文章。

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


### **添加了Style.QuotePrefix属性。**
Aspose.Cells for .NET 8.8.0已公开了Style.QuotePrefix属性，以便检测单元格值是否以单引号符号开头。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看[检测单元格值是否以单引号开头](/cells/zh/net/find-if-the-cell-value-starts-with-single-quote-mark/)的详细文章。

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
## **已弃用的API**
### **弃用了LoadOptions.ConvertNumericData属性**
Aspose.Cells 8.8.0已将LoadOptions.ConvertNumericData属性标记为弃用。请使用HTMLLoadOptions或TxtLoadOptions类中的相应属性。
{{< app/cells/assistant language="csharp" >}}
