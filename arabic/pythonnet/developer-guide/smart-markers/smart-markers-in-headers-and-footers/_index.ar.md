---
title: علامات ذكية في رؤوس وتذييلات الصفحات | Aspose.Cells for Python via .NET
linktitle: علامات ذكية في الرأس والتذييل | Aspose.Cells
description: ضع عناصر نائبة للعلامات الذكية في رؤوس وتذييلات الصفحات باستخدام بناء الشرطين المتوازيين <<>> ومفتاح WorkbookDesigner.enable_header_footer_markers باستخدام تطبيقات مخصصة لـ ICellsDataTable أو مصادر بيانات JSON، واربط الصور عبر عناوين URI للبيانات، في Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, العلامات الذكية, الرؤوس, التذييلات, معلمات علامات الرؤوس والتذييلات, enable_header_footer_markers, WorkbookDesigner, PageSetup, set_header, set_footer, set_json_data_source, set_data_source, ICellsDataTable, جدول بيانات مخصص, ربط البيانات, صورة, URI للبيانات, Aspose.Cells for Python via .NET
type: docs
weight: 196
url: /ar/python-net/smart-markers-in-headers-and-footers/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
تحتوي رؤوس الصفحات وتذييلاتها عادةً على بيانات وصفية للتقرير مثل عنوان التقرير، فترة التقرير، المؤلف، والقسم. عندما تكون هذه المعلومات موجودة بالفعل في مصدر البيانات المستخدم لملء المصنف، فإن تكرارها يدوياً يخلق تكراراً غير ضروري.  
الصياغة الكلاسيكية للعلامة الذكية، `&=Source.Field`، تُعالج في خلايا جسم ورقة العمل. إذا وضعت علامة كلاسيكية في رأس أو تذييل عبر `page_setup.set_header` أو `page_setup.set_footer`، فإنها تبقى نصاً حرفيًا لأن سلاسل الرؤوس والتذييلات ليست جزءًا من شبكة خلايا ورقة العمل التي يفحصها `workbook_designer.process()`.  
بدءًا من **Aspose.Cells for Python via .NET 26.11**، المفتاح `workbook_designer.enable_header_footer_markers`، والذي يكون `False` افتراضيًا، يجعل `process()` يحل العناصر النائبة المكتوبة كـ `<<Source.Field>>` في سلاسل أقسام الرأس أو التذييل — اضبطه إلى `True` قبل استدعاء `process()`. تستخدم العناصر النائبة في الرأس أو التذييل نفس مصدر البيانات كما في علامات الجسم.  
كل رأس أو تذييل يحتوي على ثلاثة أقسام قابلة للعنونة:
- القسم `0` هو القسم الأيسر.
- القسم `1` هو القسم الأوسط.
- القسم `2` هو القسم الأيمن.
استخدم `page_setup.set_header(section, value)` و `page_setup.set_footer(section, value)` لكتابة هذه الأقسام. بعد المعالجة، استخدم `page_setup.get_header(section)` و `page_setup.get_footer(section)` لاسترجاع النص المكتمل.

{{% alert color="primary" %}}
عنصر نائب مثل `<<Source.Field>>` يدرج قيمة الحقل كنص في سلسلة القسم. يتم ربط الصور باللاحقة `(picture)` وقيمة URI للبيانات.
{{% /alert %}}

## **تمكين علامات الرأس/التذييل باستخدام جدول بيانات مخصص**
استخدم التسلسل التالي لحل العناصر النائبة في الرأس والتذييل باستخدام مصدر بيانات جدولي مخصص في **Aspose.Cells for Python via .NET 26.11**:
1. أنشئ كائن `Workbook` واحصل على أول `Worksheet` له في الفهرس `0`.
2. اكتب عناصر نائبة `<<Source.Field>>` في أقسام الرأس والتذييل المطلوبة باستخدام `page_setup.set_header` و `page_setup.set_footer`.
3. عرّف فئة صغيرة تُطبق `ICellsDataTable` لتُظهر بيانات الصفوف الجدولية — أسماء الأعمدة، عدد الصفوف، ومؤشر يحتوي على `before_first()`, `next()`, و `__getitem__` — واستخدم اسم مصدر يتطابق مع البادئة المستخدمة في العناصر النائبة. على سبيل المثال، المصدر المسمّى `node` يدعم عناصر نائبة مثل `<<node.Name>>`. فئة بايثون عادية أو قائمة من القواميس لا تُربط على هذه المنصة؛ تنفيذ `ICellsDataTable` هو مصدر البيانات المخصص.
4. أنشئ كائن `WorkbookDesigner` للمصنف.
5. اضبط `designer.enable_header_footer_markers` إلى `True` قبل المعالجة.
6. اربط الجدول واسم المصدر باستخدام `designer.set_data_source("node", table)`.
7. استدعِ `designer.process()`.
8. بعد المعالجة، لا تعود العناصر النائبة موجودة في نص الرأس أو التذييل. استخدم `get_header` و `get_footer` لاسترجاع سلاسل الأقسام المكتملة.

```python
import aspose.cells as ac
class NodeTable(ac.ICellsDataTable):
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @property
    def columns(self):
        return ["Name", "Author"]
    @property
    def count(self):
        return len(self._rows)
    def before_first(self):
        self._i = -1
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    def __getitem__(self, key):
        column = self.columns.index(key) if isinstance(key, str) else key
        return self._rows[self._i][column]
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Center header and center footer carry <<Source.Field>> placeholders
worksheet.page_setup.set_header(1, "Quarterly Report - <<node.Name>>")
worksheet.page_setup.set_footer(1, "Prepared by <<node.Author>>")
table = NodeTable([("Q4 2026", "Aspose.Cells")])
designer = ac.WorkbookDesigner(workbook)
designer.enable_header_footer_markers = True
designer.set_data_source("node", table)
designer.process()
print("Header: " + worksheet.page_setup.get_header(1))
print("Footer: " + worksheet.page_setup.get_footer(1))
# This prints:
# Header: Quarterly Report - Q4 2026
# Footer: Prepared by Aspose.Cells
workbook.save("HeaderFooterSmartMarkers.xlsx")
```

## **استخدام مصدر بيانات JSON**
يمكنك استخدام JSON بدلًا من `ICellsDataTable` المخصص عندما تكون بيانات التقرير متاحة بالفعل بصيغة JSON. استدعِ `workbook_designer.set_json_data_source(name, json)` لإرفاق المصدر. يلعب المعامل `name` نفس الدور الذي يلعبه اسم المصدر المستخدم مع البيانات الجدولية. على سبيل المثال، الاسم `node` يدعم عناصر نائبة مثل `<<node.Company>>` و `<<node.Title>>`.  
مرّر بيانات الصف مباشرة إلى `set_json_data_source`:
- مصفوفة صفوف، مثل مصفوفة JSON تحتوي على كائن صف واحد أو أكثر، مدعومة.
- يمكن أيضًا تمرير كائن صف واحد مباشرة.
- لا تقم بلف الصفوف تحت مفتاح أعلى مستوى مسمى مثل `{"rows":[...]}`. هذا اللف غير متوقع كهيكل إدخال موجه للصفوف لهذا التدفق.  
يمكن لمصدر JSON واحد تعبئة نمطي العلامة خلال نفس استدعاء `process()`. يمكنه حل علامة كلاسيكية `&=` في خلية جسم ورقة العمل وعناصر نائبة ذات الشرطين المتوازيين `<<>>` في أقسام الرأس أو التذييل. ما زال عليك تمكين `enable_header_footer_markers` لحل العناصر النائبة في الرأس والتذييل.

```python
import aspose.cells as ac
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.page_setup.set_header(0, "<<node.Company>>")
worksheet.page_setup.set_header(2, "Page <<node.Title>>")
worksheet.cells.get("A1").put_value("&=node.Company")
designer = ac.WorkbookDesigner(workbook)
designer.enable_header_footer_markers = True
designer.set_json_data_source(
    "node",
    '[{"Company":"Aspose Pty Ltd","Title":"Half-Year Report"}]'
)
designer.process()
print("Left: " + worksheet.page_setup.get_header(0))
print("Right: " + worksheet.page_setup.get_header(2))
print("Body: " + worksheet.cells.get("A1").string_value)
# This prints:
# Left: Aspose Pty Ltd
# Right: Page Half-Year Report
# Body: Aspose Pty Ltd
workbook.save("HeaderFooterJsonMarkers.xlsx")
```

## **دلالات المفتاح ومفهوم مصدر متعدد الصفوف**
`enable_header_footer_markers` يكون `False` افتراضيًا، والمفتاح يتحكم فقط في العناصر النائبة `<<Source.Field>>` في الرأس والتذييل. عندما يكون المفتاح متوقفًا، يظل `process()` يحل علامات الجسم الكلاسيكية `&=`، لكن عنصر نائب `<<Source.Field>>` في رأس أو تذييل يبقى نصًا حرفيًا.  
قسم الرأس أو التذييل هو سلسلة واحدة، وليس شريطًا متكررًا. إذا كان مصدر البيانات يحتوي على عدة صفوف، يزود الصف الأول قيم الرأس والتذييل. بمجرد الحل، تتحول القيم إلى نص رأس أو تذييل عادي. تظل موجودة في المصنف بعد استدعاء `save` وتظهر عندما تقوم بتحميل المصنف المحفوظ مرة أخرى.  
المثال التالي ينشئ مصنفين يستخدمان نفس مصدر البيانات الجدولي متعدد الصفوف لمقارنة السلوك عند إيقاف وتمكين المفتاح. يترك `plain_designer` العنصر النائب دون تغيير، بينما يحله `enabled_designer` باستخدام الصف الأول.

```python
import aspose.cells as ac
class NodeTable(ac.ICellsDataTable):
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @property
    def columns(self):
        return ["Name"]
    @property
    def count(self):
        return len(self._rows)
    def before_first(self):
        self._i = -1
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    def __getitem__(self, key):
        column = self.columns.index(key) if isinstance(key, str) else key
        return self._rows[self._i][column]
rows = [("First Row",), ("Second Row",)]
# Without the switch the placeholder stays literal text
plain_workbook = ac.Workbook()
plain_sheet = plain_workbook.worksheets[0]
plain_sheet.page_setup.set_header(1, "<<node.Name>>")
plain_designer = ac.WorkbookDesigner(plain_workbook)
plain_designer.set_data_source("node", NodeTable(rows))
plain_designer.process()
# With the switch on, the FIRST row of a multi-row source wins
enabled_workbook = ac.Workbook()
enabled_sheet = enabled_workbook.worksheets[0]
enabled_sheet.page_setup.set_header(1, "<<node.Name>>")
enabled_designer = ac.WorkbookDesigner(enabled_workbook)
enabled_designer.enable_header_footer_markers = True
enabled_designer.set_data_source("node", NodeTable(rows))
enabled_designer.process()
print("Without switch: " + plain_sheet.page_setup.get_header(1))
print("With switch: " + enabled_sheet.page_setup.get_header(1))
# This prints:
# Without switch: <<node.Name>>
# With switch: First Row
enabled_workbook.save("HeaderFooterMarkersEnabled.xlsx")
```

## **ربط صورة في رأس أو تذييل**
اللاحقة `(picture)` تربط صورة في قسم الرأس أو التذييل. اكتب `<<node.logo(picture)>>` حيث تريد ظهور الصورة، وامنح قيمة الحقل كـ URI للبيانات — البادئة `data:image/png;base64,` تليها نص Base64 لبايتات الصورة. سلسلة Base64 بدون بادئة `data:` لا تُدرج صورة.  
بعد `process()`:
1. يتم استبدال العنصر النائب بـ `&G`، رمز الصورة القياسي للرأس والتذييل. لأن العلامة تصبح كودًا داخل سلسلة القسم، يمكن أن تتواجد ضمن نص أطول مثل `Logo: <<node.logo(picture)>>`.
2. تُضمّن بايتات الصورة في المصنف كجزء وسائط مرفق بطبقة الرسم للرأس/التذييل في تلك ورقة العمل، لذا تُطبع الصورة مع الرأس أو التذييل.

```python
import aspose.cells as ac
import base64
class LogoTable(ac.ICellsDataTable):
    def __init__(self, rows):
        self._rows = rows
        self._i = -1
    @property
    def columns(self):
        return ["logo"]
    @property
    def count(self):
        return len(self._rows)
    def before_first(self):
        self._i = -1
    def next(self):
        self._i += 1
        return self._i < len(self._rows)
    def __getitem__(self, key):
        column = self.columns.index(key) if isinstance(key, str) else key
        return self._rows[self._i][column]
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# The (picture) suffix binds the image named by the data-URI field into the header
worksheet.page_setup.set_header(1, "Logo: <<node.logo(picture)>>")
with open("logo.png", "rb") as image_file:
    logo_data_uri = "data:image/png;base64," + base64.b64encode(image_file.read()).decode("ascii")
table = LogoTable([(logo_data_uri,)])
designer = ac.WorkbookDesigner(workbook)
designer.enable_header_footer_markers = True
designer.set_data_source("node", table)
designer.process()
print("Header: " + worksheet.page_setup.get_header(1))
# This prints:
# Header: Logo: &G
workbook.save("HeaderFooterPicture.xlsx")
```

يُطبع الرمز `&G` كرمز صورة يفسره Excel عند عرض الرأس — الآن بايتات `logo.png` موجودة داخل `HeaderFooterPicture.xlsx`، وتُطبع الصورة بدلاً من الرمز. لاستخدام علامات ذكية في الرأس والتذييل، اكتب عناصر نائبة `<<Source.Field>>` في الأقسام اليسرى والوسطى واليمنى للرأس أو التذييل باستخدام `set_header` و `set_footer`. اضبط `enable_header_footer_markers` إلى `True` على `WorkbookDesigner` قبل استدعاء `process()`، ووفّر القيم عبر `set_data_source("node", table)` باستخدام تنفيذ مخصص لـ `ICellsDataTable` أو `set_json_data_source(name, json)`. اقرأ الأقسام المكتملة باستخدام `get_header` و `get_footer`. يمكن لنفس مصدر البيانات تعبئة علامات الجسم والعناصر النائبة في الرأس أو التذييل في تمريرة معالجة واحدة. أضف اللاحقة `(picture)` مع قيمة URI للبيانات لربط صورة في القسم.

## مقالات ذات صلة
- [عرض صفيف خلية منفردة باستخدام SmartMarker](/cells/ar/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="python-net" >}}