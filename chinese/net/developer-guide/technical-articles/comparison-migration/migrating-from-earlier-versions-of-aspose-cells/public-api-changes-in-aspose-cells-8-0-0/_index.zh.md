---
title: Aspose.Cells 8.0.0中的公共API更改
type: docs
weight: 10
url: /zh/net/public-api-changes-in-aspose-cells-8-0-0/
---

{{% alert color="primary" %}} 

此页面列出了Aspose.Cells 8.0.0中引入的公共API更改。不仅包括新的和已弃用的公共方法，还包括可能影响现有代码背后行为的任何更改在Aspose.Cells中。

{{% /alert %}} 
## **向LoadOptions和WorkbookSettings添加了MemorySetting**
从Aspose.Cells for .NET v8.0.0开始，我们提供了内存使用选项以用于性能考虑。MemorySetting属性现在在LoadOptions和WorkbookSettings类中可用。
##### **例子**
演示如何以优化模式读取具有大尺寸的Excel文件。

**C#**

{{< highlight csharp >}}

 //Initialize LoadOptions

LoadOptions options = new LoadOptions();

//Set memory preferences

options.MemorySetting = MemorySetting.MEMORY_PREFERENCE;

//Instantiate the Workbook with an object of LoadOptions

Workbook book = new Workbook(myDir + "large.xlsx", options);

{{< /highlight >}}

演示如何以优化模式将大型数据集写入工作表。

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

请查阅有关[在处理大文件时优化内存的详细文章](/cells/zh/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)

{{% /alert %}}
## **Row和Cell的实现已更改**
在以前的版本中，Row和Cell对象保留在内存中，以表示工作表中相应的行和单元格。每当检索**RowCollection[int index]**或**Cells[int row, int column]**时，将返回相同的实例。出于内存性能考虑，现在只会保留Row和Cell的属性和数据。因此，Row和Cell对象现已成为上述属性的包装器。
### **例子**
演示如何从现在开始比较Cell和Row对象。

**C#**

{{< highlight csharp >}}

 //..

row1.Equals(row2);


cell1.Equals(cell2);

//..

{{< /highlight >}}

由于Row和Cell对象是根据调用实例化的，它们不会被Cells组件在内存中保留和管理。因此，在进行一些插入和删除操作后，Row和Column索引可能不会被更新，甚至更糟的是，这些对象可能变得无效。
### **例子**
例如，以下代码片段将在8.0.0及以上版本中返回无效结果，

**C#**

{{< highlight csharp >}}

 Cell cell = cells["A2"];

Console.WriteLine(cell.Name + ":" + cell.Value);

cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);

Console.WriteLine(cell.Name + ":" + cell.Value);

{{< /highlight >}}



使用新版本，Cell对象将变为无效或引用带有一些不必要值的A2。为避免这种情况，请从单元格集合重新获取Row或Cell对象以检索正确的结果。

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

RowCollection不再继承CollectionBase，因为其内部列表中没有Row对象。

{{% /alert %}}
## **Cell.StringValue行为已更改**
在之前的版本中，格式化单元格值时特殊的模式 _ 会被忽略，而特殊字符 * 则总是会在格式化结果中产生一个字符。从这个版本开始，我们已经改变了处理特殊字符 _ 和 * 的逻辑，以使格式化的结果与 Excel 应用程序相同。例如，自定义的单元格格式 "_(\$* #,##0.00_)" 用来表示值 123 的结果为 "$ 123.00"。使用新版本后，Cell.StringValue 将包含结果 "$123.00"，这与将单元格复制到文本或导出到 CSV 时 Excel 应用程序表现的行为相同。
## **向 PdfSaveOptions 中添加了 CreatedTime**
现在用户在使用 PdfSaveOptions 类保存电子表格为 PDF 时可以设置或获取 PDF 创建时间。
## **向工作表添加 ShowFormulas**
从现在开始，用户可以使用工作表提供的布尔属性 ShowFormulas 来在给定工作表的公式和值之间切换视图。
## **向 FileFormatType 添加了 Ooxml**
已向 FileFormatType 类添加了一个新常量 Ooxml，用于表示加密的 Office 开放 XML 文件，如 XLSX、DOCX、PPTX 等。
## **已废弃 AutoFilter 的 FilterColumnCollection**
在 Aspose.Cells for Java 中，FilterColumnCollection 属性已被标记为过时。建议改用 AuotFilter.FilterColumns 属性。
## **用 SeriesCollection.SecondCategoryData 替换了 SeriesCollection.SecondCatergoryData**
我们已经纠正了 SeriesCollection.SecondCatergoryData 属性名称的拼写错误。您现在可以使用 SeriesCollection.SecondCategoryData 属性，而原来的属性 SeriesCollection.SecondCatergoryData 已被标记为过时。
