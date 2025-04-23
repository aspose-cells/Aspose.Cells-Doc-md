---
title: Экспорт схожего стиля границы, когда стиль границы не поддерживается веб браузерами, с C++
linktitle: Экспорт аналогичного стиля границы, когда стиль границы не поддерживается веб браузерами
type: docs
weight: 70
url: /ru/cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
description: Узнайте, как экспортировать похожие стили границ, неподдерживаемые веб браузерами, с помощью Aspose.Cells и C++.
---

## **Возможные сценарии использования**

Microsoft Excel поддерживает некоторые типы пунктирных границ, которые не поддерживаются веб-браузерами. При конвертации такого файла Excel в HTML с помощью Aspose.Cells такие границы будут удалены. Однако Aspose.Cells также может отображать такие границы с помощью свойства [**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportsimilarborderstyle/). Установите его значение в **true**, и неподдерживаемые границы также будут экспортированы в HTML.

## **Экспорт аналогичного стиля границы, когда стиль границы не поддерживается веб-браузерами**

Следующий пример загружает [пример файла Excel](64716806.xlsx), содержащий неподдерживаемые границы, как показано на скриншоте. Скриншот дополнительно иллюстрирует эффект свойства [**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportsimilarborderstyle/) в выводимом HTML ([вывод HTML](64716804.zip)).

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load the sample Excel file
    U16String inputFilePath(u"sampleExportSimilarBorderStyle.xlsx");
    Workbook workbook(inputFilePath);

    // Specify Html Save Options - Export Similar Border Style
    HtmlSaveOptions opts;
    opts.SetExportSimilarBorderStyle(true);

    // Save the workbook in Html format with specified Html Save Options
    U16String outputFilePath(u"outputExportSimilarBorderStyle.html");
    workbook.Save(outputFilePath, opts);

    std::cout << "Workbook saved successfully in HTML format with similar border styles!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
