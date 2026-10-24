---
title: 将 Excel 转换为 OFD 格式
description: Aspose.Cells 是一个用于处理电子表格文件的 C++ 库，支持将 Excel 工作簿转换为 OFD（Open Fixed-layout Document）格式。本文介绍如何创建 Excel 内容并将其导出为 OFD，以及如何使用 Aspose.Cells 将现有 Excel 文件转换为 OFD。
linktitle: OFD
keywords: Aspose.Cells, C++ 库, 电子表格, Excel 转换为 OFD, OFD 转换, SaveFormat.Ofd, 固定版式文档, 工作簿导出
type: docs
weight: 195
url: /zh/cpp/converting-excel-to-ofd-format/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 支持使用 `SaveFormat.Ofd` 枚举值将 Excel 工作簿直接转换为 OFD（Open Fixed-layout Document）格式。生成的 OFD 文档会保留工作簿的可见布局、内容、合并单元格、列宽、行高、字体、颜色、边框和数字格式。因此，Aspose.Cells 适用于需要固定版式输出的归档、打印、监管申报和政府提交流程。
{{% /alert %}}

## **简介**
OFD（Open Fixed-layout Document）是中国国家标准（GB/T 33190-2016），用于以固定的、基于页面的布局表示数字文档。对于必须精确保留源文档视觉外观的使用场景，它的作用类似于 PDF。OFD 在中华人民共和国政府提交、监管申报、电子发票和长期归档中得到了广泛采用。
将 Excel 工作簿转换为 OFD 通常用于以下场景：电子表格内容需要以只读且布局锁定的文档形式分发，而不是作为可编辑的电子表格提供。例如，向客户发送最终确定的发票、归档季度财务报告，或向监管机构提交预算电子表格。通过 `SaveFormat.Ofd` 枚举值，Aspose.Cells 无需中间转换步骤即可直接将工作簿写入 OFD。OFD 输出会保留单元格值、合并区域、字体、颜色、边框、数字格式和工作簿上配置的页面设置选项。

{{% alert color="primary" %}}
Aspose.Cells 生成的 OFD 输出会保留源工作簿的可见布局，包括单元格内容、合并单元格、列宽和行高。字体、颜色、边框、对齐方式和数字格式等单元格格式也会在固定版式输出中呈现。在工作表上配置的页面设置选项，例如纸张大小、方向和打印区域，会影响生成的 OFD 文档布局。
{{% /alert %}}

## **创建 Excel 工作簿并保存为 OFD**
Aspose.Cells 允许您以编程方式构建工作簿、填充数据，然后使用 `SaveFormat.Ofd` 枚举值直接将其保存为 OFD 格式。以下示例从头创建一张发票。它会添加公司徽标、标题信息、收货方部分、明细项目以及计算得出的总计，然后将工作簿导出为 OFD 文档。

### **使用徽标创建发票**
此示例通过以下步骤构建发票工作表：将徽标图像插入左上角区域，填充公司名称和联系信息，通过合并单元格添加“INVOICE”标题，记录发票编号和日期，列出收货方客户端，创建包含说明、数量、单价和总计列的明细项目表，并使用单元格公式计算小计、税额和总计。粗体标题、价格货币格式、边框和列宽等格式通过 `Style` 和 `Font` 对象应用。最后，使用 `SaveFormat.Ofd` 将工作簿保存为 `.ofd` 扩展名。

```cpp
// Aspose.Cells for C++ 示例
// 使用 Aspose.Cells 26.6.0（或更高版本）和 C++17（或更高版本）编译器进行编译
#include "Aspose.Cells.h"
#include <string>
#include <ctime>
using namespace Aspose::Cells;
int main()
{
    // 初始化 Aspose.Cells
    Aspose::Cells::Startup();
    // 资源和输出目录
    const char16_t* dataDir = u"C:\\Temp\\";
    // 创建新工作簿
    Workbook workbook;
    // 获取第一个工作表
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    // 设置列宽
    cells.SetColumnWidth(0, 5.0);
    cells.SetColumnWidth(1, 35.0);
    cells.SetColumnWidth(2, 12.0);
    cells.SetColumnWidth(3, 15.0);
    cells.SetColumnWidth(4, 15.0);
    cells.SetColumnWidth(5, 5.0);
    // 插入公司徽标
    worksheet.GetPictures().Add(1, 1, U16String(dataDir) + u"logo.png");
    // 公司名称和联系方式
    cells.Get(u"B3").PutValue(u"Acme Corporation");
    cells.Get(u"B4").PutValue(u"123 Business Street");
    cells.Get(u"B5").PutValue(u"City, State 12345");
    cells.Get(u"B6").PutValue(u"Phone: (555) 123-4567");
    // INVOICE 标题 - 合并单元格
    cells.Merge(7, 1, 2, 4);
    Cell titleCell = cells.Get(u"B8");
    titleCell.PutValue(u"INVOICE");
    Style titleStyle = workbook.CreateStyle();
    titleStyle.GetFont().SetIsBold(true);
    titleStyle.GetFont().SetSize(20);
    titleStyle.SetHorizontalAlignment(TextAlignmentType::Center);
    titleCell.SetStyle(titleStyle);
    // 发票编号和日期
    cells.Get(u"B11").PutValue(u"Invoice Number:");
    cells.Get(u"C11").PutValue(u"INV-2024-001");
    cells.Get(u"B12").PutValue(u"Date:");
    std::time_t t = std::time(nullptr);
    std::tm* now = std::localtime(&t);
    char dateBuffer[11];
    std::strftime(dateBuffer, sizeof(dateBuffer), "%Y-%m-%d", now);
    cells.Get(u"C12").PutValue(U16String(dateBuffer));
    // 付款方信息
    cells.Get(u"B14").PutValue(u"Bill To:");
    cells.Get(u"B15").PutValue(u"Client Name");
    cells.Get(u"B16").PutValue(u"Client Address");
    cells.Get(u"B17").PutValue(u"Client City, State");
    // 明细项目表头
    Cell headerDesc = cells.Get(u"B19");
    Cell headerQty = cells.Get(u"C19");
    Cell headerPrice = cells.Get(u"D19");
    Cell headerTotal = cells.Get(u"E19");
    headerDesc.PutValue(u"Description");
    headerQty.PutValue(u"Quantity");
    headerPrice.PutValue(u"Unit Price");
    headerTotal.PutValue(u"Total");
    Style headerStyle = workbook.CreateStyle();
    headerStyle.GetFont().SetIsBold(true);
    headerStyle.GetFont().SetColor(Color::White());
    headerStyle.SetForegroundColor(Color{0xff, 0x00, 0x00, 0x80});
    headerStyle.SetPattern(BackgroundType::Solid);
    headerStyle.SetHorizontalAlignment(TextAlignmentType::Center);
    headerStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    headerStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    headerStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    headerStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    headerDesc.SetStyle(headerStyle);
    headerQty.SetStyle(headerStyle);
    headerPrice.SetStyle(headerStyle);
    headerTotal.SetStyle(headerStyle);
    // 带边框的货币样式
    Style currencyStyle = workbook.CreateStyle();
    currencyStyle.SetCustom(u"\"$\"#,##0.00");
    currencyStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    // 用于描述/数量单元格的普通边框样式
    Style borderStyle = workbook.CreateStyle();
    borderStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    // 明细项目行
    struct LineItem { const char16_t* desc; int qty; double price; };
    LineItem lineItems[] = {
        {u"Product A - Widget", 2, 50.00},
        {u"Product B - Gadget", 3, 75.00},
        {u"Product C - Service", 1, 100.00}
    };
    for (int i = 0; i < 3; i++)
    {
        int row = 20 + i;
        Cell descCell = cells.Get(row, 1);
        Cell qtyCell = cells.Get(row, 2);
        Cell priceCell = cells.Get(row, 3);
        Cell totalCell = cells.Get(row, 4);
        descCell.PutValue(lineItems[i].desc);
        qtyCell.PutValue(lineItems[i].qty);
        priceCell.PutValue(lineItems[i].price);
        std::string formula = "C" + std::to_string(row + 1) + "*D" + std::to_string(row + 1);
        totalCell.SetFormula(U16String(formula.c_str()));
        descCell.SetStyle(borderStyle);
        qtyCell.SetStyle(borderStyle);
        priceCell.SetStyle(currencyStyle);
        totalCell.SetStyle(currencyStyle);
    }
    // 小计、税费、总计
    cells.Get(u"B24").PutValue(u"Subtotal:");
    Cell subtotalCell = cells.Get(u"E24");
    subtotalCell.SetFormula(u"SUM(E21:E23)");
    cells.Get(u"B25").PutValue(u"Tax (10%):");
    Cell taxCell = cells.Get(u"E25");
    taxCell.SetFormula(u"E24*0.1");
    cells.Get(u"B26").PutValue(u"Grand Total:");
    Cell grandTotalCell = cells.Get(u"E26");
    grandTotalCell.SetFormula(u"E24+E25");
    // 总计值的粗体 + 货币样式
    Style totalStyle = workbook.CreateStyle();
    totalStyle.GetFont().SetIsBold(true);
    totalStyle.SetCustom(u"\"$\"#,##0.00");
    subtotalCell.SetStyle(totalStyle);
    taxCell.SetStyle(totalStyle);
    grandTotalCell.SetStyle(totalStyle);
    // 总计标签的粗体样式
    Style boldStyle = workbook.CreateStyle();
    boldStyle.GetFont().SetIsBold(true);
    cells.Get(u"B24").SetStyle(boldStyle);
    cells.Get(u"B25").SetStyle(boldStyle);
    cells.Get(u"B26").SetStyle(boldStyle);
    // 将工作簿保存为 OFD 文件
    workbook.Save(U16String(dataDir) + u"Invoice.ofd", SaveFormat::Ofd);
    // 清理 Aspose.Cells 资源
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **将现有 Excel 文件转换为 OFD**
Aspose.Cells 还可以从磁盘加载现有 Excel 工作簿，并将其直接导出为 OFD 格式。这适用于批处理转换管道、归档工作流，以及源工作簿由其他工具生成、只需重新输出为固定版式文档的场景。以下示例加载现有 `.xlsx` 工作簿，从其单元格读取数据，应用可选的页面设置调整，并将结果保存为 OFD 文档。

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <iostream>
#include <ctime>
using namespace Aspose::Cells;
std::string GetCurrentTimestamp() {
    std::time_t t = std::time(nullptr);
    std::tm* now = std::localtime(&t);
    char buffer[20];
    std::strftime(buffer, sizeof(buffer), "%Y-%m-%d %H:%M:%S", now);
    return std::string(buffer);
}
int main() {
    Aspose::Cells::Startup();
    std::string dataDir = "C:\\Examples\\";
    // 从磁盘打开现有的 Excel 工作簿
    Workbook workbook(U16String((dataDir + "SampleBook.xlsx").c_str()));
    // (1) 读取并显示选定单元格的值，以确认文件已加载
    Worksheet firstSheet = workbook.GetWorksheets().Get(0);
    U16String sheetName = firstSheet.GetName();
    Cell a1 = firstSheet.GetCells().Get(u"A1");
    Cell b1 = firstSheet.GetCells().Get(u"B1");
    Cell c1 = firstSheet.GetCells().Get(u"C1");
    std::cout << "First sheet name: " << sheetName.ToUtf8() << std::endl;
    std::cout << "Cell A1: " << a1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Cell B1: " << b1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Cell C1: " << c1.GetStringValue().ToUtf8() << std::endl;
    // (2) 遍历 Worksheets 集合以枚举可用的工作表
    std::cout << "\nAvailable worksheets:" << std::endl;
    WorksheetCollection sheets = workbook.GetWorksheets();
    int sheetCount = sheets.GetCount();
    for (int i = 0; i < sheetCount; ++i) {
        Worksheet ws = sheets.Get(i);
        U16String wsName = ws.GetName();
        std::cout << "  [" << i << "] " << wsName.ToUtf8() << std::endl;
    }
    // (3) 根据需要更新时间戳单元格以反映转换情况
    std::string timestamp1 = GetCurrentTimestamp();
    firstSheet.GetCells().Get(u"A1").PutValue(U16String(("Converted on: " + timestamp1).c_str()));
    // 在数据块顶部追加摘要标题行
    firstSheet.GetCells().InsertRow(0);
    firstSheet.GetCells().Get(u"A1").PutValue(u"Conversion Summary");
    std::string timestamp2 = GetCurrentTimestamp();
    firstSheet.GetCells().Get(u"A2").PutValue(U16String(("Generated: " + timestamp2).c_str()));
    // (4) 配置工作表的 PageSetup 属性
    PageSetup pageSetup = firstSheet.GetPageSetup();
    pageSetup.SetOrientation(PageOrientationType::Landscape);
    pageSetup.SetPaperSize(PaperSizeType::PaperA4);
    pageSetup.SetFitToPagesTall(1);
    pageSetup.SetFitToPagesWide(1);
    // (5) 根据需要设置 OFD 输出的打印区域
    int lastRow = firstSheet.GetCells().GetMaxDataRow();
    int lastCol = firstSheet.GetCells().GetMaxDataColumn();
    U16String lastColLetter = CellsHelper::ColumnIndexToName(lastCol);
    std::string printArea = "A1:" + lastColLetter.ToUtf8() + std::to_string(lastRow + 1);
    firstSheet.GetPageSetup().SetPrintArea(U16String(printArea.c_str()));
    std::cout << "\nPrint area set to: " << printArea << std::endl;
    // (6) 将工作簿保存为 OFD 文件
    workbook.Save(U16String((dataDir + "SampleBook.ofd").c_str()), SaveFormat::Ofd);
    std::cout << "\nFile successfully converted to OFD format: " << dataDir << "SampleBook.ofd" << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

{{< app/cells/assistant language="cpp" >}}