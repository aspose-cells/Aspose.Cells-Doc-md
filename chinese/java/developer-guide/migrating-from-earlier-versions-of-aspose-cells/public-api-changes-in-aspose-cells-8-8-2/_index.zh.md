---
title: Aspose.Cells 8.8.2中的公共API变更
type: docs
weight: 290
url: /zh/java/public-api-changes-in-aspose-cells-8-8-2/
---

{{% alert color="primary" %}} 

本文档描述了自8.8.1版本中Aspose.Cells API到8.8.2版本的变化，可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还包括任何Aspose.Cells内部行为变化的描述。

{{% /alert %}} 
## **已添加API**
### **在删除空白行和列时自动更新引用**
Aspose.Cells for Java 8.8.2已公开了Cells.deleteBlankRows和Cells.deleteBlankColumns方法的重载版本。 新方法可以接受DeleteOptions类的实例，并可用于克服由于在公式、图表系列数据等中出现的破损引用而可能出现的情况。 DeleteOptions类目前仅具有一个成员，名为UpdateReference的布尔类型属性。 如果将该属性设置为true，并且将DeleteOptions类的实例传递给Cells.deleteBlankRows和Cells.deleteBlankColumns方法，API将在内部调整公式引用（如果有）以适应更改。 

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看[删除具有更新引用的空白行和列](/cells/zh/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)的详细文章。

{{% /alert %}} 

以下是简单的使用场景。

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook & load an existing spreadsheet

Workbook book = new Workbook(dir + "sample.xlsx");

//Access worksheet from which blank rows/columns have to be deleted

Worksheet sheet = book.getWorksheets().get(0);

//Access cells of the desired worksheet

Cells cells = sheet.getCells();

//Create an instance of DeleteOptions class

DeleteOptions options = new DeleteOptions();

//Set UpdateReference property to true;

options.setUpdateReference(true);

//Delete all blank rows and columns

cells.deleteBlankColumns(options);

cells.deleteBlankRows(options);

{{< /highlight >}}
