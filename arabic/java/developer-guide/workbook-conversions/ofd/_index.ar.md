---
title: تحويل Excel إلى تنسيق OFD
linktitle: تحويل Excel إلى تنسيق OFD
description: Aspose.Cells هي مكتبة Java للعمل مع ملفات جداول البيانات تدعم تحويل مصنفات Excel إلى تنسيق OFD (مستند التخطيط الثابت المفتوح). يوضح هذا المقال كيفية إنشاء محتوى Excel وتصديره كملف OFD، بالإضافة إلى كيفية تحويل ملفات Excel الموجودة إلى OFD باستخدام Aspose.Cells.
keywords: Aspose.Cells, مكتبة Java, جدول البيانات, Excel إلى OFD, تحويل OFD, SaveFormat.Ofd, مستند التخطيط الثابت, تصدير المصنف
type: docs
weight: 195
url: /ar/java/converting-excel-to-ofd-format/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells تدعم تحويل مصنفات Excel مباشرةً إلى تنسيق OFD (مستند التخطيط الثابت المفتوح) باستخدام قيمة التعداد `SaveFormat.Ofd`. يحافظ مستند OFD الناتج على التخطيط المرئي للمصنف، والمحتوى، والخلايا المدمجة، وعرض الأعمدة، وارتفاع الصفوف، والخطوط، والألوان، والحدود، وتنسيقات الأرقام. هذا يجعل Aspose.Cells مناسبًا لسير عمل الأرشفة والطباعة والتقديمات التنظيمية والحكومية التي تتطلب مخرجات ذات تخطيط ثابت.

{{% /alert %}}
## **مقدمة**
OFD (مستند التخطيط الثابت المفتوح) هو معيار وطني صيني (GB/T 33190-2016) لتمثيل المستندات الرقمية بتخطيط ثابت قائم على الصفحات. يؤدي دورًا مشابهًا لـ PDF في حالات الاستخدام التي يجب فيها الحفاظ على المظهر المرئي للمستند المصدر تمامًا كما تم تأليفه. يتم اعتماد OFD على نطاق واسع للتقديمات الحكومية، والإيداعات التنظيمية، والفواتير الإلكترونية، والأرشفة طويلة الأمد في جمهورية الصين الشعبية.

يعد تحويل مصنفات Excel إلى OFD مطلبًا شائعًا في السيناريوهات التي يجب فيها توزيع محتوى جدول البيانات كقطعة أثرية للقراءة فقط ذات تخطيط مقفل بدلاً من جدول بيانات قابل للتحرير. تشمل الأمثلة شحن فاتورة نهائية إلى عميل، أو أرشفة تقرير مالي ربع سنوي، أو تقديم جدول بيانات ميزانية إلى سلطة تنظيمية. تعالج Aspose.Cells هذا المتطلب من خلال قيمة التعداد `SaveFormat.Ofd`، التي تكتب المصنف مباشرةً إلى OFD دون الحاجة إلى خطوة تحويل وسيطة. يحافظ مخرج OFD على قيم الخلايا، والنطاقات المدمجة، والخطوط، والألوان، والحدود، وتنسيقات الأرقام، وخيارات إعداد الصفحة المكونة على المصنف.

{{% alert color="primary" %}}

يحافظ مخرج OFD الذي تم إنشاؤه بواسطة Aspose.Cells على التخطيط المرئي لمصنف المصدر، بما في ذلك محتوى الخلايا، والخلايا المدمجة، وعرض الأعمدة، وارتفاع الصفوف. كما يتم عرض تنسيق الخلايا مثل الخطوط والألوان والحدود والمحاذاة وتنسيقات الأرقام في مخرج التخطيط الثابت. تؤثر خيارات إعداد الصفحة المكونة على ورقة العمل، مثل حجم الورق والاتجاه ومنطقة الطباعة، على تخطيط مستند OFD الناتج.

{{% /alert %}}
## **إنشاء مصنف Excel وحفظه بتنسيق OFD**
تتيح لك Aspose.Cells إنشاء مصنف برمجيًا، وتعبئته بالبيانات، ثم حفظه مباشرةً بتنسيق OFD باستخدام تعداد `SaveFormat.Ofd`. ينشئ المثال التالي فاتورة من الصفر. يضيف شعار الشركة، ومعلومات الرأس، وقسم الفواتير، وعناصر السطر، والإجماليات المحسوبة، ثم يصدر المصنف إلى مستند OFD.
### **إنشاء فاتورة بشعار**
ينشئ المثال ورقة عمل فاتورة عن طريق إدراج صورة شعار في المنطقة العلوية اليسرى، وتعبئة اسم الشركة وتفاصيل الاتصال، وإضافة عنوان "INVOICE" عبر الخلايا المدمجة، وتسجيل رقم الفاتورة وتاريخها، وسرد عميل الفواتير، وبناء جدول عناصر السطر بأعمدة الوصف والكمية وسعر الوحدة والإجمالي، وحساب المجموع الفرعي والضريبة والإجمالي الكلي باستخدام صيغ الخلايا. يتم تطبيق التنسيق مثل الرؤوس الغامقة وتنسيق العملة للأسعار والحدود وعرض الأعمدة باستخدام كائنات `Style` و `Font`. أخيرًا، يتم حفظ المصنف بامتداد `.ofd` باستخدام `SaveFormat.Ofd`.

```java
import com.aspose.cells.*;
import java.text.SimpleDateFormat;
import java.util.Date;

String dataDir = "C:\\Temp\\";

// Create a new Workbook
Workbook workbook = new Workbook();

// Obtain the first worksheet
Worksheet worksheet = workbook.getWorksheets().get(0);

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
Cell titleCell = worksheet.getCells().get("B8");
titleCell.putValue("INVOICE");

Style titleStyle = workbook.createStyle();
titleStyle.getFont().setBold(true);
titleStyle.getFont().setSize(20);
titleStyle.setHorizontalAlignment(TextAlignmentType.CENTER);
titleCell.setStyle(titleStyle);

// Invoice number and date
worksheet.getCells().get("B11").putValue("Invoice Number:");
worksheet.getCells().get("C11").putValue("INV-2024-001");
worksheet.getCells().get("B12").putValue("Date:");
worksheet.getCells().get("C12").putValue(new SimpleDateFormat("yyyy-MM-dd").format(new Date()));

// Bill-to section
worksheet.getCells().get("B14").putValue("Bill To:");
worksheet.getCells().get("B15").putValue("Client Name");
worksheet.getCells().get("B16").putValue("Client Address");
worksheet.getCells().get("B17").putValue("Client City, State");

// Line items header
Cell headerDesc = worksheet.getCells().get("B19");
Cell headerQty = worksheet.getCells().get("C19");
Cell headerPrice = worksheet.getCells().get("D19");
Cell headerTotal = worksheet.getCells().get("E19");

headerDesc.putValue("Description");
headerQty.putValue("Quantity");
headerPrice.putValue("Unit Price");
headerTotal.putValue("Total");

Style headerStyle = workbook.createStyle();
headerStyle.getFont().setBold(true);
headerStyle.getFont().setColor(Color.getWhite());
headerStyle.setBackgroundColor(Color.getNavy());
headerStyle.setHorizontalAlignment(TextAlignmentType.CENTER);
headerStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
headerStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
headerStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
headerStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);

headerDesc.setStyle(headerStyle);
headerQty.setStyle(headerStyle);
headerPrice.setStyle(headerStyle);
headerTotal.setStyle(headerStyle);

// Currency style with borders
Style currencyStyle = workbook.createStyle();
currencyStyle.setCustom("\"$\"#,##0.00");
currencyStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
currencyStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
currencyStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
currencyStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);

// Plain border style for description/quantity cells
Style borderStyle = workbook.createStyle();
borderStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
borderStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
borderStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
borderStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);

// Line items rows
Object[][] lineItems = new Object[][] {
    {"Product A - Widget", 2, 50.00},
    {"Product B - Gadget", 3, 75.00},
    {"Product C - Service", 1, 100.00}
};

for (int i = 0; i < lineItems.length; i++)
{
    int row = 20 + i;
    Cell descCell = worksheet.getCells().get(row, 1);
    Cell qtyCell = worksheet.getCells().get(row, 2);
    Cell priceCell = worksheet.getCells().get(row, 3);
    Cell totalCell = worksheet.getCells().get(row, 4);

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
Cell subtotalCell = worksheet.getCells().get("E24");
subtotalCell.setFormula("SUM(E20:E22)");

worksheet.getCells().get("B25").putValue("Tax (10%):");
Cell taxCell = worksheet.getCells().get("E25");
taxCell.setFormula("E24*0.1");

worksheet.getCells().get("B26").putValue("Grand Total:");
Cell grandTotalCell = worksheet.getCells().get("E26");
grandTotalCell.setFormula("E24+E25");

// Bold + currency style for total values
Style totalStyle = workbook.createStyle();
totalStyle.getFont().setBold(true);
totalStyle.setCustom("\"$\"#,##0.00");

subtotalCell.setStyle(totalStyle);
taxCell.setStyle(totalStyle);
grandTotalCell.setStyle(totalStyle);

// Bold style for total labels
Style boldStyle = workbook.createStyle();
boldStyle.getFont().setBold(true);

worksheet.getCells().get("B24").setStyle(boldStyle);
worksheet.getCells().get("B25").setStyle(boldStyle);
worksheet.getCells().get("B26").setStyle(boldStyle);

// Save the workbook as an OFD file
workbook.save(dataDir + "Invoice.ofd", SaveFormat.Ofd);
```
## **تحويل ملف Excel موجود إلى OFD**
يمكن لـ Aspose.Cells أيضًا تحميل مصنف Excel موجود من القرص وتصديره مباشرةً إلى تنسيق OFD. هذا مفيد لخطوط أنابيب التحويل المجمعة، وسير عمل الأرشفة، والسيناريوهات التي تم فيها إنتاج المصنف المصدر بواسطة أداة أخرى ويحتاج فقط إلى إعادة إصداره كقطعة أثرية ذات تخطيط ثابت. يقوم المثال التالي بتحميل مصنف `.xlsx` موجود، وقراءة البيانات من خلاياه، وتطبيق تعديلات إعداد الصفحة الاختيارية، وحفظ النتيجة كمستند OFD.

```java
import com.aspose.cells.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

String dataDir = "C:\\Examples\\";

// فتح مصنف Excel موجود من القرص
Workbook workbook = new Workbook(dataDir + "SampleBook.xlsx");

// (1) قراءة وعرض القيم من الخلايا المحددة لتأكيد تحميل الملف
Worksheet firstSheet = workbook.getWorksheets().get(0);
System.out.println("First sheet name: " + firstSheet.getName());
System.out.println("Cell A1: " + firstSheet.getCells().get("A1").getStringValue());
System.out.println("Cell B1: " + firstSheet.getCells().get("B1").getStringValue());
System.out.println("Cell C1: " + firstSheet.getCells().get("C1").getStringValue());

// (2) التكرار عبر مجموعة Worksheets لتعداد الأوراق المتاحة
System.out.println("\nAvailable worksheets:");
for (int i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    Worksheet ws = workbook.getWorksheets().get(i);
    System.out.println("  [" + i + "] " + ws.getName());
}

// (3) اختيارياً، تحديث خلية الطابع الزمني لتعكس التحويل
String timestamp1 = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
firstSheet.getCells().get("A1").putValue("Converted on: " + timestamp1);

// إلحاق صف رأس ملخص في أعلى كتلة البيانات
firstSheet.getCells().insertRow(0);
firstSheet.getCells().get("A1").putValue("Conversion Summary");

String timestamp2 = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
firstSheet.getCells().get("A2").putValue("Generated: " + timestamp2);

// (4) تكوين خصائص PageSetup في ورقة العمل
PageSetup pageSetup = firstSheet.getPageSetup();
pageSetup.setOrientation(PageOrientationType.LANDSCAPE);
pageSetup.setPaperSize(PaperSizeType.PAPER_A_4);
pageSetup.setFitToPagesTall(1);
pageSetup.setFitToPagesWide(1);

// (5) اختيارياً، تعيين منطقة الطباعة لمخرجات OFD
int lastRow = firstSheet.getCells().getMaxDataRow();
int lastCol = firstSheet.getCells().getMaxDataColumn();
String lastColLetter = CellsHelper.columnIndexToName(lastCol);
String printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.getPageSetup().setPrintArea(printArea);
System.out.println("\nPrint area set to: " + printArea);

// (6) حفظ المصنف كملف OFD
workbook.save(dataDir + "SampleBook.ofd", SaveFormat.Ofd);
System.out.println("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");
```

## **مقالات ذات صلة**
- [تقسيم ملفات Excel إلى ملفات متعددة](/cells/ar/java/splitting-excel-files-into-multiple-files/)
- [إدراج صورة في خلية](/cells/ar/java/inserting-an-image-into-a-cell/)
- [قراءة وكتابة ملفات DBF](/cells/ar/java/dbf/)
- [تحويل Sparkline إلى صورة وHTML في Aspose.Cells for Java](/cells/ar/java/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="java" >}}