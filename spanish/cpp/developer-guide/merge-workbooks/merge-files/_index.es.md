---
title: Fusionar archivos con C++
linktitle: Combinar archivos
type: docs
weight: 20
url: /es/cpp/merge-files/
description: Aprende cómo fusionar archivos de Excel de manera eficiente usando Aspose.Cells for C++.
---

## **Introducción**

Aspose.Cells ofrece diferentes maneras de fusionar archivos. Para archivos simples con datos, formato y fórmulas, se puede usar el método [**Workbook.Combine()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/combine/) para combinar varios libros de trabajo, y el método [**Worksheet.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/copy/) para copiar hojas de trabajo en un nuevo libro. Estos métodos son fáciles de usar y efectivos, pero si tienes muchos archivos para fusionar, puede que tomen muchos recursos del sistema. Para evitar esto, usa el método estático [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/), una forma más eficiente de fusionar varios archivos.

## **Combina archivos usando Aspose.Cells**

El siguiente código de ejemplo ilustra cómo fusionar archivos grandes usando el método [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/). Toma dos archivos simples pero grandes, Book1.xls y Book2.xls. Los archivos contienen datos formateados y fórmulas solamente.

{{% alert color="primary" %}}

El método [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/) solo admite fusionar datos, estilos, formato y fórmulas. Objetos como gráficos, imágenes, comentarios u otros objetos pueden no fusionarse usando este método. Además, se usa un archivo en caché para almacenar datos temporales del proceso.

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
