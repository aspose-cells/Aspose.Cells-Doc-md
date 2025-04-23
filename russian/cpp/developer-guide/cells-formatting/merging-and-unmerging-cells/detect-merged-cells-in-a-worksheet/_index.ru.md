---
title: Обнаружение объединённых ячеек в листе с C++
linktitle: Обнаружение объединённых ячеек
description: Aspose.Cells — это библиотека C++ для работы с файлами таблиц. Она поддерживает обнаружение объединённых ячеек в листе, что облегчает пользователям идентификацию и управление этими ячейками. В этой статье будет описано, как использовать библиотеку Aspose.Cells для обнаружения объединённых ячеек.
keywords: Aspose.Cells, Рабочий лист, Объединение ячеек, Обнаружение, Определение, Операции
type: docs
weight: 80
url: /ru/cpp/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

Эта статья предоставляет информацию о том, как получить области объединенных ячеек в рабочем листе.

Aspose.Cells позволяет получить области объединенных ячеек в рабочем листе. Вы также можете снова разделить их. В этой статье показан самый простой код с использованием **API Aspose.Cells** для выполнения этой задачи.

{{% /alert %}}

Компонент предоставляет метод [**Cells::GetMergedAreas()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmergedareas/), который может получать все объединённые ячейки. Следующий пример показывает, как обнаружить объединённые ячейки в листе.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"SampleInput.xlsx");

    Worksheet wkSheet = workbook.GetWorksheets().Get(u"Sheet2");

    wkSheet.GetCells().Clear();

    Vector<CellArea> areas = wkSheet.GetCells().GetMergedAreas();

    for (int i = 0; i < areas.GetLength(); ++i)
    {
        int frow = areas[i].StartRow;
        int fcol = areas[i].StartColumn;
        int erow = areas[i].EndRow;
        int ecol = areas[i].EndColumn;

        int trows = erow - frow + 1;
        int tcols = ecol - fcol + 1;

        wkSheet.GetCells().UnMerge(frow, fcol, trows, tcols);
    }

    U16String outputPath = outDir + u"MergeTrial.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Worksheet processing completed successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```
