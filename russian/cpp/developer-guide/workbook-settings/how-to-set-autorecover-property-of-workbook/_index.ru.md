---
title: Как установить свойство AutoRecover рабочей книги с помощью C++
linktitle: Как установить свойство AutoRecover в Рабочей книге
type: docs
weight: 220
url: /ru/cpp/how-to-set-autorecover-property-of-workbook/
description: Научитесь включать или отключать свойство AutoRecover рабочей книги с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Вы можете использовать Aspose.Cells для установки свойства AutoRecover рабочей книги. Значение по умолчанию — **true**. Когда вы установите его в **false**, Microsoft Excel отключит автоматическое восстановление (Авосохранение) для этого файла Excel.

Aspose.Cells предоставляет свойство [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getautorecover/) для включения или отключения этой опции.

{{% /alert %}}

Следующий код объясняет, как использовать свойство [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getautorecover/) рабочей книги. Сначала он читает значение по умолчанию этого свойства, которое равно **true**, затем устанавливает его в **false** и сохраняет рабочую книгу. Потом он снова читает рабочую книгу и проверяет значение этого свойства, которое в этот момент — **false**.

## C++ код для установки свойства AutoRecover рабочей книги

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

    // Create workbook object
    Workbook workbook;

    // Read AutoRecover property
    std::cout << "AutoRecover: " << workbook.GetSettings().GetAutoRecover() << std::endl;

    // Set AutoRecover property to false
    workbook.GetSettings().SetAutoRecover(false);

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    // Read the saved workbook again
    Workbook workbook2(outDir + u"output_out.xlsx");

    // Read AutoRecover property
    std::cout << "AutoRecover: " << workbook2.GetSettings().GetAutoRecover() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Вывод**

Вот вывод в консоль вышеуказанного образца кода.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
