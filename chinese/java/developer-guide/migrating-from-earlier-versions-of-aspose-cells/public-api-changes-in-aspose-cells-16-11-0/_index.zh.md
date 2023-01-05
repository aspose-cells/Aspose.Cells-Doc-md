---
title: 公共 API Aspose.Cells 16.11.0 的变化
type: docs
weight: 360
url: /zh/java/public-api-changes-in-aspose-cells-16-11-0/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 16.10.0 到 16.11.0 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还包括对 Aspose.Cells 中幕后行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **支持全球化设置**
Aspose.Cells 16.11.0 公开了 GlobalizationSettings 类以及 WorkbookSettings.GlobalizationSettings 属性，以强制 Aspose.Cells API 对小计使用自定义标签。 GlobalizationSettings 类具有以下方法，可以在自定义实现中覆盖这些方法，以便为标签指定所需的名称**全部的** & **累计**.

- GlobalizationSettings.getTotalName：获取函数的总名称。
- GlobalizationSettings.getGrandTotalName：获取函数的总计名称。

这是一个简单的自定义类，它扩展了 GlobalizationSettings 类并覆盖了上述方法以返回合并函数 Average 的自定义标签。

**Java**

{{< highlight "csharp" >}}

 public class CustomSettings extends GlobalizationSettings

{    

    public String getTotalName(int functionType)

    {

    	 switch (functionType)

         {

             case ConsolidationFunction.AVERAGE:

                 return "AVG";

             default:

                return super.getTotalName(functionType);

         }

    }

    public String getGrandTotalName(int functionType)

    {

    	 switch (functionType)

         {

             case ConsolidationFunction.AVERAGE:

                 return "GRAND AVG";

             default:

            	 return super.getGrandTotalName(functionType);

         }



    }

}

{{< /highlight >}}

以下代码片段加载现有电子表格，并在工作表中已有的数据上添加 Average 类型的小计。在将小计添加到工作表时将调用 CustomSettings 类及其 getTotalName 和 getGrandTotalName 方法。

**Java**

{{< highlight "csharp" >}}

 //Loads an existing spreadsheet containing some data

Workbook book = new Workbook(dir + "sample.xlsx");

//Assigns the GlobalizationSettings property of the WorkbookSettings class

//to the class created in first step

book.getSettings().setGlobalizationSettings(new CustomSettings());

//Accesses the 1st worksheet from the collection which contains data

//Data resides in the cell range A2:B9

Worksheet sheet = book.getWorksheets().get(0);

//Adds SubTotal of type Average to the worksheet

sheet.getCells().subtotal(CellArea.createCellArea("A2", "B9"), 0, ConsolidationFunction.AVERAGE, new int[]{ 0,1 });

//Calculates Formulas

book.calculateFormula();

//Auto fits all columns

sheet.autoFitColumns();

//Saves the workbook on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}

GlobalizationSettings 类还提供了 getOtherName 方法，该方法可用于获取饼图“其他”标签的名称。这是 GlobalizationSettings.getOtherName 方法的一个简单使用场景。

**Java**

{{< highlight "csharp" >}}

 public class CustomSettings extends GlobalizationSettings

{ 

	public String getOtherName()

	{

		String language = Locale.getDefault().getLanguage();

		System.out.println(language);

		switch (language)

		{

			case "en":

				return "Other";

			case "fr":

				return "Autre";

			case "de":

				return "Andere";

			//Do other cases

			default:

				return super.getOtherName();

		}

	}

}

{{< /highlight >}}

以下代码片段加载包含饼图的现有电子表格，并在使用上面创建的 CustomSettings 类时将图表呈现为图像。

**Java**

{{< highlight "csharp" >}}

 //Loads an existing spreadsheet containing a pie chart

Workbook book = new Workbook(dir + "sample.xlsx");

//Assigns the GlobalizationSettings property of the WorkbookSettings class

//to the class created in first step

book.getSettings().setGlobalizationSettings(new CustomSettings());

//Accesses the 1st worksheet from the collection which contains pie chart

Worksheet sheet = book.getWorksheets().get(0);

//Accesses the 1st chart from the collection

Chart chart = sheet.getCharts().get(0);

//Refreshes the chart

chart.calculate();

//Renders the chart to image

chart.toImage(dir + "output.png", new ImageOrPrintOptions());

{{< /highlight >}}
### **添加了 CellsFactory 类**
Aspose.Cells 16.11.0暴露了CellsFactory类，目前有一个方法，即；创建样式。 CellsFactory.createStyle 方法可用于创建 Style 类的实例，而无需将其添加到工作簿样式池中。

下面是 CellsFactory.createStyle 方法的简单使用场景。

**Java**

{{< highlight "csharp" >}}

 //Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

//Creates an instance of Style

Style style = factory.createStyle();

{{< /highlight >}}
### **添加了 Workbook.AbsolutePath 属性**
Aspose.Cells 16.11.0 公开了 Workbook.AbsolutePath 属性，允许获取或设置存储在 workbook.xml 文件中的绝对工作簿路径。此属性在仅更新外部链接时很有用。
### **添加了 GridHyperlinkCollection.getHyperlink 方法**
Aspose.Cells.GridWeb 16.11.0 已将 getHyperlink 方法公开给 GridHyperlinkCollection 类，该类允许通过传递实例 GridCell 或一对对应于行列索引的整数来获取 GridHyperlink 的实例。

{{% alert color="primary" %}} 

如果在指定单元格上未找到超链接，则 getHyperlink 方法将返回 null。

{{% /alert %}} 

下面是 getHyperlink 方法的简单使用场景。

**Java**

{{< highlight "csharp" >}}

 //Gets the active worksheet from the collection

GridWorksheet sheet = gridWeb1.getWorkSheets().get(gridWeb1.getActiveSheetIndex());

//Accesses the GridHyperlinkCollection

GridHyperlinkCollection links = sheet.getHyperlinks();

//Gets hyperlink from cell A1

GridHyperlink link = links.getHyperlink(sheet.getCells().get("A1"));

//Gets hyperlink from cell D1

link = links.getHyperlink(0, 3);

{{< /highlight >}}
## **过时的 API**
### **过时的样式构造函数**
请使用 cellsFactory.createStyle 方法作为替代方法。
## **已删除的 API**
### **删除 Cell.getConditionalStyle 方法**
请改用 Cell.getConditionalFormattingResult 方法。
### **删除了 Cells.getMaxDataRowInColumn(int column) 方法**
请使用 Cells.getLastDataRow(int) 方法作为替代方法。
### **删除 PageSetup.Draft 属性**
建议改为使用 PageSetup.PrintDraft 属性。
### **已删除 AutoFilter.FilterColumnCollection 属性**
请考虑使用 AutoFilter.FilterColumns 属性来实现相同的目标。
### **删除了 TickLabels.Rotation 属性**
请改用 TickLabels.RotationAngle 属性。
