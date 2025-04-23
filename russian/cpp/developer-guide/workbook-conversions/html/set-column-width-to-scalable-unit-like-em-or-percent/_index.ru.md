---
title: Установить ширину столбца в масштабируемую единицу, такую как em или проценты, с помощью C++
linktitle: Установить ширину столбца в масштабируемые единицы, такие как em или проценты
type: docs
weight: 130
url: /ru/cpp/set-column-width-to-scalable-unit-like-em-or-percent/
description: Узнайте, как устанавливать ширину столбца в масштабируемых единицах, таких как em или проценты, используя Aspose.Cells for C++.
---

Создание HTML-файла из электронной таблицы очень распространено. Размер столбцов определен в "pt", который работает во многих случаях. Однако может возникнуть ситуация, когда этот фиксированный размер может быть необязательным. Например, если ширина панели контейнера составляет 600 пикселей, где отображается эта HTML-страница. В этом случае может появиться горизонтальная полоса прокрутки, если ширина созданной таблицы больше. Было необходимо изменить этот фиксированный размер на масштабируемую единицу, такую как em или процент, для лучшего представления. Следующий образец кода может быть использован, где [**HtmlSaveOptions.GetWidthScalable()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getwidthscalable/) установлен в **true** для создания масштабируемой ширины.

Образец исходного файла и выходные файлы можно загрузить по следующим ссылкам:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load sample source file
    Workbook wb(srcDir + u"sampleForScalableColumns.xlsx");

    // Specify Html Save Options
    HtmlSaveOptions options;

    // Set the property for scalable width
    options.SetWidthScalable(true);

    // Specify image save format
    options.SetExportImagesAsBase64(true);

    // Save the workbook in Html format with specified Html Save Options
    wb.Save(outDir + u"outsampleForScalableColumns.html", options);

    std::cout << "Workbook saved successfully with scalable columns!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
