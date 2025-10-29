---
title: Отображение маркеров, задавая значение ячейки с помощью HTML в C++
linktitle: Отображение маркеров, устанавливая значение ячейки с использованием HTML
type: docs
weight: 130
url: /ru/cpp/display-bullets-by-setting-cell-value-using/
description: Добавьте маркеры в ячейки Excel с помощью HTML и простого API Aspose.Cells for C++.
keywords: добавление маркеров в Excel, добавление маркеров в Excel c++, отображение маркеров в Excel, отображение маркеров в Excel c++, добавление маркеров в Excel с помощью HTML, добавление маркеров в Excel с помощью HTML c++, отображение маркеров в Excel с помощью HTML, отображение маркеров в Excel с помощью HTML c++, отображение маркеров в Excel с помощью HTML, добавление маркеров в Excel с помощью HTML
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает отображение маркеров с помощью HTML-кода. В этой статье будет объяснено, как отобразить маркеры, устанавливая значение ячейки с использованием HTML. Мы будем использовать свойство [**Cell.GetHtmlString()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/) для установки значения ячейки с нашим HTML.

{{% /alert %}}

## Код C++ для отображения маркеров, задавая значение ячейки с помощью HTML

Следующий код использует HTML-код для установки значения ячейки. После того, как вы запустите этот код, вы получите вывод, который показан на изображении ниже.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get("A1");

    // Set the HTML string
    cell.SetHtmlString(u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'>Text 1 </font>"
                       u"<font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font>"
                       u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 2 </font>"
                       u"<font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font>"
                       u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 3 </font>"
                       u"<font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font>"
                       u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 4 </font>");

    // Auto fit the Columns
    worksheet.AutoFitColumns();

    // Save the workbook
    U16String outputFilePath = u"BulletsInCells_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Вывод, созданный образцовым кодом

На следующем скриншоте показан вывод вышеприведенного образца кода.

![todo:image_alt_text](display-bullets-by-setting-cell-value-using-html_1.png)
{{< app/cells/assistant language="cpp" >}}
