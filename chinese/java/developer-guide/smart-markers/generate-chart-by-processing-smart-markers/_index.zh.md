---
title: 通过处理智能标记生成图表
type: docs
weight: 180
url: /zh/java/generate-chart-by-processing-smart-markers/
---

{{% alert color="primary" %}} 

Aspose.Cells API提供WorkbookDesigner类来处理智能标记，其中格式和公式位于设计者电子表格中，然后根据指定的数据源对其进行处理，以根据智能标记填充数据。也可以通过处理智能标记来创建Excel图表，需要以下步骤。

- 创建设计者电子表格
- 根据指定的数据源处理设计者电子表格
- 基于填充数据创建图表

{{% /alert %}} 
## **创建设计者电子表格**
设计者电子表格是使用Microsoft Excel应用程序或Aspose.Cells API创建的简单Excel文件，包含可在运行时填充的视觉格式、公式和智能标记的内容。

{{% alert color="primary" %}} 

智能标记的详细信息请参阅[此处](/cells/zh/java/smart-markers/)。

{{% /alert %}} 

为简化起见，我们将使用 Aspose.Cells for Java API 创建设计电子表格，然后针对动态创建的数据源进行处理，以进行演示目的。

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access the first (default) Worksheet from the collection

Worksheet dataSheet = book.getWorksheets().get(0);

//Name the first Worksheet for referencing

dataSheet.setName("ChartData");

//Access the CellsCollection of ChartData Worksheet

Cells cells = dataSheet.getCells();

//Place the markers in the Worksheet according to desired layout

cells.get("A1").putValue("&=$Headers(horizontal)");

cells.get("A2").putValue("&=$Year2000(horizontal)");

cells.get("A3").putValue("&=$Year2005(horizontal)");

cells.get("A4").putValue("&=$Year2010(horizontal)");

cells.get("A5").putValue("&=$Year2015(horizontal)");

{{< /highlight >}}

如果您在此阶段保存生成的电子表格，则工作表中的数据将如下所示。

![todo:image_alt_text](generate-chart-by-processing-smart-markers_1.png)
## **处理设计者电子表格**
为了处理设计者电子表格，我们必须具有与设计者电子表格中使用的智能标记相对应的数据源。例如，我们创建了一个名为**&=$Headers(horizontal)**的智能标记条目，该条目表示名称为Headers的变量，而**（horizontal）**键表示数据应水平填充。

为了演示这种用例，我们将从头开始创建数据源，并根据前一步骤创建的设计者电子表格对其进行处理。但是，在实时场景中，数据可能已经可用于进一步处理，因此如果数据已经可用，则可以跳过创建数据源的过程。

**Java**

{{< highlight csharp >}}

 //Create string arrays which will serve as data sources to the smart markers

String[] headers = new String[]{"", "Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7", "Item 8", "Item 9", "Item 10", "Item 11", "Item 12"};

String[] year2000 = new String[]{"2000", "310", "0", "110", "15", "20", "25", "30", "1222", "200", "421", "210", "133"};

String[] year2005 = new String[]{"2005", "508", "0", "170", "280", "190", "400", "105", "132", "303", "199", "120", "100"};

String[] year2010 = new String[]{"2010", "0", "210", "230", "1420", "1530", "160", "170", "110", "199", "129", "120", "230"};

String[] year2015 = new String[]{"2015", "2818", "320", "340", "260", "210", "310", "220", "0", "0", "0", "0", "122"};

{{< /highlight >}}

处理智能标记非常简单，如下所示。

**Java**

{{< highlight csharp >}}

 //Create an instance of WorkbookDesigner

WorkbookDesigner designer = new WorkbookDesigner();

//Set the Workbook property for the instance of WorkbookDesigner

designer.setWorkbook(book);

//Set data sources for smart markers

designer.setDataSource("Headers", headers);

designer.setDataSource("Year2000", year2000);

designer.setDataSource("Year2005", year2005);

designer.setDataSource("Year2010", year2010);

designer.setDataSource("Year2015", year2015);

//Process the designer spreadsheet against the provided data sources

designer.process();

{{< /highlight >}}

如果您在此阶段保存该电子表格，则数据将如下所示。

![todo:image_alt_text](generate-chart-by-processing-smart-markers_2.png)

{{% alert color="primary" %}} 

上述代码片段使用了在第一步创建的现有Workbook类实例。如果您已经有了设计者电子表格文件，则可以通过加载现有的设计者电子表格创建Workbook类的实例。

{{% /alert %}} 
## **创建图表**
一旦数据准备就绪，我们所需要做的就是基于数据源创建图表。为了让示例简单，我们将使用Chart.setChartDataRange方法，这样我们就不必进一步配置图表。







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GenerateChartByProcessingSmartMarkers-GenerateChartByProcessingSmartMarkers.java" >}}





最终图表如下所示。

![todo:image_alt_text](generate-chart-by-processing-smart-markers_3.png)
{{< app/cells/assistant language="java" >}}
