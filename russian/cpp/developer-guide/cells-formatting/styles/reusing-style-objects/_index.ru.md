---
title: Повторное использование объектов стилей с помощью C++
linktitle: Повторное использование объектов стиля
description: В Aspose.Cells for C++, создавая и используя повторно используемые объекты стилей, вы можете упростить управление стилями и повысить эффективность кода. Наш гид поможет вам использовать преимущества повторно используемых объектов стилей и реализовать их в вашем приложении.
keywords: Aspose.Cells for C++, Повторное использование объектов стилей, Управление стилями, Эффективность кода, Повторно используемые стили, Разработка приложений, API справка, пример кода, загрузка, поддержка.
type: docs
weight: 3000
url: /ru/cpp/reusing-style-objects/
---

{{% alert color="primary" %}}

Повторное использование объектов стиля может сэкономить память и ускорить работу программы.

{{% /alert %}}

Чтобы применить форматирование к большому диапазону ячеек на листе:

1. Создайте объект стиля.
1. Укажите атрибуты.
1. Примените стиль к ячейкам в диапазоне.

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

    // Create workbook object
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cells
    Cell cell1 = worksheet.GetCells().Get(u"A1");
    Cell cell2 = worksheet.GetCells().Get(u"B1");

    // Set the styles of both cells to Times New Roman
    Style styleObject = workbook.CreateStyle();
    styleObject.GetFont().SetColor(Color::Red());
    styleObject.GetFont().SetName(u"Times New Roman");
    cell1.SetStyle(styleObject);
    cell2.SetStyle(styleObject);

    // Put the values inside the cell
    cell1.PutValue(u"Hello World!");
    cell2.PutValue(u"Hello World!!");

    // Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
    workbook.Save(outDir + u"SampleOutput_out.xlsx");

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Поскольку подход [**Cell.GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/)/[**Cell.SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) использует гораздо меньше памяти и является эффективным, старое свойство Cell.Style, которое потребляло много ненужной памяти, было удалено с выпуском Aspose.Cells 7.1.0.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
