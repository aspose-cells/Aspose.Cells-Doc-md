---
title: Получить гиперссылки в диапазоне с помощью C++
linktitle: Получение гиперссылок в диапазоне
type: docs
weight: 100
url: /ru/cpp/get-hyperlinks-in-range/
description: Узнайте, как получить гиперссылки в диапазоне через API Aspose.Cells for C++.
keywords: Получить гиперссылки в диапазоне, Получить все гиперссылки в выбранном диапазоне, Удалить гиперссылку в диапазоне, Удалить гиперссылки в выбранном диапазоне
---

## **Получение гиперссылок в диапазоне**

Класс [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) предоставляет свойство [**GetHyperlinks()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/gethyperlinks/), которое возвращает все гиперссылки в выбранном диапазоне. Вы также можете удалить гиперссылку, вызвав метод [**Hyperlink.Delete**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/delete/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"HyperlinksSample.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Range range = worksheet.GetCells().CreateRange(u"A2", u"B3");
    Vector<Hyperlink> hyperlinks = range.GetHyperlinks();

    for (int i = 0; i < hyperlinks.GetLength(); ++i)
    {
        Hyperlink& link = hyperlinks[i];
        std::cout << link.GetArea().ToString().ToUtf8() << " : " << link.GetAddress().ToUtf8() << std::endl;
        link.Delete();
    }

    workbook.Save(outDir + u"HyperlinksSample_out.xlsx");
    std::cout << "Hyperlinks processed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
