# Go语言库 — Excel 文件格式

![版本 24.11.0](https://img.shields.io/badge/go-v24.11.0-blue)

[产品页面](https://products.aspose.com/cells/go-cpp/) | [文档](https://docs.aspose.com/cells/go-cpp/) | [演示](https://products.aspose.app/cells/family) | [API 参考](https://reference.aspose.com/cells/go-cpp) | [示例](https://github.com/aspose-cells/aspose-cells-go-cpp) | [博客](https://blog.aspose.com/category/cells/) | [版本](https://releases.aspose.com/cells/go-cpp/) | [免费支持](https://forum.aspose.com/c/cells) | [临时许可证](https://purchase.aspose.com/temporary-license/)

[Aspose.Cells for Go via C++](https://products.aspose.com/cells/go-cpp/) 是一个原生Go库，用于创建、操作、处理和转换Microsoft Excel文件，无需Microsoft Office或自动化。Excel Go API支持Excel 97-2003（XLS）、Excel 2007-2013/2016（XLSX、XLSM、XLSB）、OpenOffice XML及其他格式如CSV、TSV等。

它允许开发者在自己的 Go 应用程序中操作电子表格的行、列、数据、公式、数据透视表、工作表、表格、图表和绘图对象。

## 什么是Aspose.Cells for Go via C++？

Aspose.Cells for Go via C++是一个原生的Go本地API，用于将电子表格创建、操作和转换功能集成到您的Go应用中。它支持处理多种微软Excel（XLS、XLSX、XLSB、CSV等）和OpenOffice/LibreOffice（ODS）格式的文件。

你可以使用Aspose.Cells for Go via C++在支持Go的任何开发环境（如Microsoft Visual Studio）中开发64位应用程序。Aspose.Cells for Go via C++是一个原生程序集，只需复制即可部署。你无需担心其他服务或模块。

Aspose.Cells for Go via C++允许你操作Microsoft Excel中的内置和自定义文档属性。支持将Excel工作簿高质量转换为符合PDF/A标准的文件。可以操作公式、数据透视表、工作表、表格、区域、图表、OLE对象等。

## Excel文件处理功能

- 在没有Microsoft Excel的情况下打开电子表格文件。
- [通过路径在本地计算机或使用流打开 Excel 文件](https://docs.aspose.com/cells/go/different-ways-to-open-files/)。
- [将工作表转换为不同图片格式](https://docs.aspose.com/cells/go/converting-worksheet-to-different-image-formats/)。
- [根据需要应用条件格式](https://docs.aspose.com/cells/go/apply-conditional-formatting-in-worksheet/)。
- [操作数据透视表](https://docs.aspose.com/cells/go/manipulate-pivot-table/)。
- [将表格转换为范围](https://docs.aspose.com/cells/go/tables-and-ranges/)而不丢失格式。
- 通过提供行列索引获取单元格名称，类似地，[通过名称获取行列索引](https://docs.aspose.com/cells/go/names-and-indices/)。
- 创建 [金字塔图、折线图、气泡图](https://docs.aspose.com/cells/go/creating-and-customizing-charts/)，或自定义图表。
- [渲染](https://docs.aspose.com/cells/go/chart-rendering/) 支持的图表类型为图片或 PDF。
- [在工作表中插入OLE对象](https://docs.aspose.com/cells/go/inserting-ole-objects-into-the-worksheet/)。
- 访问工作表中的所有OLE对象以进行 [提取](https://docs.aspose.com/cells/go/extracting-ole-objects-from-worksheet/)。

## 支持的读写格式

**Microsoft Excel:** XLS, XLSX, XLSB, SpreadsheetML\
**Text:** CSV, TSV, TabDelimited\
**OpenDocument:** ODS\
**其他:** HTML、MHTML

## 保存电子表格文档为

**Microsoft Excel:** XLSM, XLTX, XLTM, XLAM\
**便携式文档格式:** PDF、XPS\
**Text:** CSV, TSV, TabDelimited\
**图像:** SVG、JPEG、PNG、BMP、GIF\
**Web:** HTML, MHTML\
**元文件:** EMF\
**其它** DIF

## 入门指南

你准备好试用Aspose.Cells for Go via C++了吗？只需执行`go get -u github.com/aspose-cells/aspose-cells-go-cpp`，然后在go文件中导入`github.com/aspose-cells/aspose-cells-go-cpp`。如果你已有Aspose.Cells for Go via C++并想升级版本，请执行`go get github.com/aspose-cells/aspose-cells-go-cpp@v24.12.0`以获取最新版本。

### 使用 Go 转换 XLS 为 XLSX、XLSB 和 CSV

尝试运行以下代码片段，了解API在你的环境中的工作方式，或查看 [GitHub 仓库](https://github.com/aspose-cells/aspose-cells-go-cpp) 获取其他常用场景。

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

### 使用 Go 创建自定义 Excel 图表

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

[产品页面](https://products.aspose.com/cells/go-cpp/) | [文档](https://docs.aspose.com/cells/go-cpp/) | [演示](https://products.aspose.app/cells/family) | [API 参考](https://reference.aspose.com/cells/go-cpp) | [示例](https://github.com/aspose-cells/aspose-cells-go-cpp) | [博客](https://blog.aspose.com/category/cells/) | [版本](https://releases.aspose.com/cells/go-cpp/) | [免费支持](https://forum.aspose.com/c/cells) | [临时许可证](https://purchase.aspose.com/temporary-license/)
