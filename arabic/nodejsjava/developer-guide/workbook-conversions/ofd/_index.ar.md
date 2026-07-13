---
title: تحويل Excel إلى تنسيق OFD
linktitle: تحويل Excel إلى تنسيق OFD
description: Aspose.Cells for Node.js via Java هي مكتبة جداول بيانات للعمل مع ملفات جداول البيانات تدعم تحويل مصنفات Excel إلى تنسيق OFD (Open Fixed-layout Document). توضح هذه المقالة كيفية إنشاء محتوى Excel وتصديره بصيغة OFD، بالإضافة إلى كيفية تحويل ملفات Excel الموجودة إلى OFD باستخدام Aspose.Cells.
keywords: Aspose.Cells, Node.js via Java library, جداول البيانات, Excel إلى OFD, تحويل OFD, SaveFormat.Ofd, مستند بتخطيط ثابت, تصدير مصنف
type: docs
weight: 195
url: /ar/nodejs-java/converting-excel-to-ofd-format/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

يدعم Aspose.Cells تحويل مصنفات Excel مباشرةً إلى تنسيق OFD (Open Fixed-layout Document) باستخدام قيمة التعداد `SaveFormat.Ofd`. يحافظ مستند OFD الناتج على التخطيط المرئي للمصنف، ومحتواه، والخلايا المدموجة، وعرض الأعمدة، وارتفاع الصفوف، والخطوط، والألوان، والحدود، وتنسيقات الأرقام. هذا يجعل Aspose.Cells مناسبًا لأعمال الأرشفة، والطباعة، والتقديمات التنظيمية، وعمليات الإيداع الحكومية التي تتطلب مخرجات ذات تخطيط ثابت.

{{% /alert %}}
## **المقدمة**
OFD (Open Fixed-layout Document) هو معيار صيني وطني (GB/T 33190-2016) لتمثيل المستندات الرقمية بتخطيط ثابت قائم على الصفحات. يؤدي دورًا مشابهًا لـ PDF في حالات الاستخدام التي يجب فيها الحفاظ على المظهر المرئي للمستند المصدر تمامًا كما تم تأليفه. يُعتمد OFD على نطاق واسع للإيداعات الحكومية، والتقديمات التنظيمية، والفواتير الإلكترونية، والأرشفة طويلة الأمد في جمهورية الصين الشعبية.

يُعد تحويل مصنفات Excel إلى OFD مطلبًا شائعًا في السيناريوهات التي يجب فيها توزيع محتوى جدول البيانات كأداة للقراءة فقط ومقيدة التخطيط بدلاً من جدول بيانات قابل للتحرير. تتضمن الأمثلة شحن فاتورة نهائية إلى عميل، أو أرشفة تقرير مالي ربع سنوي، أو تقديم جدول بيانات ميزانية إلى جهة تنظيمية. يعالج Aspose.Cells هذا المتطلب من خلال قيمة التعداد `SaveFormat.Ofd`، التي تكتب المصنف مباشرةً إلى OFD دون الحاجة إلى خطوة تحويل وسيطة. يحافظ مخرج OFD على قيم الخلايا، والنطاقات المدموجة، والخطوط، والألوان، والحدود، وتنسيقات الأرقام، وخيارات إعداد الصفحة المكونة على المصنف.

{{% alert color="primary" %}}

يحافظ مخرج OFD الذي ينتجه Aspose.Cells على التخطيط المرئي لمصنف المصدر، بما في ذلك محتوى الخلايا، والخلايا المدموجة، وعرض الأعمدة، وارتفاع الصفوف. كما يتم عرض تنسيق الخلايا مثل الخطوط والألوان والحدود والمحاذاة وتنسيقات الأرقام في المخرج ذي التخطيط الثابت. تؤثر خيارات إعداد الصفحة المكونة على ورقة العمل، مثل حجم الورق والاتجاه ومنطقة الطباعة، على تخطيط مستند OFD الناتج.

{{% /alert %}}
## **إنشاء مصنف Excel وحفظه بتنسيق OFD**
يتيح لك Aspose.Cells إنشاء مصنف برمجيًا، وتعبئته بالبيانات، ثم حفظه مباشرةً بتنسيق OFD باستخدام تعداد `SaveFormat.Ofd`. يُنشئ المثال التالي فاتورة من الصفر. يضيف شعار الشركة، ومعلومات الرأس، وقسم الفاتورة إلى، وبنود الفاتورة، والإجماليات المحسوبة، ثم يصدر المصنف إلى مستند OFD.
### **إنشاء فاتورة بشعار**
يبني المثال ورقة عمل الفاتورة عن طريق إدراج صورة شعار في المنطقة العلوية اليسرى، وتعبئة اسم الشركة وتفاصيل الاتصال، وإضافة عنوان "INVOICE" عبر الخلايا المدموجة، وتسجيل رقم الفاتورة وتاريخها، وسرد عميل الفاتورة إلى، وبناء جدول بنود الفاتورة بأعمدة الوصف والكمية وسعر الوحدة والإجمالي، وحساب المجموع الفرعي والضريبة والإجمالي الكلي باستخدام صيغ الخلايا. يتم تطبيق التنسيق مثل العناوين العريضة وتنسيق العملة للأسعار والحدود وعرض الأعمدة باستخدام كائنات `Style` و `Font`. أخيرًا، يتم حفظ المصنف بامتداد `.ofd` باستخدام `SaveFormat.Ofd`.

```javascript
let dataDir = "C:\\Temp\\";

// إنشاء مصنف جديد
let workbook = new AsposeCells.Workbook();

// الحصول على ورقة العمل الأولى
let worksheet = workbook.getWorksheets().get(0);

// تعيين عرض الأعمدة
worksheet.getCells().setColumnWidth(0, 5);
worksheet.getCells().setColumnWidth(1, 35);
worksheet.getCells().setColumnWidth(2, 12);
worksheet.getCells().setColumnWidth(3, 15);
worksheet.getCells().setColumnWidth(4, 15);
worksheet.getCells().setColumnWidth(5, 5);

// إدراج شعار الشركة
worksheet.getPictures().add(1, 1, dataDir + "logo.png");

// اسم الشركة وتفاصيل الاتصال
worksheet.getCells().get("B3").putValue("Acme Corporation");
worksheet.getCells().get("B4").putValue("123 Business Street");
worksheet.getCells().get("B5").putValue("City, State 12345");
worksheet.getCells().get("B6").putValue("Phone: (555) 123-4567");

// عنوان الفاتورة - دمج الخلايا
worksheet.getCells().merge(7, 1, 2, 4);
let titleCell = worksheet.getCells().get("B8");
titleCell.putValue("INVOICE");

let titleStyle = workbook.createStyle();
titleStyle.getFont().setIsBold(true);
titleStyle.getFont().setSize(20);
titleStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.CENTER);
titleCell.setStyle(titleStyle);

// رقم الفاتورة والتاريخ
worksheet.getCells().get("B11").putValue("Invoice Number:");
worksheet.getCells().get("C11").putValue("INV-2024-001");
worksheet.getCells().get("B12").putValue("Date:");
worksheet.getCells().get("C12").putValue(new Date().toISOString().slice(0, 10));

// قسم الفوترة
worksheet.getCells().get("B14").putValue("Bill To:");
worksheet.getCells().get("B15").putValue("Client Name");
worksheet.getCells().get("B16").putValue("Client Address");
worksheet.getCells().get("B17").putValue("Client City, State");

// رأس عناصر الفاتورة
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
headerStyle.getFont().setColor(AsposeCells.Color.getWhite());
headerStyle.setBackgroundColor(AsposeCells.Color.getNavy());
headerStyle.setHorizontalAlignment(AsposeCells.TextAlignmentType.CENTER);
headerStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
headerStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
headerStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
headerStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);

headerDesc.setStyle(headerStyle);
headerQty.setStyle(headerStyle);
headerPrice.setStyle(headerStyle);
headerTotal.setStyle(headerStyle);

// نمط العملة مع الحدود
let currencyStyle = workbook.createStyle();
currencyStyle.setCustom("\"$\"#,##0.00");
currencyStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
currencyStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
currencyStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
currencyStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);

// نمط حدود عادي لخلايا الوصف/الكمية
let borderStyle = workbook.createStyle();
borderStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
borderStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
borderStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
borderStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);

// صفوف عناصر الفاتورة
let lineItems = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
];

for (let i = 0; i < lineItems.length; i++)
{
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

// المجموع الفرعي، الضريبة، الإجمالي الكلي
worksheet.getCells().get("B24").putValue("Subtotal:");
let subtotalCell = worksheet.getCells().get("E24");
subtotalCell.setFormula("SUM(E20:E22)");

worksheet.getCells().get("B25").putValue("Tax (10%):");
let taxCell = worksheet.getCells().get("E25");
taxCell.setFormula("E24*0.1");

worksheet.getCells().get("B26").putValue("Grand Total:");
let grandTotalCell = worksheet.getCells().get("E26");
grandTotalCell.setFormula("E24+E25");

// نمط غامق + عملة لقيم الإجمالي
let totalStyle = workbook.createStyle();
totalStyle.getFont().setIsBold(true);
totalStyle.setCustom("\"$\"#,##0.00");

subtotalCell.setStyle(totalStyle);
taxCell.setStyle(totalStyle);
grandTotalCell.setStyle(totalStyle);

// نمط غامق لتسميات الإجمالي
let boldStyle = workbook.createStyle();
boldStyle.getFont().setIsBold(true);

worksheet.getCells().get("B24").setStyle(boldStyle);
worksheet.getCells().get("B25").setStyle(boldStyle);
worksheet.getCells().get("B26").setStyle(boldStyle);

// حفظ المصنف كملف OFD
workbook.save(dataDir + "Invoice.ofd", AsposeCells.SaveFormat.Ofd);
```
## **تحويل ملف Excel موجود إلى OFD**
يمكن لـ Aspose.Cells أيضًا تحميل مصنف Excel موجود من القرص وتصديره مباشرةً إلى تنسيق OFD. هذا مفيد لخطوط أنابيب التحويل المجمعة، وسير عمل الأرشفة، والسيناريوهات التي تم فيها إنتاج المصنف المصدر بواسطة أداة أخرى ولا يحتاج إلا إلى إعادة إصداره كأداة ذات تخطيط ثابت. يُحمّل المثال التالي مصنف `.xlsx` موجودًا، ويقرأ البيانات من خلاياه، ويطبق تعديلات إعداد الصفحة الاختيارية، ويحفظ النتيجة كمستند OFD.

```javascript
const AsposeCells = require("aspose.cells");

const dataDir = "C:\\Examples\\";

// فتح مصنف Excel موجود من القرص
const workbook = new AsposeCells.Workbook(dataDir + "SampleBook.xlsx");

// (1) قراءة وعرض القيم من الخلايا المحددة للتأكد من تحميل الملف
const firstSheet = workbook.getWorksheets().get(0);
console.log("First sheet name: " + firstSheet.getName());
console.log("Cell A1: " + firstSheet.getCells().get("A1").getStringValue());
console.log("Cell B1: " + firstSheet.getCells().get("B1").getStringValue());
console.log("Cell C1: " + firstSheet.getCells().get("C1").getStringValue());

// (2) التكرار عبر مجموعة أوراق العمل لتعداد الأوراق المتاحة
console.log("\nAvailable worksheets:");
for (let i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    const ws = workbook.getWorksheets().get(i);
    console.log("  [" + i + "] " + ws.getName());
}

// (3) اختياريًا، تحديث خلية الطابع الزمني لتعكس التحويل
firstSheet.getCells().get("A1").putValue("Converted on: " + formatDate(new Date()));

// إلحاق صف رأس ملخص في أعلى كتلة البيانات
firstSheet.getCells().insertRow(0);
firstSheet.getCells().get("A1").putValue("Conversion Summary");
firstSheet.getCells().get("A2").putValue("Generated: " + formatDate(new Date()));

// (4) تكوين خصائص PageSetup في ورقة العمل
const pageSetup = firstSheet.getPageSetup();
pageSetup.setOrientation(AsposeCells.PageOrientationType.Landscape);
pageSetup.setPaperSize(AsposeCells.PaperSizeType.PaperA4);
pageSetup.setFitToPagesTall(1);
pageSetup.setFitToPagesWide(1);

// (5) اختياريًا، تعيين منطقة الطباعة لمخرجات OFD
const lastRow = firstSheet.getCells().getMaxDataRow();
const lastCol = firstSheet.getCells().getMaxDataColumn();
const lastColLetter = AsposeCells.CellsHelper.columnIndexToName(lastCol);
const printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.getPageSetup().setPrintArea(printArea);
console.log("\nPrint area set to: " + printArea);

// (6) حفظ المصنف كملف OFD
workbook.save(dataDir + "SampleBook.ofd", AsposeCells.SaveFormat.Ofd);
console.log("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");

function formatDate(date) {
    const pad = (n) => n.toString().padStart(2, '0');
    return date.getFullYear() + "-" + pad(date.getMonth() + 1) + "-" + pad(date.getDate()) + " " + pad(date.getHours()) + ":" + pad(date.getMinutes()) + ":" + pad(date.getSeconds());
}
```

## **مقالات ذات صلة**
- [تقسيم ملفات Excel إلى ملفات متعددة](/cells/ar/nodejs-java/splitting-excel-files-into-multiple-files/)
- [إدراج صورة في خلية](/cells/ar/nodejs-java/inserting-an-image-into-a-cell/)
- [قراءة وكتابة ملفات DBF](/cells/ar/nodejs-java/dbf/)
- [تحويل Sparkline إلى صورة وHTML في Aspose.Cells for Node.js via Java](/cells/ar/nodejs-java/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="javascript" >}}