---
title: Aspose.Cells 8.8.2 中的公共 API 更改
type: docs
weight: 280
url: /zh/net/public-api-changes-in-aspose-cells-8-8-2/
---

{{% alert color="primary" %}} 

本文档描述了从版本 8.8.1 到 8.8.2 的 Aspose.Cells API 更改，可能会引起模块/应用程序开发人员的兴趣。它不仅包括新的和更新的公共方法、新增和删除的类等，还包括 Aspose.Cells 后台行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **在删除空白行和列时自动更新引用**
Aspose.Cells for .NET 8.8.2已经公开了Cells.DeleteBlankRows和Cells.DeleteBlankColumns方法的重载版本。新方法可以接受DeleteOptions类的实例，并且可以用于克服由于公式、图表系列数据等中断引用而可能引发的情况。DeleteOptions类目前只有一个成员，名为UpdateReference的布尔类型属性。如果该属性被设置为true，并且DeleteOptions类的实例被传递给Cells.DeleteBlankRows和Cells.DeleteBlankColumns方法，API将在内部调整公式引用（如果有的话）以适应更改。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请参阅[删除带有更新引用的空白行和列](/cells/zh/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)的详细文章。

{{% /alert %}} 

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook & load an existing spreadsheet

var book = new Workbook(dir + "sample.xlsx");

//Access worksheet from which blank rows/columns have to be deleted

var sheet = book.Worksheets[0];

//Access cells of the desired worksheet

var cells = sheet.Cells;

//Create an instance of DeleteOptions class

DeleteOptions options = new DeleteOptions();

//Set UpdateReference property to true;

options.UpdateReference = true;

//Delete all blank rows and columns

cells.DeleteBlankColumns(options);

cells.DeleteBlankRows(options);

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
