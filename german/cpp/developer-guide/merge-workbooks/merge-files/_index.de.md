---
title: Dateien mit C++ zusammenführen
linktitle: Dateien zusammenführen
type: docs
weight: 20
url: /de/cpp/merge-files/
description: Lernen Sie, wie Sie Excel Dateien effizient mit Aspose.Cells for C++ zusammenführen.
---

## **Einführung**

Aspose.Cells bietet verschiedene Möglichkeiten zum Zusammenführen von Dateien. Für einfache Dateien mit Daten, Formatierungen und Formeln kann die [**Workbook.Combine()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/combine/)-Methode verwendet werden, um mehrere Arbeitsmappen zu kombinieren, und die [**Worksheet.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/copy/)-Methode, um Arbeitsblätter in eine neue Arbeitsmappe zu kopieren. Diese Methoden sind einfach und effektiv, aber wenn Sie viele Dateien zusammenführen müssen, könnten sie systemintensiv sein. Um dies zu vermeiden, verwenden Sie die statische Methode [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/), die effizienter ist, um mehrere Dateien zu zusammenzuführen.

## **Dateien mit Aspose.Cells zusammenführen**

Der folgende Beispielcode zeigt, wie große Dateien mit der [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/)-Methode zusammengeführt werden. Es nimmt zwei einfache, aber große Dateien, Book1.xls und Book2.xls. Die Dateien enthalten formatierten Daten und Formeln.

{{% alert color="primary" %}}

Die [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/)-Methode unterstützt nur das Zusammenführen von Daten, Styles, Formatierungen und Formeln. Objekte wie Diagramme, Bilder, Kommentare oder andere Objekte werden möglicherweise nicht mit dieser Methode zusammengeführt. Außerdem wird eine zwischengespeicherte Datei verwendet, um temporäre Daten für den Vorgang zu speichern.

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
