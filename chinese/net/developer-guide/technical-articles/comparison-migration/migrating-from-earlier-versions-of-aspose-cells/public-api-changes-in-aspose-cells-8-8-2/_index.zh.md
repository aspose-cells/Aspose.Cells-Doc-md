---
title: 公共 API Aspose.Cells 8.8.2 的变化
type: docs
weight: 280
url: /zh/net/public-api-changes-in-aspose-cells-8-8-2/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.8.1 到 8.8.2 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还包括对 Aspose.Cells 中幕后行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **删除空白行和列时自动更新引用**
Aspose.Cells for .NET 8.8.2 公开了 Cells.DeleteBlankRows 和 Cells.DeleteBlankColumns 方法的重载版本。新方法可以接受 DeleteOptions 类的一个实例，并可用于克服由于公式、图表系列数据等中的引用损坏而可能出现的情况。 DeleteOptions 类目前只有一个成员，名为 UpdateReference 的布尔类型属性。如果上述属性设置为 true 并且 DeleteOptions 类的实例传递给 Cells.DeleteBlankRows 和 Cells.DeleteBlankColumns 方法，则 API 将在内部调整公式引用（如果有）以适应更改。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看详细文章[使用更新的参考删除空白行和列](/cells/zh/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/).

{{% /alert %}} 

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

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
