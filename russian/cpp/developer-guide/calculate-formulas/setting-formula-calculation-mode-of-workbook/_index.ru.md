---
title: Настройка режима вычисления формул книги с помощью C++
linktitle: Установка режима расчета формул в книге Excel
description: Эта статья рассказывает, как установить режим вычисления формул книги в Microsoft Excel с помощью Aspose.Cells и C++. Загружая существующий файл Excel или создавая новый, мы можем использовать предоставленный Aspose.Cells метод для установки режима вычислений формул и получения результата. В конце сохраняем изменённый файл Excel.
keywords: Aspose.Cells, Excel, книга, режим вычисления формул, настройки, C++
type: docs
weight: 110
url: /ru/cpp/setting-formula-calculation-mode-of-workbook/
---

{{% alert color="primary" %}}

В Microsoft Excel вы можете установить режим вычисления формул, то есть способ, которым происходит вычисление формул. Существуют три возможных значения:

- Автоматический - пересчитывать при изменении чего-либо и каждый раз при открытии книги.
- Автоматический, за исключением таблиц данных - пересчитывать при изменении чего-либо, но исключая таблицы данных.
- Ручной - пересчитывать только при явном запросе пользователя нажатием F9 или CTRL+ALT+F9, или при сохранении книги.

{{% /alert %}}

Для установки режима вычисления формул в Microsoft Excel:

1. Выберите **Формулы**, а затем **Параметры расчета**.
1. Выберите один из вариантов.

Aspose.Cells также позволяет установить **Режим вычисления формул** с использованием свойства режима [**FormulaSettings.GetCalculationMode()**](https://reference.aspose.com/cells/cpp/aspose.cells/formulasettings/getcalculationmode/). Вы можете назначить ему перечисление [**CalcModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/calcmodetype/), которое имеет одно из следующих значений:

- Тип режима вычислений::Автоматический
- Тип режима вычислений::Исключая таблицу автоматического вычисления
- Ручной режим вычислений

```c++
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

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create a workbook
    Workbook workbook;

    // Set the Formula Calculation Mode to Manual
    workbook.GetSettings().GetFormulaSettings().SetCalculationMode(CalcModeType::Manual);

    // Save the workbook
    workbook.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully with manual calculation mode!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
