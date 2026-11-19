---
title: تحويل Excel إلى تنسيق OFD
linktitle: تحويل Excel إلى تنسيق OFD
description: Aspose.Cells هي مكتبة Node.js للعمل مع ملفات جداول البيانات تدعم تحويل مصنفات Excel إلى تنسيق OFD (مستند التخطيط الثابت المفتوح). توضح هذه المقالة كيفية إنشاء محتوى Excel وتصديره بتنسيق OFD، وكذلك كيفية تحويل ملفات Excel الحالية إلى OFD باستخدام Aspose.Cells.
keywords: Aspose.Cells, مكتبة Node.js, جدول بيانات, تحويل Excel إلى OFD, تحويل OFD, SaveFormat.Ofd, مستند ذي تخطيط ثابت, تصدير مصنف
type: docs
weight: 195
url: /ar/nodejs-cpp/converting-excel-to-ofd-format/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells تحويل مصنفات Excel مباشرةً إلى تنسيق OFD (مستند التخطيط الثابت المفتوح) باستخدام قيمة التعداد `SaveFormat.Ofd`. وتحافظ مستندات OFD الناتجة على التخطيط المرئي للمصنف، ومحتواه، والخلايا المدمجة، وعروض الأعمدة، وارتفاعات الصفوف، والخطوط، والألوان، والحدود، وتنسيقات الأرقام. نتيجة لذلك، تناسب Aspose.Cells تدفقات العمل التي تتطلب مخرجات ذات تخطيط ثابت، مثل الأرشفة والطباعة والإيداع التنظيمي والإرسال الحكومي.
{{% /alert %}}

## **مقدمة**
يمثل OFD (مستند التخطيط الثابت المفتوح) معيارًا وطنيًا صينيًا (GB/T 33190-2016) لتمثيل المستندات الرقمية في تخطيط ثابت قائم على الصفحات. ويؤدي دورًا مشابهًا لـ PDF في حالات الاستخدام التي يجب فيها الحفاظ على المظهر البصري للمستند المصدر تمامًا حسب إعداده الأصلي. ويُستخدم OFD على نطاق واسع للإرسال الحكومي والإيداع التنظيمي والفواتير الإلكترونية والأرشفة طويلة الأجل في جمهورية الصين الشعبية.
يُعد تحويل مصنفات Excel إلى OFD متطلبًا شائعًا في السيناريوهات التي يجب فيها توزيع محتوى جدول البيانات كملف للقراءة فقط ومقفل التخطيط، بدلًا من جدول بيانات قابل للتحرير. ومن بين الأمثلة إرسال فاتورة مكتملة إلى عميل، أو أرشفة تقرير مالي ربع سنوي، أو تقديم جدول بيانات ميزانية إلى جهة تنظيمية. يعالج Aspose.Cells هذا المتطلب من خلال قيمة التعداد `SaveFormat.Ofd`، التي تكتب المصنف مباشرةً بتنسيق OFD دون الحاجة إلى خطوة تحويل وسيطة. كما يحافظ ملف OFD الناتج على قيم الخلايا والنطاقات المدمجة والخطوط والألوان والحدود وتنسيقات الأرقام وإعدادات تخطيط الصفحة التي تم تكوينها للمصنف.

{{% alert color="primary" %}}
تحافظ مخرجات OFD التي ينتجها Aspose.Cells على التخطيط المرئي للمصنف المصدر، بما في ذلك محتوى الخلايا والخلايا المدمجة وعروض الأعمدة وارتفاعات الصفوف. كما تُعرض تنسيقات الخلايا، مثل الخطوط والألوان والحدود والمحاذاة وتنسيقات الأرقام، في المخرج ذي التخطيط الثابت. وتؤثر خيارات تخطيط الصفحة التي تم إعدادها لورقة العمل، مثل حجم الورق والاتجاه ومنطقة الطباعة، في تخطيط مستند OFD الناتج.
{{% /alert %}}

## **إنشاء مصنف Excel وحفظه بتنسيق OFD**
يتيح لك Aspose.Cells إنشاء مصنف برمجيًا، وتعبئته بالبيانات، ثم حفظه مباشرةً بتنسيق OFD باستخدام تعداد `SaveFormat.Ofd`. ينشئ المثال التالي فاتورة من الصفر. يضيف شعار الشركة ومعلومات الترويسة وقسم بيانات العميل وبنود الفاتورة والإجماليات المحسوبة، ثم يصدّر المصنف إلى مستند OFD.

### **إنشاء فاتورة مع شعار**
يبني المثال ورقة عمل الفاتورة عن طريق إدراج صورة شعار في المنطقة العلوية اليسرى، وتعبئة اسم الشركة وبيانات الاتصال، وإضافة عنوان "فاتورة" عبر خلايا مدمجة، وتسجيل رقم الفاتورة وتاريخها، وسرد العميل الذي تذهب إليه الفاتورة، وبناء جدول لبنود الفاتورة يتضمن أعمدة الوصف والكمية وسعر الوحدة والإجمالي، وحساب المجموع الفرعي والضريبة والإجمالي النهائي باستخدام صيغ الخلايا. ويُطبَّق تنسيقٌ مثل العناوين الغامقة وتنسيق عملة للأسعار والحدود وعروض الأعمدة باستخدام كائنات `Style` و`Font`. وأخيرًا، يُحفظ المصنف بامتداد `.ofd` باستخدام `SaveFormat.Ofd`.

```javascript
const AsposeCells = require("aspose.cells.node");
let dataDir = "C:\\Temp\\";
// Create a new Workbook
let workbook = new AsposeCells.Workbook();
// Obtain the first worksheet
let worksheet = workbook.getWorksheets().get(0);
// Set column widths
worksheet.getCells().setColumnWidth(0, 5);
worksheet.getCells().setColumnWidth(1, 35);
worksheet.getCells().setColumnWidth(2, 12);
worksheet.getCells().setColumnWidth(3, 15);
worksheet.getCells().setColumnWidth(4, 15);
worksheet.getCells().setColumnWidth(5, 5);
// Insert company logo
worksheet.getPictures().add(1, 1, dataDir + "logo.png");
// Company name and contact details
worksheet.getCells().get("B3").putValue("Acme Corporation");
worksheet.getCells().get("B4").putValue("123 Business Street");
worksheet.getCells().get("B5").putValue("City, State 12345");
worksheet.getCells().get("B6").putValue("Phone: (555) 123-4567");
// INVOICE title - merge cells
worksheet.getCells().merge(7, 1, 2, 4);
let titleCell = worksheet.getCells().get("B8");
titleCell.putValue("INVOICE");
let titleStyle = workbook.createStyle();
titleStyle.getFont().setIsBold(true);
titleStyle.getFont().setSize(20);
titleStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);
titleCell.setStyle(titleStyle);
// Invoice number and date
worksheet.getCells().get("B11").putValue("Invoice Number:");
worksheet.getCells().get("C11").putValue("INV-2024-001");
worksheet.getCells().get("B12").putValue("Date:");
let now = new Date();
let dateStr = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}-${String(now.getDate()).padStart(2, '0')}`;
worksheet.getCells().get("C12").putValue(dateStr);
// Bill-to section
worksheet.getCells().get("B14").putValue("Bill To:");
worksheet.getCells().get("B15").putValue("Client Name");
worksheet.getCells().get("B16").putValue("Client Address");
worksheet.getCells().get("B17").putValue("Client City, State");
// Line items header
let headerDesc = worksheet.getCells().get("B19");
let headerQty = worksheet.getCells().get("C19");
let headerPrice = worksheet.getCells().get("D19");
let headerTotal = worksheet.getCells().get("E19");
headerDesc.putValue("Description");
headerQty.putValue("Quantity");
headerPrice.putValue("Unit Price");
headerTotal.putValue("Total");
let headerStyle = workbook.createStyle();
headerStyle.getFont().setIsBold(true);
headerStyle.getFont().setColor(AsposeCells.Color.White);
headerStyle.setBackgroundColor(AsposeCells.Color.Navy);
headerStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
headerStyle.getBorders().getByBorderType(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
headerDesc.setStyle(headerStyle);
headerQty.setStyle(headerStyle);
headerPrice.setStyle(headerStyle);
headerTotal.setStyle(headerStyle);
// Currency style with borders
let currencyStyle = workbook.createStyle();
currencyStyle.setCustom("\"$\"#,##0.00");
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
currencyStyle.getBorders().getByBorderType(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
// Plain border style for description/quantity cells
let borderStyle = workbook.createStyle();
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
borderStyle.getBorders().getByBorderType(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
// Line items rows
let lineItems = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
];
for (let i = 0; i < lineItems.length; i++) {
    let row = 20 + i;
    let descCell = worksheet.getCells().get(row, 1);
    let qtyCell = worksheet.getCells().get(row, 2);
    let priceCell = worksheet.getCells().get(row, 3);
    let totalCell = worksheet.getCells().get(row, 4);
    descCell.putValue(lineItems[i][0]);
    qtyCell.putValue(lineItems[i][1]);
    priceCell.putValue(lineItems[i][2]);
    totalCell.setFormula("C" + row + "*D" + row);
    descCell.setStyle(borderStyle);
    qtyCell.setStyle(borderStyle);
    priceCell.setStyle(currencyStyle);
    totalCell.setStyle(currencyStyle);
}
// Subtotal, tax, grand total
worksheet.getCells().get("B24").putValue("Subtotal:");
let subtotalCell = worksheet.getCells().get("E24");
subtotalCell.setFormula("SUM(E20:E22)");
worksheet.getCells().get("B25").putValue("Tax (10%):");
let taxCell = worksheet.getCells().get("E25");
taxCell.setFormula("E24*0.1");
worksheet.getCells().get("B26").putValue("Grand Total:");
let grandTotalCell = worksheet.getCells().get("E26");
grandTotalCell.setFormula("E24+E25");
// Bold + currency style for total values
let totalStyle = workbook.createStyle();
totalStyle.getFont().setIsBold(true);
totalStyle.setCustom("\"$\"#,##0.00");
subtotalCell.setStyle(totalStyle);
taxCell.setStyle(totalStyle);
grandTotalCell.setStyle(totalStyle);
// Bold style for total labels
let boldStyle = workbook.createStyle();
boldStyle.getFont().setIsBold(true);
worksheet.getCells().get("B24").setStyle(boldStyle);
worksheet.getCells().get("B25").setStyle(boldStyle);
worksheet.getCells().get("B26").setStyle(boldStyle);
// Save the workbook as an OFD file
workbook.save(dataDir + "Invoice.ofd", AsposeCells.SaveFormat.Ofd);
```

## **تحويل ملف Excel موجود إلى OFD**
يمكن لـ Aspose.Cells أيضًا تحميل مصنف Excel موجود من القرص وتصديره مباشرةً بتنسيق OFD. ويفيد ذلك في خطوط أنابيب التحويل الدفعي وتدفقات عمل الأرشفة والسيناريوهات التي أُنتج فيها المصنف المصدر بواسطة أداة أخرى ولا يحتاج فيه إلى أكثر من إعادة إصداره كعنصر ذي تخطيط ثابت. يحمّل المثال التالي مصنفًا موجودًا بصيغة `.xlsx`، ويقرأ البيانات من خلاياه، ويطبّق تعديلات اختيارية على تخطيط الصفحة، ثم يحفظ النتيجة كمستند OFD.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook(dataDir + "SampleBook.xlsx");
// (1) Read and display values from selected cells to confirm the file was loaded
let firstSheet = workbook.getWorksheets().get(0);
console.log("First sheet name: " + firstSheet.getName());
console.log("Cell A1: " + firstSheet.getCells().get("A1").getStringValue());
console.log("Cell B1: " + firstSheet.getCells().get("B1").getStringValue());
console.log("Cell C1: " + firstSheet.getCells().get("C1").getStringValue());
// (2) Iterate over the Worksheets collection to enumerate available sheets
console.log("\nAvailable worksheets:");
for (let i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    let ws = workbook.getWorksheets().get(i);
    console.log("  [" + i + "] " + ws.getName());
}
// (3) Optionally update a timestamp cell to reflect the conversion
firstSheet.getCells().get("A1").putValue("Converted on: " + formatDate(new Date()));
// Append a summary header row at the top of the data block
firstSheet.getCells().insertRow(0);
firstSheet.getCells().get("A1").putValue("Conversion Summary");
firstSheet.getCells().get("A2").putValue("Generated: " + formatDate(new Date()));
// (4) Configure PageSetup properties on the worksheet
let pageSetup = firstSheet.getPageSetup();
pageSetup.setOrientation(AsposeCells.PageOrientationType.Landscape);
pageSetup.setPaperSize(AsposeCells.PaperSizeType.PaperA4);
pageSetup.setFitToPagesTall(1);
pageSetup.setFitToPagesWide(1);
// (5) Optionally set the print area for the OFD output
let lastRow = firstSheet.getCells().getMaxDataRow();
let lastCol = firstSheet.getCells().getMaxDataColumn();
let lastColLetter = AsposeCells.CellsHelper.columnIndexToName(lastCol);
let printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.getPageSetup().setPrintArea(printArea);
console.log("\nPrint area set to: " + printArea);
// (6) Save the workbook as an OFD file
workbook.save(dataDir + "SampleBook.ofd", AsposeCells.SaveFormat.Ofd);
console.log("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");
```

## **مقالات ذات صلة**
- [تقسيم ملفات Excel إلى ملفات متعددة](/cells/ar/nodejs-cpp/splitting-excel-files-into-multiple-files/)
- [إدراج صورة في خلية](/cells/ar/nodejs-cpp/inserting-an-image-into-a-cell/)
- [قراءة ملفات DBF وكتابتها](/cells/ar/nodejs-cpp/dbf/)

{{< app/cells/assistant language="nodejs-cpp" >}}