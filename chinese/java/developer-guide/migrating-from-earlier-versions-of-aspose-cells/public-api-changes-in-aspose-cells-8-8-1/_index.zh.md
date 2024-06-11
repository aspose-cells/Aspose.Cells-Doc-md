---
title: Aspose.Cells 8.8.1中的公共API更改
type: docs
weight: 280
url: /zh/java/public-api-changes-in-aspose-cells-8-8-1/
---

{{% alert color="primary" %}} 

该文档描述了从版本8.8.0到8.8.1的Aspose.Cells API的更改，这可能对模块/应用程序开发人员很有兴趣。它不仅包括新的和已更新的公共方法，增加和删除的类等，还包括Aspose.Cells后台行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **为加载过滤数据**
Aspose.Cells for Java 8.8.1已公开了LoadDataFilterOptions枚举及LoadOptions.LoadDataFilterOptions属性，可用于指定在从模板文件构建工作簿时应加载的数据类型。过滤加载的数据可以改善特殊目的的性能，特别是在使用LightCells API时。

LoadDataFilterOptions枚举提供以下选择。

1. ALL加载电子表格中的所有内容。
1. NONE不加载电子表格中的任何内容。
1. CELL_BLANK加载值为空的单元格。
1. CELL_BOOL加载值为布尔值的单元格。
1. CELL_DATA加载包括值、公式和格式在内的单元格数据。
1. CELL_ERROR加载值为错误的单元格。
1. CELL_NUMERIC加载值为数字的单元格（包括日期和时间）。
1. CELL_STRING加载值为文本/字符串的单元格。
1. CELL_VALUE仅加载单元格值（所有类型）。
1. CHART仅加载图表。
1. CONDITIONAL_FORMATTING仅加载条件格式规则。
1. DATA_VALIDATION仅加载数据验证规则。
1. DOCUMENT_PROPERTIES仅加载文档属性。
1. FORMULA加载包括已定义名称的公式。
1. MERGED_AREA仅加载合并的单元格。
1. PIVOT_TABLE仅加载数据透视表。
1. 设置仅加载工作簿和工作表设置。
1. 形状仅加载形状。
1. 样式加载单元格格式。
1. 表加载Excel表/列表对象。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请参阅[加载时过滤数据](/cells/zh/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)的详细文章。

{{% /alert %}} 

以下是简单的使用场景。

Java

{{< highlight csharp >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

LoadOptions options = new LoadOptions(LoadFormat.XLSX);

//Set LoadDataFilterOptions to load only shapes

options.setLoadDataFilterOptions(LoadDataFilterOptions.SHAPE);

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

Workbook book = new Workbook(filePath, options);

{{< /highlight >}}
### **直接将图表转换为PDF**
Aspose.Cells API已经提供了在使用Chart.toPdf方法时将图表呈现为PDF的功能。通过此版本，API已公开了另一个重载版本的该方法，该重载版本可以接受一个OutputStream实例，允许用户将图表的PDF保存在一个ByteArrayOutputStream实例中。

以下是简单的使用场景。

Java

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet with a chart

Workbook workbook = new Workbook(filePath);

//Access first worksheet containing a chart

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first chart from the worksheet

Chart chart = worksheet.getCharts().get(0);

//Save the chart to PDF as Stream

ByteArrayOutputStream outStream = new ByteArrayOutputStream();

chart.toPdf(outStream);

{{< /highlight >}}
### **增加了WorkbookSettings.PaperSize属性**
Aspose.Cells for Java 8.8.1已公开了WorkbookSettings.PaperSize属性，以设置整个电子表格的默认打印纸张大小。WorkbookSettings.PaperSize属性接受来自PaperSizeType枚举的值，该枚举包含用于大多数常用打印纸张类型的预定义大小。

Java

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook();

//Access WorkbookSettings from the Workbook

WorkbookSettings settings = book.getSettings();

//Set the default printing paper size for the Workbook

settings.setPaperSize(PaperSizeType.PAPER_A_4);

{{< /highlight >}}
### **增加了Shape.TextBody属性**
此版本的Aspose.Cells for Java API已公开了Shape.TextBody，以便操纵形状中文本的各个方面。以下代码片段使用了该属性来设置TextBox中文本的阴影效果。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请参阅[设置文本阴影效果](/cells/zh/java/setting-shadow-of-text-effects-of-shape-or-textbox/)的详细文章。

{{% /alert %}} 

Java

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet of the Workbook

Worksheet sheet = book.getWorksheets().get(0);

//Add a TextBox to the ShapeCollection

int index = sheet.getTextBoxes().add(2, 2, 100, 400);

TextBox textBox = sheet.getTextBoxes().get(index);

//Set the text of the TextBox

textBox.setText("This text has the following settings.\n\nText Effects > Shadow > Offset Bottom");

//Set shadow effect for text

for (int i = 0; i < textBox.getTextBody().getCount(); i++)

{

  textBox.getTextBody().get(i).getShapeFont().getFillFormat().getShadowEffect().setPresetType(PresetShadowType.OFFSET_BOTTOM);

}

{{< /highlight >}}
### **增加了Worksheet.calculateFormula(string formula, CalculationOptions opts)方法**
Aspose.Cells for Java 8.8.1还公开了Worksheet.calculateFormula方法的另一个重载版本，可提供直接使用自定义选项计算给定公式的能力。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请参阅[直接计算自定义函数](/cells/zh/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)的详细文章。

{{% /alert %}} 
### **增加了GridCell.createValidation方法**
在使用GridCell.createValidation方法时，Aspose.Cells.GridWeb已提供了直接向单个单元格添加验证规则的能力。该方法需要2个参数。第一个是GridValidationType类型，用于确定验证类型，而第二个参数(isRequied)是布尔型。

Java

{{< highlight csharp >}}

 //Access first worksheet

GridWorksheet sheet = gridweb.getWorkSheets().get(0);

//Access cell B3

GridCell cell = sheet.getCells().get("B3");

//Add validation inside the GridCell

//Any value which is not between 20 and 40 will cause error in a GridCell

GridValidation val = cell.createValidation(GridValidationType.WHOLE_NUMBER, true);

val.setFormula1("=20");

val.setFormula2("=40");

val.setOperator(OperatorType.BETWEEN);

val.setShowError(true);

val.setShowInput(true);

{{< /highlight >}}
### **增加了GridCell.removeValidation方法**
Aspose.Cells.GridWeb 还提供了使用 GridCell.removeValidation 方法从 GridCell 中移除数据验证规则的能力。
## **已弃用的API**
### **已弃用 Shape.TextFrame 属性**
建议改用 Shape.TextBody.TextAlignment 属性。
