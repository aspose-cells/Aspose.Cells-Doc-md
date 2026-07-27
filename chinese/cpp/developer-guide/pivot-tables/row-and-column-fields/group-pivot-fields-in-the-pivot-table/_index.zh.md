---
title: 用 C++ 在数据透视表中分组字段
linktitle: 在透视表中对透视字段进行分组
type: docs
weight: 80
url: /zh/cpp/group-pivot-fields-in-the-pivot-table/
description: 学习如何使用 Aspose.Cells for C++ 在数据透视表中分组字段。
---

## **可能的使用场景**

Microsoft Excel允许您对透视表的透视字段进行分组。当与透视字段相关的数据量很大时，通常将它们分组成部分很有用。Aspose.Cells也提供使用[**PivotTable.GroupBy()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfield/groupby/)方法的此功能。

## **在透视表中对透视字段进行分组**

以下示例代码加载[示例Excel文件](64716818.xlsx)，并使用[**PivotTable.GroupBy()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfield/groupby/)方法对第一个透视字段执行分组。然后刷新和计算透视表的数据，并将工作簿保存为[输出Excel文件](64716817.xlsx)。屏幕截图显示了示例代码对示例Excel文件的效果。如屏幕截图所示，第一个透视字段现在按月份和季度分组。

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **示例代码**

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
