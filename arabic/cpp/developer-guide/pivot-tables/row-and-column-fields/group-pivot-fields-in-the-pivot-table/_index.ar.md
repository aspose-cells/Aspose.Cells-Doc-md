---
title: تجميع حقول Pivot في جدول Pivot باستخدام C++
linktitle: تجميع حقول الجدول المحوري في جدول الدوران
type: docs
weight: 80
url: /ar/cpp/group-pivot-fields-in-the-pivot-table/
description: تعلم كيف تقوم بتجميع حقول Pivot في جدول محوري باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

يسمح Microsoft Excel لك بتجميع حقول الجدول المحوري في الجدول المحوري. عند وجود كمية كبيرة من البيانات المتعلقة بحقل محوري، من النافع غالبًا تجميعها إلى أقسام. Aspose.Cells توفر أيضًا هذه الميزة باستخدام طريقة [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfield/groupby/).

## **تجميع حقول الجدول المحوري**

يقوم الكود العيني التالي بتحميل ملف الإكسل العيني وينفذ عمليات التجميع على الحقل المحوري الأول باستخدام طريقة [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfield/groupby/). ثم يقوم بتحديث وحساب بيانات الجدول المحوري ويحفظ الدفتر كملف إكسل جديد. توضح الصورة الناتجة تأثير الكود العيني على ملف الإكسل العيني. كما يظهر في الصورة، تم تجميع الحقل المحوري الأول الآن حسب الشهور والربع.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
	Aspose::Cells::Startup();

	U16String srcDir(u"../Data/01_SourceDirectory/");
	U16String outDir(u"../Data/02_OutputDirectory/");

	Workbook wb(srcDir + u"sampleGroupPivotFieldsInPivotTable.xlsx");

	Worksheet ws = wb.GetWorksheets().Get(1);

	PivotTable pt = ws.GetPivotTables().Get(0);

	Date dtStart{ 2023, 12, 31, 0, 0, 0, 0 };
	Date dtEnd{ 2025, 9, 5 , 0, 0, 0, 0 };

	Vector<PivotGroupByType> groupTypeList{
		 PivotGroupByType::Months,
		 PivotGroupByType::Quarters
	};

	PivotField field = pt.GetRowFields().Get(0);
	field.GroupBy(dtStart, dtEnd, groupTypeList, 1, true);

	pt.RefreshData();
	pt.CalculateData();

	wb.Save(outDir + u"outputGroupPivotFieldsInPivotTable2.xlsx");

	std::cout << "Pivot field grouped successfully." << std::endl;

	Aspose::Cells::Cleanup();
	return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
