---
title: Aspose.Cells 8.8.2 中的公共 API 更改
type: docs
weight: 290
url: /zh/java/public-api-changes-in-aspose-cells-8-8-2/
---

{{% alert color="primary" %}} 

本文档描述了从版本 8.8.1 到 8.8.2 的 Aspose.Cells API 更改，可能会引起模块/应用程序开发人员的兴趣。它不仅包括新的和更新的公共方法、新增和删除的类等，还包括 Aspose.Cells 后台行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **在删除空白行和列时自动更新引用**
Aspose.Cells for Java 8.8.2版本已暴露了Cells.deleteBlankRows和Cells.deleteBlankColumns方法的重载版本。新方法可以接受DeleteOptions类的实例，并可以用于克服由于公式、图表系列数据等中的坏引用导致的情况。DeleteOptions类目前只有一个成员，一个名为UpdateReference的布尔类型属性。如果该属性设置为true，并且DeleteOptions类的实例被传递给Cells.deleteBlankRows和Cells.deleteBlankColumns方法，API将在内部调整公式引用（如果有的话）以适应更改。 

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看关于 [在删除工作表中的空白列和行时更新引用](/cells/zh/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/) 的详细文章。

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
