---
title: Конвертация ревизий XLSB в XLSM с помощью C++
linktitle: Преобразование ревизии из XLSB в XLSM
type: docs
weight: 290
url: /ru/cpp/convert-revision-of-xlsb-to-xlsm/
description: Узнайте, как преобразовать ревизии XLSB в формат XLSM с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}} 

Aspose.Cells теперь полностью поддерживает преобразование ревизий XLSB в XLSM. Ревизии находятся внутри папки \xl\revisions. Чтобы просмотреть их, измените расширение файла XLSB на ZIP. Папка \xl\revisions содержит файлы с расширениями .bin.

При конвертации XLSB файла в XLSM с помощью Aspose.Cells эти .bin файлы успешно преобразуются в .xml файлы, как показано на двух скриншотах.

{{% /alert %}} 

Следующий пример показывает, как конвертировать XLSB в XLSM с помощью Aspose.Cells.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsb";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Save Workbook to XLSM format
    workbook.Save(outDir + u"output_out.xlsm", SaveFormat::Xlsm);

    std::cout << "Workbook saved successfully in XLSM format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
