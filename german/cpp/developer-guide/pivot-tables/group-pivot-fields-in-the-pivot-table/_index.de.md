---
title: Gruppierung von Pivot Feldern in der PivotTable mit C++
linktitle: Gruppieren von Pivot Feldern in der Pivot Tabelle
type: docs
weight: 80
url: /de/cpp/group-pivot-fields-in-the-pivot-table/
description: Erfahren Sie, wie Sie Pivot Felder mit Aspose.Cells for C++ in einer Pivot Tabelle gruppieren.
---

## **Mögliche Verwendungsszenarien**

Microsoft Excel ermöglicht es Ihnen, Pivot-Felder der Pivot-Tabelle zu gruppieren. Wenn eine große Menge von Daten mit einem Pivot-Feld verbunden ist, ist es oft nützlich, sie in Abschnitte zu gruppieren. Aspose.Cells bietet diese Funktion auch mit der Methode [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfield/groupby/).

## **Gruppieren von Pivot-Feldern in der Pivot-Tabelle**

Der folgende Beispielcode lädt die [Beispieldatei Excel](64716818.xlsx) und führt eine Gruppierung des ersten Pivot-Felds mit der Methode [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfield/groupby/) durch. Anschließend aktualisiert und berechnet er die Daten der Pivot-Tabelle und speichert die Arbeitsmappe als [Ausgabedatei Excel](64716817.xlsx). Der Screenshot zeigt die Auswirkung des Beispielcodes auf die Beispieldatei Excel. Wie im Screenshot zu sehen ist, ist das erste Pivot-Feld nun nach Monaten und Quartalen gruppiert.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Beispielcode**

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
