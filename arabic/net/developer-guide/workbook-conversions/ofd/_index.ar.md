---
title: تحويل Excel إلى تنسيق OFD
linktitle: تحويل Excel إلى تنسيق OFD
description: Aspose.Cells هي مكتبة .NET للعمل مع ملفات جداول البيانات تدعم تحويل مصنفات Excel إلى تنسيق OFD (مستند التخطيط الثابت المفتوح). يوضح هذا المقال كيفية إنشاء محتوى Excel وتصديره كملف OFD، وكذلك كيفية تحويل ملفات Excel الموجودة إلى OFD باستخدام Aspose.Cells.
keywords: Aspose.Cells, مكتبة NET, جدول بيانات, Excel إلى OFD, تحويل OFD, SaveFormat.Ofd, مستند تخطيط ثابت, تصدير المصنف
type: docs
weight: 195
url: /ar/net/converting-excel-to-ofd-format/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells يدعم تحويل مصنفات Excel مباشرةً إلى تنسيق OFD (مستند التخطيط الثابت المفتوح) باستخدام قيمة التعداد `SaveFormat.Ofd`. يحافظ مستند OFD الناتج على التخطيط المرئي للمصنف، ومحتواه، والخلايا المدمجة، وعرض الأعمدة، وارتفاع الصفوف، والخطوط، والألوان، والحدود، وتنسيقات الأرقام. وهذا يجعل Aspose.Cells مناسبًا لأرشفة المستندات، والطباعة، والتقديمات التنظيمية، وسير عمل تقديم المستندات الحكومية التي تتطلب مخرجات ذات تخطيط ثابت.

{{% /alert %}}
## **مقدمة**
OFD (مستند التخطيط الثابت المفتوح) هو معيار صيني وطني (GB/T 33190-2016) لتمثيل المستندات الرقمية بتخطيط ثابت قائم على الصفحات. ويؤدي دورًا مشابهًا لـ PDF في حالات الاستخدام التي يجب فيها الحفاظ على المظهر المرئي للمستند المصدر تمامًا كما تم تأليفه. يُعتمد OFD على نطاق واسع في التقديمات الحكومية، والإيداعات التنظيمية، والفواتير الإلكترونية، والأرشفة طويلة الأمد في جمهورية الصين الشعبية.

يعد تحويل مصنفات Excel إلى OFD مطلبًا شائعًا في السيناريوهات التي يجب فيها توزيع محتوى جداول البيانات كقطعة ثابتة التخطيط للقراءة فقط بدلاً من جدول بيانات قابل للتحرير. تتضمن الأمثلة شحن فاتورة نهائية إلى العميل، أو أرشفة تقرير مالي ربع سنوي، أو تقديم جدول بيانات الميزانية إلى سلطة تنظيمية. تعالج Aspose.Cells هذا المتطلب من خلال قيمة التعداد `SaveFormat.Ofd`، التي تكتب المصنف مباشرةً بصيغة OFD دون الحاجة إلى خطوة تحويل وسيطة. يحافظ مخرج OFD على قيم الخلايا، والنطاقات المدمجة، والخطوط، والألوان، والحدود، وتنسيقات الأرقام، وخيارات إعداد الصفحة المُكوّنة على المصنف.

{{% alert color="primary" %}}

يحافظ مخرج OFD الذي تنتجه Aspose.Cells على التخطيط المرئي لمصنف المصدر، بما في ذلك محتوى الخلايا، والخلايا المدمجة، وعرض الأعمدة، وارتفاع الصفوف. كما يتم عرض تنسيقات الخلايا مثل الخطوط، والألوان، والحدود، والمحاذاة، وتنسيقات الأرقام في مخرج التخطيط الثابت. تؤثر خيارات إعداد الصفحة المُكوّنة على ورقة العمل، مثل حجم الورق، والاتجاه، ومنطقة الطباعة، على تخطيط مستند OFD الناتج.

{{% /alert %}}
## **إنشاء مصنف Excel وحفظه بصيغة OFD**
تتيح لك Aspose.Cells إنشاء مصنف برمجيًا، وملئه بالبيانات، ثم حفظه مباشرةً بتنسيق OFD باستخدام تعداد `SaveFormat.Ofd`. يُنشئ المثال التالي فاتورة من الصفر. يضيف شعار الشركة، ومعلومات الترويسة، وقسم الفوترة، وبنود الفاتورة، والإجماليات المحسوبة، ثم يُصدّر المصنف إلى مستند OFD.
### **بناء فاتورة بشعار**
يُنشئ المثال ورقة عمل الفاتورة عن طريق إدراج صورة الشعار في المنطقة العلوية اليسرى، وملء اسم الشركة وتفاصيل الاتصال، وإضافة عنوان "INVOICE" عبر الخلايا المدمجة، وتسجيل رقم الفاتورة وتاريخها، وإضافة العميل إلى قسم الفوترة، وبناء جدول بنود الفاتورة بأعمدة الوصف، والكمية، وسعر الوحدة، والإجمالي، وحساب الإجمالي الفرعي، والضريبة، والإجمالي الكلي باستخدام صيغ الخلايا. يتم تطبيق التنسيقات مثل العناوين الغامقة، وتنسيق العملة للأسعار، والحدود، وعرض الأعمدة باستخدام كائنات `Style` و`Font`. وأخيرًا، يتم حفظ المصنف بامتداد `.ofd` باستخدام `SaveFormat.Ofd`.

```csharp
using System;
using Aspose.Cells;
using System.Drawing;

string dataDir = "C:\\Temp\\";

// إنشاء مصنف جديد
Workbook workbook = new Workbook();

// الحصول على ورقة العمل الأولى
Worksheet worksheet = workbook.Worksheets[0];

// تعيين عرض الأعمدة
worksheet.Cells.SetColumnWidth(0, 5);
worksheet.Cells.SetColumnWidth(1, 35);
worksheet.Cells.SetColumnWidth(2, 12);
worksheet.Cells.SetColumnWidth(3, 15);
worksheet.Cells.SetColumnWidth(4, 15);
worksheet.Cells.SetColumnWidth(5, 5);

// إدراج شعار الشركة
worksheet.Pictures.Add(1, 1, dataDir + "logo.png");

// اسم الشركة وتفاصيل الاتصال
worksheet.Cells["B3"].PutValue("Acme Corporation");
worksheet.Cells["B4"].PutValue("123 Business Street");
worksheet.Cells["B5"].PutValue("City, State 12345");
worksheet.Cells["B6"].PutValue("Phone: (555) 123-4567");

// عنوان الفاتورة - دمج الخلايا
worksheet.Cells.Merge(7, 1, 2, 4);
Cell titleCell = worksheet.Cells["B8"];
titleCell.PutValue("INVOICE");

Style titleStyle = workbook.CreateStyle();
titleStyle.Font.IsBold = true;
titleStyle.Font.Size = 20;
titleStyle.HorizontalAlignment = TextAlignmentType.Center;
titleCell.SetStyle(titleStyle);

// رقم الفاتورة والتاريخ
worksheet.Cells["B11"].PutValue("Invoice Number:");
worksheet.Cells["C11"].PutValue("INV-2024-001");
worksheet.Cells["B12"].PutValue("Date:");
worksheet.Cells["C12"].PutValue(DateTime.Now.ToString("yyyy-MM-dd"));

// قسم الفوترة
worksheet.Cells["B14"].PutValue("Bill To:");
worksheet.Cells["B15"].PutValue("Client Name");
worksheet.Cells["B16"].PutValue("Client Address");
worksheet.Cells["B17"].PutValue("Client City, State");

// رأس عناصر الفاتورة
Cell headerDesc = worksheet.Cells["B19"];
Cell headerQty = worksheet.Cells["C19"];
Cell headerPrice = worksheet.Cells["D19"];
Cell headerTotal = worksheet.Cells["E19"];

headerDesc.PutValue("Description");
headerQty.PutValue("Quantity");
headerPrice.PutValue("Unit Price");
headerTotal.PutValue("Total");

Style headerStyle = workbook.CreateStyle();
headerStyle.Font.IsBold = true;
headerStyle.Font.Color = Color.White;
headerStyle.BackgroundColor = Color.Navy;
headerStyle.HorizontalAlignment = TextAlignmentType.Center;
headerStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;

headerDesc.SetStyle(headerStyle);
headerQty.SetStyle(headerStyle);
headerPrice.SetStyle(headerStyle);
headerTotal.SetStyle(headerStyle);

// نمط العملة مع الحدود
Style currencyStyle = workbook.CreateStyle();
currencyStyle.Custom = "\"$\"#,##0.00";
currencyStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;

// نمط حدود بسيط لخلايا الوصف والكمية
Style borderStyle = workbook.CreateStyle();
borderStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;

// صفوف عناصر الفاتورة
object[,] lineItems = new object[,] {
    {"Product A - Widget", 2, 50.00},
    {"Product B - Gadget", 3, 75.00},
    {"Product C - Service", 1, 100.00}
};

for (int i = 0; i < lineItems.GetLength(0); i++)
{
    int row = 20 + i;
    Cell descCell = worksheet.Cells[row, 1];
    Cell qtyCell = worksheet.Cells[row, 2];
    Cell priceCell = worksheet.Cells[row, 3];
    Cell totalCell = worksheet.Cells[row, 4];

    descCell.PutValue(lineItems[i, 0]);
    qtyCell.PutValue(lineItems[i, 1]);
    priceCell.PutValue(lineItems[i, 2]);
    totalCell.Formula = "C" + row + "*D" + row;

    descCell.SetStyle(borderStyle);
    qtyCell.SetStyle(borderStyle);
    priceCell.SetStyle(currencyStyle);
    totalCell.SetStyle(currencyStyle);
}

// المجموع الفرعي والضريبة والمجموع الكلي
worksheet.Cells["B24"].PutValue("Subtotal:");
Cell subtotalCell = worksheet.Cells["E24"];
subtotalCell.Formula = "SUM(E20:E22)";

worksheet.Cells["B25"].PutValue("Tax (10%):");
Cell taxCell = worksheet.Cells["E25"];
taxCell.Formula = "E24*0.1";

worksheet.Cells["B26"].PutValue("Grand Total:");
Cell grandTotalCell = worksheet.Cells["E26"];
grandTotalCell.Formula = "E24+E25";

// نمط غامق + عملة لقيم الإجماليات
Style totalStyle = workbook.CreateStyle();
totalStyle.Font.IsBold = true;
totalStyle.Custom = "\"$\"#,##0.00";

subtotalCell.SetStyle(totalStyle);
taxCell.SetStyle(totalStyle);
grandTotalCell.SetStyle(totalStyle);

// نمط غامق لتسميات الإجماليات
Style boldStyle = workbook.CreateStyle();
boldStyle.Font.IsBold = true;

worksheet.Cells["B24"].SetStyle(boldStyle);
worksheet.Cells["B25"].SetStyle(boldStyle);
worksheet.Cells["B26"].SetStyle(boldStyle);

// حفظ المصنف كملف OFD
workbook.Save(dataDir + "Invoice.ofd", SaveFormat.Ofd);
```
## **تحويل ملف Excel موجود إلى OFD**
يمكن لـ Aspose.Cells أيضًا تحميل مصنف Excel موجود من القرص وتصديره مباشرةً إلى تنسيق OFD. وهذا مفيد لخطوط أنابيب التحويل المجمعة، وسير عمل الأرشفة، والسيناريوهات التي تم فيها إنتاج مصنف المصدر بواسطة أداة أخرى ويحتاج فقط إلى إعادة إصداره كقطعة ثابتة التخطيط. يُحمّل المثال التالي مصنف `.xlsx` موجودًا، ويقرأ البيانات من خلاياه، ويُطبق تعديلات إعداد الصفحة الاختيارية، ويحفظ النتيجة كمستند OFD.

```csharp
using System;
using Aspose.Cells;

string dataDir = "C:\\Examples\\";

// فتح مصنف Excel موجود من القرص
Workbook workbook = new Workbook(dataDir + "SampleBook.xlsx");

// (1) قراءة وعرض القيم من الخلايا المحددة للتأكد من تحميل الملف
Worksheet firstSheet = workbook.Worksheets[0];
Console.WriteLine("First sheet name: " + firstSheet.Name);
Console.WriteLine("Cell A1: " + firstSheet.Cells["A1"].StringValue);
Console.WriteLine("Cell B1: " + firstSheet.Cells["B1"].StringValue);
Console.WriteLine("Cell C1: " + firstSheet.Cells["C1"].StringValue);

// (2) التكرار على مجموعة أوراق العمل لتعداد الأوراق المتاحة
Console.WriteLine("\nAvailable worksheets:");
for (int i = 0; i < workbook.Worksheets.Count; i++)
{
    Worksheet ws = workbook.Worksheets[i];
    Console.WriteLine("  [" + i + "] " + ws.Name);
}

// (3) اختيارياً تحديث خلية الطابع الزمني لتعكس عملية التحويل
firstSheet.Cells["A1"].PutValue("Converted on: " + DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss"));

// إدراج صف رأس ملخص في أعلى كتلة البيانات
firstSheet.Cells.InsertRow(0);
firstSheet.Cells["A1"].PutValue("Conversion Summary");
firstSheet.Cells["A2"].PutValue("Generated: " + DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss"));

// (4) تكوين خصائص PageSetup على ورقة العمل
PageSetup pageSetup = firstSheet.PageSetup;
pageSetup.Orientation = PageOrientationType.Landscape;
pageSetup.PaperSize = PaperSizeType.PaperA4;
pageSetup.FitToPagesTall = 1;
pageSetup.FitToPagesWide = 1;

// (5) اختيارياً تعيين منطقة الطباعة لمخرجات OFD
int lastRow = firstSheet.Cells.MaxDataRow;
int lastCol = firstSheet.Cells.MaxDataColumn;
string lastColLetter = CellsHelper.ColumnIndexToName(lastCol);
string printArea = "A1:" + lastColLetter + (lastRow + 1);
firstSheet.PageSetup.PrintArea = printArea;
Console.WriteLine("\nPrint area set to: " + printArea);

// (6) حفظ المصنف كملف OFD
workbook.Save(dataDir + "SampleBook.ofd", SaveFormat.Ofd);
Console.WriteLine("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd");
```

## **مقالات ذات صلة**
- [تقسيم ملفات Excel إلى ملفات متعددة](/cells/ar/net/splitting-excel-files-into-multiple-files/)
- [إدراج صورة في خلية](/cells/ar/net/inserting-an-image-into-a-cell/)
- [قراءة وكتابة ملفات DBF](/cells/ar/net/dbf/)
- [تحويل Sparkline إلى صورة وHTML في Aspose.Cells for .NET](/cells/ar/net/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="csharp" >}}