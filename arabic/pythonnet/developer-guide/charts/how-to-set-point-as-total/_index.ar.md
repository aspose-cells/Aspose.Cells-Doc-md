---
title: كيفية تعيين نقطة على أنها إجمالي باستخدام Python.NET
linktitle: كيفية تعيين نقطة كإجمالي
type: docs
weight: 72
url: /ar/python-net/how-to-set-point-as-total/
description: تعلم كيفية تكوين النقاط الإجمالية في مخططات الشلال في Excel باستخدام Aspose.Cells لبايثون via .NET من خلال هذا الدليل خطوة بخطوة.
---

## **ما هو "تعيين نقطة كإجمالي" في مخطط Excel**

في بعض مخططات Excel مثل مخططات الشلال، تمثل بعض نقاط البيانات مجموعًا تراكميًا للقيم السابقة. يوضح هذا المقال كيفية تكوين هذه النقاط الإجمالية برمجيًا باستخدام Aspose.Cells.

## **مخطط الشلال يتطلب نقاط إجمالية**

![todo:image_alt_text](set-as-total1.png)

يُظهر مثال مخطط الشلال هذا أربع نقاط "إجمالي" يجب أن تجمع القيم السابقة. النقطة المميزة "إجمالي 2024" تظهر حالة إجمالي غير مكونة في الملف الأصلي. قم بتحميل ملف إكسل النموذجي [SampleSheet.xlsx](SampleSheet.xlsx) للمتابعة.

## **تكوين النقاط الإجمالية باستخدام Aspose.Cells لبايثون**

يوضح الرمز التالي تكوين النقاط الإجمالية بشكل صحيح:

```python
import aspose.cells as cells
from aspose.cells.charts import ChartType

# Load sample workbook
workbook = cells.Workbook("SampleSheet.xlsx")

try:
    # Access first worksheet and chart
    worksheet = workbook.worksheets[0]
    chart = worksheet.charts[0]

    # Verify chart type
    if chart.type == ChartType.WATERFALL:
        # Configure chart data range
        chart.set_data_range("A1:B8", True)

        # Customize series formatting
        chart.n_series.is_color_varied = True

        # Configure total points (0-based indices)
        total_points = [3, 5, 7]  # Points to mark as totals
        for i in total_points:
            point = chart.n_series.points[i]
            point.is_total = True

        # Save modified workbook
        workbook.save("output.xlsx")

except Exception as e:
    print(f"Error processing workbook: {str(e)}")
```

```python
import os
from aspose.cells import Workbook

file_path = ""
wb = Workbook(os.path.join(file_path, "SampleSheet.xlsx"))
worksheet = wb.worksheets[0]
chart = worksheet.charts.get("Graphiq5")

# Set some points as total column
# In this example, we set points 0, 4, 8, 12 as total
chart.n_series[0].layout_properties.subtotals = [0, 4, 8, 12]
wb.save(os.path.join(file_path, "output.xlsx"))
```

يعمل [ملف الإخراج](output.xlsx) الآن بشكل صحيح على تكوين النقاط الإجمالية:

![todo:image_alt_text](set-as-total2.png)

تفاصيل التنفيذ الرئيسية:
- استخدام فهارس تبدأ من 0 لبيانات النقاط
- ضبط خاصية `is_total` على كائنات `ChartPoint`
- ضمان تكوين نطاق البيانات بشكل صحيح
- التعامل مع التحقق من نوع المخطط

انظر [توثيق ChartPoint](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/) للخيارات المتقدمة في التكوين.
{{< app/cells/assistant language="python-net" >}}
