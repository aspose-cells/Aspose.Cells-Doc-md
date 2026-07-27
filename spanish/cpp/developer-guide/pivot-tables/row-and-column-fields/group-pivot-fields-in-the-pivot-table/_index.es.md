---
title: Agrupar campos dinámicos en la tabla dinámica con C++
linktitle: Agrupar campos de pivote en la tabla dinámica
type: docs
weight: 80
url: /es/cpp/group-pivot-fields-in-the-pivot-table/
description: Aprenda cómo agrupar campos dinámicos en una tabla dinámica usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Microsoft Excel te permite agrupar campos de tabla dinámica de la tabla dinámica. Cuando hay una gran cantidad de datos relacionados con un campo de tabla dinámica, a menudo es útil agruparlos en secciones. Aspose.Cells también proporciona esta función utilizando el método [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfield/groupby/).

## **Agrupar campos de la tabla dinámica**

El siguiente código de muestra carga el [archivo Excel de muestra](64716818.xlsx) y realiza agrupaciones en el primer campo de tabla dinámica utilizando el método [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfield/groupby/). Luego actualiza y calcula los datos de la tabla dinámica y guarda la hoja de cálculo como [archivo Excel de salida](64716817.xlsx). La captura de pantalla muestra el efecto del código de muestra en el archivo Excel de muestra. Como se puede ver en la captura de pantalla, el primer campo de tabla dinámica está ahora agrupado por meses y trimestres.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Código de muestra**

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
