---
title: Добавить значки в рабочий лист с C++
linktitle: Управление значками
type: docs
weight: 100
url: /ru/cpp/insert-svg-to-excel/
description: Узнайте, как добавлять значки в Excel лист с помощью Aspose.Cells и C++.
---

## Добавление значков на лист в Aspose.Cells

Если вам нужно использовать [Aspose.Cells](https://products.aspose.com/cells/) для добавления 'значков' в файл Excel, то этот документ может предоставить вам некоторую помощь.

Интерфейс Excel, соответствующий операции вставки значка, выглядит следующим образом:

![](1.png)

- Выберите позицию для вставки значка на лист
- Левый щелчок *Вставка*->*Значки*
- В открывшемся окне выберите значок в красном прямоугольнике на рисунке выше
- Левый щелчок *Вставить*, он вставится в файл Excel.

Эффект будет следующий:

![](2.png)

Здесь мы подготовили *пример кода*, чтобы помочь вставить иконки с помощью [Aspose.Cells](https://products.aspose.com/cells/). Также есть необходимый [пример файла](sample.xlsx) и [ресурсный файл иконок](icon.zip). Мы использовали интерфейс Excel для вставки иконки с таким же визуальным эффектом, как у [ресурсного файла](icon.zip) в [примерном файле](sample.xlsx).

### C++

```cpp
#include <iostream>
#include <fstream>
#include <vector>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    U16String fileName = u"icon.svg";
    std::ifstream fsSource(fileName.ToUtf8(), std::ios::binary);
    if (!fsSource) {
        std::cerr << "Failed to open file: " << fileName.ToUtf8() << std::endl;
        return -1;
    }

    fsSource.seekg(0, std::ios::end);
    size_t fileSize = fsSource.tellg();
    fsSource.seekg(0, std::ios::beg);

    std::vector<uint8_t> bytes(fileSize);
    fsSource.read(reinterpret_cast<char*>(bytes.data()), fileSize);
    fsSource.close();

    Aspose::Cells::Vector<uint8_t> asposeBytes(bytes.size());
    if (!bytes.empty()) {
        memcpy(asposeBytes.GetData(), bytes.data(), bytes.size());
    }

    Workbook workbook(u"sample.xlsx");
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    sheet.GetShapes().AddIcons(3, 0, 7, 0, 100, 100, asposeBytes, Aspose::Cells::Vector<uint8_t>());

    Cell c = sheet.GetCells().Get(8, 7);
    c.PutValue(u"Insert via Aspose.Cells");
    Style s = c.GetStyle();
    s.GetFont().SetColor(Color::Blue());
    c.SetStyle(s);

    workbook.Save(u"sample2.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```

Когда вы выполните вышеуказанный код в своем проекте, вы получите следующие результаты:

![](3.png)
