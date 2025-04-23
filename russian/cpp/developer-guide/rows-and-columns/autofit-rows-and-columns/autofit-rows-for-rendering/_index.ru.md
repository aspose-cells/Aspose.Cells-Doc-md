---
title: Автонастройка строк для отображения с помощью C++
linktitle: Автонастройка строк для визуализации
type: docs
weight: 130
url: /ru/cpp/autofit-rows-for-rendering/
description: Узнайте, как автоматически подгонять строки для отображения в файлах Excel с помощью Aspose.Cells и C++.
---

Обычно, когда вы хотите отобразить весь текст в ячейке, вы можете автоматически подстроить строку в обычном виде с масштабом 100% в Microsoft Excel. Это позволяет тексту полностью отображаться в обычном виде, даже при печати или сохранении файла в формате PDF, текст будет отображаться правильно.

Однако в некоторых случаях автоматическая подгонка строки работает хорошо в обычном виде, но при переходе в вид для печати или сохранении файла в формате PDF текст обрезается. Пожалуйста, проверьте исходный файл [Book1.xlsx](Book1.xlsx) и скриншоты.

![текст обрезан в виде для печати](text_clipped_in_printview.png)

Если вы хотите предотвратить обрезку текста в сохранённом PDF-файле, вы можете автонастроить строки с помощью параметра [AutoFitterOptions.GetForRendering()](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getforrendering/) на.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Initialize workbook instance
    Workbook workbook(u"Book1.xlsx");

    // Set autofit options for rendering
    AutoFitterOptions autoFitterOptions;
    autoFitterOptions.SetForRendering(true);

    // Autofit rows with options
    workbook.GetWorksheets().Get(0).AutoFitRows(autoFitterOptions);

    // Save to PDF
    workbook.Save(u"output.pdf", SaveFormat::Pdf);

    Aspose::Cells::Cleanup();
}
```

Теперь текст не обрезается в сохраненном файле PDF.

![текст не обрезается в сохраненном pdf](text_not_clipped_in_saved_pdf.png)
