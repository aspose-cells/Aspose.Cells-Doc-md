---
title: تحويل Excel إلى صيغة OFD
linktitle: تحويل Excel إلى صيغة OFD
description: Aspose.Cells for Python via Java هي مكتبة للعمل مع ملفات جداول البيانات تدعم تحويل مصنفات Excel إلى صيغة OFD (Open Fixed-layout Document). توضح هذه المقالة كيفية إنشاء محتوى Excel وتصديره بصيغة OFD، بالإضافة إلى كيفية تحويل ملفات Excel الموجودة إلى OFD باستخدام Aspose.Cells for Python via Java.
keywords: Aspose.Cells, Python via Java library, spreadsheet, Excel to OFD, OFD conversion, SaveFormat.Ofd, fixed-layout document, workbook export
type: docs
weight: 195
url: /ar/python-java/converting-excel-to-ofd-format/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

تدعم Aspose.Cells for Python via Java تحويل مصنفات Excel مباشرةً إلى صيغة OFD (Open Fixed-layout Document) باستخدام قيمة تعداد `SaveFormat.Ofd`. يحافظ مستند OFD الناتج على التخطيط المرئي للمصنف، ومحتواه، والخلايا المدمجة، وعرض الأعمدة، وارتفاع الصفوف، والخطوط، والألوان، والحدود، وصيغ الأرقام. هذا يجعل Aspose.Cells for Python via Java مناسبة للأرشفة، والطباعة، والإيداع التنظيمي، وسير عمل التقديمات الحكومية التي تتطلب مخرجات بتخطيط ثابت.

{{% /alert %}}
## **المقدمة**
OFD (Open Fixed-layout Document) هو معيار وطني صيني (GB/T 33190-2016) لتمثيل المستندات الرقمية بتخطيط ثابت قائم على الصفحات. يؤدي دورًا مشابهًا لـ PDF في حالات الاستخدام التي يجب فيها الحفاظ على المظهر المرئي للمستند المصدر تمامًا كما تمت تأليفه. يتم اعتماد OFD على نطاق واسع للتقديمات الحكومية، والإيداعات التنظيمية، والفواتير الإلكترونية، والأرشفة طويلة الأمد في جمهورية الصين الشعبية.

يُعد تحويل مصنفات Excel إلى OFD متطلبًا شائعًا في السيناريوهات التي يجب فيها توزيع محتوى جدول البيانات كمستند للقراءة فقط بتخطيط مقفل بدلاً من جدول بيانات قابل للتحرير. تتضمن الأمثلة شحن فاتورة نهائية إلى عميل، أو أرشفة تقرير مالي ربع سنوي، أو تقديم جدول بيانات ميزانية إلى جهة تنظيمية. تعالج Aspose.Cells for Python via Java هذا المتطلب من خلال قيمة تعداد `SaveFormat.Ofd`، التي تكتب المصنف مباشرةً إلى OFD دون الحاجة إلى خطوة تحويل وسيطة. يحافظ مخرج OFD على قيم الخلايا، والنطاقات المدمجة، والخطوط، والألوان، والحدود، وصيغ الأرقام، وخيارات إعداد الصفحة المكونة على المصنف.

{{% alert color="primary" %}}

يحافظ مخرج OFD الذي يولده Aspose.Cells for Python via Java على التخطيط المرئي للمصنف المصدر، بما في ذلك محتوى الخلايا، والخلايا المدمجة، وعرض الأعمدة، وارتفاع الصفوف. كما يتم عرض تنسيق الخلايا مثل الخطوط، والألوان، والحدود، والمحاذاة، وصيغ الأرقام في المخرج بتخطيط ثابت. تؤثر خيارات إعداد الصفحة المكونة على ورقة العمل، مثل حجم الورق، والاتجاه، ومنطقة الطباعة، على تخطيط مستند OFD الناتج.

{{% /alert %}}
## **إنشاء مصنف Excel وحفظه بصيغة OFD**
تتيح لك Aspose.Cells for Python via Java إنشاء مصنف برمجيًا، وتعبئته بالبيانات، ثم حفظه مباشرةً بصيغة OFD باستخدام تعداد `SaveFormat.Ofd`. يُنشئ المثال التالي فاتورة من الصفر. يضيف شعار الشركة، ومعلومات الرأس، وقسم "فاتورة إلى"، وعناصر البنود، والإجماليات المحسوبة، ثم يصدر المصنف إلى مستند OFD.
### **بناء فاتورة مع شعار**
يُنشئ المثال ورقة عمل الفاتورة عن طريق إدراج صورة شعار في المنطقة العلوية اليسرى، وتعبئة اسم الشركة وتفاصيل الاتصال، وإضافة عنوان "INVOICE" عبر الخلايا المدمجة، وتسجيل رقم الفاتورة وتاريخها، وذكر عميل "الفاتورة إلى"، وبناء جدول عناصر البنود بأعمدة الوصف، والكمية، وسعر الوحدة، والإجمالي، وحساب المجموع الفرعي، والضريبة، والإجمالي الكلي باستخدام صيغ الخلايا. يتم تطبيق التنسيق مثل العناوين الغامقة، وصيغة العملة للأسعار، والحدود، وعرض الأعمدة باستخدام كائنات `Style` و `Font`. أخيرًا، يتم حفظ المصنف بامتداد `.ofd` باستخدام `SaveFormat.Ofd`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, Style, Cell, TextAlignmentType, BorderType, CellBorderType, Color

dataDir = "/tmp/"

# إنشاء مصنف جديد
workbook = Workbook()

# الحصول على ورقة العمل الأولى
worksheet = workbook.getWorksheets().get(0)

# تعيين عرض الأعمدة
worksheet.getCells().setColumnWidth(0, 5)
worksheet.getCells().setColumnWidth(1, 35)
worksheet.getCells().setColumnWidth(2, 12)
worksheet.getCells().setColumnWidth(3, 15)
worksheet.getCells().setColumnWidth(4, 15)
worksheet.getCells().setColumnWidth(5, 5)

# إدراج شعار الشركة
worksheet.getPictures().add(1, 1, dataDir + "logo.png")

# اسم الشركة وتفاصيل الاتصال
worksheet.getCells().get("B3").putValue("Acme Corporation")
worksheet.getCells().get("B4").putValue("123 Business Street")
worksheet.getCells().get("B5").putValue("City, State 12345")
worksheet.getCells().get("B6").putValue("Phone: (555) 123-4567")

# عنوان الفاتورة - دمج الخلايا
worksheet.getCells().merge(7, 1, 2, 4)
titleCell = worksheet.getCells().get("B8")
titleCell.putValue("INVOICE")

titleStyle = workbook.createStyle()
titleStyle.getFont().setBold(True)
titleStyle.getFont().setSize(20)
titleStyle.setHorizontalAlignment(TextAlignmentType.CENTER)
titleCell.setStyle(titleStyle)

# رقم الفاتورة والتاريخ
worksheet.getCells().get("B11").putValue("Invoice Number:")
worksheet.getCells().get("C11").putValue("INV-2024-001")
worksheet.getCells().get("B12").putValue("Date:")
worksheet.getCells().get("C12").putValue(datetime.datetime.now().strftime("%Y-%m-%d"))

# قسم الفاتورة إلى
worksheet.getCells().get("B14").putValue("Bill To:")
worksheet.getCells().get("B15").putValue("Client Name")
worksheet.getCells().get("B16").putValue("Client Address")
worksheet.getCells().get("B17").putValue("Client City, State")

# رأس بنود الفاتورة
headerDesc = worksheet.getCells().get("B19")
headerQty = worksheet.getCells().get("C19")
headerPrice = worksheet.getCells().get("D19")
headerTotal = worksheet.getCells().get("E19")

headerDesc.putValue("Description")
headerQty.putValue("Quantity")
headerPrice.putValue("Unit Price")
headerTotal.putValue("Total")

headerStyle = workbook.createStyle()
headerStyle.getFont().setBold(True)
headerStyle.getFont().setColor(Color.getWhite())
headerStyle.setBackgroundColor(Color.getNavy())
headerStyle.setHorizontalAlignment(TextAlignmentType.CENTER)
headerStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
headerStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
headerStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
headerStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)

headerDesc.setStyle(headerStyle)
headerQty.setStyle(headerStyle)
headerPrice.setStyle(headerStyle)
headerTotal.setStyle(headerStyle)

# نمط العملة مع الحدود
currencyStyle = workbook.createStyle()
currencyStyle.setCustom("\"$\"#,##0.00")
currencyStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
currencyStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
currencyStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
currencyStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)

# نمط حدود بسيط لخلايا الوصف والكمية
borderStyle = workbook.createStyle()
borderStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
borderStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
borderStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
borderStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)

# صفوف بنود الفاتورة
lineItems = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
]

for i in range(len(lineItems)):
    row = 20 + i
    descCell = worksheet.getCells().get(row, 1)
    qtyCell = worksheet.getCells().get(row, 2)
    priceCell = worksheet.getCells().get(row, 3)
    totalCell = worksheet.getCells().get(row, 4)

    descCell.putValue(lineItems[i][0])
    qtyCell.putValue(lineItems[i][1])
    priceCell.putValue(lineItems[i][2])
    totalCell.setFormula("C" + str(row) + "*D" + str(row))

    descCell.setStyle(borderStyle)
    qtyCell.setStyle(borderStyle)
    priceCell.setStyle(currencyStyle)
    totalCell.setStyle(currencyStyle)

# المجموع الفرعي، الضريبة، الإجمالي الكلي
worksheet.getCells().get("B24").putValue("Subtotal:")
subtotalCell = worksheet.getCells().get("E24")
subtotalCell.setFormula("SUM(E20:E22)")

worksheet.getCells().get("B25").putValue("Tax (10%):")
taxCell = worksheet.getCells().get("E25")
taxCell.setFormula("E24*0.1")

worksheet.getCells().get("B26").putValue("Grand Total:")
grandTotalCell = worksheet.getCells().get("E26")
grandTotalCell.setFormula("E24+E25")

# نمط عريض + عملة لقيم الإجمالي
totalStyle = workbook.createStyle()
totalStyle.getFont().setBold(True)
totalStyle.setCustom("\"$\"#,##0.00")

subtotalCell.setStyle(totalStyle)
taxCell.setStyle(totalStyle)
grandTotalCell.setStyle(totalStyle)

# نمط عريض لتسميات الإجمالي
boldStyle = workbook.createStyle()
boldStyle.getFont().setBold(True)

worksheet.getCells().get("B24").setStyle(boldStyle)
worksheet.getCells().get("B25").setStyle(boldStyle)
worksheet.getCells().get("B26").setStyle(boldStyle)

# حفظ المصنف كملف OFD
workbook.save(dataDir + "Invoice.ofd", SaveFormat.Ofd)

jpype.shutdownJVM()
```
## **تحويل ملف Excel موجود إلى OFD**
يمكن لـ Aspose.Cells for Python via Java أيضًا تحميل مصنف Excel موجود من القرص وتصديره مباشرةً بصيغة OFD. هذا مفيد لخطوط أنابيب التحويل الدفعية، وسير عمل الأرشفة، والسيناريوهات التي تم فيها إنتاج المصنف المصدر بواسطة أداة أخرى ولا يحتاج إلا إلى إعادة إصداره كمستند بتخطيط ثابت. يُحمّل المثال التالي مصنف `.xlsx` موجودًا، ويقرأ البيانات من خلاياه، ويطبق تعديلات إعداد الصفحة الاختيارية، ويحفظ النتيجة كمستند OFD.

```python
from datetime import datetime
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PageOrientationType, PaperSizeType, CellsHelper

dataDir = "C:\\Examples\\"

# فتح مصنف Excel موجود من القرص
workbook = Workbook(dataDir + "SampleBook.xlsx")

# (1) قراءة وعرض القيم من الخلايا المحددة للتأكد من تحميل الملف
firstSheet = workbook.getWorksheets().get(0)
print("First sheet name: " + firstSheet.getName())
print("Cell A1: " + firstSheet.getCells().get("A1").getStringValue())
print("Cell B1: " + firstSheet.getCells().get("B1").getStringValue())
print("Cell C1: " + firstSheet.getCells().get("C1").getStringValue())

# (2) التكرار على مجموعة أوراق العمل لتعداد الأوراق المتاحة
print("\nAvailable worksheets:")
for i in range(workbook.getWorksheets().getCount()):
    ws = workbook.getWorksheets().get(i)
    print("  [" + str(i) + "] " + ws.getName())

# (3) اختيارياً: تحديث خلية الطابع الزمني لتعكس عملية التحويل
firstSheet.getCells().get("A1").putValue("Converted on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# إضافة صف رأس ملخص في أعلى كتلة البيانات
firstSheet.getCells().insertRow(0)
firstSheet.getCells().get("A1").putValue("Conversion Summary")
firstSheet.getCells().get("A2").putValue("Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# (4) تكوين خصائص إعداد الصفحة في ورقة العمل
pageSetup = firstSheet.getPageSetup()
pageSetup.setOrientation(PageOrientationType.LANDSCAPE)
pageSetup.setPaperSize(PaperSizeType.PAPER_A_4)
pageSetup.setFitToPagesTall(1)
pageSetup.setFitToPagesWide(1)

# (5) اختيارياً: تعيين منطقة الطباعة لمخرجات OFD
lastRow = firstSheet.getCells().getMaxDataRow()
lastCol = firstSheet.getCells().getMaxDataColumn()
lastColLetter = CellsHelper.columnIndexToName(lastCol)
printArea = "A1:" + lastColLetter + str(lastRow + 1)
firstSheet.getPageSetup().setPrintArea(printArea)
print("\nPrint area set to: " + printArea)

# (6) حفظ المصنف كملف OFD
workbook.save(dataDir + "SampleBook.ofd", SaveFormat.Ofd)
print("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd")

jpype.shutdownJVM()
```

## **مقالات ذات صلة**
- [تقسيم ملفات Excel إلى ملفات متعددة](/cells/ar/python-java/splitting-excel-files-into-multiple-files/)
- [إدراج صورة في خلية](/cells/ar/python-java/inserting-an-image-into-a-cell/)
- [قراءة وكتابة ملفات DBF](/cells/ar/python-java/dbf/)
- [تحويل Sparkline إلى صورة وHTML في Aspose.Cells for Python via Java](/cells/ar/python-java/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="python" >}}