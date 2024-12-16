# Go Library for Excel File Formats

![Version 24.11.0](https://img.shields.io/badge/go-v24.11.0-blue)

[Product Page](https://products.aspose.com/cells/go-cpp/) | [Docs](https://docs.aspose.com/cells/go-cpp/) | [Demos](https://products.aspose.app/cells/family) | [API Reference](https://reference.aspose.com/cells/go-cpp) | [Examples](https://github.com/aspose-cells/aspose-cells-go-cpp) | [Blog](https://blog.aspose.com/category/cells/) | [Releases](https://releases.aspose.com/cells/go-cpp/) | [Free Support](https://forum.aspose.com/c/cells) | [Temporary License](https://purchase.aspose.com/temporary-license/)

[Aspose.Cells for Go via C++](https://products.aspose.com/cells/go-cpp/) is a native Go library to create, manipulate, process, and convert Microsoft Excel? files without needing Microsoft Office? or Automation. The Excel Go API supports Excel 97-2003 (XLS), Excel 2007-2013/2016 (XLSX, XLSM, XLSB), OpenOffice XML, and other formats such as CSV, TSV, and more.

It allows the developers to work with spreadsheet rows, columns, data, formulas, pivot tables, worksheets, tables, charts, and drawing objects from their own Go applications.

## What is Aspose.Cells for Go via C++?

Aspose.Cells for Go via C++ is a native Go on premise API to integrate Spreadsheet creation, manipulation and conversion features into your Go Apps. It supports working with many popular spreadsheet file formats from Microsoft Excel (XLS, XLSX, XLSB, CSV, etc.) and OpenOffice/LibreOffice (ODS).

You can use Aspose.Cells for Go via C++ to develop 64-bit applications in any development environment that supports Go, such as, Microsoft Visual Studio. Aspose.Cells for Go via C++ is a native assembly that can be deployed by simply copying it. You do not have to worry about other services or modules.

Aspose.Cells for Go via C++ allows you to work with the built-in as well as the custom document properties in Microsoft Excel. Supports high-quality conversion of Excel Workbooks to PDF/A compliant files. Work with formulas, pivot tables, worksheets, tables, ranges, charts, OLE objects and much more.

## Excel File Processing Features

- Open a spreadsheet file without Microsoft Excel.
- [Open an Excel file](https://docs.aspose.com/cells/go/different-ways-to-open-files/) via a path on the local computer or using a stream.
- [Convert worksheet](https://docs.aspose.com/cells/go/converting-worksheet-to-different-image-formats/) to different image formats.
- [Apply conditional formatting](https://docs.aspose.com/cells/go/apply-conditional-formatting-in-worksheet/) as per your choice.
- [Manipulate pivot tables](https://docs.aspose.com/cells/go/manipulate-pivot-table/) in your spreadsheets.
- [Convert table to range](https://docs.aspose.com/cells/go/tables-and-ranges/) without losing formatting.
- Fetch a cell's name by providing the row and column index, similarly, [fetch row and column index of the cell](https://docs.aspose.com/cells/go/names-and-indices/) from its name.
- Create [Pyramid chart, Line chart, Bubble chart](https://docs.aspose.com/cells/go/creating-and-customizing-charts/), or a custom chart.
- [Render](https://docs.aspose.com/cells/go/chart-rendering/) supported chart types to images or PDF.
- [Insert an OLE object into the worksheet](https://docs.aspose.com/cells/go/inserting-ole-objects-into-the-worksheet/).
- Access all the OLE objects contained in the worksheet for [extraction](https://docs.aspose.com/cells/go/extracting-ole-objects-from-worksheet/).

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

Are you ready to give Aspose.Cells for Go via C++ a try? Simply execute `go get -u github.com/aspose-cells/aspose-cells-go-cpp` and import `github.com/aspose-cells/aspose-cells-go-cpp` from go file. If you already have Aspose.Cells for Go via C++ and want to upgrade the version, please execute `go get github.com/aspose-cells/aspose-cells-go-cpp@v24.12.0` to get the latest version.

### Convert XLS to XLSX, XLSB & CSV using Go

Try executing the below snippet to see how API works in your environment or check the [GitHub Repository](https://github.com/aspose-cells/aspose-cells-go-cpp) for other common usage scenarios.

```Go
lic, _ := NewLicense()
lic.SetLicense_String(os.Getenv("LicensePath"))
workbook, err1 := NewWorkbook_String("Book1.xlsx")
if err1 != nil {
    println(err1)
}
workbook.Save_String("Book1.pdf")
workbook.Save_String("Book1.png")
workbook.Save_String("Book1.txt")
workbook.Save_String("Book1.ods")
workbook.Save_String("Book1.md")
workbook.Save_String("Book1.json")
workbook.Save_String("Book1.html")
```

### Create a Custom Excel Chart with Go

```Go
package main

import (
 . "asposecells"
 "os"
)

func main() {
 lic, _ := NewLicense()
 lic.SetLicense_String(os.Getenv("LicensePath"))

 workbook, _ := NewWorkbook()
 worksheets, _ := workbook.GetWorksheets()
 worksheet, _ := worksheets.Get_Int(0)
 cells, _ := worksheet.GetCells()
 cell, _ := cells.Get_String("A1")
 cell.PutValue_Int(50)
 cell, _ = cells.Get_String("A2")
 cell.PutValue_Int(100)
 cell, _ = cells.Get_String("A3")
 cell.PutValue_Int(150)
 cell, _ = cells.Get_String("B1")
 cell.PutValue_Int(4)
 cell, _ = cells.Get_String("B2")
 cell.PutValue_Int(20)
 cell, _ = cells.Get_String("B3")
 cell.PutValue_Int(50)
 charts, _ := worksheet.GetCharts()
 chartIndex, _ := charts.Add_ChartType_Int_Int_Int_Int(ChartType_Pyramid, 5, 0, 20, 8)
 chart, _ := charts.Get_Int(chartIndex)
 series, _ := chart.GetNSeries()
 series.Add_String_Bool("A1:B3", true)
 workbook.Save_String("CreateChart.xlsx")
}

```

[Product Page](https://products.aspose.com/cells/go-cpp/) | [Docs](https://docs.aspose.com/cells/go-cpp/) | [Demos](https://products.aspose.app/cells/family) | [API Reference](https://reference.aspose.com/cells/go-cpp) | [Examples](https://github.com/aspose-cells/aspose-cells-go-cpp) | [Blog](https://blog.aspose.com/category/cells/) | [Releases](https://releases.aspose.com/cells/go-cpp/) | [Free Support](https://forum.aspose.com/c/cells) | [Temporary License](https://purchase.aspose.com/temporary-license/)
