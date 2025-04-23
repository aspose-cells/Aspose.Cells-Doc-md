---
title: Объединение файлов с помощью C++
linktitle: Объединить файлы
type: docs
weight: 20
url: /ru/cpp/merge-files/
description: Узнайте, как эффективно объединять файлы Excel, используя Aspose.Cells for C++.
---

## **Введение**

Aspose.Cells предоставляет различные способы объединения файлов. Для простых файлов с данными, форматированием и формулами можно использовать метод [**Workbook.Combine()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/combine/) для объединения нескольких книг, а метод [**Worksheet.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/copy/) — для копирования листов в новую книгу. Эти методы просты в использовании и эффективны, но при большом количестве файлов их использование может потреблять много ресурсов системы. Чтобы этого избежать, используйте статический метод [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/), более эффективный способ объединения нескольких файлов.

## **Объединение файлов с помощью Aspose.Cells**

Следующий пример показывает, как объединять большие файлы, используя метод [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/). Он берет два простых, но больших файла, Book1.xls и Book2.xls. Эти файлы содержат отформатированные данные и формулы.

{{% alert color="primary" %}}

Метод [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/) поддерживает только объединение данных, стилей, форматирования и формул. Объекты, такие как диаграммы, картинки, комментарии или другие объекты, могут не объединяться при использовании этого метода. Более того, используется кешированный файл для временного хранения данных процесса.

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
