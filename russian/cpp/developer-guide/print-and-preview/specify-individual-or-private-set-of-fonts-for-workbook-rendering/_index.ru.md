---
title: Укажите отдельный или приватный набор шрифтов для рендеринга рабочей книги с C++
linktitle: Указание индивидуального или частного набора шрифтов для рендеринга книги
type: docs
weight: 40
url: /ru/cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/
description: Узнайте, как указывать отдельный или приватный набор шрифтов для рендеринга рабочей книги с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

В основном, вы указываете директорию шрифтов или список шрифтов для всех рабочих книг, но иногда необходимо указывать отдельный или приватный набор шрифтов для ваших рабочих книг. Aspose.Cells предоставляет класс [**IndividualFontConfigs**](https://reference.aspose.com/cells/cpp/aspose.cells/individualfontconfigs/), который можно использовать для указания отдельного или приватного набора шрифтов для вашей рабочей книги.

## **Указание индивидуального или частного набора шрифтов для рендеринга книги**

Следующий пример загружает [пример файла Excel](67338268.xlsx) со своим отдельным или приватным набором шрифтов, указанных с помощью класса [**IndividualFontConfigs**](https://reference.aspose.com/cells/cpp/aspose.cells/individualfontconfigs/). Ознакомьтесь также с [шрифтом](67338271.zip), использованным внутри кода, а также с [выходным PDF](67338269.pdf), сгенерированным этим кодом. Следующий скриншот показывает, как выглядит результативный PDF, если шрифт был успешно обнаружен.

![todo:image_alt_text](specify-individual-or-private-set-of-fonts-for-workbook-rendering_1.png)

## **Образец кода**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path of your custom font directory
    U16String customFontsDir(u"C:\\TempDir\\CustomFonts");

    // Specify individual font configs custom font directory
    IndividualFontConfigs fontConfigs;

    // If you comment this line or if custom font directory is wrong or 
    // if it does not contain required font then output pdf will not be rendered correctly
    fontConfigs.SetFontFolder(customFontsDir, false);

    // Specify load options with font configs
    LoadOptions opts(LoadFormat::Xlsx);
    opts.SetFontConfigs(fontConfigs);

    // Load the sample Excel file with individual font configs
    Workbook wb(u"sampleSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.xlsx", opts);

    // Save to PDF format
    wb.Save(u"outputSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.pdf", SaveFormat::Pdf);

    std::cout << "Workbook saved to PDF with custom font configurations successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
