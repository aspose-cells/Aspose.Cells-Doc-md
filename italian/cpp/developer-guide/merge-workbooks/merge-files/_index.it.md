---
title: Unisci file con C++
linktitle: Unire file
type: docs
weight: 20
url: /it/cpp/merge-files/
description: Impara come unire file Excel in modo efficiente usando Aspose.Cells for C++.
---

## **Introduzione**

Aspose.Cells fornisce diversi metodi per unire file. Per file semplici con dati, formattazione e formule, si può usare il metodo [**Workbook.Combine()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/combine/) per combinare diversi libri di lavoro, e il metodo [**Worksheet.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/copy/) per copiare fogli di lavoro in un nuovo libro. Questi metodi sono facili da usare ed efficienti, ma se hai molti file da unire, potresti trovare che richiedono molte risorse di sistema. Per evitarlo, usa il metodo statico [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/), un modo più efficiente per unire diversi file.

## **Unire file utilizzando Aspose.Cells**

Il seguente esempio di codice illustra come unire grandi file usando il metodo [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/). Prende due file semplici ma grandi, Book1.xls e Book2.xls. I file contengono solo dati formattati e formule.

{{% alert color="primary" %}}

Il metodo [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/) supporta solo l'unione di dati, stili, formattazione e formule. Oggetti come grafici, immagini, commenti o altri oggetti potrebbero non essere uniti usando questo metodo. Inoltre, viene utilizzato un file cache per memorizzare dati temporanei per il processo.

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
