---
title: كيفية إضافة تنسيق مشروط لخطوط البيانات
description: كيفية استخدام مكتبة Aspose.Cells لـ Python via .NET لتطبيق تنسيق البيانات الشرطي باستخدام أشرطة البيانات. من خلال تعديل هذه المعايير، يكون لديك مزيد من التحكم في مظهر الخلايا ومظهرها.
keywords: Aspose.Cells، تنسيق البيانات الشرطي باستخدام أشرطة البيانات، بايثون، شرطي، تنسيق
type: docs
weight: 70
url: /ar/python-net/how-to-add-databars-conditional-formatting/
---

## **سيناريوهات الاستخدام المحتملة**
استخدام خطوط البيانات في التنسيق الشرطي هو وسيلة قوية (ومرئية!) لفهم بياناتك بسرعة.

1. مقارنة بصرية للقيم: تحوّل خطوط البيانات الأرقام إلى خطوط أفقية، مما يسهل مقارنة القيم جنبًا إلى جنب — مثل مخطط بياني صغير داخل خلاياك!
1. التعرف على الأنماط فورًا: يمكنك أن ترى على الفور القمم، والأدنى، والقيم الشاذة بدون تصنيف أو مسح الأرقام.
1. تحسين قابلية القراءة: مفيد بشكل خاص في الجداول الطويلة — يقلل من العبء المعرفي ويساعدك على فهم الاتجاهات الرئيسية بسرعة.
1. ديناميكي وواقعي: مع تغير القيم، تتحدث الأشرطة تلقائيًا — ممتاز لتتبع المؤشرات الحية، التقدم، أو مؤشرات الأداء الرئيسية.
1. لوحات معلومات ذات مظهر احترافي: تضيف مظهرًا نظيفًا ومر modern وpolished للتقارير أو لوحات المعلومات.

## **كيفية إضافة تنسيق مشروط لخطوط البيانات باستخدام Excel**
لإضافة تنسيق مشروط لخطوط البيانات في Excel، إليك الخطوات خطوة بخطوة:

1. حدد نطاق البيانات الخاص بك، مثلاً: C2:C20 — يمكن أن تكون مبيعات، أو نتائج، أو قيم التقدم.
1. انتقل إلى علامة التبويب الصفحة الرئيسية على الشريط.
1. انقر على التنسيق الشرطي في مجموعة الأساليب.
1. مرر فوق خطوط البيانات.
1. اختر نمطًا: تعبئة تدرجية (تتلاشى الأشرطة من اليسار إلى اليمين) وتعبئة صلبة (الأشرطة لها لون موحد).
1. انقر على النمط الذي تفضله — وقد انتهيت!

## **كيفية إضافة تنسيق البيانات الشرطي باستخدام أشرطة البيانات باستخدام Aspose.Cells لـ Python via .NET**

يدعم Aspose.Cells لـ Python via .NET تمامًا التنسيق الشرطي المقدم من قبل Microsoft Excel 2007 والإصدارات اللاحقة بصيغة XLSX على الخلايا عند التشغيل. يُظهر هذا المثال تمرينًا لتنسيق البيانات باستخدام أشرطة البيانات مع مجموعات مختلفة من السمات.

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

        self.add_data_bar1()
        self.add_data_bar2()

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "Testoutput.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)    

    def add_data_bar2(self):
        conds = self.get_format_condition("E3:G4", Color.light_green)
        idx = conds.add_condition(FormatConditionType.DATA_BAR)
        cond = conds[idx]
        cond.data_bar.color = Color.orange
        cond.data_bar.min_cfvo.type = FormatConditionValueType.PERCENTILE
        cond.data_bar.min_cfvo.value = 30.78
        cond.data_bar.show_value = False

    def add_data_bar1(self):
        conds = self.get_format_condition("E1:G2", Color.yellow_green)
        idx = conds.add_condition(FormatConditionType.DATA_BAR)
        cond = conds[idx]

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

{{< app/cells/assistant language="python-net" >}}
