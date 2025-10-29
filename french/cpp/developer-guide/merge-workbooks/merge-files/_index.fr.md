---
title: Fusionner des fichiers avec C++
linktitle: Fusionner des fichiers
type: docs
weight: 20
url: /fr/cpp/merge-files/
description: Découvrez comment fusionner efficacement des fichiers Excel en utilisant Aspose.Cells for C++.
---

## **Introduction**

Aspose.Cells offre plusieurs méthodes pour fusionner des fichiers. Pour des fichiers simples avec données, formatage, et formules, la méthode [**Workbook.Combine()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/combine/) peut être utilisée pour combiner plusieurs classeurs, et la méthode [**Worksheet.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/copy/) pour copier des feuilles de calcul dans un nouveau classeur. Ces méthodes sont faciles à utiliser et efficaces, mais si vous avez beaucoup de fichiers à fusionner, vous constaterez qu'elles consomment beaucoup de ressources système. Pour éviter cela, utilisez la méthode statique [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/), une façon plus efficace de fusionner plusieurs fichiers.

## **Fusionner des fichiers à l'aide d'Aspose.Cells**

Le code d'échantillon suivant illustre comment fusionner de grands fichiers en utilisant la méthode [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/). Il prend deux fichiers simples mais volumineux, Book1.xls et Book2.xls. Les fichiers contiennent uniquement des données formatées et des formules.

{{% alert color="primary" %}}

La méthode [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/) ne prend en charge que la fusion de données, styles, mise en forme, et formules. Des objets tels que des graphiques, images, commentaires ou autres objets pourraient ne pas être fusionnés avec cette méthode. De plus, un fichier en cache est utilisé pour stocker des données temporaires durant le processus.

{{% /alert %}}

```c++
#include <iostream>
#include <string>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
	Aspose::Cells::Startup();

	U16String srcDir(u"../Data/01_SourceDirectory/");
	U16String outDir(u"../Data/02_OutputDirectory/");

	Vector<U16String> data{
	  srcDir + u"Book1.xls",
	  srcDir + u"Book2.xls"
	};

	U16String cacheFile = outDir + u"test.txt";
	U16String dest = outDir + u"output.xlsx";

	CellsHelper::MergeFiles(data, cacheFile, dest);

	Workbook workbook(dest);

	WorksheetCollection sheets = workbook.GetWorksheets();
	int count = sheets.GetCount();
	for (int idx = 0; idx < count; ++idx)
	{
		Worksheet sheet = sheets.Get(idx);
		U16String sheetName = U16String(u"Sheet_");
		U16String numStr = U16String(std::to_string(idx+1).c_str());
		sheet.SetName(sheetName + numStr);
	}

	workbook.Save(dest);

	Aspose::Cells::Cleanup();
	return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
