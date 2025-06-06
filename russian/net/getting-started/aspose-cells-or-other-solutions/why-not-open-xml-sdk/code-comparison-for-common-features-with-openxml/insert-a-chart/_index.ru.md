---
title: Вставить диаграмму
type: docs
weight: 60
url: /ru/net/insert-a-chart/
---

## **OpenXML Excel**
{{< highlight csharp >}}

 string FilePath = @"..\..\..\..\Sample Files\";

string FileName = FilePath + "Insert a chart.xlsx";

string worksheetName = "Sheet1";

string title = "New Chart";

Dictionary<string, int> data = new Dictionary<string, int>();

data.Add("abc", 1);

InsertChartInSpreadsheet(FileName, worksheetName, title, data);

// Given a document name, a worksheet name, a chart title, and a Dictionary collection of text keys

// and corresponding integer data, creates a column chart with the text as the series and the integers as the values.

private static void InsertChartInSpreadsheet(string docName, string worksheetName, string title,

Dictionary<string, int> data)

{

    // Open the document for editing.

    using (SpreadsheetDocument document = SpreadsheetDocument.Open(docName, true))

    {

        IEnumerable<Sheet> sheets = document.WorkbookPart.Workbook.Descendants<Sheet>().

Where(s => s.Name == worksheetName);

        if (sheets.Count() == 0)

        {

            // The specified worksheet does not exist.

            return;

        }

        WorksheetPart worksheetPart = (WorksheetPart)document.WorkbookPart.GetPartById(sheets.First().Id);

        // Add a new drawing to the worksheet.

        DrawingsPart drawingsPart = worksheetPart.AddNewPart<DrawingsPart>();

        worksheetPart.Worksheet.Append(new DocumentFormat.OpenXml.Spreadsheet.Drawing() { Id = worksheetPart.GetIdOfPart(drawingsPart) });

        worksheetPart.Worksheet.Save();

        // Add a new chart and set the chart language to English-US.

        ChartPart chartPart = drawingsPart.AddNewPart<ChartPart>();

        chartPart.ChartSpace = new ChartSpace();

        chartPart.ChartSpace.Append(new EditingLanguage() { Val = new StringValue("en-US") });

        DocumentFormat.OpenXml.Drawing.Charts.Chart chart = chartPart.ChartSpace.AppendChild<DocumentFormat.OpenXml.Drawing.Charts.Chart>(

            new DocumentFormat.OpenXml.Drawing.Charts.Chart());

        // Create a new clustered column chart.

        PlotArea plotArea = chart.AppendChild<PlotArea>(new PlotArea());

        Layout layout = plotArea.AppendChild<Layout>(new Layout());

        BarChart barChart = plotArea.AppendChild<BarChart>(new BarChart(new BarDirection() { Val = new EnumValue<BarDirectionValues>(BarDirectionValues.Column) },

            new BarGrouping() { Val = new EnumValue<BarGroupingValues>(BarGroupingValues.Clustered) }));

        uint i = 0;

        // Iterate through each key in the Dictionary collection and add the key to the chart Series

        // and add the corresponding value to the chart Values.

        foreach (string key in data.Keys)

        {

            BarChartSeries barChartSeries = barChart.AppendChild<BarChartSeries>(new BarChartSeries(new Index()

            {

                Val =

                    new UInt32Value(i)

            },

                new Order() { Val = new UInt32Value(i) },

                new SeriesText(new NumericValue() { Text = key })));

            StringLiteral strLit = barChartSeries.AppendChild<CategoryAxisData>(new CategoryAxisData()).AppendChild<StringLiteral>(new StringLiteral());

            strLit.Append(new PointCount() { Val = new UInt32Value(1U) });

            strLit.AppendChild<StringPoint>(new StringPoint() { Index = new UInt32Value(0U) }).Append(new NumericValue(title));

            NumberLiteral numLit = barChartSeries.AppendChild<DocumentFormat.OpenXml.Drawing.Charts.Values>(

                new DocumentFormat.OpenXml.Drawing.Charts.Values()).AppendChild<NumberLiteral>(new NumberLiteral());

            numLit.Append(new FormatCode("General"));

            numLit.Append(new PointCount() { Val = new UInt32Value(1U) });

            numLit.AppendChild<NumericPoint>(new NumericPoint() { Index = new UInt32Value(0u) }).Append

(new NumericValue(data[key].ToString()));

            i++;

        }

        barChart.Append(new AxisId() { Val = new UInt32Value(48650112u) });

        barChart.Append(new AxisId() { Val = new UInt32Value(48672768u) });

        // Add the Category Axis.

        CategoryAxis catAx = plotArea.AppendChild<CategoryAxis>(new CategoryAxis(new AxisId() { Val = new UInt32Value(48650112u) }, new Scaling(new Orientation()

        {

            Val = new EnumValue<DocumentFormat.

                OpenXml.Drawing.Charts.OrientationValues>(DocumentFormat.OpenXml.Drawing.Charts.OrientationValues.MinMax)

        }),

            new AxisPosition() { Val = new EnumValue<AxisPositionValues>(AxisPositionValues.Bottom) },

            new TickLabelPosition() { Val = new EnumValue<TickLabelPositionValues>(TickLabelPositionValues.NextTo) },

            new CrossingAxis() { Val = new UInt32Value(48672768U) },

            new Crosses() { Val = new EnumValue<CrossesValues>(CrossesValues.AutoZero) },

            new AutoLabeled() { Val = new BooleanValue(true) },

            new LabelAlignment() { Val = new EnumValue<LabelAlignmentValues>(LabelAlignmentValues.Center) },

            new LabelOffset() { Val = new UInt16Value((ushort)100) }));

        // Add the Value Axis.

        ValueAxis valAx = plotArea.AppendChild<ValueAxis>(new ValueAxis(new AxisId() { Val = new UInt32Value(48672768u) },

            new Scaling(new Orientation()

            {

                Val = new EnumValue<DocumentFormat.OpenXml.Drawing.Charts.OrientationValues>(

                    DocumentFormat.OpenXml.Drawing.Charts.OrientationValues.MinMax)

            }),

            new AxisPosition() { Val = new EnumValue<AxisPositionValues>(AxisPositionValues.Left) },

            new MajorGridlines(),

            new DocumentFormat.OpenXml.Drawing.Charts.NumberingFormat()

            {

                FormatCode = new StringValue("General"),

                SourceLinked = new BooleanValue(true)

            }, new TickLabelPosition()

            {

                Val = new EnumValue<TickLabelPositionValues>

                    (TickLabelPositionValues.NextTo)

            }, new CrossingAxis() { Val = new UInt32Value(48650112U) },

            new Crosses() { Val = new EnumValue<CrossesValues>(CrossesValues.AutoZero) },

            new CrossBetween() { Val = new EnumValue<CrossBetweenValues>(CrossBetweenValues.Between) }));

        // Add the chart Legend.

        Legend legend = chart.AppendChild<Legend>(new Legend(new LegendPosition() { Val = new EnumValue<LegendPositionValues>(LegendPositionValues.Right) },

            new Layout()));

        chart.Append(new PlotVisibleOnly() { Val = new BooleanValue(true) });

        // Save the chart part.

        chartPart.ChartSpace.Save();

        // Position the chart on the worksheet using a TwoCellAnchor object.

        drawingsPart.WorksheetDrawing = new WorksheetDrawing();

        TwoCellAnchor twoCellAnchor = drawingsPart.WorksheetDrawing.AppendChild<TwoCellAnchor>(new TwoCellAnchor());

        twoCellAnchor.Append(new DocumentFormat.OpenXml.Drawing.Spreadsheet.FromMarker(new ColumnId("9"),

            new ColumnOffset("581025"),

            new RowId("17"),

            new RowOffset("114300")));

        twoCellAnchor.Append(new DocumentFormat.OpenXml.Drawing.Spreadsheet.ToMarker(new ColumnId("17"),

            new ColumnOffset("276225"),

            new RowId("32"),

            new RowOffset("0")));

        // Append a GraphicFrame to the TwoCellAnchor object.

        DocumentFormat.OpenXml.Drawing.Spreadsheet.GraphicFrame graphicFrame =

            twoCellAnchor.AppendChild<DocumentFormat.OpenXml.

Drawing.Spreadsheet.GraphicFrame>(new DocumentFormat.OpenXml.Drawing.

Spreadsheet.GraphicFrame());

        graphicFrame.Macro = "";

        graphicFrame.Append(new DocumentFormat.OpenXml.Drawing.Spreadsheet.NonVisualGraphicFrameProperties(

            new DocumentFormat.OpenXml.Drawing.Spreadsheet.NonVisualDrawingProperties() { Id = new UInt32Value(2u), Name = "Chart 1" },

            new DocumentFormat.OpenXml.Drawing.Spreadsheet.NonVisualGraphicFrameDrawingProperties()));

        graphicFrame.Append(new Transform(new Offset() { X = 0L, Y = 0L },

                                                                new Extents() { Cx = 0L, Cy = 0L }));

        graphicFrame.Append(new Graphic(new GraphicData(new ChartReference() { Id = drawingsPart.GetIdOfPart(chartPart) }) { Uri = "http://schemas.openxmlformats.org/drawingml/2006/chart" }));

        twoCellAnchor.Append(new ClientData());

        // Save the WorksheetDrawing object.

        drawingsPart.WorksheetDrawing.Save();

    }

}

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight csharp >}}

 string FilePath = @"..\..\..\..\Sample Files\";

string FileName = FilePath + "Insert a chart.xlsx";

string worksheetName = "Sheet1";

string title = "New Chart";

string dataRange = "A1:B3";

InsertChartInSpreadsheet(FileName, worksheetName, title, dataRange);

private static void InsertChartInSpreadsheet(string docName, string worksheetName, string title, string dataRange)

{

    //Instantiating a Workbook object

    Workbook workbook = new Workbook(docName);

    //Obtaining the reference of the worksheet by passing its Name

    Worksheet worksheet = workbook.Worksheets[worksheetName];

    //Adding a chart to the worksheet

    int chartIndex = worksheet.Charts.Add(Aspose.Cells.Charts.ChartType.Bar, 5, 0, 15, 5);

    //Accessing the instance of the newly added chart

    Aspose.Cells.Charts.Chart chart = worksheet.Charts[chartIndex];

    //Set title of the chart

    chart.Name = title;

    //Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"

    chart.NSeries.Add(dataRange, true);

    //Saving the Excel file

    workbook.Save(docName);

}

{{< /highlight >}}
## **Загрузить образец кода**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/AsposeCellsVsOpenXMLv1.1)
- [Sourceforge](https://sourceforge.net/projects/asposeopenxml/files/Aspose.Cells%20Vs%20OpenXML/Insert%20a%20chart%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Insert%20a%20chart%20\(Aspose.Cells\).zip)
{{< app/cells/assistant language="csharp" >}}
