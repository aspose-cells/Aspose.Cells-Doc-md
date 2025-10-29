---
title: Включить пользовательские свойства CSS при сохранении в HTML с помощью C++
linktitle: Включить пользовательские CSS свойства при сохранении в HTML
type: docs
weight: 320
url: /ru/cpp/enable-css-custom-properties-while-saving-to-html/
description: Узнайте, как включить пользовательские свойства CSS при сохранении файлов Excel в HTML с помощью Aspose.Cells for C++. Улучшите производительность за счет уменьшения повторяющихся данных изображений.
---

## **Возможные сценарии использования**

При сохранении файла Excel в HTML, при наличии нескольких случаев одного изображения в base64, с помощью пользовательского свойства данные изображения нужно сохранять только один раз, что повышает производительность полученного HTML. Используйте свойство [**HtmlSaveOptions.GetEnableCssCustomProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getenablecsscustomproperties/) и установите его в **true** при сохранении в HTML.

![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg)

## **Включить пользовательские свойства CSS при сохранении в HTML**

Следующий пример показывает использование свойства [**HtmlSaveOptions.GetEnableCssCustomProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getenablecsscustomproperties/). Скриншот отображает эффект этого свойства, когда оно не установлено в **true**. Скачайте [пример файла Excel](50528260.xlsx), используемый в этом коде, и [сгенерированный HTML](50528261.zip) для ознакомления.

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
    Workbook wb(srcDir + u"sampleEnableCssCustomProperties.xlsx");

    // Create HtmlSaveOptions object
    HtmlSaveOptions opts;

    // Set ExportImagesAsBase64 to true
    opts.SetExportImagesAsBase64(true);

    // Enable EnableCssCustomProperties
    opts.SetEnableCssCustomProperties(true);

    // Save the workbook in HTML format
    wb.Save(outDir + u"outputEnableCssCustomProperties.html", opts);

    std::cout << "Workbook saved successfully with CSS custom properties enabled!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
