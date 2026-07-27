---
title: Grouper les champs de pivot dans le tableau croisé dynamique avec C++
linktitle: Regrouper les champs de tableau croisé dynamique dans le tableau croisé dynamique
type: docs
weight: 80
url: /fr/cpp/group-pivot-fields-in-the-pivot-table/
description: Apprenez comment grouper les champs de pivot dans un tableau croisé dynamique en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Microsoft Excel vous permet de regrouper les champs de tableau croisé dynamique. Lorsqu'il y a une grande quantité de données liées à un champ de tableau croisé dynamique, il est souvent utile de les regrouper en sections. Aspose.Cells fournit également cette fonctionnalité en utilisant la méthode [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfield/groupby/).

## **Grouper les champs du tableau croisé dynamique dans le tableau croisé dynamique**

Le code d'exemple suivant charge le [fichier Excel d'exemple](64716818.xlsx) et effectue un groupement sur le premier champ de tableau croisé dynamique en utilisant la méthode [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfield/groupby/). Ensuite, il actualise et calcule les données du tableau croisé dynamique et enregistre le classeur sous le nom de [fichier Excel de sortie](64716817.xlsx). La capture d'écran montre l'effet du code d'exemple sur le fichier Excel d'exemple. Comme vous pouvez le voir sur la capture d'écran, le premier champ de tableau croisé dynamique est maintenant regroupé par mois et par trimestres.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Code d'exemple**

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
