---
title: Gruppare i campi pivot nella tabella pivot con C++
linktitle: Raggruppa i campi pivot nella tabella pivot
type: docs
weight: 80
url: /it/cpp/group-pivot-fields-in-the-pivot-table/
description: Impara come raggruppare i campi pivot in una tabella pivot usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

Microsoft Excel consente di raggruppare i campi pivot della tabella pivot. Quando c'è una grande quantità di dati relativi a un campo pivot, è spesso utile raggrupparli in sezioni. Aspose.Cells fornisce anche questa funzionalità utilizzando il metodo [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfield/groupby/).

## **Raggruppa i campi pivot nella tabella pivot**

Il codice di esempio seguente carica il [file Excel di esempio](64716818.xlsx) e esegue il raggruppamento sul primo campo pivot utilizzando il metodo [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfield/groupby/). Aggiorna quindi e calcola i dati della tabella pivot e salva il foglio di calcolo come [file Excel di output](64716817.xlsx). Lo screenshot mostra l'effetto del codice di esempio sul file Excel di esempio. Come si può vedere dallo screenshot, il primo campo pivot è ora raggruppato per mesi e trimestri.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Codice di Esempio**

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
