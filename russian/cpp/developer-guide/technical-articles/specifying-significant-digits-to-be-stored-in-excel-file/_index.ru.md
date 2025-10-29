---
title: Указание значительных цифр для хранения в Excel файле с помощью C++
linktitle: Указание значительных цифр
type: docs
weight: 30
url: /ru/cpp/specifying-significant-digits-to-be-stored-in-excel-file/
description: Узнайте, как указывать значительные цифры, которые необходимо сохранять в файлах Excel, с помощью Aspose.Cells и C++.
---

## **Возможные сценарии использования**

По умолчанию Aspose.Cells сохраняет 17 значимых цифр для чисел с плавающей точкой внутри файла Excel, в отличие от MS-Excel, который сохраняет только 15 значимых цифр. Вы можете изменить стандартное поведение Aspose.Cells с 17 на 15 значимых цифр, используя свойство [**GetSignificantDigits()**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/getsignificantdigits/).

## **Указание значащих разрядов для хранения в файле Excel**

Следующий пример кода принуждает Aspose.Cells использовать 15 значимых цифр при сохранении чисел с плавающей точкой внутри файла Excel. Проверьте [выходной файл Excel](22774105.xlsx). Поменяйте его расширение на .zip, распакуйте, и вы увидите, что внутри файла сохранено только 15 значимых цифр. Следующий скриншот показывает эффект свойства [**GetSignificantDigits()**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/getsignificantdigits/) на выходном файле Excel.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Образец кода**

```cpp
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

    // By default, Aspose.Cells stores 17 significant digits unlike
    // MS-Excel which stores only 15 significant digits
    CellsHelper::SetSignificantDigits(15);

    // Create workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell c = worksheet.GetCells().Get(u"A1");

    // Put double value, only 15 significant digits as specified by
    // CellsHelper.SignificantDigits above will be stored in excel file just like MS-Excel does
    c.PutValue(1234567890.123451711);

    // Save the workbook
    workbook.Save(outDir + u"out_SignificantDigits.xlsx");

    std::cout << "Workbook saved successfully with significant digits set to 15!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
