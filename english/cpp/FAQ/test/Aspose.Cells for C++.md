# C++ Library for Excel File Formats

![Version 23.11.0](https://img.shields.io/badge/nuget-v23.11.0-blue) ![NuGet](https://img.shields.io/nuget/dt/Aspose.Cells.Cpp)

[![banner](https://raw.githubusercontent.com/Aspose/aspose.github.io/master/img/banners/aspose_cells-for-cpp-banner.png)](https://releases.aspose.com/cells/cpp/)

[Product Page](https://products.aspose.com/cells/cpp/) | [Docs](https://docs.aspose.com/cells/cpp/) | [Demos](https://products.aspose.app/cells/family) | [API Reference](https://reference.aspose.com/cells/cpp) | [Examples](https://github.com/aspose-cells/Aspose.Cells-for-C) | [Blog](https://blog.aspose.com/category/cells/) | [Releases](https://releases.aspose.com/cells/cpp/) | [Free Support](https://forum.aspose.com/c/cells) | [Temporary License](https://purchase.aspose.com/temporary-license/)

[Aspose.Cells for C++](https://products.aspose.com/cells/cpp/) is a native C++ library to create, manipulate, process, and convert Microsoft Excel? files without needing Microsoft Office? or Automation. The Excel C++ API supports Excel 97-2003 (XLS), Excel 2007-2013/2016 (XLSX, XLSM, XLSB), OpenOffice XML, and other formats such as CSV, TSV, and more.

It allows the developers to work with spreadsheet rows, columns, data, formulas, pivot tables, worksheets, tables, charts, and drawing objects from their own C++ applications.

## What is Aspose.Cells for C++?

Aspose.Cells for C++ is a native C++ on premise API to integrate Spreadsheet creation, manipulation and conversion features into your C++ Apps. It supports working with many popular spreadsheet file formats from Microsoft Excel (XLS, XLSX, XLSB, CSV, etc.) and OpenOffice/LibreOffice (ODS).

You can use Aspose.Cells for C++ to develop 64-bit applications in any development environment that supports C++, such as, Microsoft Visual Studio. Aspose.Cells for C++ is a native assembly that can be deployed by simply copying it. You do not have to worry about other services or modules.

Aspose.Cells for C++ allows you to work with the built-in as well as the custom document properties in Microsoft Excel. Supports high-quality conversion of Excel Workbooks to PDF/A compliant files. Work with formulas, pivot tables, worksheets, tables, ranges, charts, OLE objects and much more.

## Excel File Processing Features

- Open a spreadsheet file without Microsoft Excel.
- [Open an Excel file](https://docs.aspose.com/cells/cpp/different-ways-to-open-files/) via a path on the local computer or using a stream.
- [Convert worksheet](https://docs.aspose.com/cells/cpp/converting-worksheet-to-different-image-formats/) to different image formats.
- [Apply conditional formatting](https://docs.aspose.com/cells/cpp/apply-conditional-formatting-in-worksheet/) as per your choice.
- [Manipulate pivot tables](https://docs.aspose.com/cells/cpp/manipulate-pivot-table/) in your spreadsheets.
- [Convert table to range](https://docs.aspose.com/cells/cpp/tables-and-ranges/) without losing formatting.
- Fetch a cell's name by providing the row and column index, similarly, [fetch row and column index of the cell](https://docs.aspose.com/cells/cpp/names-and-indices/) from its name.
- Create [Pyramid chart, Line chart, Bubble chart](https://docs.aspose.com/cells/cpp/creating-and-customizing-charts/), or a custom chart.
- [Render](https://docs.aspose.com/cells/cpp/chart-rendering/) supported chart types to images or PDF.
- [Insert an OLE object into the worksheet](https://docs.aspose.com/cells/cpp/inserting-ole-objects-into-the-worksheet/).
- Access all the OLE objects contained in the worksheet for [extraction](https://docs.aspose.com/cells/cpp/extracting-ole-objects-from-worksheet/).

## Supported Read & Write Formats

**Microsoft Excel:** XLS, XLSX, XLSB, SpreadsheetML\
**Text:** CSV, TSV, TabDelimited\
**OpenDocument:** ODS\
**Other:** HTML, MHTML

## Save Spreadsheet Documents As

**Microsoft Excel:** XLSM, XLTX, XLTM, XLAM\
**Portable Document Format:** PDF, XPS\
**Text:** CSV, TSV, TabDelimited\
**Images:** SVG, JPEG, PNG, BMP, GIF\
**Web:** HTML, MHTML\
**Metafile:** EMF\
**Other** DIF

## Get Started

Are you ready to give Aspose.Cells for C++ a try? Simply execute `Install-Package Aspose.Cells.Cpp` from Package Manager Console in Visual Studio to fetch the NuGet package. If you already have Aspose.Cells for C++ and want to upgrade the version, please execute `Update-Package Aspose.Cells.Cpp` to get the latest version.

### Convert XLS to XLSX, XLSB & CSV using C++

Try executing the below snippet to see how API works in your environment or check the [GitHub Repository](https://github.com/aspose-cells/Aspose.Cells-for-C) for other common usage scenarios.

```c++
U16String dir(u"your path");
// load the file to be converted
Workbook book(dir + u"template.xls");
// save in different formats
book.Save(dir + u"output.xlsx", SaveFormat::Xlsx);
book.Save(dir + u"output.xlsb", SaveFormat::Xlsb);
book.Save(dir + u"output.csv", SaveFormat::CSV);
book.Save(dir + u"output.json", SaveFormat::Json);
```

### Create a Custom Excel Chart with C++

```c++
// create a new workbook
Workbook workbook;

// get first worksheet which is created by default
Worksheet worksheet = workbook.GetWorksheets().Get(0);

// add sample data
worksheet.GetCells().Get(u"A1").PutValue(50);
worksheet.GetCells().Get(u"A2").PutValue(100);
worksheet.GetCells().Get(u"A3").PutValue(150);
worksheet.GetCells().Get(u"A4").PutValue(110);
worksheet.GetCells().Get(u"B1").PutValue(260);
worksheet.GetCells().Get(u"B2").PutValue(12);
worksheet.GetCells().Get(u"B3").PutValue(50);
worksheet.GetCells().Get(u"B4").PutValue(100);

// add a chart to the worksheet
int chartIndex = worksheet.GetCharts().Add(Aspose::Cells::Charts::ChartType::Column, 5, 0, 20, 8);

// access the instance of the newly added chart
Chart chart = worksheet.GetCharts().Get(chartIndex);

// add SeriesCollection (chart data source) to the chart ranging from A1 to B4
chart.GetNSeries().Add(u"A1:B4", true);

// set the chart type of 2nd NSeries to display as line chart
chart.GetNSeries().Get(1).SetType(
	Aspose::Cells::Charts::ChartType::Line);

// save the Excel file
workbook.Save(u"output.xlsx");
```

[Product Page](https://products.aspose.com/cells/cpp/) | [Docs](https://docs.aspose.com/cells/cpp/) | [Demos](https://products.aspose.app/cells/family) | [API Reference](https://reference.aspose.com/cells/cpp) | [Examples](https://github.com/aspose-cells/Aspose.Cells-for-C) | [Blog](https://blog.aspose.com/category/cells/) | [Releases](https://releases.aspose.com/cells/cpp/) | [Free Support](https://forum.aspose.com/c/cells) | [Temporary License](https://purchase.aspose.com/temporary-license/)
{{< app/cells/assistant language="cpp" >}}