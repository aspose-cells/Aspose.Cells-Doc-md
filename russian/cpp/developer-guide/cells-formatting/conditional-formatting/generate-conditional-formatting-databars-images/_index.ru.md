---
title: Создание изображений условных форматированных DataBars с помощью C++
linktitle: Генерация изображений полос данных условного форматирования
description: Aspose.Cells — это библиотека C++ для работы с электронными таблицами. Она поддерживает создание условных графиков данных и изображений, позволяя пользователям настраивать отображение таблицы в зависимости от значения ячеек. В этой статье рассказывается, как использовать библиотеку Aspose.Cells для генерации условных графиков данных и изображений.
keywords: Aspose.Cells, Условное форматирование, Панели данных, Изображения, Таблицы
type: docs
weight: 40
url: /ru/cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Иногда вам может потребоваться создать изображения условного форматирования панелей данных. Вы можете использовать метод Aspose.Cells [**DataBar.ToImage()**](https://reference.aspose.com/cells/cpp/aspose.cells/databar/toimage/) для создания этих изображений. В этой статье показано, как создать изображение панели данных с помощью Aspose.Cells.

{{% /alert %}}

Следующий пример кода создает изображение DataBar для ячейки C1. Он сначала обращается к объекту условного форматирования ячейки, затем через этот объект — к [**DataBar**](https://reference.aspose.com/cells/cpp/aspose.cells/databar/) объекту и использует его метод [**ToImage()**](https://reference.aspose.com/cells/cpp/aspose.cells/databar/toimage/) для генерации изображения ячейки. В конце он сохраняет изображение на диск.

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"sampleGenerateDatabarImage.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cell cell = worksheet.GetCells().Get(u"C1");

    int idx = worksheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcc = worksheet.GetConditionalFormattings().Get(idx);
    fcc.AddCondition(FormatConditionType::DataBar);
    fcc.AddArea(CellArea::CreateCellArea(u"C1", u"C4"));

    DataBar dbar = fcc.Get(0).GetDataBar();

    ImageOrPrintOptions opts;
    opts.SetImageType(ImageType::Png);

    Vector<uint8_t> imgBytes = dbar.ToImage(cell, opts);

    std::ofstream outFile((outDir + u"outputGenerateDatabarImage.png").ToUtf8(), std::ios::binary);
    outFile.write(reinterpret_cast<const char*>(imgBytes.GetData()), imgBytes.GetLength());
    outFile.close();

    Aspose::Cells::Cleanup();
}
```
