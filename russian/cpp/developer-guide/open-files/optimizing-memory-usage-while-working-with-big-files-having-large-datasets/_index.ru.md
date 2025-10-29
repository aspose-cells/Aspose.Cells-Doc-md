---
title: Оптимизация использования памяти при работе с большими файлами и крупными наборами данных в C++
linktitle: Оптимизация использования памяти
type: docs
weight: 180
url: /ru/cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
description: Узнайте, как оптимизировать использование памяти при работе с крупными файлами Excel с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}}

При создании книги с большими наборами данных или чтении большого файла Microsoft Excel всегда возникает вопрос - какой объем ОЗУ займет данный процесс. Предлагаются меры, которые можно принять для справки с этим вызовом. Aspose.Cells предоставляет некоторые соответствующие параметры и вызовы API для снижения, уменьшения и оптимизации использования памяти. Кроме того, это может помочь процессу работать более эффективно и быстро.

Используйте опцию [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) для оптимизации использования памяти для данных ячеек и уменьшения общей затраты памяти. При создании большого набора данных для ячеек можно сохранить определенное количество памяти по сравнению с использованием настройки по умолчанию ([**MemorySetting.Normal**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/)).

{{% /alert %}}

## **Оптимизация памяти**

### **Чтение больших файлов Excel**

Следующий пример показывает, как считать большой файл Microsoft Excel в оптимизированном режиме.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Specify the LoadOptions
    LoadOptions opt;

    // Set the memory preferences
    opt.SetMemorySetting(MemorySetting::MemoryPreference);

    // Instantiate the Workbook
    // Load the Big Excel file having large Data set in it
    Workbook wb(srcDir + u"Book1.xlsx", opt);

    std::cout << "Workbook loaded successfully with memory preference setting!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Запись больших файлов Excel**

Следующий пример показывает, как записать большой набор данных на листе в оптимизированном режиме.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook wb;

    // Set the memory preferences
    // Note: This setting cannot take effect for the existing worksheets that are created before using the below line of code
    wb.GetSettings().SetMemorySetting(MemorySetting::MemoryPreference);

    // Note: The memory settings also would not work for the default sheet i.e., "Sheet1" etc. automatically created by the Workbook

    // To change the memory setting of existing sheets, please change memory setting for them manually:
    Cells cells = wb.GetWorksheets().Get(0).GetCells();
    cells.SetMemorySetting(MemorySetting::MemoryPreference);

    // Input large dataset into the cells of the worksheet.
    // Your code goes here.
    // .........

    // Get cells of the newly created Worksheet "Sheet2" whose memory setting is same with the one defined in WorkbookSettings:
    cells = wb.GetWorksheets().Add(u"Sheet2").GetCells();

    // Input large dataset into the cells of the worksheet.
    // Your code goes here.
    // .........

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Предостережение**

Настройка по умолчанию, [**MemorySetting.Normal**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/), применяется ко всем версиям. В некоторых ситуациях, таких как создание книги с большим набором данных для ячеек, опция [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) может оптимизировать использование памяти и уменьшить затраты памяти для приложения. Однако, эта опция может ухудшить производительность в некоторых специальных случаях, таких как следующие.

1. **Доступ к ячейкам в произвольном порядке и повторно**: Самая эффективная последовательность доступа к коллекции ячеек - путем перебора ячеек по одной строке, а затем строка за строкой. Особенно, если вы получаете доступ к строкам/ячейкам с помощью перечислителя, полученного из [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/), [**RowCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/) и [**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/), производительность будет максимальной с [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/).
1. **Вставка и удаление ячеек и строк**: Обратите внимание, что если есть много операций вставки/удаления для Ячеек/Строк, деградация производительности будет значительной в режиме *MemoryPreference* по сравнению с режимом *Normal*.
1. **Работа с различными типами ячеек**: Если большинство ячеек содержат строковые значения или формулы, затраты памяти будут такими же, как в режиме *Normal*, но если есть много пустых ячеек, или значения ячейки являются числовыми, логическими и т. д., то [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) позволит добиться лучшей производительности.
{{< app/cells/assistant language="cpp" >}}
