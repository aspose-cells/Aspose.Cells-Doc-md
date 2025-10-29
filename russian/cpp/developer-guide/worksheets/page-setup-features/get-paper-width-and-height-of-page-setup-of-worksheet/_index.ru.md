---
title: Получить ширину и высоту бумаги настройки страницы листа с помощью C++
linktitle: Получить ширину и высоту бумаги настройки страницы
type: docs
weight: 50
url: /ru/cpp/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Узнайте, как программно получить ширину и высоту бумаги листа настройки страницы Excel с помощью C++ API Aspose.Cells for C++.
keywords: ширина бумаги Excel c++, высота бумаги Excel c++
---

## **Возможные сценарии использования**

Иногда вам нужно знать ширину и высоту установленной в настройках страницы бумаги. Пожалуйста, используйте методы [**GetPaperWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperwidth/) и [**GetPaperHeight()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperheight/) для этой цели.

## **Получение ширины и высоты бумаги на листе Excel**

Следующий пример кода объясняет использование методов [**GetPaperWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperwidth/) и [**GetPaperHeight()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperheight/). Он сначала изменяет размер бумаги на *A2*, затем находит ширину и высоту бумаги, затем изменяет его на *A3*, *A4*, *Letter* и соответственно находит ширину и высоту бумаги.

### **Образец кода**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook class
    Workbook book;

    // Access first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Set paper size to A2 and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA2);
    cout << "PaperA2: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    // Set paper size to A3 and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA3);
    cout << "PaperA3: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    // Set paper size to A4 and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA4);
    cout << "PaperA4: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    // Set paper size to Letter and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperLetter);
    cout << "PaperLetter: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Вывод в консоль**

Вот вывод в консоль вышеуказанного образца кода.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
