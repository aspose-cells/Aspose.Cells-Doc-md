---
title: كيفية إضافة التنسيق الشرطي للنص
description: كيفية استخدام مكتبة Aspose.Cells لـ Python via .NET لتطبيق التنسيق النصي الشرطي. من خلال تعديل هذه المعايير، يكون لديك مزيد من التحكم في مظهر الخلايا ومظهرها.
keywords: Aspose.Cells، تنسيق النص الشرطي، بايثون، شرطي، تنسيق
type: docs
weight: 70
url: /ar/python-net/how-to-add-text-conditional-formatting/
---

## **سيناريوهات الاستخدام المحتملة**
استخدام التنسيق الشرطي المبني على النص في جداول البيانات مفيد لتسليط الضوء على الخلايا التي تلبي معايير نصية معينة. يمكن أن يحسن تحليل البيانات ويسهل العثور على المعلومات الرئيسية في مجموعة بيانات كبيرة. إليك بعض الأسباب لاستخدام التنسيق الشرطي للنص:

1. تسليط الضوء على نص معين: يمكنك تطبيق تنسيق استنادًا إلى كلمات أو عبارات أو رموز محددة. على سبيل المثال، قد ترغب في تمييز جميع الخلايا التي تحتوي على كلمة "عاجل" أو "مكتمل" لتمييز المهام في مشروع معين.
1. التعرف على الأنماط أو الاتجاهات: إذا كنت تعمل مع فئات أو حالات (مثل "عالي"، "متوسط"، "منخفض")، يمكن للتنسيق الشرطي النصي أن يميزها بصريًا، مما يسهل تتبع التقدم أو تحديد أولويات المهام.
1. تنبيهات الأخطاء أو إدخال البيانات: يمكن أن يميز التنسيق النصي الإدخالات غير المتناسقة أو الخاطئة، مثل الأخطاء الإملائية، النص غير المكتمل، أو القيم غير الصحيحة. هذا مفيد بشكل خاص في مجموعات البيانات التي تحتوي على الكثير من الإدخالات النصية.
1. تحسين قابلية القراءة: تساعد ترميز الألوان للنص أو تغيير نمطه (غامق، مائل، إلخ) على إبراز المعلومات المهمة، مما يحسن من السهولة العامة لقراءة الجدول الخاص بك.
1. ردود فعل ديناميكية: يمكنك إعداد قواعد تعدل التنسيق تلقائيًا عندما يتطابق النص مع شروط معينة. هذا يعني أنك لست بحاجة إلى تحديث التنسيق يدويًا مع تغير البيانات.

باختصار، يساعدك التنسيق الشرطي النصي على التعرف بسرعة على المعلومات ذات الصلة، الأخطاء، والنمط، مما يجعله أداة قوية لإدارة وتحليل البيانات النصية.

## **كيفية إضافة التنسيق الشرطي للنص باستخدام Excel**
لإضافة تنسيق شرطي يعتمد على النص في Excel، اتبع الخطوات التالية:

1. حدد نطاق الخلايا: ظلل الخلايا التي تريد تطبيق التنسيق الشرطي عليها.
1. افتح قائمة التنسيق الشرطي: انتقل إلى علامة التبويب الصفحة الرئيسية في شريط Excel. انقر على التنسيق الشرطي في مجموعة "الأساليب".
1. اختر "قاعدة جديدة": من القائمة المنسدلة، اختر قاعدة جديدة.
1. اختر "تنسق فقط الخلايا التي تحتوي": في مربع حوار قاعدة التنسيق الجديدة، اختر تنسيق فقط الخلايا التي تحتوي تحت قسم "حدد نوع القاعدة".
1. حدد معايير القاعدة: في قسم "تنسق خلايا تحتوي على"، اختر نص محدد من القائمة المنسدلة. اختر إما يحتوي على، يبدأ بـ، أو ينتهي بـ، اعتمادًا على الشرط الذي تريد تطبيقه. أدخل النص الذي تريد تنسيقه (مثل كلمة محددة مثل "عاجل" أو "مكتمل").
1. اختر تنسيق الخلية: اضغط على زر تنسيق. في مربع حوار تنسيق الخلايا، يمكنك اختيار لون الخط، لون التعبئة، أو أي خيارات تنسيق أخرى تفضلها.
1. طبق القاعدة: بمجرد تعيين التنسيق المطلوب، اضغط على موافق لتطبيق القاعدة. ثم اضغط على موافق مرة أخرى في مربع حوار قاعدة التنسيق الجديدة لإغلاقه.
1. عرض النتائج: ستحتوي الخلايا التي تحتوي على النص المحدد الآن على التنسيق الذي تم تطبيقه، مما يسهل عليك رؤية المعلومات ذات الصلة.


## **كيفية إضافة تنسيق النص الشرطي باستخدام Aspose.Cells لـ Python via .NET**

يدعم Aspose.Cells لـ Python via .NET تمامًا التنسيق الشرطي المقدم من قبل Microsoft Excel 2007 والإصدارات اللاحقة بصيغة XLSX على الخلايا عند التشغيل. يُظهر هذا المثال تمرينًا للتنسيقات الشرطية المتقدمة بما في ذلك BeginsWith، ContainsBlank، ContainsText وغير ذلك.

### **تنسيق الخلية عندما يبدأ القيمة بالنص المحدد**

```python
from aspose.cells import Workbook
from aspose.cells import Workbook, Worksheet, CellArea, FormatConditionType, IconSetType, FormatConditionValueType, BackgroundType, TimePeriodType
from aspose.pydrawing import Color
from datetime import datetime
import aspose.cells
import os
import pytest

class ConditionalFormatting:
    def __init__(self):
        self._sheet = None

    @staticmethod
    def run():
        # The path to the documents directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, "data")
        obj = ConditionalFormatting()
        obj.do_test(data_dir)

    def do_test(self, data_dir):
        book = Workbook()
        sheet1 = book.worksheets[0]
        self._sheet = sheet1

        self.add_begin_with()        

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "add_begin_with.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)


    def add_begin_with(self):
        conds = self.get_format_condition("E15:G16", Color.light_goldenrod_yellow)
        idx = conds.add_condition(FormatConditionType.BEGINS_WITH)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        cond.text = "ab"
        self._sheet.cells.get("E15").put_value("abc")
        self._sheet.cells.get("G16").put_value("babx")


    def get_format_condition(self, cell_area_name, color):
        index = self._sheet.conditional_formattings.add()
        format_conditions = self._sheet.conditional_formattings[index]
        area = self.get_cell_area_by_name(cell_area_name)
        format_conditions.add_area(area)
        self.fill_cell(cell_area_name, color)
        return format_conditions

    def fill_cell(self, cell_area_name, color):
        area = self.get_cell_area_by_name(cell_area_name)
        k = 0
        for i in range(area.start_column, area.end_column + 1):
            for j in range(area.start_row, area.end_row + 1):
                c = self._sheet.cells.get(j, i)
                if color != Color.empty:
                    s = c.get_style()
                    s.foreground_color = color
                    s.pattern = BackgroundType.SOLID
                    c.set_style(s)
                value = j + i + k
                c.put_value(value)
                k += 1

    @staticmethod
    def get_cell_area_by_name(s):
        area = CellArea()
        str_cell_range = s.replace("$", "").split(':')
        start_row, start_col = CellsHelper.cell_name_to_index(str_cell_range[0])
        area.start_row = start_row
        area.start_column = start_col
        if len(str_cell_range) == 1:
            area.end_row = start_row
            area.end_column = start_col
        else:
            end_row, end_col = CellsHelper.cell_name_to_index(str_cell_range[1])
            area.end_row = end_row
            area.end_column = end_col
        return area

```
### **تنسيق الخلية عندما تحتوي القيمة على فارغ**

```python
from aspose.cells import Workbook
from aspose.cells import Workbook, Worksheet, CellArea, FormatConditionType, IconSetType, FormatConditionValueType, BackgroundType, TimePeriodType
from aspose.pydrawing import Color
from datetime import datetime
import aspose.cells
import os
import pytest

class ConditionalFormatting:
    def __init__(self):
        self._sheet = None

    @staticmethod
    def run():
        # The path to the documents directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, "data")
        obj = ConditionalFormatting()
        obj.do_test(data_dir)

    def do_test(self, data_dir):
        book = Workbook()
        sheet1 = book.worksheets[0]
        self._sheet = sheet1

        self.add_contains_blank()        

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "add_contains_blank.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)

    def add_contains_blank(self):
        conds = self.get_format_condition("E9:G10", Color.light_blue)
        idx = conds.add_condition(FormatConditionType.CONTAINS_BLANKS)
        cond = conds[idx]
        cond.style.background_color = Color.yellow
        cond.style.pattern = BackgroundType.SOLID
        self._sheet.cells.get("E9").put_value("  ")
        self._sheet.cells.get("G10").put_value("  ")

```

### **تنسيق الخلية عندما تحتوي القيمة على أخطاء**

```python
from aspose.cells import Workbook
from aspose.cells import Workbook, Worksheet, CellArea, FormatConditionType, IconSetType, FormatConditionValueType, BackgroundType, TimePeriodType
from aspose.pydrawing import Color
from datetime import datetime
import aspose.cells
import os
import pytest

class ConditionalFormatting:
    def __init__(self):
        self._sheet = None

    @staticmethod
    def run():
        # The path to the documents directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, "data")
        obj = ConditionalFormatting()
        obj.do_test(data_dir)

    def do_test(self, data_dir):
        book = Workbook()
        sheet1 = book.worksheets[0]
        self._sheet = sheet1

        self.add_contains_error()        

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "add_contains_error.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)


    def add_contains_error(self):
        conds = self.get_format_condition("E17:G18", Color.light_sky_blue)
        idx = conds.add_condition(FormatConditionType.CONTAINS_ERRORS)
        cond = conds[idx]
        cond.style.background_color = Color.yellow
        cond.style.pattern = BackgroundType.SOLID
        self._sheet.cells.get("E17").put_value("  ")
        self._sheet.cells.get("G18").put_value("  ")

```

### **تنسيق الخلية عندما تحتوي القيمة على نص محدد**

```python
from aspose.cells import Workbook
from aspose.cells import Workbook, Worksheet, CellArea, FormatConditionType, IconSetType, FormatConditionValueType, BackgroundType, TimePeriodType
from aspose.pydrawing import Color
from datetime import datetime
import aspose.cells
import os
import pytest

class ConditionalFormatting:
    def __init__(self):
        self._sheet = None

    @staticmethod
    def run():
        # The path to the documents directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, "data")
        obj = ConditionalFormatting()
        obj.do_test(data_dir)

    def do_test(self, data_dir):
        book = Workbook()
        sheet1 = book.worksheets[0]
        self._sheet = sheet1

        self.add_contains_text()        

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "add_contains_text.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)

    def add_contains_text(self):
        conds = self.get_format_condition("E5:G6", Color.light_blue)
        idx = conds.add_condition(FormatConditionType.CONTAINS_TEXT)
        cond = conds[idx]
        cond.style.background_color = Color.yellow
        cond.style.pattern = BackgroundType.SOLID
        cond.text = "1"

```

### **تنسيق الخلية عندما تحتوي القيمة على قيم مكررة**

```python
from aspose.cells import Workbook
from aspose.cells import Workbook, Worksheet, CellArea, FormatConditionType, IconSetType, FormatConditionValueType, BackgroundType, TimePeriodType
from aspose.pydrawing import Color
from datetime import datetime
import aspose.cells
import os
import pytest

class ConditionalFormatting:
    def __init__(self):
        self._sheet = None

    @staticmethod
    def run():
        # The path to the documents directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, "data")
        obj = ConditionalFormatting()
        obj.do_test(data_dir)

    def do_test(self, data_dir):
        book = Workbook()
        sheet1 = book.worksheets[0]
        self._sheet = sheet1

        self.add_duplicate()        

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "add_duplicate.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)

    def add_duplicate(self):
        conds = self.get_format_condition("E23:G24", Color.light_slate_gray)
        idx = conds.add_condition(FormatConditionType.DUPLICATE_VALUES)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        self._sheet.cells.get("E23").put_value("bb")
        self._sheet.cells.get("G24").put_value("bb")

```

### **تنسيق الخلية عندما تنتهي القيمة بنص معين**

```python
from aspose.cells import Workbook
from aspose.cells import Workbook, Worksheet, CellArea, FormatConditionType, IconSetType, FormatConditionValueType, BackgroundType, TimePeriodType
from aspose.pydrawing import Color
from datetime import datetime
import aspose.cells
import os
import pytest

class ConditionalFormatting:
    def __init__(self):
        self._sheet = None

    @staticmethod
    def run():
        # The path to the documents directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, "data")
        obj = ConditionalFormatting()
        obj.do_test(data_dir)

    def do_test(self, data_dir):
        book = Workbook()
        sheet1 = book.worksheets[0]
        self._sheet = sheet1

        self.add_end_with()        

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "add_end_with.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)


    def add_end_with(self):
        conds = self.get_format_condition("E13:G14", Color.light_gray)
        idx = conds.add_condition(FormatConditionType.ENDS_WITH)
        cond = conds[idx]
        cond.style.background_color = Color.yellow
        cond.style.pattern = BackgroundType.SOLID
        cond.text = "ab"
        self._sheet.cells.get("E13").put_value("nnnab")
        self._sheet.cells.get("G14").put_value("mmmabc")

```

### **تنسيق الخلية عندما لا تحتوي القيمة على فارغ**

```python
from aspose.cells import Workbook
from aspose.cells import Workbook, Worksheet, CellArea, FormatConditionType, IconSetType, FormatConditionValueType, BackgroundType, TimePeriodType
from aspose.pydrawing import Color
from datetime import datetime
import aspose.cells
import os
import pytest

class ConditionalFormatting:
    def __init__(self):
        self._sheet = None

    @staticmethod
    def run():
        # The path to the documents directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, "data")
        obj = ConditionalFormatting()
        obj.do_test(data_dir)

    def do_test(self, data_dir):
        book = Workbook()
        sheet1 = book.worksheets[0]
        self._sheet = sheet1

        self.add_not_contains_blank()        

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "add_not_contains_blank.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)

    def add_not_contains_blank(self):
        conds = self.get_format_condition("E11:G12", Color.light_coral)
        idx = conds.add_condition(FormatConditionType.NOT_CONTAINS_BLANKS)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        self._sheet.cells.get("E11").put_value("abc")
        self._sheet.cells.get("G12").put_value("  ")

```

### **تنسيق الخلية عندما لا تحتوي القيمة على أخطاء**

```python
from aspose.cells import Workbook
from aspose.cells import Workbook, Worksheet, CellArea, FormatConditionType, IconSetType, FormatConditionValueType, BackgroundType, TimePeriodType
from aspose.pydrawing import Color
from datetime import datetime
import aspose.cells
import os
import pytest

class ConditionalFormatting:
    def __init__(self):
        self._sheet = None

    @staticmethod
    def run():
        # The path to the documents directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, "data")
        obj = ConditionalFormatting()
        obj.do_test(data_dir)

    def do_test(self, data_dir):
        book = Workbook()
        sheet1 = book.worksheets[0]
        self._sheet = sheet1

        self.add_not_contains_error()        

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "add_not_contains_error.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)

    def add_not_contains_error(self):
        conds = self.get_format_condition("E19:G20", Color.light_sea_green)
        idx = conds.add_condition(FormatConditionType.NOT_CONTAINS_ERRORS)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        self._sheet.cells.get("E19").put_value("  ")
        self._sheet.cells.get("G20").put_value("  ")

```

### **تنسيق الخلية عندما لا تحتوي القيمة على نص معين**

```python
from aspose.cells import Workbook
from aspose.cells import Workbook, Worksheet, CellArea, FormatConditionType, IconSetType, FormatConditionValueType, BackgroundType, TimePeriodType
from aspose.pydrawing import Color
from datetime import datetime
import aspose.cells
import os
import pytest

class ConditionalFormatting:
    def __init__(self):
        self._sheet = None

    @staticmethod
    def run():
        # The path to the documents directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, "data")
        obj = ConditionalFormatting()
        obj.do_test(data_dir)

    def do_test(self, data_dir):
        book = Workbook()
        sheet1 = book.worksheets[0]
        self._sheet = sheet1

        self.add_not_contains_text()        

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "add_not_contains_text.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)

    def add_not_contains_text(self):
        conds = self.get_format_condition("E7:G8", Color.light_coral)
        idx = conds.add_condition(FormatConditionType.NOT_CONTAINS_TEXT)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        cond.text = "3"
```

### **تنسيق الخلية عندما تحتوي القيمة على قيم فريدة**

```python
from aspose.cells import Workbook
from aspose.cells import Workbook, Worksheet, CellArea, FormatConditionType, IconSetType, FormatConditionValueType, BackgroundType, TimePeriodType
from aspose.pydrawing import Color
from datetime import datetime
import aspose.cells
import os
import pytest

class ConditionalFormatting:
    def __init__(self):
        self._sheet = None

    @staticmethod
    def run():
        # The path to the documents directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, "data")
        obj = ConditionalFormatting()
        obj.do_test(data_dir)

    def do_test(self, data_dir):
        book = Workbook()
        sheet1 = book.worksheets[0]
        self._sheet = sheet1

        self.add_unique()        

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "add_unique.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)


    def add_unique(self):
        conds = self.get_format_condition("E21:G22", Color.light_salmon)
        idx = conds.add_condition(FormatConditionType.UNIQUE_VALUES)
        cond = conds[idx]
        cond.style.background_color = Color.yellow
        cond.style.pattern = BackgroundType.SOLID
        self._sheet.cells.get("E21").put_value("aa")
        self._sheet.cells.get("G22").put_value("aa")

```

{{< app/cells/assistant language="python-net" >}}
