---
title: كيفية إضافة تنسيق شرطي لأعلى 10
description: كيفية استخدام مكتبة Aspose.Cells لـ Python via .NET لتطبيق التنسيق الشرطي لأعلى 10. من خلال تعديل هذه المعايير، يكون لديك مزيد من التحكم في مظهر الخلايا ومظهرها.
keywords: Aspose.Cells، تنسيق أعلى 10، بايثون، شرطي، تنسيق
type: docs
weight: 70
url: /ar/python-net/how-to-add-top10-conditional-formatting/
---

## **سيناريوهات الاستخدام المحتملة**
يساعد استخدام التنسيق الشرطي Top10 في إكسل على إبراز قيم الأداء الأعلى بسرعة في مجموعة البيانات — ليس فقط أعلى 10 قيم حرفيًا، ولكن غالبًا أعلى N قيم أو أعلى N% (يمكنك الاختيار!).

1. اكتشاف الاتجاهات والقيم الشاذة: حدد بسرعة الأفضل أداءً (على سبيل المثال، أفضل 10 مندوبي مبيعات، أفضل المعدلات، أشهر الأرباح). يسهل التحليل دون ترتيب البيانات.
1. تصور البيانات: يضيف تلميحات لون تجعل نقاط البيانات المهمة تبرز بصريًا. يساعد مشاهدين جدول البيانات على فهم القيم الرئيسية بنظرة سريعة.
1. مقارنات سريعة: مفيد في لوحات المعلومات والتقارير حيث تريد إبراز التميز أو القمم.
1. تحديثات ديناميكية: إذا تغيرت بياناتك، يتحدث التنسيق الشرطي تلقائيًا ليعكس القيم الأعلى الجديدة.

## **كيفية إضافة التنسيق الشرطي Top10 باستخدام Excel**
إليك كيفية إضافة التنسيق الشرطي Top10 في Excel، خطوة بخطوة:

1. حدد نطاق الخلايا الذي تريد تحليله. على سبيل المثال: حدد B2:B100، إذا كنت تعمل مع الدرجات أو أرقام المبيعات.
1. اذهب إلى علامة التبويب الصفحة الرئيسية في شريط أدوات Excel.
1. انقر على التنسيق الشرطي في مجموعة الأنماط.
1. مرر فوق قواعد القمة / القاع في القائمة المنسدلة.
1. انقر على أعلى 10 عناصر...
1. ستظهر نافذة حوار: ستقول: تنسيق الخلايا التي تتصدر الترتيب في أعلى 10. يمكنك تغيير الرقم (مثلاً، أعلى 5، أعلى 3، إلخ.). اختر تنسيقًا (مثل تعبئة خفيفة حمرا، نص عريض، أو انقر على تنسيق مخصص لمزيد من الخيارات).
1. انقر على موافق.


## **كيفية إضافة تنسيق أعلى 10 باستخدام Aspose.Cells لـ Python via .NET**

يدعم Aspose.Cells لـ Python via .NET تمامًا التنسيق الشرطي المقدم من قبل Microsoft Excel 2007 والإصدارات اللاحقة بصيغة XLSX على الخلايا عند التشغيل. يُظهر هذا المثال تمرينًا لتنسيق أعلى 10 مع مجموعات مختلفة من السمات.

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

        self.add_top10_1()
        self.add_top10_2()
        self.add_top10_3()
        self.add_top10_4()

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "Testoutput.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)    

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

    def add_top10_1(self):
        conds = self.get_format_condition("A17:C20", Color.gray)
        idx = conds.add_condition(FormatConditionType.TOP10)
        cond = conds[idx]
        cond.style.background_color = Color.yellow
        cond.style.pattern = BackgroundType.SOLID

    def add_top10_2(self):
        conds = self.get_format_condition("A21:C24", Color.green)
        idx = conds.add_condition(FormatConditionType.TOP10)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        cond.top10.is_bottom = True

    def add_top10_3(self):
        conds = self.get_format_condition("A25:C28", Color.orange)
        idx = conds.add_condition(FormatConditionType.TOP10)
        cond = conds[idx]
        cond.style.background_color = Color.blue
        cond.style.pattern = BackgroundType.SOLID
        cond.top10.is_percent = True

    def add_top10_4(self):
        conds = self.get_format_condition("A29:C32", Color.gold)
        idx = conds.add_condition(FormatConditionType.TOP10)
        cond = conds[idx]
        cond.style.background_color = Color.green
        cond.style.pattern = BackgroundType.SOLID
        cond.top10.rank = 3
```

{{< app/cells/assistant language="csharp" >}}
{{< app/cells/assistant language="python-net" >}}
