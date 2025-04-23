---
title: Группировать поля сводной таблицы в сводной таблице с помощью C++
linktitle: Группировка полей сводной таблицы
type: docs
weight: 80
url: /ru/cpp/group-pivot-fields-in-the-pivot-table/
description: Узнайте, как группировать поля сводной таблицы с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

В Microsoft Excel можно группировать поля сводной таблицы. Когда имеется большое количество данных, связанных с полем сводной таблицы, часто полезно сгруппировать их по разделам. Aspose.Cells также предоставляет эту функцию с помощью метода [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfield/groupby/).

## **Группировка полей сводной таблицы**

Приведенный ниже образец кода загружает [образец файла Excel](64716818.xlsx) и выполняет группировку по первому полю сводной таблицы с помощью метода [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfield/groupby/). Затем он обновляет и вычисляет данные сводной таблицы и сохраняет книгу Excel как [выходной файл Excel](64716817.xlsx). На скриншоте показан эффект образца кода на образцовый файл Excel. Как видно на скриншоте, первое поле сводной таблицы теперь сгруппировано по месяцам и кварталам.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Образец кода**

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
