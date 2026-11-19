---
title: العلامات الذكية في رؤوس وتذييلات الصفحات | Aspose.Cells for Python via Java
linktitle: علامات ذكية في الرأس والتذييل | Aspose.Cells
description: ضع علامات ذكية في رؤوس وتذييلات الصفحات باستخدام صيغة القوسين المزدوجين وتبديل WorkbookDesigner.setEnableHeaderFooterMarkers باستخدام مصادر بيانات صفية جدولة أو JSON، واربط الصور عبر عناوين URI للبيانات، في Aspose.Cells for Python via Java.
keywords: Aspose.Cells, Aspose.Cells for Python via Java, العلامات الذكية, رؤوس, تذييلات, علامات الرأس والتذييل, setEnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, setHeader, setFooter, setJsonDataSource, ICellsDataTable, جدول بيانات مخصص, ربط البيانات, صورة, URI للبيانات, Python via Java
type: docs
weight: 196
url: /ar/python-java/smart-markers-in-headers-and-footers/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
غالبًا ما تحتوي رؤوس وتذييلات الصفحات على بيانات تعريفية للتقرير مثل عنوان التقرير، فترة التقرير، المؤلف، والقسم. عندما تكون هذه المعلومات موجودة بالفعل في مصدر البيانات المستخدم لملء المصنف، فإن تكرارها يدويًا يخلق تكرارًا غير ضروري.
صيغة العلامة الذكية الكلاسيكية، `&=Source.Field`، يتم معالجتها في خلايا جسم ورقة العمل. إذا وضعت علامةً كلاسيكيةً في رأس أو تذييل عبر `PageSetup.setHeader` أو `PageSetup.setFooter`، سيبقى نصًا حرفيًا لأن سلاسل الرأس والتذييل ليست جزءًا من شبكة خلايا ورقة العمل التي يفحصها `WorkbookDesigner.process()`.
بدءًا من **Aspose.Cells for Python via Java 26.11**، يجعل التبديل `WorkbookDesigner.setEnableHeaderFooterMarkers`، وهو `False` افتراضيًا، عملية `process()` تحلّ العلامات المكتوبة كـ `<<Source.Field>>` في سلاسل أقسام الرأس والتذييل — اضبطه على `True` قبل استدعاء `process()`. تستخدم علامات الرأس والتذييل نفس مصدر البيانات مثل علامات الجسم.
كل رأس وتذييل يحتوي على ثلاث أقسام يمكن العنونة إليها:
- القسم `0` هو القسم الأيسر.
- القسم `1` هو القسم الأوسط.
- القسم `2` هو القسم الأيمن.
استخدم `PageSetup.setHeader(int section, str value)` و `PageSetup.setFooter(int section, str value)` لكتابة هذه الأقسام. بعد المعالجة، استخدم `PageSetup.getHeader(int section)` و `PageSetup.getFooter(int section)` لاسترداد النص المكتمل.

{{% alert color="primary" %}}
علامة مكانية مثل `<<Source.Field>>` تُدرج قيمة الحقل كنص داخل سلسلة القسم. يتم ربط الصور باستخدام اللاحقة `(picture)` وقيمة URI للبيانات.
{{% /alert %}}

## **تمكين علامات الرأس/التذييل باستخدام جدول بيانات مخصص**
استخدم التسلسل التالي لحل علامات الرأس والتذييل باستخدام مصدر بيانات جدولي مخصص في **Aspose.Cells for Python via Java 26.11**:
1. أنشئ كائن `Workbook` واحصل على أول `Worksheet` له عند الفهرس `0` باستخدام `workbook.getWorksheets().get(0)`.
2. اكتب علامات `<<Source.Field>>` في أقسام الرأس والتذييل المطلوبة باستخدام `worksheet.getPageSetup().setHeader(section, value)` و `worksheet.getPageSetup().setFooter(section, value)`.
3. عرّف فئة صغيرة تُنفّذ `ICellsDataTable` لتوفير بيانات الصف الجدولي — أسماء الأعمدة، عدد الصفوف، ومؤشر مع `beforeFirst()`, `next()`, و `get()` — واستخدم اسم مصدر يطابق البادئة المستخدمة في العلامات. على سبيل المثال، مصدر باسم `node` يدعم علامات مثل `<<node.Name>>`. فئة بايثون عادية أو قائمة من القواميس لا تُربط في هذه المنصة؛ تنفيذ `ICellsDataTable` هو مصدر البيانات المخصص.
4. أنشئ كائن `WorkbookDesigner` للمصنف.
5. استدعِ `designer.setEnableHeaderFooterMarkers(True)` قبل المعالجة.
6. أرفق الجدول واسم المصدر باستخدام `designer.setDataSource("node", table)`.
7. استدعِ `designer.process()`.
8. بعد المعالجة، لا تعود العلامات موجودة في نص الرأس أو التذييل. استخدم `worksheet.getPageSetup().getHeader(section)` و `worksheet.getPageSetup().getFooter(section)` لاسترداد سلاسل الأقسام المكتملة.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    WorkbookDesigner,
    ICellsDataTable,
)
from jpype import JImplements, JOverride
@JImplements(ICellsDataTable)
class NodeTable:
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @JOverride
    def getColumns(self):
        return ["Name", "Author"]
    @JOverride
    def getCount(self):
        return len(self._rows)
    @JOverride
    def beforeFirst(self):
        self._i = -1
    @JOverride
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    @JOverride
    def get(self, key):
        columns = self.getColumns()
        column_index = columns.index(key) if isinstance(key, str) else int(key)
        return self._rows[self._i][column_index]
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Center header and center footer carry <<Source.Field>> placeholders
worksheet.getPageSetup().setHeader(1, "Quarterly Report - <<node.Name>>")
worksheet.getPageSetup().setFooter(1, "Prepared by <<node.Author>>")
table = NodeTable([("Q4 2026", "Aspose.Cells")])
designer = WorkbookDesigner(workbook)
designer.setEnableHeaderFooterMarkers(True)
designer.setDataSource("node", table)
designer.process()
print("Header: " + worksheet.getPageSetup().getHeader(1))
print("Footer: " + worksheet.getPageSetup().getFooter(1))
# This prints:
# Header: Quarterly Report - Q4 2026
# Footer: Prepared by Aspose.Cells
workbook.save("HeaderFooterSmartMarkers.xlsx")
jpype.shutdownJVM()
```

## **استخدام مصدر بيانات JSON**
يمكنك استعمال JSON بدلاً من `ICellsDataTable` المخصص عندما تكون بيانات التقرير متاحة بالفعل بصيغة JSON. استدعِ `designer.setJsonDataSource(name, json)` لإرفاق المصدر.
المعامل `name` له نفس الدور الذي يلعبه اسم المصدر المستخدم مع البيانات الجدولية. على سبيل المثال، الاسم `node` يدعم علامات مثل `<<node.Company>>` و `<<node.Title>>`.
مرّر بيانات الصف مباشرة إلى `setJsonDataSource`:
- مصفوفة صفوف، مثل مصفوفة JSON تحتوي على كائن صف أو أكثر، مدعومة.
- يمكن أيضًا تمرير كائن صف واحد مباشرة.
- لا تغلف الصفوف تحت مفتاح علوي مسمى مثل `{"rows":[...]}`. هذا التغليف ليس الشكل المتوقع لمدخلات الصفوف في هذا التدفق.
يمكن لمصدر JSON واحد تعبئة نمطي العلامتين أثناء استدعاء `process()` نفسه. يمكنه حل علامة `&=` الكلاسيكية في خلية جسم ورقة العمل وعلامات `<<>>` في أقسام الرأس والتذييل. لا يزال يلزمك تمكين `setEnableHeaderFooterMarkers` حتى تُحل علامات الرأس والتذييل.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.getPageSetup().setHeader(0, "<<node.Company>>")
worksheet.getPageSetup().setHeader(2, "Page <<node.Title>>")
worksheet.getCells().get("A1").putValue("&=node.Company")
designer = WorkbookDesigner(workbook)
designer.setEnableHeaderFooterMarkers(True)
designer.setJsonDataSource(
    "node",
    '[{"Company":"Aspose Pty Ltd","Title":"Half-Year Report"}]'
)
designer.process()
print("Left: " + worksheet.getPageSetup().getHeader(0))
print("Right: " + worksheet.getPageSetup().getHeader(2))
print("Body: " + worksheet.getCells().get("A1").getStringValue())
workbook.save("HeaderFooterJsonMarkers.xlsx")
jpype.shutdownJVM()
```

## **تبديل وسياقات مصدر متعدد الصفوف**
إعداد علامة الرأس والتذييل هو `False` افتراضيًا، و `designer.setEnableHeaderFooterMarkers(True)` يتحكم فقط في علامات `<<Source.Field>>` في الرأس والتذييل. عندما يكون التبديل مغلقًا، لا يزال `process()` يحل علامات الجسم الكلاسيكية `&=`، لكن علامة `<<Source.Field>>` في رأس أو تذييل تظل نصًا حرفيًا.
القسم في الرأس أو التذييل هو سلسلة واحدة، وليس شريطًا متكررًا. إذا كان مصدر البيانات يحتوي على عدة صفوف، فإن الصف الأول يزود قيم الرأس والتذييل. بمجرد الحل، تصبح القيم نصًا عاديًا في الرأس أو التذييل. تظل هذه القيم في المصنف بعد استدعاء `workbook.save(...)` وتظهر عند تحميل المصنف المحفوظ مرة أخرى.
المثال التالي ينشئ مصنفين باستخدام نفس مصدر البيانات الجدولي متعدد الصفوف لتوضيح السلوك المتعطّل والمفعّل. يبقى `plainDesigner` العلامة دون تغيير، بينما `enabledDesigner` يحلّها باستخدام الصف الأول.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    WorkbookDesigner,
    ICellsDataTable,
)
from jpype import JImplements, JOverride
@JImplements(ICellsDataTable)
class NodeTable:
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @JOverride
    def getColumns(self):
        return ["Name"]
    @JOverride
    def getCount(self):
        return len(self._rows)
    @JOverride
    def beforeFirst(self):
        self._i = -1
    @JOverride
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    @JOverride
    def get(self, key):
        columns = self.getColumns()
        column_index = columns.index(key) if isinstance(key, str) else int(key)
        return self._rows[self._i][column_index]
table = NodeTable([
    ("First Row",),
    ("Second Row",),
])
# Without the switch the placeholder stays literal text
plain_workbook = Workbook()
plain_sheet = plain_workbook.getWorksheets().get(0)
plain_sheet.getPageSetup().setHeader(1, "<<node.Name>>")
plain_designer = WorkbookDesigner(plain_workbook)
plain_designer.setDataSource("node", table)
plain_designer.process()
# With the switch on, the FIRST row of a multi-row source wins
enabled_workbook = Workbook()
enabled_sheet = enabled_workbook.getWorksheets().get(0)
enabled_sheet.getPageSetup().setHeader(1, "<<node.Name>>")
enabled_designer = WorkbookDesigner(enabled_workbook)
enabled_designer.setEnableHeaderFooterMarkers(True)
enabled_designer.setDataSource("node", table)
enabled_designer.process()
print("Without switch: " + plain_sheet.getPageSetup().getHeader(1))
print("With switch: " + enabled_sheet.getPageSetup().getHeader(1))
# This prints:
# Without switch: <<node.Name>>
# With switch: First Row
enabled_workbook.save("HeaderFooterMarkersEnabled.xlsx")
jpype.shutdownJVM()
```

## **ربط صورة في رأس أو تذييل**
اللاحقة `(picture)` تربط صورة في قسم الرأس أو التذييل. اكتب `<<node.logo(picture)>>` في المكان الذي تريد ظهور الصورة فيه، وقدم قيمة الحقل كـ URI للبيانات — البادئة `data:image/png;base64,` متبوعةً بنص Base64 لبايتات الصورة. تُعامل الصورة المفكوكة كمصفوفة `byte[]`. سلسلة Base64 مجردة بدون بادئة `data:` لا تُضمّن صورة.
بعد `process()`:
1. تُستبدل العلامة بـ `&G`، وهو رمز الصورة القياسي في الرأس والتذييل. لأن العلامة تصبح شفرة داخل سلسلة القسم، يمكن أن تتواجد ضمن نص أطول مثل `Logo: <<node.logo(picture)>>`.
2. تُضمّن بايتات الصورة في المصنف كجزء وسائط مرتبط بطبقة رسم الرأس/التذييل لتلك الورقة، وبالتالي تُطبع الصورة مع الرأس أو التذييل.

```python
import base64
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    WorkbookDesigner,
    ICellsDataTable,
)
from jpype import JImplements, JOverride
@JImplements(ICellsDataTable)
class NodeTable:
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @JOverride
    def getColumns(self):
        return ["logo"]
    @JOverride
    def getCount(self):
        return len(self._rows)
    @JOverride
    def beforeFirst(self):
        self._i = -1
    @JOverride
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    @JOverride
    def get(self, key):
        columns = self.getColumns()
        column_index = columns.index(key) if isinstance(key, str) else int(key)
        return self._rows[self._i][column_index]
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# The (picture) suffix binds the image named by the data-URI field into the header
worksheet.getPageSetup().setHeader(1, "Logo: <<node.logo(picture)>>")
with open("logo.png", "rb") as image_file:
    image_bytes = image_file.read()
logo_data = "data:image/png;base64," + base64.b64encode(image_bytes).decode("ascii")
table = NodeTable([(logo_data,)])
designer = WorkbookDesigner(workbook)
designer.setEnableHeaderFooterMarkers(True)
designer.setDataSource("node", table)
designer.process()
print("Header: " + worksheet.getPageSetup().getHeader(1))
# This prints:
# Header: Logo: &G
workbook.save("HeaderFooterPicture.xlsx")
jpype.shutdownJVM()
```

يُطبع الرمز `&G` الذي تفسره Excel عند عرض الرأس — بايتات `logo.png` الآن موجودة داخل `HeaderFooterPicture.xlsx`، وتُطبع الصورة مكان الشفرة.
لاستخدام العلامات الذكية في الرأس والتذييل، اكتب علامات `<<Source.Field>>` في الأقسام اليسرى والوسطى واليمنى باستخدام `setHeader` و `setFooter`. استدعِ `designer.setEnableHeaderFooterMarkers(True)` قبل استدعاء `process()`، وزوّد القيم إما عبر `designer.setDataSource("node", table)` مع تنفيذ مخصص لـ `ICellsDataTable` أو عبر `designer.setJsonDataSource(name, json)`. اقرأ الأقسام المكتملة باستخدام `getHeader` و `getFooter`. يمكن لنفس مصدر البيانات تعبئة علامات الجسم وعلامات الرأس أو التذييل في تمريرة معالجة واحدة. أضف اللاحقة `(picture)` مع قيمة URI للبيانات لربط صورة في قسم.

## **مقالات ذات صلة**
- [عرض مصفوفة خلية واحدة للمؤشر الذكي](/cells/ar/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="python" >}}