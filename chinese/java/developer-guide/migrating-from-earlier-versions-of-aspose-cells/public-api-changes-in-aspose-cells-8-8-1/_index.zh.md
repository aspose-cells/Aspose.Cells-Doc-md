---
title: Aspose.Cells 8.8.1中的公共API更改
type: docs
weight: 280
url: /zh/java/public-api-changes-in-aspose-cells-8-8-1/
---

{{% alert color="primary" %}} 

本文档描述了Aspose.Cells API从版本8.8.0到8.8.1的更改，可能对模块/应用程序开发人员感兴趣。它不仅包括新添加和更新的公共方法、添加和删除的类等，还包括Aspose.Cells幕后行为的任何更改的描述。

{{% /alert %}} 
## **已添加API**
### **加载数据进行过滤**
Aspose.Cells for Java 8.8.1已经公开了LoadDataFilterOptions枚举及LoadOptions.LoadDataFilterOptions属性，这些可用于指定在从模板文件构建工作簿时应加载的数据类型。过滤加载的数据可以改进特殊用途的性能，尤其是在使用LightCells API时。

LoadDataFilterOptions枚举提供了以下选择。

1. ALL用于从电子表格中加载所有内容。
1. NONE用于从电子表格中加载任何内容。
1. CELL_BLANK用于加载数值为空的单元格。
1. CELL_BOOL用于加载值为布尔类型的单元格。
1. CELL_DATA用于加载包括值、公式和格式在内的单元格数据。
1. CELL_ERROR用于加载值为错误值的单元格。
1. CELL_NUMERIC用于加载值为数值（包括日期和时间）的单元格。
1. CELL_STRING用于加载值为文本/字符串的单元格。
1. CELL_VALUE仅用于加载单元格值（所有类型）。
1. CHART仅用于加载图表。
1. CONDITIONAL_FORMATTING仅用于加载条件格式规则。
1. DATA_VALIDATION 仅加载数据验证规则。
1. DOCUMENT_PROPERTIES 仅加载文档属性。
1. FORMULA 加载包括定义名称的公式。
1. MERGED_AREA 仅加载合并单元格。
1. PIVOT_TABLE 加载数据透视表。
1. SETTINGS 仅加载工作簿和工作表设置。
1. SHAPE 仅加载形状。
1. STYLE 加载单元格格式设置。
1. TABLE 加载Excel表/数据透视表。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看[加载数据时过滤数据](/cells/zh/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)的详细文章。

{{% /alert %}} 

以下是简单的使用场景。

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

LoadOptions options = new LoadOptions(LoadFormat.XLSX);

//Set LoadDataFilterOptions to load only shapes

options.setLoadDataFilterOptions(LoadDataFilterOptions.SHAPE);

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

Workbook book = new Workbook(filePath, options);

{{< /highlight >}}
### **直接将图表转换为PDF**
Aspose.Cells API已经提供了使用Chart.toPdf方法将图表呈现为PDF的功能。通过此版本，API公开了该方法的另一个重载版本，可以接受OutputStream的实例，允许用户将图表的PDF保存在ByteArrayOutputStream的实例中。

以下是简单的使用场景。

**Java**

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
### **新增 WorkbookSettings.PaperSize 属性**
Aspose.Cells for Java 8.8.1已将WorkbookSettings.PaperSize属性公开，以设置整个电子表格的默认打印纸张大小。 WorkbookSettings.PaperSize属性接受PaperSizeType枚举中的值，其中包含大多数常用打印纸张类型的预定义大小。

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook();

//Access WorkbookSettings from the Workbook

WorkbookSettings settings = book.getSettings();

//Set the default printing paper size for the Workbook

settings.setPaperSize(PaperSizeType.PAPER_A_4);

{{< /highlight >}}
### **新增 Shape.TextBody 属性**
此版Aspose.Cells for Java API已公开Shape.TextBody，以操作形状中文本的方面。以下代码段使用该属性来设置文本框中文本的阴影效果。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看[设置文本的阴影效果](/cells/zh/java/setting-shadow-of-text-effects-of-shape-or-textbox/)的详细文章。

{{% /alert %}} 

**Java**

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
### **添加了Worksheet.calculateFormula(string formula, CalculationOptions opts)方法**
Aspose.Cells for Java 8.8.1已为Worksheet.calculateFormula方法公开了另一个重载，该重载提供了直接使用自定义选项计算给定公式的能力。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看[直接计算自定义函数](/cells/zh/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)的详细文章。

{{% /alert %}} 
### **添加了GridCell.createValidation方法**
Aspose.Cells.GridWeb已提供了使用GridCell.createValidation方法直接向单个单元格添加验证规则的功能。 该方法需要2个参数。 第一个参数是GridValidationType类型，用于确定验证类型，而第二个参数（isRequied）是布尔类型。

**Java**

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
### **添加了GridCell.removeValidation方法**
Aspose.Cells.GridWeb还提供了在使用GridCell.removeValidation方法删除GridCell中的数据验证规则的功能。
## **已废弃的API**
### **弃用的Shape.TextFrame属性**
建议使用Shape.TextBody.TextAlignment属性。
