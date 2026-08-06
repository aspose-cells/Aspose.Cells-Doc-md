---
title: تعديل تخطيط حقل الصفحة في الجدول المحوري
linktitle: تعديل تخطيط حقل الصفحة في الجدول المحوري
description: تعلّم كيفية التحكم في تخطيط منطقة حقل الصفحة في الجدول المحوري باستخدام Aspose.Cells for Python via Java، بما في ذلك تعيين ترتيب العرض وعدد الالتفاف وترتيب الحقول لحقول الصفحة في أعلى الجدول المحوري.
keywords: Aspose.Cells for Python via Java, مكتبة Python Java, جدول بيانات, جدول محوري, حقل الصفحة, ترتيب حقل الصفحة, عدد التفاف حقل الصفحة, نقل حقل الصفحة
type: docs
weight: 191
url: /ar/python-java/change-page-field-layout/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
هذه المقالة هي امتداد لموضوع **إضافة حقل صفحة في الجدول المحوري**. توضح كيفية التحكم في تخطيط منطقة حقل الصفحة — وهي شريط عناصر تحكم التصفية الموجود في أعلى الجدول المحوري — بما في ذلك ترتيب العرض وعدد الالتفاف وإعادة ترتيب الحقول.
{{% /alert %}}
## **مقدمة**
يعرض الجدول المحوري في Microsoft Excel **منطقة حقل صفحة** مخصصة تقع فوق منطقة الصفوف/الأعمدة/البيانات في الجدول. تُعرض هذه المنطقة كشريط من عناصر تحكم القائمة المنسدلة للتصفية (واحد لكل حقل صفحة)، وهي التي ينقر عليها المستخدمون لتقسيم الجدول المحوري بحسب معايير مثل السنة أو المنطقة. يقوم Aspose.Cells for Python via Java بنمذجة هذه المنطقة من خلال مجموعة `pivot_table.page_fields` ويعرض ثلاث خصائص تتحكم في كيفية عرض الشريط بصرياً:
- `pivot_table.page_field_order` (قيمة من النوع `Aspose.Cells.PrintOrderType`) يحدد ما إذا كانت حقول الصفحة الإضافية ستوضع *بجانب* الحقول الموجودة أو *أسفل* منها.
- `pivot_table.page_field_wrap_count` يحدد عدد حقول الصفحة التي توضع في كل صف أو عمود قبل الالتفاف.
- `pivot_table.page_fields.move(curr_index, dest_index)` يعيد ترتيب حقول الصفحة دون تغيير وضع الترتيب.
تستعرض هذه المقالة ثلاثة أمثلة برمجية توضح كل عملية من هذه العمليات على مجموعة بيانات مشتركة، حتى تتمكن من مقارنة التخطيطات الناتجة جنباً إلى جنب.
## **بيانات المصدر**
تحمّل جميع الأمثلة الثلاثة أدناه صفوف بيانات المبيعات الثمانية هذه في ورقة عمل باسم `PivotData`. تحتوي البيانات على مرشحَين محتملَين لحقل الصفحة (`Year`، `Region`)، ومرشحاً واحداً لحقل الصف (`Fruit`)، ومقياساً واحداً (`Amount`)، مما يجعل شريط حقل الصفحة جديراً بالفحص.
يتم ملء جميع الصفوف الثمانية في كل مثال برمجي، وبنفس الترتيب، لذا لا تختلف بيانات المصدر أبداً بين السيناريوهات — فقط خصائص تخطيط حقل الصفحة هي التي تتغير.
## **المثال 1: من اليسار إلى اليمين ثم للأسفل (Over Then Down)**
في السيناريو الأول، نُكوّن حقلَي الصفحة (`Year`، `Region`) ليظهروا **جنباً إلى جنب في صف واحد** في أعلى الجدول المحوري. نخصص `Fruit` لمحور الصفوف، ونضع `Year` أولاً و`Region` ثانياً على محور الصفحة (يحدد ترتيب استدعاءات `add_field_to_area` مؤشر البداية)، ونضيف `Amount` (Sum) كحقل بيانات، ثم نعيّن `page_field_order` إلى `PrintOrderType.OVER_THEN_DOWN` مع `page_field_wrap_count = 2`. باستخدام `OVER_THEN_DOWN` وعدد التفاف قدره 2، يتم ترتيب حقلَي الصفحة أفقياً جنباً إلى جنب في صف واحد في أعلى الجدول المحوري، لذا يشغل الشريط صفاً واحداً بعرض اثنين.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, WorksheetCollection, Worksheet, Cells, PivotTableCollection, PivotTable, PivotFieldType, ConsolidationFunction, PrintOrderType

dataDir = "output"
if not os.path.exists(dataDir):
    os.makedirs(dataDir, exist_ok=True)

workbook = Workbook()
worksheets = workbook.getWorksheets()

pivotDataIdx = worksheets.add("PivotData")
pivotDataSheet = worksheets.get(pivotDataIdx)
pivotDataCells = pivotDataSheet.getCells()

# العناوين (الصف 0)
pivotDataCells.get(0, 0).putValue("Fruit")
pivotDataCells.get(0, 1).putValue("Year")
pivotDataCells.get(0, 2).putValue("Region")
pivotDataCells.get(0, 3).putValue("Amount")

# الصف 1: تفاح، 2022، شمال، 150
pivotDataCells.get(1, 0).putValue("Apple")
pivotDataCells.get(1, 1).putValue(2022)
pivotDataCells.get(1, 2).putValue("North")
pivotDataCells.get(1, 3).putValue(150)

# الصف 2: تفاح، 2023، شمال، 180
pivotDataCells.get(2, 0).putValue("Apple")
pivotDataCells.get(2, 1).putValue(2023)
pivotDataCells.get(2, 2).putValue("North")
pivotDataCells.get(2, 3).putValue(180)

# الصف 3: موز، 2022، جنوب، 120
pivotDataCells.get(3, 0).putValue("Banana")
pivotDataCells.get(3, 1).putValue(2022)
pivotDataCells.get(3, 2).putValue("South")
pivotDataCells.get(3, 3).putValue(120)

# الصف 4: موز، 2023، جنوب، 140
pivotDataCells.get(4, 0).putValue("Banana")
pivotDataCells.get(4, 1).putValue(2023)
pivotDataCells.get(4, 2).putValue("South")
pivotDataCells.get(4, 3).putValue(140)

# الصف 5: كرز، 2022، شرق، 200
pivotDataCells.get(5, 0).putValue("Cherry")
pivotDataCells.get(5, 1).putValue(2022)
pivotDataCells.get(5, 2).putValue("East")
pivotDataCells.get(5, 3).putValue(200)

# الصف 6: كرز، 2023، شرق، 220
pivotDataCells.get(6, 0).putValue("Cherry")
pivotDataCells.get(6, 1).putValue(2023)
pivotDataCells.get(6, 2).putValue("East")
pivotDataCells.get(6, 3).putValue(220)

# الصف 7: عنب، 2022، غرب، 90
pivotDataCells.get(7, 0).putValue("Grape")
pivotDataCells.get(7, 1).putValue(2022)
pivotDataCells.get(7, 2).putValue("West")
pivotDataCells.get(7, 3).putValue(90)

# الصف 8: عنب، 2023، غرب، 110
pivotDataCells.get(8, 0).putValue("Grape")
pivotDataCells.get(8, 1).putValue(2023)
pivotDataCells.get(8, 2).putValue("West")
pivotDataCells.get(8, 3).putValue(110)

# إضافة ورقة تقرير الجدول المحوري
pivotTableSheetIdx = worksheets.add("PivotTableReport")
pivotTableSheet = worksheets.get(pivotTableSheetIdx)
pivotTables = pivotTableSheet.getPivotTables()

# إنشاء جدول محوري مصدره PivotData!A1:D9 موضوع في A1 على PivotTableReport
pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1")
pivotTable = pivotTables.get(pivotIndex)

# إضافة الحقول
pivotTable.addFieldToArea(PivotFieldType.ROW, 0)   # الفاكهة
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1)  # السنة
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2)  # المنطقة
pivotTable.addFieldToArea(PivotFieldType.DATA, 3)  # المبلغ
pivotTable.getDataFields().get(0).setFunction(ConsolidationFunction.SUM)

# تكوين تخطيط منطقة حقل الصفحة: وضع حقول الصفحة أفقياً أولاً، والالتفاف بعد كل حقلين
pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN)
pivotTable.setPageFieldWrapCount(2)

# التحديث والحساب
pivotTable.calculateData()

# الحفظ
workbook.save(os.path.join(dataDir, "pageFieldLayout_overThenDown.xlsx"))

jpype.shutdownJVM()
```
## **المثال 2: من الأعلى إلى الأسفل ثم لليمين (Down Then Over)**
في هذا المثال، نضع `Fruit` على محور الصفوف، و`Year` و`Region` على محور الصفحة (مع `Year` أولاً)، و`Amount` (Sum) كحقل بيانات — تماماً كما في المثال 1. ثم نعيّن `page_field_order` إلى `PrintOrderType.DOWN_THEN_OVER` و`page_field_wrap_count` إلى `2`. باستخدام `DOWN_THEN_OVER` وعدد تفاف قدره 2، يتم تكديس حقلَي الصفحة عمودياً — `Year` في الأعلى، و`Region` تحته مباشرة — مشكلَين عموداً واحداً في أعلى الجدول المحوري. وبالتالي يشغل الشريط صفَين بعرض واحد، على عكس المثال 1.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType, PrintOrderType

workbook = Workbook()
pivotData = workbook.getWorksheets().get(0)
pivotData.setName("PivotData")
pivotReportIdx = workbook.getWorksheets().add("PivotTableReport")
pivotReport = workbook.getWorksheets().get(pivotReportIdx)

headers = ["Fruit", "Year", "Region", "Amount"]
for c in range(len(headers)):
    pivotData.getCells().get(0, c).putValue(headers[c])

data = [
    ["Apple", 2022, "North", 150],
    ["Apple", 2023, "North", 180],
    ["Banana", 2022, "South", 120],
    ["Banana", 2023, "South", 140],
    ["Cherry", 2022, "East", 200],
    ["Cherry", 2023, "East", 220],
    ["Grape", 2022, "West", 90],
    ["Grape", 2023, "West", 110]
]

for r in range(len(data)):
    for c in range(len(data[r])):
        pivotData.getCells().get(r + 1, c).putValue(data[r][c])

idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable")
pivotTable = pivotReport.getPivotTables().get(idx)

pivotTable.addFieldToArea(PivotFieldType.ROW, 0)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2)
pivotTable.addFieldToArea(PivotFieldType.DATA, 3)

pivotTable.setPageFieldOrder(PrintOrderType.DOWN_THEN_OVER)
pivotTable.setPageFieldWrapCount(2)

pivotTable.calculateData()

workbook.save("pageFieldLayout_downThenOver.xlsx")

jpype.shutdownJVM()
```
## **المثال 3: نقل حقل صفحة**
في السيناريو الثالث، نحتفظ بمجموعة البيانات وتخصيص الحقول هذا، ونعيّن تخطيطاً محايداً (`OVER_THEN_DOWN` مع عدد تفاف `2`)، ثم نوضح عملية `page_fields.move`. ينقل استدعاء `move(0, 1)` حقل الصفحة عند المؤشر 0 (`Year`) إلى الموضع 1، وحقل الصفحة الذي كان في الموضع 1 (`Region`) ينتقل إلى الموضع 0. بعد هذا الاستدعاء، يصبح `Region` هو حقل الصفحة الأول و`Year` هو الثاني. يظل وضع الالتفاف والترتيب بدون تغيير، لذا يُعرض الشريط أفقياً جنباً إلى جنب — فقط ترتيب القائمتَين المنسدلتَين قد تبدّل.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType, PrintOrderType

workbook = Workbook()

dataSheet = workbook.getWorksheets().get(0)
dataSheet.setName("PivotData")

dataSheet.getCells().get("A1").putValue("Fruit")
dataSheet.getCells().get("B1").putValue("Year")
dataSheet.getCells().get("C1").putValue("Region")
dataSheet.getCells().get("D1").putValue("Amount")

dataSheet.getCells().get("A2").putValue("Apple")
dataSheet.getCells().get("B2").putValue(2022)
dataSheet.getCells().get("C2").putValue("North")
dataSheet.getCells().get("D2").putValue(150)

dataSheet.getCells().get("A3").putValue("Apple")
dataSheet.getCells().get("B3").putValue(2023)
dataSheet.getCells().get("C3").putValue("North")
dataSheet.getCells().get("D3").putValue(180)

dataSheet.getCells().get("A4").putValue("Banana")
dataSheet.getCells().get("B4").putValue(2022)
dataSheet.getCells().get("C4").putValue("South")
dataSheet.getCells().get("D4").putValue(120)

dataSheet.getCells().get("A5").putValue("Banana")
dataSheet.getCells().get("B5").putValue(2023)
dataSheet.getCells().get("C5").putValue("South")
dataSheet.getCells().get("D5").putValue(140)

dataSheet.getCells().get("A6").putValue("Cherry")
dataSheet.getCells().get("B6").putValue(2022)
dataSheet.getCells().get("C6").putValue("East")
dataSheet.getCells().get("D6").putValue(200)

dataSheet.getCells().get("A7").putValue("Cherry")
dataSheet.getCells().get("B7").putValue(2023)
dataSheet.getCells().get("C7").putValue("East")
dataSheet.getCells().get("D7").putValue(220)

dataSheet.getCells().get("A8").putValue("Grape")
dataSheet.getCells().get("B8").putValue(2022)
dataSheet.getCells().get("C8").putValue("West")
dataSheet.getCells().get("D8").putValue(90)

dataSheet.getCells().get("A9").putValue("Grape")
dataSheet.getCells().get("B9").putValue(2023)
dataSheet.getCells().get("C9").putValue("West")
dataSheet.getCells().get("D9").putValue(110)

pivotSheetIdx = workbook.getWorksheets().add("PivotTableReport")
pivotSheet = workbook.getWorksheets().get(pivotSheetIdx)

pivotIdx = pivotSheet.getPivotTables().add("PivotData!A1:D9", "A3", "PivotTable")
pivotTable = pivotSheet.getPivotTables().get(pivotIdx)

pivotTable.addFieldToArea(PivotFieldType.ROW, 0)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2)
pivotTable.addFieldToArea(PivotFieldType.DATA, 3)

pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN)
pivotTable.setPageFieldWrapCount(2)

pivotTable.getPageFields().move(0, 1)

pivotTable.calculateData()

workbook.save("pageFieldLayout_move.xlsx")

jpype.shutdownJVM()
```
## **مقالات ذات صلة**
- [إضافة حقل صفحة في الجدول المحوري](/cells/ar/python-java/add-page-field-in-pivot-table/) — الصفحة الأصلية التي توضح كيفية إضافة حقول الصفحة إلى الجدول المحوري.
- [حقول الصفوف والأعمدة في الجدول المحوري](/cells/ar/python-java/row-and-column-fields/) — يغطي تخصيص الحقول لمحورَي الصفوف والأعمدة، مما يكمل العمل على محور الصفحة الموضح هنا.
- [إدارة حقول القيم في الجدول المحوري](/cells/ar/python-java/manage-value-fields/) — يصف كيفية تكوين منطقة البيانات (القيم)، بما في ذلك تجميع `SUM` المستخدم في هذه المقالة.
- [تحديث الجدول المحوري](/cells/ar/python-java/refresh-pivot-table/) — يوضح `refresh_data` و`calculate_data`، المطلوبَين بعد إعادة ترتيب حقول الصفحة.
- [تطبيق نمط على الجدول المحوري](/cells/ar/python-java/apply-style-to-pivot-table/) — يوضح كيفية تنسيق الجدول المحوري المعروض بعد وضع شريط حقل الصفحة.
{{< app/cells/assistant language="python" >}}