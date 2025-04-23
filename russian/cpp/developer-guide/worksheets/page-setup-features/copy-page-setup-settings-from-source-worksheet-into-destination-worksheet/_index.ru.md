---
title: Копировать настройки Page Setup из исходного листа в целевой с помощью C++
linktitle: Копировать настройки Page Setup
type: docs
weight: 80
url: /ru/cpp/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: В этой статье объясняется, как использовать пример кода API или библиотеки C++, чтобы программно копировать настройки Page Setup из исходного листа в целевой.
keywords: копировать настройки страницы c++, копировать настройки страницы на целевой лист c++
---

## **Возможные сценарии использования**

При добавлении нового листа в книгу, он содержит настройки *Параметры страницы* по умолчанию. Иногда может возникнуть необходимость передать настройки ([**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)) с одного листа на другой. В этом документе объясняется, как скопировать настройки Параметры страницы с одного листа на другой с использованием API Aspose.Cells.

## **Копирование настроек страницы с исходного листа на целевой лист**

Следующий образец кода иллюстрирует, как скопировать *Параметры страницы* с одного листа на другой с использованием метода [**PageSetup.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/copy/). Обратитесь к следующему образцу кода и его выводу консоли для справки.

## **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook wb;

    wb.GetWorksheets().Add(u"TestSheet1");
    wb.GetWorksheets().Add(u"TestSheet2");

    Worksheet TestSheet1 = wb.GetWorksheets().Get(u"TestSheet1");
    Worksheet TestSheet2 = wb.GetWorksheets().Get(u"TestSheet2");

    TestSheet1.GetPageSetup().SetPaperSize(PaperSizeType::PaperA3ExtraTransverse);

    std::cout << "Before Paper Size: " << static_cast<int>(TestSheet1.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << "Before Paper Size: " << static_cast<int>(TestSheet2.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << std::endl;

    CopyOptions copyOptions;
    TestSheet2.GetPageSetup().Copy(TestSheet1.GetPageSetup(), copyOptions);

    std::cout << "After Paper Size: " << static_cast<int>(TestSheet1.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << "After Paper Size: " << static_cast<int>(TestSheet2.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Вывод в консоль**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
