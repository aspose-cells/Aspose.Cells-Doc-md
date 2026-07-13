---
title: تحويل Excel إلى تنسيق OFD
linktitle: تحويل Excel إلى تنسيق OFD
description: Aspose.Cells هي مكتبة C++ للعمل مع ملفات جداول البيانات تدعم تحويل مصنفات Excel إلى تنسيق OFD (مستند التخطيط الثابت المفتوح). توضح هذه المقالة كيفية إنشاء محتوى Excel وتصديره كـ OFD، بالإضافة إلى كيفية تحويل ملفات Excel الموجودة إلى OFD باستخدام Aspose.Cells.
keywords: Aspose.Cells, مكتبة C++, جدول بيانات, Excel إلى OFD, تحويل OFD, SaveFormat.Ofd, مستند التخطيط الثابت, تصدير مصنف
type: docs
weight: 195
url: /ar/cpp/converting-excel-to-ofd-format/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

يدعم Aspose.Cells تحويل مصنفات Excel مباشرة إلى تنسيق OFD (مستند التخطيط الثابت المفتوح) باستخدام قيمة التعداد `SaveFormat.Ofd`. يحافظ مستند OFD الناتج على التخطيط المرئي للمصنف ومحتواه والخلايا المدمجة وعروض الأعمدة وارتفاعات الصفوف والخطوط والألوان والحدود وتنسيقات الأرقام. هذا يجعل Aspose.Cells مناسبًا لأرشفة وسير عمل الطباعة والتقديمات التنظيمية والحكومية التي تتطلب إخراجًا بتخطيط ثابت.

{{% /alert %}}
## **مقدمة**
OFD (مستند التخطيط الثابت المفتوح) هو معيار وطني صيني (GB/T 33190-2016) لتمثيل المستندات الرقمية في تخطيط ثابت قائم على الصفحات. يؤدي دورًا مشابهًا لـ PDF في حالات الاستخدام التي يجب فيها الحفاظ على المظهر المرئي للمستند المصدر تمامًا كما تم تأليفه. يُعتمد OFD على نطاق واسع في التقديمات الحكومية والإيداعات التنظيمية والفواتير الإلكترونية والأرشفة طويلة الأمد في جمهورية الصين الشعبية.

يُعد تحويل مصنفات Excel إلى OFD متطلبًا شائعًا في السيناريوهات التي يجب فيها توزيع محتوى جدول البيانات كمادة للقراءة فقط بتخطيط مقفل بدلاً من جدول بيانات قابل للتحرير. تتضمن الأمثلة شحن فاتورة نهائية إلى عميل، أو أرشفة تقرير مالي ربع سنوي، أو تقديم جدول بيانات ميزانية إلى سلطة تنظيمية. يعالج Aspose.Cells هذا المتطلب من خلال قيمة التعداد `SaveFormat.Ofd`، التي تكتب المصنف مباشرة إلى OFD دون الحاجة إلى خطوة تحويل وسيطة. يحافظ إخراج OFD على قيم الخلايا والنطاقات المدمجة والخطوط والألوان والحدود وتنسيقات الأرقام وخيارات إعداد الصفحة التي تم تكوينها في المصنف.

{{% alert color="primary" %}}

يحافظ إخراج OFD الذي تم إنشاؤه بواسطة Aspose.Cells على التخطيط المرئي للمصنف المصدر، بما في ذلك محتوى الخلايا والخلايا المدمجة وعروض الأعمدة وارتفاعات الصفوف. يتم أيضًا عرض تنسيق الخلايا مثل الخطوط والألوان والحدود والمحاذاة وتنسيقات الأرقام في الإخراج بتخطيط ثابت. تؤثر خيارات إعداد الصفحة التي تم تكوينها على ورقة العمل، مثل حجم الورق والاتجاه ومنطقة الطباعة، على تخطيط مستند OFD الناتج.

{{% /alert %}}
## **إنشاء مصنف Excel وحفظه بتنسيق OFD**
يتيح لك Aspose.Cells إنشاء مصنف برمجيًا، وتعبئته بالبيانات، ثم حفظه مباشرة بتنسيق OFD باستخدام تعداد `SaveFormat.Ofd`. ينشئ المثال التالي فاتورة من الصفر. يضيف شعار الشركة ومعلومات الرأس وقسم الفواتير وعناصر البنود والإجماليات المحسوبة، ثم يصدر المصنف إلى مستند OFD.
### **إنشاء فاتورة مع شعار**
يبني المثال ورقة عمل الفاتورة عن طريق إدراج صورة شعار في المنطقة العلوية اليسرى، وملء اسم الشركة وتفاصيل الاتصال، وإضافة عنوان "INVOICE" عبر الخلايا المدمجة، وتسجيل رقم الفاتورة وتاريخها، وسرد عميل الفواتير، وبناء جدول عناصر البنود بأعمدة الوصف والكمية وسعر الوحدة والإجمالي، وحساب الإجمالي الفرعي والضريبة والإجمالي الكلي باستخدام صيغ الخلايا. يتم تطبيق التنسيق مثل العناوين الغامقة وتنسيق العملة للأسعار والحدود وعروض الأعمدة باستخدام كائنات `Style` و `Font`. أخيرًا، يتم حفظ المصنف بامتداد `.ofd` باستخدام `SaveFormat.Ofd`.

```cpp
// Aspose.Cells for C++ example
// Compile with Aspose.Cells 26.6.0 (or later) and a C++17 (or later) compiler

#include "Aspose.Cells.h"
#include <string>
#include <ctime>

using namespace Aspose::Cells;

int main()
{
    // Initialize Aspose.Cells
    Aspose::Cells::Startup();

    // Directory for resources and output
    const char16_t* dataDir = u"C:\\Temp\\";

    // Create a new workbook
    Workbook workbook;

    // Obtain the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Set column widths
    cells.SetColumnWidth(0, 5.0);
    cells.SetColumnWidth(1, 35.0);
    cells.SetColumnWidth(2, 12.0);
    cells.SetColumnWidth(3, 15.0);
    cells.SetColumnWidth(4, 15.0);
    cells.SetColumnWidth(5, 5.0);

    // Insert company logo
    worksheet.GetPictures().Add(1, 1, U16String(dataDir) + u"logo.png");

    // Company name and contact details
    cells.Get(u"B3").PutValue(u"Acme Corporation");
    cells.Get(u"B4").PutValue(u"123 Business Street");
    cells.Get(u"B5").PutValue(u"City, State 12345");
    cells.Get(u"B6").PutValue(u"Phone: (555) 123-4567");

    // INVOICE title - merge cells
    cells.Merge(7, 1, 2, 4);
    Cell titleCell = cells.Get(u"B8");
    titleCell.PutValue(u"INVOICE");

    Style titleStyle = workbook.CreateStyle();
    titleStyle.GetFont().SetIsBold(true);
    titleStyle.GetFont().SetSize(20);
    titleStyle.SetHorizontalAlignment(TextAlignmentType::Center);
    titleCell.SetStyle(titleStyle);

    // Invoice number and date
    cells.Get(u"B11").PutValue(u"Invoice Number:");
    cells.Get(u"C11").PutValue(u"INV-2024-001");
    cells.Get(u"B12").PutValue(u"Date:");

    std::time_t t = std::time(nullptr);
    std::tm* now = std::localtime(&t);
    char dateBuffer[11];
    std::strftime(dateBuffer, sizeof(dateBuffer), "%Y-%m-%d", now);
    cells.Get(u"C12").PutValue(U16String(dateBuffer));

    // Bill-to section
    cells.Get(u"B14").PutValue(u"Bill To:");
    cells.Get(u"B15").PutValue(u"Client Name");
    cells.Get(u"B16").PutValue(u"Client Address");
    cells.Get(u"B17").PutValue(u"Client City, State");

    // Line items header
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
    headerStyle.SetForegroundColor(Color{0, 0, 128});
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

    // Currency style with borders
    Style currencyStyle = workbook.CreateStyle();
    currencyStyle.SetCustom(u"\"$\"#,##0.00");
    currencyStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);

    // Plain border style for description/quantity cells
    Style borderStyle = workbook.CreateStyle();
    borderStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);

    // Line items rows
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

        std::string formula = "C" + std::to_string(row) + "*D" + std::to_string(row);
        totalCell.SetFormula(U16String(formula.c_str()));

        descCell.SetStyle(borderStyle);
        qtyCell.SetStyle(borderStyle);
        priceCell.SetStyle(currencyStyle);
        totalCell.SetStyle(currencyStyle);
    }

    // Subtotal, tax, grand total
    cells.Get(u"B24").PutValue(u"Subtotal:");
    Cell subtotalCell = cells.Get(u"E24");
    subtotalCell.SetFormula(u"SUM(E20:E22)");

    cells.Get(u"B25").PutValue(u"Tax (10%):");
    Cell taxCell = cells.Get(u"E25");
    taxCell.SetFormula(u"E24*0.1");

    cells.Get(u"B26").PutValue(u"Grand Total:");
    Cell grandTotalCell = cells.Get(u"E26");
    grandTotalCell.SetFormula(u"E24+E25");

    // Bold + currency style for total values
    Style totalStyle = workbook.CreateStyle();
    totalStyle.GetFont().SetIsBold(true);
    totalStyle.SetCustom(u"\"$\"#,##0.00");

    subtotalCell.SetStyle(totalStyle);
    taxCell.SetStyle(totalStyle);
    grandTotalCell.SetStyle(totalStyle);

    // Bold style for total labels
    Style boldStyle = workbook.CreateStyle();
    boldStyle.GetFont().SetIsBold(true);

    cells.Get(u"B24").SetStyle(boldStyle);
    cells.Get(u"B25").SetStyle(boldStyle);
    cells.Get(u"B26").SetStyle(boldStyle);

    // Save the workbook as an OFD file
    workbook.Save(U16String(dataDir) + u"Invoice.ofd", SaveFormat::Ofd);

    // Cleanup Aspose.Cells resources
    Aspose::Cells::Cleanup();

    return 0;
}
```
## **تحويل ملف Excel موجود إلى OFD**
يمكن لـ Aspose.Cells أيضًا تحميل مصنف Excel موجود من القرص وتصديره مباشرة إلى تنسيق OFD. هذا مفيد لخطوط أنابيب التحويل المجمعة وسير عمل الأرشفة والسيناريوهات التي تم فيها إنتاج المصنف المصدر بواسطة أداة أخرى ولا يحتاج إلا إلى إعادة إصداره كمادة بتخطيط ثابت. يقوم المثال التالي بتحميل مصنف `.xlsx` موجود، وقراءة البيانات من خلاياه، وتطبيق تعديلات إعداد الصفحة الاختيارية، وحفظ النتيجة كمستند OFD.

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

    // افتح مصنف Excel موجود من القرص
    Workbook workbook(U16String((dataDir + "SampleBook.xlsx").c_str()));

    // (1) اقرأ واعرض القيم من الخلايا المحددة لتأكيد تحميل الملف
    Worksheet firstSheet = workbook.GetWorksheets().Get(0);
    U16String sheetName = firstSheet.GetName();
    Cell a1 = firstSheet.GetCells().Get(u"A1");
    Cell b1 = firstSheet.GetCells().Get(u"B1");
    Cell c1 = firstSheet.GetCells().Get(u"C1");

    std::cout << "First sheet name: " << sheetName.ToUtf8() << std::endl;
    std::cout << "Cell A1: " << a1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Cell B1: " << b1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Cell C1: " << c1.GetStringValue().ToUtf8() << std::endl;

    // (2) تكرار عبر مجموعة أوراق العمل لتعداد الأوراق المتاحة
    std::cout << "\nAvailable worksheets:" << std::endl;
    WorksheetCollection sheets = workbook.GetWorksheets();
    int sheetCount = sheets.GetCount();
    for (int i = 0; i < sheetCount; ++i) {
        Worksheet ws = sheets.Get(i);
        U16String wsName = ws.GetName();
        std::cout << "  [" << i << "] " << wsName.ToUtf8() << std::endl;
    }

    // (3) اختياريًا، قم بتحديث خلية الطابع الزمني لتعكس التحويل
    std::string timestamp1 = GetCurrentTimestamp();
    firstSheet.GetCells().Get(u"A1").PutValue(U16String(("Converted on: " + timestamp1).c_str()));

    // أضف صف رأس ملخص في أعلى كتلة البيانات
    firstSheet.GetCells().InsertRow(0);
    firstSheet.GetCells().Get(u"A1").PutValue(u"Conversion Summary");

    std::string timestamp2 = GetCurrentTimestamp();
    firstSheet.GetCells().Get(u"A2").PutValue(U16String(("Generated: " + timestamp2).c_str()));

    // (4) تكوين خصائص PageSetup في ورقة العمل
    PageSetup pageSetup = firstSheet.GetPageSetup();
    pageSetup.SetOrientation(PageOrientationType::Landscape);
    pageSetup.SetPaperSize(PaperSizeType::PaperA4);
    pageSetup.SetFitToPagesTall(1);
    pageSetup.SetFitToPagesWide(1);

    // (5) اختياريًا، قم بتعيين منطقة الطباعة لمخرجات OFD
    int lastRow = firstSheet.GetCells().GetMaxDataRow();
    int lastCol = firstSheet.GetCells().GetMaxDataColumn();
    U16String lastColLetter = CellsHelper::ColumnIndexToName(lastCol);
    std::string printArea = "A1:" + lastColLetter.ToUtf8() + std::to_string(lastRow + 1);
    firstSheet.GetPageSetup().SetPrintArea(U16String(printArea.c_str()));
    std::cout << "\nPrint area set to: " << printArea << std::endl;

    // (6) احفظ المصنف كملف OFD
    workbook.Save(U16String((dataDir + "SampleBook.ofd").c_str()), SaveFormat::Ofd);
    std::cout << "\nFile successfully converted to OFD format: " << dataDir << "SampleBook.ofd" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **مقالات ذات صلة**
- [تقسيم ملفات Excel إلى ملفات متعددة](/cells/ar/cpp/splitting-excel-files-into-multiple-files/)
- [إدراج صورة في خلية](/cells/ar/cpp/inserting-an-image-into-a-cell/)
- [قراءة وكتابة ملفات DBF](/cells/ar/cpp/dbf/)
- [تحويل Sparkline إلى صورة وHTML في Aspose.Cells for C++](/cells/ar/cpp/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="cpp" >}}