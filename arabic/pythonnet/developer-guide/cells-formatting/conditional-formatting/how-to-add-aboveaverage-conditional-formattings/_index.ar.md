---
title: كيفية إضافة تنسيق شرطي فوق المتوسط
description: كيفية استخدام مكتبة Aspose.Cells لـ Python via .NET لتطبيق تنسيق شرطي فوق المتوسط. من خلال تعديل هذه المعايير، يكون لديك مزيد من التحكم في مظهر الخلايا.
keywords: Aspose.Cells، تنسيق شرطي فوق المتوسط، بايثون، تنسيق، تنسيق شرطي
type: docs
weight: 70
url: /ar/python-net/how-to-add-above-average-conditional-formatting/
---

## **سيناريوهات الاستخدام المحتملة**
استخدام التنسيق الشرطي فوق المتوسط في أدوات مثل Microsoft Excel أو Google Sheets هو وسيلة سريعة ومرئية لتسليط الضوء على البيانات التي تبرز — بالتحديد القيم الأعلى من المتوسط في نطاق معين. إليك الأسباب التي قد تدفعك لاستخدامه:
1. اكتشاف الاتجاهات بسرعة: يساعدك على تحديد القيم عالية الأداء على الفور دون حساب المتوسطات يدويًا أو فحص الأرقام.
1. تبسيط تحليل البيانات: لا تحتاج إلى حساب أو إدخال أي صيغ — إنها طريقة تلقائية لتطبيق التنسيق القائم على المنطق، مما يوفر الوقت.
1. تحسين الجاذبية البصرية: يساعد الترميز بالألوان على جعل جدول البيانات أسهل في القراءة وأكثر جاذبية بصريًا، خاصة أثناء العروض التقديمية.
1. دعم اتخاذ القرار: تحديد القيم فوق المتوسط بسرعة يمكن أن يدفع إلى إجراءات، مثل مكافأة الم.Lowperformers أو التحقيق في سبب تفوق بعض المنتجات على الأخرى.

## **كيفية إضافة التنسيق الشرطي فوق المتوسط باستخدام إكسل**
لإضافة التنسيق الشرطي فوق المتوسط في إكسل، إليك الخطوة خطوة:

1. حدد نطاق الخلايا التي تريد تطبيق التنسيق عليها. على سبيل المثال: A1:A20.
1. انتقل إلى علامة التبويب الصفحة الرئيسية على الشريط.
1. انقر على التنسيق الشرطي في مجموعة الأنماط.
1. مرر فوق قواعد العلو/السفل.
1. انقر فوق فوق المتوسط...
1. في مربع الحوار الذي يظهر: سوف يكتشف تلقائيًا "تنسق الخلايا التي فوق المتوسط." يمكنك تغيير نمط التنسيق بالنقر على السهم المنسدل بجانب (على سبيل المثال، اختيار تعبئة لون أو تنسيق مخصص).
1. انقر على موافق. ستتم إبراز جميع الخلايا في النطاق الذي حددته والتي تفوق متوسط هذا النطاق.


## **كيفية إضافة تنسيق شرطي فوق المتوسط باستخدام Aspose.Cells لـ Python via .NET**

يدعم Aspose.Cells لـ Python via .NET بشكل كامل التنسيق الشرطي المقدم من قبل Microsoft Excel 2007 والإصدارات الأحدث في تنسيق XLSX على الخلايا أثناء وقت التشغيل. يُظهر هذا المثال تمرينًا على التنسيق الشرطي فوق المتوسط باستخدام مجموعات مختلفة من السمات.

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

        self.add_above_average()
        self.add_above_average2()
        self.add_above_average3()        

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

    def add_above_average(self):
        conds = self.get_format_condition("A11:C12", Color.tomato)
        idx = conds.add_condition(FormatConditionType.ABOVE_AVERAGE)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID

    def add_above_average2(self):
        conds = self.get_format_condition("A13:C14", Color.empty)
        idx = conds.add_condition(FormatConditionType.ABOVE_AVERAGE)
        cond = conds[idx]
        cond.above_average.is_above_average = False
        cond.above_average.is_equal_average = True
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID

    def add_above_average3(self):
        conds = self.get_format_condition("A15:C16", Color.empty)
        idx = conds.add_condition(FormatConditionType.ABOVE_AVERAGE)
        cond = conds[idx]
        cond.above_average.is_above_average = False
        cond.above_average.is_equal_average = True
        cond.above_average.std_dev = 3
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID

```
{{< app/cells/assistant language="python-net" >}}
