---
title: Aspose.Cells 8.0.0中的公共API更改
type: docs
weight: 10
url: /zh/net/public-api-changes-in-aspose-cells-8-0-0/
---

{{% alert color="primary" %}} 

本页面列出了Aspose.Cells 8.0.0中引入的公共API更改。它不仅包括新的和已弃用的公共方法，还包括Aspose.Cells后台行为的任何更改的描述，这可能会影响现有代码。

{{% /alert %}} 
## **将MemorySetting添加到LoadOptions和WorkbookSettings**
从Aspose.Cells for .NET的v8.0.0开始，我们为性能考虑提供了内存使用选项。现在在LoadOptions和WorkbookSettings类中提供了MemorySetting属性。
##### **示例**
演示如何在优化模式下读取大型Excel文件。

**C#**

{{< highlight csharp >}}

 //Initialize LoadOptions

LoadOptions options = new LoadOptions();

//Set memory preferences

options.MemorySetting = MemorySetting.MEMORY_PREFERENCE;

//Instantiate the Workbook with an object of LoadOptions

Workbook book = new Workbook(myDir + "large.xlsx", options);

{{< /highlight >}}

演示如何在优化模式下将大型数据集写入工作表。

**C#**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences for WorkbookSettings

book.Settings.MemorySetting = MemorySetting.MEMORY_PREFERENCE;

//Input large data into the cells

//.........

{{< /highlight >}}

{{% alert color="primary" %}} 

请查看有关[优化处理大文件时的内存使用情况](/cells/zh/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)的详细文章。

{{% /alert %}}
## **Row和Cell的实现发生了变化**
在之前的版本中，Row和Cell对象被保留在内存中，以表示工作表中对应的行和单元格。每当检索**RowCollection[int index]**或**Cells[int row, int column]**时，都会返回相同的实例。出于内存性能的考虑，现在将仅保存Row和Cell的属性和数据在内存中。因此，Row和Cell对象现在变成了前述属性的包装器。
### **示例**
演示如何从现在开始比较单元格对象和行对象。

**C#**

{{< highlight csharp >}}

 //..

row1.Equals(row2);


cell1.Equals(cell2);

//..

{{< /highlight >}}

因为Row和Cell对象是根据调用实例化的，它们将不会被Cells组件保持和管理在内存中。因此，在一些插入和删除操作之后，Row和Column索引可能没有更新，甚至更糟糕的是，这些对象变得无效。
### **示例**
例如，以下代码片段将在8.0.0及以上版本中返回无效结果，

**C#**

{{< highlight csharp >}}

 Cell cell = cells["A2"];

Console.WriteLine(cell.Name + ":" + cell.Value);

cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);

Console.WriteLine(cell.Name + ":" + cell.Value);

{{< /highlight >}}



使用新版本，Cell对象将变得无效或引用A2的一些不需要的值。为了避免这种情况，重新从cell集合中获取Row或Cell对象以检索正确的结果。

**C#**

{{< highlight csharp >}}

 Cell cell = cells["A2"];

Console.WriteLine(cell.Name + ":" + cell.Value);

cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);

//Fetch the cell reference again

Cell cell = cells["A3"];

Console.WriteLine(cell.Name + ":" + cell.Value);

{{< /highlight >}}

{{% alert color="primary" %}} 

RowCollection不再继承CollectionBase，因为其内部列表中不再有Row对象。

{{% /alert %}}
## **Cell.StringValue的行为已更改**
在以前的版本中，特殊模式下的_被忽略，而特殊字符*总是将一个字符放入格式化的结果中。从这个版本开始，我们已经改变了处理特殊字符_和*的逻辑，以使格式化的结果与Excel应用程序的行为相同。例如，自定义单元格格式"_(\$* #,##0.00_)"用于表示值123产生的结果为"$ 123.00"。使用新版本，Cell.StringValue将包含结果"$123.00"，这与Excel应用程序在将单元格复制到文本或导出为CSV时展示的行为相同。
## **添加了CreatedTime到PdfSaveOptions**
现在用户可以在使用PdfSaveOptions类保存电子表格为PDF时获取或设置PDF创建时间。
## **向Worksheet添加了ShowFormulas**
从现在开始，用户可以通过Worksheet提供的Boolean属性ShowFormulas来改变给定工作表的视图，从公式视图切换到数值视图。
## **添加了Ooxml到FileFormatType**
为FileFormatType类添加了一个新的常量Ooxml，用来表示加密的Office开放XML文件，比如XLSX、DOCX、PPTX等。
## **已过时FilterColumnCollection的AutoFilter**
使用Aspose.Cells for Java时，FilterColumnCollection属性已经标记为过时。建议改用AuotFilter.FilterColumns属性。
## **用SeriesCollection.SecondCategoryData替换了SeriesCollection.SecondCatergoryData**
我们基本上纠正了SeriesCollection.SecondCatergoryData属性名称的拼写错误。您可以从现在开始使用SeriesCollection.SecondCategoryData属性，而原始属性SeriesCollection.SecondCatergoryData已被标记为废弃。
