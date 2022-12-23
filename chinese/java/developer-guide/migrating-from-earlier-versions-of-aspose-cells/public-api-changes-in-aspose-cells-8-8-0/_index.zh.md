---
title: 公共 API Aspose.Cells 8.8.0 的变化
type: docs
weight: 270
url: /zh/java/public-api-changes-in-aspose-cells-8-8-0/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.7.2 到 8.8.0 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还包括对 Aspose.Cells 中幕后行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **获取 Cell 外部连接参考**
Aspose.Cells for Java 8.8.0 公开了以下新属性，这些属性有助于检索存储在电子表格中的外部连接的目标和输出单元格引用。

1. QueryTable.ConnectionId：获取查询表的连接Id。
1. ExternalConnection.Id：获取外部连接的Id。
1. ListObject.QueryTable：获取链接的QueryTable。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看详细文章[查找与外部数据连接相关的查询表和列表对象](/cells/zh/java/find-query-tables-and-list-objects-related-to-external-data-connections/)

{{% /alert %}} 
### **添加了 HTMLLoadOptions.KeepPrecision 属性**
Aspose.Cells for Java 8.8.0 添加了 HTMLLoadOptions.KeepPrecision 属性，以控制在导入 HTML 文件时将长数值转换为指数表示法。默认情况下，如果数据是从 HTML 字符串或文件导入的，任何超过 15 位的值都会转换为指数表示法。但是，现在用户可以借助 HTMLLoadOptions.KeepPrecision 属性来控制此行为。如果上述属性设置为 true，则这些值将按它们在源中的原样导入。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看详细文章[避免将大数值转换为指数表示法](/cells/zh/java/avoid-exponential-notation-of-large-numbers-while-importing-from/)

{{% /alert %}} 

以下是简单的使用场景。

**Java**

{{< highlight "csharp" >}}

 //Sample Html containing large number with digits greater than 15

String html = "<html>"

		+ "<body>"

		+ "<p>1234567890123456</p>"

		+ "</body>"

		+ "</html>";

//Convert Html to byte array

byte[]byteArray = html.getBytes();

//Set Html load options and keep precision true

HTMLLoadOptions loadOptions = new HTMLLoadOptions(LoadFormat.HTML);

loadOptions.setKeepPrecision(true);

//Convert byte array into stream

java.io.ByteArrayInputStream stream = new java.io.ByteArrayInputStream(byteArray);

//Create workbook from stream with Html load options

Workbook workbook = new Workbook(stream, loadOptions);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Auto fit the sheet columns

worksheet.autoFitColumns();

//Save the workbook

workbook.save(dataDir + "output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **添加了 HTMLLoadOptions.DeleteRedundantSpaces 属性**
Aspose.Cells for Java 8.8.0 公开了 HTMLLoadOptions.DeleteRedundantSpaces 属性，以便保留或删除换行标记后的额外空格 (<br>标签），同时从 HTML 字符串或文件导入数据。 HTMLLoadOptions.DeleteRedundantSpaces 属性的默认值为 false，这意味着所有额外的空格都将被保留并导入到 Workbook 对象中，但是，当设置为 true 时，API 将删除换行标记之后的所有冗余空格。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看详细文章[从 HTML 中删除冗余空间](/cells/zh/java/delete-redundant-spaces-after-line-break-while-importing/)

{{% /alert %}} 

简单的使用场景如下。

**Java**

{{< highlight "csharp" >}}

 //Sample Html containing redundant spaces after <br> tag

String html = "<html>"

		+ "<body>"

			+ "<table>"

				+ "<tr>"

					+ "<td>"

						+ "<br>    This is sample data"

						+ "<br>    This is sample data"

						+ "<br>    This is sample data"

					+ "</td>"

				+ "</tr>"

			+ "</table>"

		+ "</body>"

	+ "</html>";

//Convert Html to byte array

byte[]byteArray = html.getBytes();

//Set Html load options and keep precision true

HTMLLoadOptions loadOptions = new HTMLLoadOptions(LoadFormat.HTML);

loadOptions.setDeleteRedundantSpaces(true);

//Convert byte array into stream

java.io.ByteArrayInputStream stream = new java.io.ByteArrayInputStream(byteArray);

//Create workbook from stream with Html load options

Workbook workbook = new Workbook(stream, loadOptions);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Auto fit the sheet columns

worksheet.autoFitColumns();

//Save the workbook

workbook.save(dataDir + "output-" + loadOptions.getDeleteRedundantSpaces() + ".xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **添加了 Style.QuotePrefix 属性**
Aspose.Cells for Java 8.8.0 公开了 Style.QuotePrefix 属性以检测单元格值是否以单引号开头。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看详细文章[在 Cell 值的开头检测单引号](/cells/zh/java/find-if-the-cell-value-starts-with-single-quote-mark/)

{{% /alert %}} 

简单的使用场景如下。

**Java**

{{< highlight "csharp" >}}

 //Create an instance of workbook

Workbook workbook = new Workbook();

//Access first worksheet from the collection

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cells A1 and A2

Cell a1 = worksheet.getCells().get("A1");

Cell a2 = worksheet.getCells().get("A2");

//Add simple text to cell A1 and text with quote prefix to cell A2

a1.putValue("sample");

a2.putValue("'sample");

//Print their string values, A1 and A2 both are same

System.out.println("String value of A1: " + a1.getStringValue());

System.out.println("String value of A2: " + a2.getStringValue());

//Access styles of cells A1 and A2

Style s1 = a1.getStyle();

Style s2 = a2.getStyle();

System.out.println();

//Check if A1 and A2 has a quote prefix

System.out.println("A1 has a quote prefix: " + s1.getQuotePrefix());

System.out.println("A2 has a quote prefix: " + s2.getQuotePrefix());

{{< /highlight >}}
## **过时的 API**
### **废弃的 LoadOptions.ConvertNumericData 属性**
Aspose.Cells 8.8.0 已将 LoadOptions.ConvertNumericData 属性标记为已废弃。请使用 HTMLLoadOptions 或 TxtLoadOptions 类中的相应属性。
