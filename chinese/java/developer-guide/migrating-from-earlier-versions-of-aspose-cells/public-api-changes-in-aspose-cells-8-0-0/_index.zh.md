---
title: Aspose.Cells 8.0.0中的公共API更改
type: docs
weight: 20
url: /zh/java/public-api-changes-in-aspose-cells-8-0-0/
---

{{% alert color="primary" %}} 

此页面列出了Aspose.Cells 8.0.0中引入的公共API更改。不仅包括新的和已弃用的公共方法，还包括可能影响现有代码背后行为的任何更改在Aspose.Cells中。

{{% /alert %}} 
## **向LoadOptions和WorkbookSettings添加了MemorySetting**
从 Aspose.Cells for Java v8.0.0 开始，我们为性能考虑提供了内存使用选项。 MemorySetting 属性现在在 LoadOptions 和 WorkbookSettings 类中可用。
### **例子**
演示如何以优化模式读取具有大尺寸的Excel文件。

**Java**

{{< highlight csharp >}}

 //Initialize LoadOptions

LoadOptions options = new LoadOptions();

//Set memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook with an object of LoadOptions

Workbook book = new Workbook(myDir + "large.xlsx", options);

{{< /highlight >}}

演示如何以优化模式将大型数据集写入工作表。

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

请查看有关[在处理大文件时优化内存](/cells/zh/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)的详细文章。

{{% /alert %}}
## **Row和Cell的实现已更改**
在以前的版本中，Row和Cell对象保留在内存中，以表示工作表中相应的行和单元格。每当检索**RowCollection[int index]**或**Cells[int row, int column]**时，将返回相同的实例。出于内存性能考虑，现在只会保留Row和Cell的属性和数据。因此，Row和Cell对象现已成为上述属性的包装器。
### **例子**
演示如何从现在开始比较Cell和Row对象。

**Java**

{{< highlight csharp >}}

 //..

row1.equals(row2);


cell1.equals(cell2);

//..

{{< /highlight >}}

由于Row和Cell对象是根据调用实例化的，它们不会被Cells组件在内存中保留和管理。因此，在进行一些插入和删除操作后，Row和Column索引可能不会被更新，甚至更糟的是，这些对象可能变得无效。
### **例子**
例如，以下代码片段将在8.0.0及以上版本中返回无效结果，

**Java**

{{< highlight csharp >}}

 Cell cell = cells.get("A2");

System.out.println(cell.getName() + ":" + cell.getValue());

cells.insertRange(CellArea.createCellArea("A1", "A1"), ShiftType.DOWN);

System.out.println(cell.getName() + ":" + cell.getValue());

{{< /highlight >}}

使用新版本，Cell对象将变为无效或引用带有一些不必要值的A2。为避免这种情况，请从单元格集合重新获取Row或Cell对象以检索正确的结果。

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

RowCollection不再继承CollectionBase，因为其内部列表中没有Row对象。

{{% /alert %}}
## **Cell.StringValue行为已更改**
在以前的版本中，特殊模式 _ 在格式化单元格值时被忽略，而特殊字符 * 永远会产生一个字符到格式化结果中。从这个版本开始，我们已经更改了处理特殊字符 _ 和 * 的逻辑，以使格式化结果与 Excel 应用程序相同。例如，自定义单元格格式"_(\$* #,##0.00_)"用于表示值 123，结果为"$ 123.00"。使用新版本，Cell.StringValue 将包含结果为"$123.00"，这与 Excel 应用程序在将单元格复制到文本或导出为 CSV 时表现相同。
## **向 PdfSaveOptions 中添加了 CreatedTime**
现在用户在使用 PdfSaveOptions 类保存电子表格为 PDF 时可以设置或获取 PDF 创建时间。
## **向工作表添加 ShowFormulas**
从现在开始，用户可以使用 Worksheet 提供的 ShowFormulas 布尔属性在给定工作表的公式和值之间切换视图。
## **向 FileFormatType 添加了 Ooxml**
已向 FileFormatType 类添加了一个新常量 Ooxml，用于表示加密的 Office 开放 XML 文件，如 XLSX、DOCX、PPTX 等。
## **已废弃 AutoFilter 的 FilterColumnCollection**
使用 Aspose.Cells for Java，getFilterColumnCollection 方法被标记为已过时。建议使用 AutoFilter.getFilterColumns 方法。
## **用 SeriesCollection.SecondCategoryData 替换了 SeriesCollection.SecondCatergoryData**
我们基本上纠正了 SeriesCollection.getSecondCatergoryData 方法名的拼写错误。您现在可以使用 SeriesCollection.getSecondCategoryData 方法，而原有方法 SeriesCollection.getSecondCatergoryData 已被标记为已过时。
