---
title: 公共 API Aspose.Cells 8.0.0 的变化
type: docs
weight: 20
url: /zh/java/public-api-changes-in-aspose-cells-8-0-0/
---
{{% alert color="primary" %}} 

此页面列出了 Aspose.Cells 8.0.0 中引入的公共 API 更改。它不仅包括新的和过时的公共方法，还包括对 Aspose.Cells 中可能影响现有代码的幕后行为的任何更改的描述。

{{% /alert %}} 
## **将 MemorySetting 添加到 LoadOptions 和 WorkbookSettings**
从 Aspose.Cells for Java 的 v8.0.0 开始，我们提供了用于性能考虑的内存使用选项。 MemorySetting 属性现在在 LoadOptions 和 WorkbookSettings 类中可用。
### **例子**
演示如何在优化模式下读取 Excel 文件（具有大尺寸）。

**Java**

{{< highlight "csharp" >}}

 //Initialize LoadOptions

LoadOptions options = new LoadOptions();

//Set memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook with an object of LoadOptions

Workbook book = new Workbook(myDir + "large.xlsx", options);

{{< /highlight >}}

演示如何在优化模式下将大型数据集写入工作表。

**Java**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences for WorkbookSettings

book.getSettings().setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Input large data into the cells

//.........

{{< /highlight >}}

{{% alert color="primary" %}} 

请查看详细文章[处理大文件时优化内存](/cells/zh/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)秒。

{{% /alert %}}
## **Row & Cell 的实现已更改**
在以前的版本中，Row 和 Cell 对象被保存在内存中以表示工作表中相应的行和单元格。每当返回相同的实例**RowCollection[int 索引]**或者**Cells[整数行，整数列]**被找回。出于内存性能的考虑，现在内存中只保留Row和Cell的属性和数据。因此，Row & Cell 对象已成为上述属性的包装器。
### **例子**
从现在开始演示如何比较 Cell 和 Row 对象。

**Java**

{{< highlight "csharp" >}}

 //..

row1.equals(row2);


cell1.equals(cell2);

//..

{{< /highlight >}}

因为Row和Cell对象是根据调用实例化的，所以不会被Cells组件在内存中保存和管理。因此，经过一些插入和删除操作后，Row & Column 索引可能不会更新，甚至更糟，这些对象变得无效。
### **例子**
例如，以下代码片段将使用 8.0.0 及更高版本返回无效结果，

**Java**

{{< highlight "csharp" >}}

 Cell cell = cells.get("A2");

System.out.println(cell.getName() + ":" + cell.getValue());

cells.insertRange(CellArea.createCellArea("A1", "A1"), ShiftType.DOWN);

System.out.println(cell.getName() + ":" + cell.getValue());

{{< /highlight >}}

在新版本中，Cell 对象将变得无效或使用一些不需要的值引用 A2。为了避免这种情况，再次从单元格集合中获取 Row 或 Cell 对象以检索正确的结果。

**Java**

{{< highlight "csharp" >}}

 Cell cell = cells.get("A2");

System.out.println(cell.getName() + ":" + cell.getValue());

cells.insertRange(CellArea.createCellArea("A1", "A1"), ShiftType.DOWN);

//Fetch the cell reference again

Cell cell = cells.get("A3");

System.out.println(cell.getName() + ":" + cell.getValue());

{{< /highlight >}}

{{% alert color="primary" %}} 

RowCollection 不再继承 CollectionBase，因为它的内部列表中没有 Row 对象。

{{% /alert %}}
## **Cell.StringValue 行为已更改**
在以前的版本中，特殊模式_在格式化单元格值时被忽略，其中特殊字符 * 总是在格式化结果中产生一个字符。从这个版本开始，我们改变了处理特殊字符的逻辑_和*为了使格式化结果与 Excel 应用程序相同。例如，自定义单元格格式“_(\$* #,##0.00_)”用于表示值 123 产生的结果为“$ 123.00”。在新版本中，Cell.StringValue 将包含结果为“$123.00”，这与 Excel 应用程序在复制单元格时表现出的行为相同发送文本或导出为 CSV。
## **将 CreatedTime 添加到 PdfSaveOptions**
现在，用户可以在使用 PdfSaveOptions 类将电子表格保存为 PDF 时获取或设置 PDF 创建时间。
## **添加 ShowFormulas 到工作表**
从现在开始，用户可以使用 Worksheet 提供的布尔属性 ShowFormulas 在给定工作表的公式和值之间切换视图。
## **将 Ooxml 添加到 FileFormatType**
FileFormatType 类中添加了一个新常量 Ooxml，用于表示 XLSX、DOCX、PPTX 等加密的 Office 打开 XML 文件。
## **AutoFilter 的废弃 FilterColumnCollection**
对于 Aspose.Cells for Java，getFilterColumnCollection 方法已被标记为已废弃。建议改用 AuotFilter.getFilterColumns 方法。
## **将 SeriesCollection.SecondCategoryData 替换为 SeriesCollection.SecondCategoryData**
我们基本上纠正了 SeriesCollection.getSecondCatergoryData 的方法名称中的拼写错误。您现在可以使用 SeriesCollection.getSecondCategoryData 方法，而原始方法 SeriesCollection.getSecondCatergoryData 已被标记为已废弃。
