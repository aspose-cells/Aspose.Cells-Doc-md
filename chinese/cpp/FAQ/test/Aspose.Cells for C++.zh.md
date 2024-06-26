# 用于Excel文件格式的C++库

![版本23.11.0](https://img.shields.io/badge/nuget-v23.11.0-blue) ![NuGet](https://img.shields.io/nuget/dt/Aspose.Cells.Cpp)

[![横幅](https://raw.githubusercontent.com/Aspose/aspose.github.io/master/img/banners/aspose_cells-for-cpp-banner.png)](https://releases.aspose.com/cells/cpp/)

[产品页面](https://products.aspose.com/cells/cpp/) | [文档](https://docs.aspose.com/cells/cpp/) | [演示](https://products.aspose.app/cells/family) | [API 参考](https://reference.aspose.com/cells/cpp) | [示例](https://github.com/aspose-cells/Aspose.Cells-for-C) | [博客](https://blog.aspose.com/category/cells/) | [发布](https://releases.aspose.com/cells/cpp/) | [免费支持](https://forum.aspose.com/c/cells) | [临时许可证](https://purchase.aspose.com/temporary-license/)

[Aspose.Cells for C++](https://products.aspose.com/cells/cpp/) 是一个原生的C++库，可以在不需要使用Microsoft Office或自动化的情况下创建，操作，处理和转换Microsoft Excel?文件。Excel C++ API支持Excel 97-2003（XLS），Excel 2007-2013/2016（XLSX，XLSM，XLSB），OpenOffice XML和其他格式，如CSV，TSV等。

它允许开发人员从他们自己的C++应用程序中处理电子表格行、列、数据、公式、数据透视表、工作表、表格、图表和绘图对象。

## Aspose.Cells for C++ 是什么？

Aspose.Cells for C++ 是一个原生的C++本地API，用于将电子表格创建，操作和转换功能集成到您的C++应用中。它支持与来自Microsoft Excel（XLS，XLSX，XLSB，CSV等）和OpenOffice/LibreOffice（ODS）的许多流行电子表格文件格式一起工作。

您可以在支持C++的任何开发环境（如Microsoft Visual Studio）中使用 Aspose.Cells for C++ 开发64位应用程序。 Aspose.Cells for C++ 是本地组件，可以通过简单地复制部署。 您不必担心其他服务或模块。

Aspose.Cells for C++ 允许您处理Microsoft Excel中的内置和自定义文档属性。支持将Excel工作簿高质量地转换为符合PDF/A标准的文件。处理公式，数据透视表，工作表，表，范围，图表，OLE对象等。

## Excel文件处理功能

- 在没有Microsoft Excel的情况下打开电子表格文件。
- [通过本地计算机上的路径或使用流](https://docs.aspose.com/cells/cpp/different-ways-to-open-files/)打开Excel文件。
- [将工作表](https://docs.aspose.com/cells/cpp/converting-worksheet-to-different-image-formats/)转换为不同的图像格式。
- 根据您的选择[应用条件格式](https://docs.aspose.com/cells/cpp/apply-conditional-formatting-in-worksheet/)。
- 在您的电子表格中[操作数据透视表](https://docs.aspose.com/cells/cpp/manipulate-pivot-table/)。
- [转换表格为范围](https://docs.aspose.com/cells/cpp/tables-and-ranges/)而不会丢失格式。
- 通过提供行和列索引来获取单元格的名称，类似地，可以通过其名称[获取单元格的行和列索引](https://docs.aspose.com/cells/cpp/names-and-indices/)。
- 创建[金字塔图表、折线图、气泡图](https://docs.aspose.com/cells/cpp/creating-and-customizing-charts/)，或自定义图表。
- 将支持的图表类型[呈现为图像或PDF](https://docs.aspose.com/cells/cpp/chart-rendering/)。
- 在工作表中[插入OLE对象](https://docs.aspose.com/cells/cpp/inserting-ole-objects-into-the-worksheet/)。
- 访问工作表中包含的所有OLE对象，进行[提取](https://docs.aspose.com/cells/cpp/extracting-ole-objects-from-worksheet/)。

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

您准备好尝试 Aspose.Cells for C++ 了吗？只需在Visual Studio的包管理器控制台中执行 `Install-Package Aspose.Cells.Cpp` 来获取NuGet包。如果您已经安装了 Aspose.Cells for C++ 并想要升级版本，请执行 `Update-Package Aspose.Cells.Cpp` 来获取最新版本。

### 使用 C++ 将 XLS 转换为 XLSX、XLSB 和 CSV

尝试执行以下代码片段以查看 API 在您的环境中的工作方式，或者查看 [GitHub 存储库](https://github.com/aspose-cells/Aspose.Cells-for-C) 了解其他常见用法场景。

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

### 使用 C++ 创建自定义 Excel 图表

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

[产品页面](https://products.aspose.com/cells/cpp/) | [文档](https://docs.aspose.com/cells/cpp/) | [演示](https://products.aspose.app/cells/family) | [API 参考](https://reference.aspose.com/cells/cpp) | [示例](https://github.com/aspose-cells/Aspose.Cells-for-C) | [博客](https://blog.aspose.com/category/cells/) | [发布](https://releases.aspose.com/cells/cpp/) | [免费支持](https://forum.aspose.com/c/cells) | [临时许可证](https://purchase.aspose.com/temporary-license/)
