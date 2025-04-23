---
title: إنشاء وتعديل أو إزالة السيناريوهات من أوراق العمل باستخدام بايثون via .NET.
linktitle: إدارة السيناريوهات
type: docs
weight: 190
url: /ar/python-net/create-manipulate-or-remove-scenarios-from-worksheets/
description: تعلم كيفية إنشاء وتعديل وحذف السيناريوهات في أوراق إكسل برمجياً باستخدام API لـ Aspose.Cells لبايثون via .NET.
keywords: سيناريوهات إكسل بايثون، إدارة سيناريوهات ورقة العمل، إضافة سيناريو، حذف سيناريو، تعديل سيناريوهات.
---

{{% alert color="primary" %}}

أحياناً تحتاج إلى إنشاء أو تعديل أو حذف سيناريوهات في جداول البيانات. السيناريو هو نموذج مسمى 'ماذا لو؟' يتضمن خلايا إدخال متغيرة مرتبطة بواسطة صيغة واحدة أو أكثر. قبل إنشاء سيناريو، قم بتصميم ورقة العمل بحيث تحتوي على صيغة واحدة على الأقل تعتمد على خلايا يمكن قبول قيم مختلفة فيها. يوضح هذا المثال كيفية إدارة السيناريوهات في أوراق العمل باستخدام Aspose.Cells لبايثون via .NET.

{{% /alert %}}

توفر Aspose.Cells العديد من الفئات للعمل مع السيناريوهات:
- [**ScenarioCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/scenariocollection/)
- [**Scenario**](https://reference.aspose.com/cells/python-net/aspose.cells/scenario/)
- [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/scenarioinputcellcollection/)
- [**ScenarioInputCell**](https://reference.aspose.com/cells/python-net/aspose.cells/scenarioinputcell/)

استخدم الخاصية [**Worksheet.scenarios**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/scenarios/) للوصول إلى السيناريوهات. يوضح الكود التالي كيفية:
1. فتح ملف إكسل يحتوي على سيناريوهات
2. إزالة سيناريو موجود مسبقاً
3. إضافة سيناريو جديد

4. حفظ ملف العمل بعد التعديلات

```python
import os
from aspose.cells import Workbook

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Instantiate the Workbook and load an Excel file
workbook = Workbook(os.path.join(data_dir, "aspose-sample.xlsx"))
# Access first worksheet
worksheet = workbook.worksheets[0]

if len(worksheet.scenarios) > 0:
    # Remove the existing first scenario from the sheet
    worksheet.scenarios.remove_at(0)

    # Create a scenario
    i = worksheet.scenarios.add("MyScenario")
    # Get the scenario
    scenario = worksheet.scenarios[i]
    # Add comment to it
    scenario.comment = "Test sceanrio is created."
    # Get the input cells for the scenario
    sic = scenario.input_cells
    # Add the scenario on B4 (as changing cell) with default value
    sic.add(3, 1, "1100000")

    output_path = os.path.join(data_dir, "outBk_scenarios1.out.xlsx")

    # Save the Excel file
    workbook.save(output_path)
    print(f"\nProcess completed successfully.\nFile saved at {output_path}")
```

