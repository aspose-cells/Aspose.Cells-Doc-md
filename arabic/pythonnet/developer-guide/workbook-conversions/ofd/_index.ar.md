---
title: تحويل Excel إلى تنسيق OFD
linktitle: تحويل Excel إلى تنسيق OFD
description: Aspose.Cells for Python via .NET هي مكتبة لمعالجة جداول البيانات تدعم تحويل مصنفات Excel إلى تنسيق OFD (Open Fixed-layout Document). يوضح هذا المقال كيفية إنشاء محتوى Excel وتصديره كملف OFD، بالإضافة إلى كيفية تحويل ملفات Excel الموجودة إلى OFD باستخدام Aspose.Cells.
keywords: Aspose.Cells, مكتبة Python عبر .NET, جدول بيانات, Excel إلى OFD, تحويل OFD, SaveFormat.Ofd, مستند تخطيط ثابت, تصدير مصنف
type: docs
weight: 195
url: /ar/python-net/converting-excel-to-ofd-format/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

يدعم Aspose.Cells تحويل مصنفات Excel مباشرة إلى تنسيق OFD (Open Fixed-layout Document) باستخدام قيمة التعداد `SaveFormat.Ofd`. يحافظ مستند OFD الناتج على التخطيط المرئي للمصنف، والمحتوى، والخلايا المدمجة، وعرض الأعمدة، وارتفاع الصفوف، والخطوط، والألوان، والحدود، وتنسيقات الأرقام. هذا يجعل Aspose.Cells مناسبًا لسير عمل الأرشفة، والطباعة، والإيداع التنظيمي، والتقديمات الحكومية التي تتطلب إخراجًا بتخطيط ثابت.

{{% /alert %}}
## **المقدمة**
OFD (Open Fixed-layout Document) هو معيار وطني صيني (GB/T 33190-2016) لتمثيل المستندات الرقمية بتخطيط ثابت قائم على الصفحات. يؤدي دورًا مشابهًا لـ PDF في حالات الاستخدام التي يجب فيها الحفاظ على المظهر المرئي للمستند المصدر تمامًا كما تم تأليفه. يُعتمد OFD على نطاق واسع للتقديمات الحكومية، والإيداعات التنظيمية، والفواتير الإلكترونية، والأرشفة طويلة الأمد في جمهورية الصين الشعبية.

يعد تحويل مصنفات Excel إلى OFD متطلبًا شائعًا في السيناريوهات التي يجب فيها توزيع محتوى جدول البيانات كقطعة ثابتة التخطيط للقراءة فقط بدلاً من جدول بيانات قابل للتحرير. تشمل الأمثلة شحن فاتورة نهائية إلى عميل، أو أرشفة تقرير مالي ربع سنوي، أو تقديم جدول بيانات ميزانية إلى جهة تنظيمية. يعالج Aspose.Cells هذا المتطلب من خلال قيمة التعداد `SaveFormat.Ofd`، التي تكتب المصنف مباشرة إلى OFD دون الحاجة إلى خطوة تحويل وسيطة. يحافظ إخراج OFD على قيم الخلايا، والنطاقات المدمجة، والخطوط، والألوان، والحدود، وتنسيقات الأرقام، وخيارات إعداد الصفحة التي تم تكوينها على المصنف.

{{% alert color="primary" %}}

يحافظ إخراج OFD الذي تم إنشاؤه بواسطة Aspose.Cells على التخطيط المرئي للمصنف المصدر، بما في ذلك محتوى الخلايا، والخلايا المدمجة، وعرض الأعمدة، وارتفاع الصفوف. يتم أيضًا عرض تنسيق الخلايا مثل الخطوط، والألوان، والحدود، والمحاذاة، وتنسيقات الأرقام في الإخراج بتخطيط ثابت. تؤثر خيارات إعداد الصفحة التي تم تكوينها على ورقة العمل، مثل حجم الورق، والاتجاه، ومنطقة الطباعة، على تخطيط مستند OFD الناتج.

{{% /alert %}}
## **إنشاء مصنف Excel وحفظه بتنسيق OFD**
يتيح لك Aspose.Cells إنشاء مصنف برمجيًا، وملئه بالبيانات، ثم حفظه مباشرة بتنسيق OFD باستخدام تعداد `SaveFormat.Ofd`. يُنشئ المثال التالي فاتورة من الصفر. يضيف شعار الشركة، ومعلومات الرأس، وقسم الفواتير، وعناصر السطر، والإجماليات المحسوبة، ثم يصدر المصنف إلى مستند OFD.
### **بناء فاتورة بشعار**
ينشئ المثال ورقة عمل فاتورة عن طريق إدراج صورة شعار في المنطقة العلوية اليسرى، وملء اسم الشركة وتفاصيل الاتصال، وإضافة عنوان "INVOICE" عبر الخلايا المدمجة، وتسجيل رقم الفاتورة وتاريخها، وسرد عميل الفواتير، وبناء جدول عناصر السطر بأعمدة الوصف، والكمية، وسعر الوحدة، والإجمالي، وحساب المجموع الفرعي، والضريبة، والإجمالي الكلي باستخدام صيغ الخلايا. يتم تطبيق التنسيق مثل العناوين الغامقة، وتنسيق العملة للأسعار، والحدود، وعرض الأعمدة باستخدام كائنات `Style` و `Font`. أخيرًا، يتم حفظ المصنف بامتداد `.ofd` باستخدام `SaveFormat.Ofd`.

```python
from datetime import datetime

data_dir = "C:\\Temp\\"

# إنشاء مصنف جديد
workbook = ac.Workbook()

# الحصول على ورقة العمل الأولى
worksheet = workbook.worksheets[0]

# تعيين عرض الأعمدة
worksheet.cells.set_column_width(0, 5)
worksheet.cells.set_column_width(1, 35)
worksheet.cells.set_column_width(2, 12)
worksheet.cells.set_column_width(3, 15)
worksheet.cells.set_column_width(4, 15)
worksheet.cells.set_column_width(5, 5)

# إدراج شعار الشركة
worksheet.pictures.add(1, 1, data_dir + "logo.png")

# اسم الشركة وتفاصيل الاتصال
worksheet.cells["B3"].put_value("Acme Corporation")
worksheet.cells["B4"].put_value("123 Business Street")
worksheet.cells["B5"].put_value("City, State 12345")
worksheet.cells["B6"].put_value("Phone: (555) 123-4567")

# عنوان الفاتورة - دمج الخلايا
worksheet.cells.merge(7, 1, 2, 4)
title_cell = worksheet.cells["B8"]
title_cell.put_value("INVOICE")

title_style = workbook.create_style()
title_style.font.is_bold = True
title_style.font.size = 20
title_style.horizontal_alignment = ac.TextAlignmentType.CENTER
title_cell.set_style(title_style)

# رقم الفاتورة والتاريخ
worksheet.cells["B11"].put_value("Invoice Number:")
worksheet.cells["C11"].put_value("INV-2024-001")
worksheet.cells["B12"].put_value("Date:")
worksheet.cells["C12"].put_value(datetime.now().strftime("%Y-%m-%d"))

# قسم الفاتورة إلى
worksheet.cells["B14"].put_value("Bill To:")
worksheet.cells["B15"].put_value("Client Name")
worksheet.cells["B16"].put_value("Client Address")
worksheet.cells["B17"].put_value("Client City, State")

# رأس عناصر الفاتورة
header_desc = worksheet.cells["B19"]
header_qty = worksheet.cells["C19"]
header_price = worksheet.cells["D19"]
header_total = worksheet.cells["E19"]

header_desc.put_value("Description")
header_qty.put_value("Quantity")
header_price.put_value("Unit Price")
header_total.put_value("Total")

header_style = workbook.create_style()
header_style.font.is_bold = True
header_style.font.color = drawing.Color.white
header_style.background_color = drawing.Color.navy
header_style.horizontal_alignment = ac.TextAlignmentType.CENTER
header_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
header_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
header_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
header_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN

header_desc.set_style(header_style)
header_qty.set_style(header_style)
header_price.set_style(header_style)
header_total.set_style(header_style)

# نمط العملة مع الحدود
currency_style = workbook.create_style()
currency_style.custom = "\"$\"#,##0.00"
currency_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
currency_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
currency_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
currency_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN

# نمط حدود عادي لخلايا الوصف/الكمية
border_style = workbook.create_style()
border_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
border_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
border_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
border_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN

# صفوف عناصر الفاتورة
line_items = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
]

for i in range(len(line_items)):
    row = 20 + i
    desc_cell = worksheet.cells[row, 1]
    qty_cell = worksheet.cells[row, 2]
    price_cell = worksheet.cells[row, 3]
    total_cell = worksheet.cells[row, 4]

    desc_cell.put_value(line_items[i][0])
    qty_cell.put_value(line_items[i][1])
    price_cell.put_value(line_items[i][2])
    total_cell.formula = "C" + str(row) + "*D" + str(row)

    desc_cell.set_style(border_style)
    qty_cell.set_style(border_style)
    price_cell.set_style(currency_style)
    total_cell.set_style(currency_style)

# المجموع الفرعي، الضريبة، المجموع الكلي
worksheet.cells["B24"].put_value("Subtotal:")
subtotal_cell = worksheet.cells["E24"]
subtotal_cell.formula = "SUM(E20:E22)"

worksheet.cells["B25"].put_value("Tax (10%):")
tax_cell = worksheet.cells["E25"]
tax_cell.formula = "E24*0.1"

worksheet.cells["B26"].put_value("Grand Total:")
grand_total_cell = worksheet.cells["E26"]
grand_total_cell.formula = "E24+E25"

# نمط غامق + عملة لقيم الإجمالي
total_style = workbook.create_style()
total_style.font.is_bold = True
total_style.custom = "\"$\"#,##0.00"

subtotal_cell.set_style(total_style)
tax_cell.set_style(total_style)
grand_total_cell.set_style(total_style)

# نمط غامق لتسميات الإجمالي
bold_style = workbook.create_style()
bold_style.font.is_bold = True

worksheet.cells["B24"].set_style(bold_style)
worksheet.cells["B25"].set_style(bold_style)
worksheet.cells["B26"].set_style(bold_style)

# حفظ المصنف كملف OFD
workbook.save(data_dir + "Invoice.ofd", ac.SaveFormat.Ofd)
```
## **تحويل ملف Excel موجود إلى OFD**
يمكن لـ Aspose.Cells أيضًا تحميل مصنف Excel موجود من القرص وتصديره مباشرة إلى تنسيق OFD. هذا مفيد لخطوط أنابيب التحويل الدفعية، وسير عمل الأرشفة، والسيناريوهات التي تم فيها إنتاج المصنف المصدر بواسطة أداة أخرى ولا يحتاج إلا إلى إعادة إصداره كقطعة ثابتة التخطيط. يحمّل المثال التالي مصنف `.xlsx` موجودًا، ويقرأ البيانات من خلاياه، ويطبق تعديلات إعداد الصفحة الاختيارية، ويحفظ النتيجة كمستند OFD.

```python
from datetime import datetime

dataDir = "C:\\Examples\\"

# افتح مصنف Excel موجود من القرص
workbook = ac.Workbook(dataDir + "SampleBook.xlsx")

# (1) قراءة وعرض القيم من الخلايا المحددة للتأكد من تحميل الملف
firstSheet = workbook.worksheets[0]
print("First sheet name: " + firstSheet.name)
print("Cell A1: " + firstSheet.cells["A1"].string_value)
print("Cell B1: " + firstSheet.cells["B1"].string_value)
print("Cell C1: " + firstSheet.cells["C1"].string_value)

# (2) التكرار عبر مجموعة أوراق العمل لتعداد الأوراق المتاحة
print("\nAvailable worksheets:")
for i in range(workbook.worksheets.count):
    ws = workbook.worksheets[i]
    print("  [" + str(i) + "] " + ws.name)

# (3) اختيارياً، قم بتحديث خلية الطابع الزمني لتعكس التحويل
firstSheet.cells["A1"].put_value("Converted on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# إلحاق صف رأس ملخص في أعلى كتلة البيانات
firstSheet.cells.insert_row(0)
firstSheet.cells["A1"].put_value("Conversion Summary")
firstSheet.cells["A2"].put_value("Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# (4) تكوين خصائص PageSetup على ورقة العمل
pageSetup = firstSheet.page_setup
pageSetup.orientation = ac.PageOrientationType.LANDSCAPE
pageSetup.paper_size = ac.PaperSizeType.PAPER_A4
pageSetup.fit_to_pages_tall = 1
pageSetup.fit_to_pages_wide = 1

# (5) اختيارياً، قم بتعيين منطقة الطباعة لمخرجات OFD
lastRow = firstSheet.cells.max_data_row
lastCol = firstSheet.cells.max_data_column
lastColLetter = ac.CellsHelper.column_index_to_name(lastCol)
printArea = "A1:" + lastColLetter + str(lastRow + 1)
firstSheet.page_setup.print_area = printArea
print("\nPrint area set to: " + printArea)

# (6) حفظ المصنف كملف OFD
workbook.save(dataDir + "SampleBook.ofd", ac.SaveFormat.Ofd)
print("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd")
```

## **مقالات ذات صلة**
- [Splitting Excel Files into Multiple Files](/cells/ar/python-net/splitting-excel-files-into-multiple-files/)
- [Inserting an Image into a Cell](/cells/ar/python-net/inserting-an-image-into-a-cell/)
- [Reading and Writing DBF Files](/cells/ar/python-net/dbf/)
- [Convert Sparkline to Image and HTML in Aspose.Cells for Python via .NET](/cells/ar/python-net/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="python" >}}