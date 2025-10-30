---
title: Foga samman filer med C++
linktitle: Slå samman filer
type: docs
weight: 20
url: /sv/cpp/merge-files/
description: Lär dig hur du effektivt sammanfogar Excel filer med Aspose.Cells for C++.
---

## **Introduktion**

Aspose.Cells tillhandahåller olika metoder för att slå ihop filer. För enkla filer med data, formatering och formler kan [**Workbook.Combine()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/combine/)-metoden användas för att kombinera flera arbetsböcker, och [**Worksheet.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/copy/)-metoden för att kopiera kalkylblad till en ny arbetsbok. Dessa metoder är enkla att använda och effektiva, men om du har många filer att sammanfoga kan du märka att de tar mycket systemresurser. För att undvika detta, använd den [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/) statiska metoden, ett mer effektivt sätt att slå ihop flera filer.

## **Slå samman filer med hjälp av Aspose.Cells**

Följande kodexempel visar hur man sammanfogar stora filer med [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/)-metoden. Det tar två enkla men stora filer, Book1.xls och Book2.xls. Filmerna innehåller endast formaterad data och formler.

{{% alert color="primary" %}}

Metoden [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/) stöder endast sammanslagning av data, stilar, formatering och formler. Objekt som diagram, bilder, kommentarer eller andra objekt kanske inte kan slås samman med denna metod. Dessutom används en cache-fil för att lagra tillfällig data för processen.

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
