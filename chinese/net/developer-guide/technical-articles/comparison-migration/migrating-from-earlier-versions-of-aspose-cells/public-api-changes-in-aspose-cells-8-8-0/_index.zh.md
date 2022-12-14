---
title: 公共 API Aspose.Cells 8.8.0 的变化
type: docs
weight: 260
url: /zh/net/public-api-changes-in-aspose-cells-8-8-0/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.7.2 到 8.8.0 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还包括对 Aspose.Cells 中幕后行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **获取 Cell 外部连接参考**
Aspose.Cells for .NET 8.8.0 公开了以下新属性，这些属性有助于检索存储在电子表格中的外部连接的目标和输出单元格引用。

1. QueryTable.ConnectionId：获取查询表的连接Id。
1. ExternalConnection.Id：获取外部连接的Id。
1. ListObject.QueryTable：获取链接的QueryTable。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看详细文章[查找与外部数据连接相关的查询表和列表对象](/cells/zh/net/find-query-tables-and-list-objects-related-to-external-data-connections/)

{{% /alert %}} 
### **添加了 HTMLLoadOptions.KeepPrecision 属性**
Aspose.Cells for .NET 8.8.0 添加了 HTMLLoadOptions.KeepPrecision 属性，以便在导入 HTML 文件时控制长数值到指数表示法的转换。默认情况下，如果数据是从 HTML 字符串或文件导入的，任何超过 15 位的值都会转换为指数表示法。但是，现在用户可以借助 HTMLLoadOptions.KeepPrecision 属性来控制此行为。如果上述属性设置为 true，则这些值将按它们在源中的原样导入。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看详细文章[避免将大数值转换为指数表示法](/cells/zh/net/avoid-exponential-notation-of-large-numbers-while-importing-from/)

{{% /alert %}} 

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

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

byte[]byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.KeepPrecision = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

Worksheet sheet = workbook.Worksheets[0];

sheet.AutoFitColumns();

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **添加了 HTMLLoadOptions.DeleteRedundantSpaces 属性**
Aspose.Cells for .NET 8.8.0 公开了 HTMLLoadOptions.DeleteRedundantSpaces 属性，以便保留或删除换行标记后的额外空格 (<br>标记），同时从 HTML 字符串或文件导入数据。 HTMLLoadOptions.DeleteRedundantSpaces 属性的默认值为 false，这意味着所有额外的空格都将被保留并导入到 Workbook 对象中，但是，当设置为 true 时，API 将删除换行符标记之后的所有冗余空格。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看详细文章[从 HTML 中删除冗余空格](/cells/zh/net/delete-redundant-spaces-after-line-break-while-importing/)

{{% /alert %}} 

简单的使用场景如下。

**C#**

{{< highlight "csharp" >}}

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

byte[]byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.DeleteRedundantSpaces = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **添加了 Style.QuotePrefix 属性**
Aspose.Cells for .NET 8.8.0 公开了 Style.QuotePrefix 属性以检测单元格值是否以单引号开头。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看详细文章[在 Cell 值的开头检测单引号](/cells/zh/net/find-if-the-cell-value-starts-with-single-quote-mark/)

{{% /alert %}} 

简单的使用场景如下。

**C#**

{{< highlight "csharp" >}}

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
## **过时的 API**
### **废弃的 LoadOptions.ConvertNumericData 属性**
Aspose.Cells 8.8.0 已将 LoadOptions.ConvertNumericData 属性标记为已废弃。请使用 HTMLLoadOptions 或 TxtLoadOptions 类中的相应属性。
