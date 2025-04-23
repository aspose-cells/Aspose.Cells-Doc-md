---
title: Автоматическая подгонка высоты строки при загрузке файла с помощью C++
linktitle: Автоматическое подгонение высоты строки при загрузке файла
type: docs
weight: 120
url: /ru/cpp/autofit-row-height/
description: Узнайте, как автоматически подгонять высоту строк, у которых она не настроена вручную, с помощью Aspose.Cells и C++.
keywords: Автоматическая подгонка высоты строки при загрузке файла, автоматическая настройка высоты строки при открытии файла Excel.
---

## **Возможные сценарии использования**
Высота строки автоматически подстраивается под размер шрифта содержимого, но когда высота загруженной строки не совпадает с содержимым файла, MS Excel автоматически корректирует высоту строки при загрузке файла, в то время как Aspose.Cells этого делать не будет для повышения производительности. Если необходимо, чтобы при загрузке файлов Aspose.Cells автоматически подгонял высоты строк, можно достичь этого через параметр [LoadOptions.GetOnlyAuto()](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getonlyauto/).

Пожалуйста, обратитесь к следующим данным изображения. Мы видим, что высота кэшированной строки в строке 11 равна 15, но Excel автоматически подгоняет высоту строки при загрузке файла.
<br>
<img src="1.png" width=70% />

## **Настройка высоты строки с помощью Aspose.Cells**
Если вы загружаете файл непосредственно и сохраняете его в формате PDF, данные не будут полностью отображены в PDF, потому что высота кэшированной строки равна только 15.
<br>
<img src="2.png" width=70% />
<br>
Если при загрузке файла установить параметр [LoadOptions.GetOnlyAuto()](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getonlyauto/) в значение true, то Aspose.Cells автоматически скорректирует высоту строки. Скорректированная высота строки может эффективно соответствовать требованиям отображения текста.
<br>
<img src="3.png" width=70% />

## **Пример кода на C++**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Define the file path
    U16String filePath(u"..\\Data\\01_SourceDirectory\\");

    // Open an existing Excel file and save it as PDF
    {
        Workbook wb(filePath + u"sample.xlsx");
        wb.Save(filePath + u"out.pdf");
    }

    // Set load options for the second workbook
    LoadOptions loadOptions;
    {
        AutoFitterOptions autoFitterOptions;
        autoFitterOptions.SetOnlyAuto(true);
        loadOptions.SetAutoFitterOptions(autoFitterOptions);
    }

    // Open the existing Excel file with load options and save it as PDF
    {
        Workbook book(filePath + u"sample.xlsx", loadOptions);
        book.Save(filePath + u"out2.pdf");
    }

    std::cout << "PDF files created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
