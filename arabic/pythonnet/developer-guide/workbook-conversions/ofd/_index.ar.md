---
title: تحويل Excel إلى تنسيق OFD
linktitle: تحويل Excel إلى تنسيق OFD
description: Aspose.Cells for Python عبر .NET هي مكتبة لمعالجة جداول البيانات تدعم تحويل مصنفات Excel إلى تنسيق OFD (المستند المفتوح ذو التخطيط الثابت). توضح هذه المقالة كيفية إنشاء محتوى Excel وتصديره بتنسيق OFD، وكذلك كيفية تحويل ملفات Excel الموجودة إلى OFD باستخدام Aspose.Cells.
keywords: Aspose.Cells, مكتبة Python عبر .NET, جدول بيانات, Excel إلى OFD, تحويل OFD, SaveFormat.OFD, مستند ذو تخطيط ثابت, تصدير مصنف
type: docs
weight: 195
url: /ar/python-net/converting-excel-to-ofd-format/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells تحويل مصنفات Excel مباشرةً إلى تنسيق OFD (المستند المفتوح ذو التخطيط الثابت) باستخدام قيمة التعداد `SaveFormat.OFD`. يحافظ مستند OFD الناتج على التخطيط المرئي للمصنف ومحتواه والخلايا المدمجة وعروض الأعمدة وارتفاعات الصفوف والخطوط والألوان والحدود وتنسيقات الأرقام. وهذا يجعل Aspose.Cells ملائمًا لعمليات الأرشفة والطباعة والإيداع لدى الهيئات التنظيمية وتقديم المستندات إلى الجهات الحكومية التي تتطلب إخراجًا ذا تخطيط ثابت.
{{% /alert %}}

## **Introduction**
OFD (المستند المفتوح ذو التخطيط الثابت) هو معيار وطني صيني (GB/T 33190-2016) لتمثيل المستندات الرقمية في تخطيط ثابت قائم على الصفحات. ويؤدي دورًا مشابهًا لدور PDF في حالات الاستخدام التي يجب فيها الحفاظ على المظهر المرئي للمستند المصدر بدقة كما تم إعداده. ويُستخدم OFD على نطاق واسع في تقديم المستندات الحكومية، والإيداع لدى الهيئات التنظيمية، والفواتير الإلكترونية، والأرشفة طويلة الأمد في جمهورية الصين الشعبية.
يعد تحويل مصنفات Excel إلى OFD متطلبًا شائعًا في السيناريوهات التي يجب فيها توزيع محتوى جدول البيانات كملف للقراءة فقط ومقفل التخطيط بدلاً من جدول بيانات قابل للتحرير. وتشمل الأمثلة إرسال فاتورة مكتملة إلى عميل، أو أرشفة تقرير مالي ربع سنوي، أو تقديم جدول بيانات الميزانية إلى جهة تنظيمية. تعالج Aspose.Cells هذا المتطلب من خلال قيمة التعداد `SaveFormat.OFD`، التي تكتب المصنف مباشرةً إلى OFD دون الحاجة إلى خطوة تحويل وسيطة. يحافظ إخراج OFD على قيم الخلايا والنطاقات المدمجة والخطوط والألوان والحدود وتنسيقات الأرقام وخيارات إعداد الصفحة التي تم تكوينها على المصنف.

{{% alert color="primary" %}}
يحافظ إخراج OFD الذي لإنشائه Aspose.Cells على التخطيط المرئي لمصنف المصدر، بما في ذلك محتوى الخلايا والخلايا المدمجة وعروض الأعمدة وارتفاعات الصفوف. كما تتمتع تنسيقات الخلايا مثل الخطوط والألوان والحدود والمحاذاة وتنسيقات الأرقام بالعرض في الإخراج ذي التخطيط الثابت. وتؤثر خيارات إعداد الصفحة التي تم تكوينها على ورقة العمل، مثل حجم الورق واتجاه الصفحة ومنطقة الطباعة، في تخطيط مستند OFD الناتج.
{{% /alert %}}

## **Creating an Excel Workbook and Saving as OFD**
يتيح Aspose.Cells لك إنشاء مصنف برمجيًا، وتعبئته بالبيانات، ثم حفظه مباشرةً بتنسيق OFD باستخدام قيمة التعداد `SaveFormat.OFD`. ينشئ المثال التالي فاتورة من الصفر. يضيف شعار الشركة ومعلومات الرأسية وقسم بيانات العميل المُحاسَب إليه وبنود الفاتورة والإجماليات المحسوبة، ثم يصدّر المصنف إلى مستند OFD.

### **Building an Invoice with a Logo**
ينشئ المثال ورقة عمل لفاتورة عن طريق إدراج صورة شعار في المنطقة العلوية اليسرى، وتعبئة اسم الشركة وبيانات الاتصال، وإضافة عنوان "INVOICE" في خلايا مدمجة، وتسجيل رقم الفاتورة وتاريخها، وسرد العميل المُحاسَب إليه، وإنشاء جدول لبنود الفاتورة يتضمن أعمدة الوصف والكمية وسعر الوحدة والإجمالي. يحسب المثال المجموع الفرعي والضريبة والإجمالي النهائي باستخدام صيغ الخلايا. ويطبق تنسيقات مثل العناوين الغامقة وتنسيق العملة للأسعار والحدود وعروض الأعمدة باستخدام كائنات `Style` و`Font`. وأخيرًا، يُحفظ المصنف بامتداد `.ofd` باستخدام `SaveFormat.OFD`.

```python
import aspose.cells as ac
from datetime import datetime
data_dir = "C:\\Temp\\"
# Create a new Workbook
workbook = ac.Workbook()
# Obtain the first worksheet
worksheet = workbook.worksheets[0]
# Set column widths
worksheet.cells.set_column_width(0, 5.0)
worksheet.cells.set_column_width(1, 35.0)
worksheet.cells.set_column_width(2, 12.0)
worksheet.cells.set_column_width(3, 15.0)
worksheet.cells.set_column_width(4, 15.0)
worksheet.cells.set_column_width(5, 5.0)
# Insert company logo
worksheet.pictures.add(1, 1, data_dir + "logo.png")
# Company name and contact details
worksheet.cells.get("B3").put_value("Acme Corporation")
worksheet.cells.get("B4").put_value("123 Business Street")
worksheet.cells.get("B5").put_value("City, State 12345")
worksheet.cells.get("B6").put_value("Phone: (555) 123-4567")
# INVOICE title - merge cells
worksheet.cells.merge(7, 1, 2, 4)
title_cell = worksheet.cells.get("B8")
title_cell.put_value("INVOICE")
title_style = workbook.create_style()
title_style.font.is_bold = True
title_style.font.size = 20
title_style.horizontal_alignment = ac.TextAlignmentType.CENTER
title_cell.set_style(title_style)
# Invoice number and date
worksheet.cells.get("B11").put_value("Invoice Number:")
worksheet.cells.get("C11").put_value("INV-2024-001")
worksheet.cells.get("B12").put_value("Date:")
worksheet.cells.get("C12").put_value(datetime.now().strftime("%Y-%m-%d"))
# Bill-to section
worksheet.cells.get("B14").put_value("Bill To:")
worksheet.cells.get("B15").put_value("Client Name")
worksheet.cells.get("B16").put_value("Client Address")
worksheet.cells.get("B17").put_value("Client City, State")
# Line items header
header_desc = worksheet.cells.get("B19")
header_qty = worksheet.cells.get("C19")
header_price = worksheet.cells.get("D19")
header_total = worksheet.cells.get("E19")
header_desc.put_value("Description")
header_qty.put_value("Quantity")
header_price.put_value("Unit Price")
header_total.put_value("Total")
header_style = workbook.create_style()
header_style.font.is_bold = True
header_style.font.color = drawing.Color.white
header_style.background_color = drawing.Color.navy
header_style.horizontal_alignment = ac.TextAlignmentType.CENTER
header_style.borders.get(ac.BorderType.TOP_BORDER).line_style = ac.CellBorderType.THIN
header_style.borders.get(ac.BorderType.BOTTOM_BORDER).line_style = ac.CellBorderType.THIN
header_style.borders.get(ac.BorderType.LEFT_BORDER).line_style = ac.CellBorderType.THIN
header_style.borders.get(ac.BorderType.RIGHT_BORDER).line_style = ac.CellBorderType.THIN
header_desc.set_style(header_style)
header_qty.set_style(header_style)
header_price.set_style(header_style)
header_total.set_style(header_style)
# Currency style with borders
currency_style = workbook.create_style()
currency_style.custom = "\"$\"#,##0.00"
currency_style.borders.get(ac.BorderType.TOP_BORDER).line_style = ac.CellBorderType.THIN
currency_style.borders.get(ac.BorderType.BOTTOM_BORDER).line_style = ac.CellBorderType.THIN
currency_style.borders.get(ac.BorderType.LEFT_BORDER).line_style = ac.CellBorderType.THIN
currency_style.borders.get(ac.BorderType.RIGHT_BORDER).line_style = ac.CellBorderType.THIN
# Plain border style for description/quantity cells
border_style = workbook.create_style()
border_style.borders.get(ac.BorderType.TOP_BORDER).line_style = ac.CellBorderType.THIN
border_style.borders.get(ac.BorderType.BOTTOM_BORDER).line_style = ac.CellBorderType.THIN
border_style.borders.get(ac.BorderType.LEFT_BORDER).line_style = ac.CellBorderType.THIN
border_style.borders.get(ac.BorderType.RIGHT_BORDER).line_style = ac.CellBorderType.THIN
# Line items rows
line_items = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
]
for i in range(len(line_items)):
    row = 20 + i
    desc_cell = worksheet.cells.get(row, 1)
    qty_cell = worksheet.cells.get(row, 2)
    price_cell = worksheet.cells.get(row, 3)
    total_cell = worksheet.cells.get(row, 4)
    desc_cell.put_value(line_items[i][0])
    qty_cell.put_value(line_items[i][1])
    price_cell.put_value(line_items[i][2])
    total_cell.formula = "C" + str(row) + "*D" + str(row)
    desc_cell.set_style(border_style)
    qty_cell.set_style(border_style)
    price_cell.set_style(currency_style)
    total_cell.set_style(currency_style)
# Subtotal, tax, grand total
worksheet.cells.get("B24").put_value("Subtotal:")
subtotal_cell = worksheet.cells.get("E24")
subtotal_cell.formula = "SUM(E20:E22)"
worksheet.cells.get("B25").put_value("Tax (10%):")
tax_cell = worksheet.cells.get("E25")
tax_cell.formula = "E24*0.1"
worksheet.cells.get("B26").put_value("Grand Total:")
grand_total_cell = worksheet.cells.get("E26")
grand_total_cell.formula = "E24+E25"
# Bold + currency style for total values
total_style = workbook.create_style()
total_style.font.is_bold = True
total_style.custom = "\"$\"#,##0.00"
subtotal_cell.set_style(total_style)
tax_cell.set_style(total_style)
grand_total_cell.set_style(total_style)
# Bold style for total labels
bold_style = workbook.create_style()
bold_style.font.is_bold = True
worksheet.cells.get("B24").set_style(bold_style)
worksheet.cells.get("B25").set_style(bold_style)
worksheet.cells.get("B26").set_style(bold_style)
# Save the workbook as an OFD file
workbook.save(data_dir + "Invoice.ofd", ac.SaveFormat.OFD)
```

## **Converting an Existing Excel File to OFD**
يمكن لـ Aspose.Cells أيضًا تحميل مصنف Excel موجود من القرص وتصديره مباشرةً بتنسيق OFD. وهذا مفيد في مسارات التحويل على دفعات وعمليات الأرشفة والسيناريوهات التي أُنشئ فيها مصنف المصدر بواسطة أداة أخرى ولا يلزم سوى إعادة إخراجه كملف ذي تخطيط ثابت. يحمّل المثال التالي مصنف `.xlsx` موجودًا، ويقرأ البيانات من خلاياه، ويطبق تعديلات اختيارية على إعداد الصفحة، ثم يحفظ النتيجة كمستند OFD.

```python
import aspose.cells as ac
from datetime import datetime
dataDir = "C:\\Examples\\"
# Open an existing Excel workbook from disk
workbook = ac.Workbook(dataDir + "SampleBook.xlsx")
# (1) Read and display values from selected cells to confirm the file was loaded
firstSheet = workbook.worksheets[0]
print("First sheet name: " + firstSheet.name)
print("Cell A1: " + firstSheet.cells.get("A1").string_value)
print("Cell B1: " + firstSheet.cells.get("B1").string_value)
print("Cell C1: " + firstSheet.cells.get("C1").string_value)
# (2) Iterate over the Worksheets collection to enumerate available sheets
print("\nAvailable worksheets:")
for i in range(len(workbook.worksheets)):
    ws = workbook.worksheets[i]
    print("  [" + str(i) + "] " + ws.name)
# (3) Optionally update a timestamp cell to reflect the conversion
firstSheet.cells.get("A1").put_value("Converted on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# Append a summary header row at the top of the data block
firstSheet.cells.insert_row(0)
firstSheet.cells.get("A1").put_value("Conversion Summary")
firstSheet.cells.get("A2").put_value("Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# (4) Configure PageSetup properties on the worksheet
pageSetup = firstSheet.page_setup
pageSetup.orientation = ac.PageOrientationType.LANDSCAPE
pageSetup.paper_size = ac.PaperSizeType.PAPER_A4
pageSetup.fit_to_pages_tall = 1
pageSetup.fit_to_pages_wide = 1
# (5) Optionally set the print area for the OFD output
lastRow = firstSheet.cells.max_data_row
lastCol = firstSheet.cells.max_data_column
lastColLetter = ac.CellsHelper.column_index_to_name(lastCol)
printArea = "A1:" + lastColLetter + str(lastRow + 1)
firstSheet.page_setup.print_area = printArea
print("\nPrint area set to: " + printArea)
# (6) Save the workbook as an OFD file
workbook.save(dataDir + "SampleBook.ofd", ac.SaveFormat.OFD)
print("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd")
```

## **Related Articles**
- [تقسيم ملفات Excel إلى ملفات متعددة](/cells/ar/python-net/splitting-excel-files-into-multiple-files/)
- [إدراج صورة في خلية](/cells/ar/python-net/inserting-an-image-into-a-cell/)
- [قراءة ملفات DBF وكتابتها](/cells/ar/python-net/dbf/)

{{< app/cells/assistant language="python-net" >}}