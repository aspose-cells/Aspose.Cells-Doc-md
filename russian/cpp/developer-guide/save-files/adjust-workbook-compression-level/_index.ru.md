---
title: Настройка уровня сжатия рабочей книги с помощью C++
linktitle: Настройка уровня сжатия рабочей книги
type: docs
weight: 180
url: /ru/cpp/adjust-workbook-compression-level/
description: Узнайте, как настроить уровень сжатия рабочей книги с помощью Aspose.Cells for C++ для оптимизации размера файла и времени обработки.
---

## **Настройка уровня сжатия книги**

Разработчики могут настраивать уровень сжатия книги при работе с большими книгами. Разработчики могут отдавать предпочтение более низким размерам файлов над временем обработки или наоборот. Aspose.Cells предоставляет перечисление [**OoxmlCompressionType**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompressiontype/), которое можно использовать для установки уровня сжатия книги. Перечисление [**OoxmlCompressionType**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompressiontype/) предоставляет следующие члены.

- Level1: Самое быстрое, но наименее эффективное сжатие.
- Level2: Немного медленнее, но лучше, чем уровень 1.
- Level3: Немного медленнее, но лучше, чем уровень 2.
- Level4: Немного медленнее, но лучше, чем уровень 3.
- Level5: Немного медленнее, чем уровень 4, но с лучшим сжатием.
- Level6: Хороший баланс скорости и эффективности сжатия.
- Уровень7: Довольно хорошее сжатие!
- Уровень8: Лучшее сжатие, чем на уровне 7!
- Уровень9: Самое "лучшее" сжатие, где лучший означает наибольшее уменьшение размера входного потока данных. Это также самое медленное сжатие.

В следующем фрагменте кода демонстрируется использование перечисления [**OoxmlCompressionType**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompressiontype/) и сравнение времени преобразования для уровней 1, 6 и 9. Также можно сравнить размеры созданных файлов.

```cpp
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std::chrono;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the workbook
    Workbook workbook(srcDir + u"LargeSampleFile.xlsx");

    // Create XlsbSaveOptions object
    XlsbSaveOptions options;

    // Set compression level to 1 and save the workbook
    options.SetCompressionType(OoxmlCompressionType::Level1);
    auto start = high_resolution_clock::now();
    workbook.Save(outDir + u"LargeSampleFile_level_1_out.xlsb", options);
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(stop - start);
    std::cout << "Level 1 Elapsed Time: " << duration.count() << std::endl;

    // Set compression level to 6 and save the workbook
    options.SetCompressionType(OoxmlCompressionType::Level6);
    start = high_resolution_clock::now();
    workbook.Save(outDir + u"LargeSampleFile_level_6_out.xlsb", options);
    stop = high_resolution_clock::now();
    duration = duration_cast<milliseconds>(stop - start);
    std::cout << "Level 6 Elapsed Time: " << duration.count() << std::endl;

    // Set compression level to 9 and save the workbook
    options.SetCompressionType(OoxmlCompressionType::Level9);
    start = high_resolution_clock::now();
    workbook.Save(outDir + u"LargeSampleFile_level_9_out.xlsb", options);
    stop = high_resolution_clock::now();
    duration = duration_cast<milliseconds>(stop - start);
    std::cout << "Level 9 Elapsed Time: " << duration.count() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
