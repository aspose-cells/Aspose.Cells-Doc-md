---
title: Aspose.Cells 8.0.0中的公共API更改
type: docs
weight: 20
url: /zh/java/public-api-changes-in-aspose-cells-8-0-0/
---

{{% alert color="primary" %}} 

本页面列出了Aspose.Cells 8.0.0中引入的公共API更改。它不仅包括新的和已弃用的公共方法，还包括Aspose.Cells后台行为的任何更改的描述，这可能会影响现有代码。

{{% /alert %}} 
## **将MemorySetting添加到LoadOptions和WorkbookSettings**
从Aspose.Cells for Java v8.0.0开始，我们提供了内存使用选项以进行性能考虑。MemorySetting属性现在在LoadOptions和WorkbookSettings类中可用。
### **示例**
演示如何在优化模式下读取大型Excel文件。

**Java**

{{< highlight csharp >}}

 //Initialize LoadOptions

LoadOptions options = new LoadOptions();

//Set memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook with an object of LoadOptions

Workbook book = new Workbook(myDir + "large.xlsx", options);

{{< /highlight >}}

演示如何在优化模式下将大型数据集写入工作表。

**Java**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences for WorkbookSettings

book.getSettings().setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Input large data into the cells

//.........

{{< /highlight >}}

{{% alert color="primary" %}} 

请查看 [在处理大数据集的大文件时优化内存使用](/cells/zh/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/) 的详细文章。

{{% /alert %}}
## **Row和Cell的实现发生了变化**
在之前的版本中，Row和Cell对象被保留在内存中，以表示工作表中对应的行和单元格。每当检索**RowCollection[int index]**或**Cells[int row, int column]**时，都会返回相同的实例。出于内存性能的考虑，现在将仅保存Row和Cell的属性和数据在内存中。因此，Row和Cell对象现在变成了前述属性的包装器。
### **示例**
演示如何从现在开始比较单元格对象和行对象。

**Java**

{{< highlight csharp >}}

 //..

row1.equals(row2);


cell1.equals(cell2);

//..

{{< /highlight >}}

因为Row和Cell对象是根据调用实例化的，它们将不会被Cells组件保持和管理在内存中。因此，在一些插入和删除操作之后，Row和Column索引可能没有更新，甚至更糟糕的是，这些对象变得无效。
### **示例**
例如，以下代码片段将在8.0.0及以上版本中返回无效结果，

**Java**

{{< highlight csharp >}}

 Cell cell = cells.get("A2");

System.out.println(cell.getName() + ":" + cell.getValue());

cells.insertRange(CellArea.createCellArea("A1", "A1"), ShiftType.DOWN);

System.out.println(cell.getName() + ":" + cell.getValue());

{{< /highlight >}}

使用新版本，Cell对象将变得无效或引用A2的一些不需要的值。为了避免这种情况，重新从cell集合中获取Row或Cell对象以检索正确的结果。

**Java**

{{< highlight csharp >}}

 Cell cell = cells.get("A2");

System.out.println(cell.getName() + ":" + cell.getValue());

cells.insertRange(CellArea.createCellArea("A1", "A1"), ShiftType.DOWN);

//Fetch the cell reference again

Cell cell = cells.get("A3");

System.out.println(cell.getName() + ":" + cell.getValue());

{{< /highlight >}}

{{% alert color="primary" %}} 

RowCollection不再继承CollectionBase，因为其内部列表中不再有Row对象。

{{% /alert %}}
## **Cell.StringValue的行为已更改**
在以前的版本中，在格式化单元格值时，特殊模式_会被忽略，而特殊字符*总是会产生一个字符到格式化结果中。从这个版本开始，我们已经改变了处理特殊字符_和*的逻辑，以使格式化结果与Excel应用程序相同。例如，自定义单元格格式"_(\$* #,##0.00_)"用于表示值123时，产生结果"$ 123.00"。在新版本中，Cell.StringValue将包含结果"$123.00"，这与在将单元格复制到文本或导出到CSV时Excel应用程序展现的行为相同。
## **添加了CreatedTime到PdfSaveOptions**
现在用户可以在使用PdfSaveOptions类保存电子表格为PDF时获取或设置PDF创建时间。
## **向Worksheet添加了ShowFormulas**
从现在开始，用户可以使用Worksheet提供的布尔属性ShowFormulas来在给定工作表的公式和值之间切换视图。
## **添加了Ooxml到FileFormatType**
为FileFormatType类添加了一个新的常量Ooxml，用来表示加密的Office开放XML文件，比如XLSX、DOCX、PPTX等。
## **已过时FilterColumnCollection的AutoFilter**
使用Aspose.Cells for Java，getFilterColumnCollection方法已被标记为过时。建议改用AuotFilter.getFilterColumns方法。
## **用SeriesCollection.SecondCategoryData替换了SeriesCollection.SecondCatergoryData**
我们基本上纠正了方法名SeriesCollection.getSecondCatergoryData的拼写错误。您可以从现在开始使用SeriesCollection.getSecondCategoryData方法，而原方法SeriesCollection.getSecondCatergoryData已被标记为过时。
