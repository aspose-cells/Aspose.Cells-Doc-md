---
title: Gruppera pivotelement i pivot tabellen med C++
linktitle: Gruppera Pivot Fields i PivotTable
type: docs
weight: 80
url: /sv/cpp/group-pivot-fields-in-the-pivot-table/
description: Lär dig hur du grupperar pivotelement i en pivot tabell med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Microsoft Excel tillåter dig att gruppera pivottabellens pivotfält. När det finns en stor mängd data relaterad till ett pivotfält är det ofta användbart att gruppera dem i avsnitt. Aspose.Cells tillhandahåller också denna funktion med hjälp av [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfield/groupby/)-metoden.

## **Gruppera Pivot Fields i PivotTable**

Följande exempelkod laddar den [provpå Excel-filen](64716818.xlsx) och utför gruppering på det första pivotfältet med [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfield/groupby/)-metoden. Sedan uppdaterar och beräknar det pivotabellens data och sparar arbetsboken som [utdata Excel-fil](64716817.xlsx). Skärmbilden visar effekten av exempelkoden på den provpå Excel-filen. Som du kan se på skärmbilden är det första pivotfältet nu grupperat efter månader och kvartal.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Exempelkod**

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
