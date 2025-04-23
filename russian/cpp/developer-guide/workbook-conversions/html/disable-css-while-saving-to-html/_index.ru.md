---
title: Отключить CSS при сохранении в HTML с помощью C++
linktitle: Отключить CSS при сохранении в HTML
type: docs
weight: 320
url: /ru/cpp/disable-css-while-saving-to-html/
description: Узнайте, как отключить CSS при сохранении файлов Excel в HTML с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

При сохранении файла Excel в одностраничный HTML, CSS-элементы обычно внедряются в HTML-файл и располагаются в разделе HEAD. Если вы прикрепите этот файл как содержимое/тело электронной почты, большинство почтовых клиентов удалит CSS-элементы, что приведет к неправильному отображению. В версии Aspose.Cells 24.12 появилась возможность опционально отключить CSS, позволяя применять стили непосредственно внутри HTML-элементов. Если вы хотите установить HTML как содержимое/тело письма, используйте свойство [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisablecss/) и установите его в значение **true**.

## **Отключить CSS при сохранении в HTML**

Следующий пример кода показывает использование свойства [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisablecss/).

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

    // Load sample workbook
    Workbook wb(srcDir + u"sampleDisableCss.xlsx");

    // Disable CSS
    HtmlSaveOptions opts;
    opts.SetDisableCss(true);

    // Save the workbook in HTML
    wb.Save(outDir + u"outputDisable.html", opts);

    std::cout << "Workbook saved with CSS disabled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
