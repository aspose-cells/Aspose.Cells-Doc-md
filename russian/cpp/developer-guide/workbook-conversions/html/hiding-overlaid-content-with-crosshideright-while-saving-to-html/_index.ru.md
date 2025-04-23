---
title: Скрытие перекрытого содержимого с помощью CrossHideRight при сохранении в HTML с C++
linktitle: Скрытие перекрывающегося контента с помощью CrossHideRight при сохранении в HTML
type: docs
weight: 100
url: /ru/cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
description: Используйте CrossHideRight с Aspose.Cells в C++, чтобы скрывать перекрытый контент при сохранении в HTML.
---

## **Возможные сценарии использования**

При сохранении файла Excel в HTML вы можете указать разные типы перекрестий для строк ячеек. По умолчанию Aspose.Cells генерирует HTML согласно Microsoft Excel, однако при изменении типа пересечения на [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype) он скрывает все строки справа в ячейке, которые перекрываются или налегают на содержимое ячейки.

## **Скрытие перекрывающегося содержимого с CrossHideRight при сохранении в Html**

Следующий пример загружает [пример файла Excel](64716894.xlsx) и сохраняет его в [вывод HTML](64716893.zip) после установки [**HtmlSaveOptions.GetHtmlCrossStringType()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gethtmlcrossstringtype/) в [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype). Скриншот показывает, как [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype) влияет на вывод HTML по сравнению со стандартным выводом.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    Workbook wb(sourceDir + u"sampleHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.xlsx");

    // Specify HtmlSaveOptions - Hide Overlaid Content with CrossHideRight while saving to Html
    HtmlSaveOptions opts;
    opts.SetHtmlCrossStringType(HtmlCrossType::CrossHideRight);

    // Save to HTML with HtmlSaveOptions
    wb.Save(outputDir + u"outputHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.html", opts);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
