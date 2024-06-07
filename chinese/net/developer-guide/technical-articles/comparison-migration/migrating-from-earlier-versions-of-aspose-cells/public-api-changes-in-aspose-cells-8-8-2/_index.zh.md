---
title: Aspose.Cells 8.8.2中的公共API变更
type: docs
weight: 280
url: /zh/net/public-api-changes-in-aspose-cells-8-8-2/
---

{{% alert color="primary" %}} 

本文档描述了自8.8.1版本中Aspose.Cells API到8.8.2版本的变化，可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还包括任何Aspose.Cells内部行为变化的描述。

{{% /alert %}} 
## **已添加API**
### **在删除空白行和列时自动更新引用**
Aspose.Cells for .NET 8.8.2现在公开了Cells.DeleteBlankRows和Cells.DeleteBlankColumns方法的重载版本。新方法可以接受一个DeleteOptions类的实例，并可以用来解决由于公式、图表系列数据等引用中断而可能出现的情况。DeleteOptions类目前只有一个成员，名为UpdateReference的Boolean类型属性。如果该属性设置为true并且将DeleteOptions类的实例传递给Cells.DeleteBlankRows和Cells.DeleteBlankColumns方法，API将在内部调整公式引用（如果有）以适应更改。

{{% alert color="primary" %}} 

有关此功能的更多详情，请查看有关删除具有更新引用的空白行和列的详细文章。

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
