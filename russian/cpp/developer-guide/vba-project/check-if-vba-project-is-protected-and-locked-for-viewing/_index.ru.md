---
title: Проверьте, защищен ли VBA проект и заблокирован ли для просмотра с помощью C++
linktitle: Проверка защищен ли проект VBA и заблокирован для просмотра
type: docs
weight: 30
url: /ru/cpp/check-if-vba-project-is-protected-and-locked-for-viewing/
description: Узнайте, как проверить, защищен ли VBA проект и заблокирован ли для просмотра в файлах Excel, используя Aspose.Cells for C++.
---

## Проверьте, защищен ли VBA-проект и заблокирован ли для просмотра в C++

Aspose.Cells позволяет проверить, защищен ли VBA-проект файла Excel и заблокирован ли для просмотра. Для этого API предоставляет свойство [**VbaProject.GetIslockedForViewing()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getislockedforviewing/). Если он заблокирован для просмотра, то свойство [**VbaProject.GetIslockedForViewing()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getislockedforviewing/) возвращает **true**.

## **Образец кода**

Следующий пример кода загружает [пробный файл Excel](43352065.xlsm) и проверяет, защищен ли VBA-проект файла Excel и заблокирован ли для просмотра. Также посмотрите его вывод в консоли для справки.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Vba;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleCheckifVBAProjectisProtected.xlsm";

    // Load your source Excel file
    Workbook wb(inputFilePath);

    // Access the VBA project of the workbook
    VbaProject vbaProject = wb.GetVbaProject();

    // Check if "Lock project for viewing" is true or not
    std::cout << "Is VBA Project Locked for Viewing: " << vbaProject.GetIslockedForViewing() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Вывод в консоль**

Это вывод в консоль вышеупомянутого примера кода при выполнении с предоставленным [образцовым файлом Excel](43352065.xlsm).

{{< highlight java >}}

Is VBA Project Locked for Viewing: True

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
