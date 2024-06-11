---
title: Aspose.Cells 16.11.0 的公共 API 变更。
type: docs
weight: 350
url: /zh/net/public-api-changes-in-aspose-cells-16-11-0/
---

{{% alert color="primary" %}} 

本文描述了从版本 16.10.0 到 16.11.0 中 Aspose.Cells API 的更改，可能对模块/应用程序开发人员感兴趣。不仅包括新的和更新的公共方法、添加和删除的类等，还包括在 Aspose.Cells 后台行为中的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **支持全球化设置。**
Aspose.Cells 16.11.0 已公开了 GlobalizationSettings 类以及 WorkbookSettings.GlobalizationSettings 属性，以便强制 Aspose.Cells API 使用自定义标签来进行小计。GlobalizationSettings 类具有以下方法，可以在自定义实现中重写这些方法，以为“总计”和“总计”标签提供所需的名称。

- GlobalizationSettings.GetTotalName: 获取功能的总名称。
- GlobalizationSettings.GetGrandTotalName: 获取功能的总总名称。

这里是一个简单的自定义类，它扩展了 GlobalizationSettings 类，并重写了上述方法，以返回合并函数 Average 的自定义标签。

**C#**

{{< highlight csharp >}}

 class CustomSettings : GlobalizationSettings

{

    public override string GetTotalName(ConsolidationFunction functionType)

    {

        switch (functionType)

        {

            case ConsolidationFunction.Average:

                return "AVG";

            default:

                return base.GetTotalName(functionType);

        }

    }

    public override string GetGrandTotalName(ConsolidationFunction functionType)

    {

        switch (functionType)

        {

            case ConsolidationFunction.Average:

                return "GRD AVG";

            default:

                return base.GetGrandTotalName(functionType);

        }

    }

}

{{< /highlight >}}



以下代码片段载入了包含工作表中已有数据的现有电子表格，并添加了“平均”类型的小计。在添加小计时，将调用 CustomSettings 类及其 GetTotalName 和 GetGrandTotalName 方法。

**C#**

{{< highlight csharp >}}

 // Loads an existing spreadsheet containing some data

Workbook book = new Workbook(dir + "sample.xlsx");

// Assigns the GlobalizationSettings property of the WorkbookSettings class

// to the class created in first step

book.Settings.GlobalizationSettings = new Cells.CustomSettings();

// Accesses the 1st worksheet from the collection which contains data

// Data resides in the cell range A2:B9

Worksheet sheet = book.Worksheets[0];

// Adds SubTotal of type Average to the worksheet

sheet.Cells.Subtotal(CellArea.CreateCellArea("A2", "B9"), 0, ConsolidationFunction.Average, new int[] { 0,1 });

// Calculates Formulas

book.CalculateFormula();

// Auto fits all columns

sheet.AutoFitColumns();

// Saves the workbook on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}



GlobalizationSettings 类还提供了 GetOtherName 方法，用于获取饼图的“其他”标签的名称。这里是 GlobalizationSettings.GetOtherName 方法的简单使用场景。

**C#**

{{< highlight csharp >}}

 class CustomSettings : GlobalizationSettings

{

    public override string GetOtherName()

    {

        int lcid = System.Globalization.CultureInfo.CurrentCulture.LCID;

        switch (lcid)

        {

            case 1033:

                return "Other";

            case 1036:

                return "Autre";

            case 1031:

                return "Andere";

            //Do other case

            default:

                return base.GetOtherName();

        }

    }

}

{{< /highlight >}}



以下代码片段加载了包含饼图的现有电子表格，并在利用上述创建的 CustomSettings 类的情况下将图表呈现为图像。

**C#**

{{< highlight csharp >}}

 // Loads an existing spreadsheet containing a pie chart

Workbook book = new Workbook(dir + "sample.xlsx");

// Assigns the GlobalizationSettings property of the WorkbookSettings class

// to the class created in first step

book.Settings.GlobalizationSettings = new Cells.CustomSettings();

// Accesses the 1st worksheet from the collection which contains pie chart

Worksheet sheet = book.Worksheets[0];

// Accesses the 1st chart from the collection

Chart chart = sheet.Charts[0];

// Refreshes the chart

chart.Calculate();

// Renders the chart to image

chart.ToImage(dir + "output.png", new ImageOrPrintOptions());

{{< /highlight >}}


### **添加了CellsFactory类**
Aspose.Cells 16.11.0已经暴露了CellsFactory类，该类目前具有一个方法，即CreateStyle。CellsFactory.CreateStyle方法可用于创建Style类的实例，而无需将其添加到工作簿样式池中。

这是CellsFactory.CreateStyle方法的简单使用情景。

**C#**

{{< highlight csharp >}}

 // Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

// Creates an instance of Style

Style style = factory.CreateStyle();

{{< /highlight >}}


### **添加了Workbook.AbsolutePath属性**
Aspose.Cells 16.11.0已经暴露了Workbook.AbsolutePath属性，允许获取或设置存储在workbook.xml文件中的绝对工作簿路径。此属性在仅更新外部链接时非常有用。
### **添加了GridHyperlinkCollection.GetHyperlink方法**
Aspose.Cells.GridWeb 16.11.0已经向GridHyperlinkCollection类暴露了GetHyperlink方法，该方法允许通过传递GridCell的实例或与行列索引对应的整数对来获取GridHyperlink的实例。

{{% alert color="primary" %}} 

如果在指定单元格上未找到超链接，则GetHyperlink方法将返回null。

{{% /alert %}} 

这是GetHyperlink方法的简单使用情景。

**C#**

{{< highlight csharp >}}

 // Gets the active worksheet from the collection

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Accesses the GridHyperlinkCollection

GridHyperlinkCollection links = sheet.Hyperlinks;

// Gets hyperlink from cell A1

GridHyperlink link = links.GetHyperlink(sheet.Cells["A1"]);

// Gets hyperlink from cell D1

link = links.GetHyperlink(0, 3);

{{< /highlight >}}
## **已弃用的API**
### **已弃用的Style构造函数**
请使用cellsFactory.CreateStyle方法作为替代。
## **删除的API**
### **删除的Cell.GetConditionalStyle方法**
请改用Cell.GetConditionalFormattingResult方法。
### **删除的Cells.MaxDataRowInColumn(int column)方法**
请使用Cells.GetLastDataRow(int)方法作为替代。
### **删除的PageSetup.Draft属性**
建议改用PageSetup.PrintDraft属性。
### **删除的AutoFilter.FilterColumnCollection属性**
请考虑使用 AutoFilter.FilterColumns 属性来实现相同的目标。
### **已删除 TickLabels.Rotation 属性**
请改用 TickLabels.RotationAngle 属性。
