---
title: Aspose.Cells 8.8.0版本的公共API更改
type: docs
weight: 270
url: /zh/java/public-api-changes-in-aspose-cells-8-8-0/
---

{{% alert color="primary" %}} 

此文档描述了从版本8.7.2到8.8.0的Aspose.Cells API的更改，这可能会对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还包括对Aspose.Cells后台行为的任何更改的描述。

{{% /alert %}} 
## **已添加API**
### **获取外部连接的单元引用**
Aspose.Cells for Java 8.8.0已经公开了以下新属性，可帮助检索保存在电子表格中的外部连接的目标和输出单元引用。 

1. QueryTable.ConnectionId: 获取查询表的连接ID。
1. ExternalConnection.Id: 获取外部连接的ID。
1. ListObject.QueryTable: 获取链接的查询表。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看[查找与外部数据连接相关的查询表和列表对象](/cells/zh/java/find-query-tables-and-list-objects-related-to-external-data-connections/)的详细文章。

{{% /alert %}} 
### **已添加HTMLLoadOptions.KeepPrecision属性**
发布Aspose.Cells for Java 8.8.0后，添加了HTMLLoadOptions.KeepPrecision属性，以控制从HTML文件导入时长数字值转换为指数符号的行为。使用HTMLLoadOptions.KeepPrecision属性可以控制此行为。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看[避免从HTML导入时将大数转换为指数符号](/cells/zh/java/avoid-exponential-notation-of-large-numbers-while-importing-from/)的详细文章。

{{% /alert %}} 

以下是简单的使用场景。

**Java**

{{< highlight csharp >}}

 //Sample Html containing large number with digits greater than 15

String html = "<html>"

		+ "<body>"

		+ "<p>1234567890123456</p>"

		+ "</body>"

		+ "</html>";

//Convert Html to byte array

byte[] byteArray = html.getBytes();

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
### **已添加HTMLLoadOptions.DeleteRedundantSpaces属性**
Aspose.Cells for Java 8.8.0 has exposed the HTMLLoadOptions.DeleteRedundantSpaces property in order to keep or delete the extra spaces after the line break tag (<br> Tag) while importing the data from the HTML string or file. The HTMLLoadOptions.DeleteRedundantSpaces property has the default value as false that means, all extra spaces will be preserved and imported to the Workbook object, however, when set to true, the API will delete all the redundant spaces coming after the line break tag.

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看[从HTML删除冗余空格](/cells/zh/java/delete-redundant-spaces-after-line-break-while-importing/)的详细文章。

{{% /alert %}} 

简单的使用场景如下。 

**Java**

{{< highlight csharp >}}

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

byte[] byteArray = html.getBytes();

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
### **已添加Style.QuotePrefix属性**
发布Aspose.Cells for Java 8.8.0后，已公开了Style.QuotePrefix属性，以检测单元格值是否以单引号符号开头。 

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看[检测单元格值是否以单引号开头](/cells/zh/java/find-if-the-cell-value-starts-with-single-quote-mark/)的详细文章。

{{% /alert %}} 

简单的使用场景如下。 

**Java**

{{< highlight csharp >}}

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
## **已废弃的API**
### **已废弃LoadOptions.ConvertNumericData属性**
Aspose.Cells 8.8.0已标记LoadOptions.ConvertNumericData属性为废弃。请使用HTMLLoadOptions或TxtLoadOptions类中相应的属性。
