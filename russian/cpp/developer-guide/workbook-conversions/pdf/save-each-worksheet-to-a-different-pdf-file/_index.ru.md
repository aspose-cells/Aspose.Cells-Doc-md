---
title: Сохранять каждый лист в отдельный PDF файл с помощью C++
linktitle: Сохраните каждый рабочий лист в отдельный файл PDF
type: docs
weight: 130
url: /ru/cpp/save-each-worksheet-to-a-different-pdf-file/
description: Узнайте, как сохранить каждый лист Excel в отдельный PDF файл с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Aspose.Cells поддерживает преобразование XLS-файлов (с содержимым изображений, графиков и т. д.) в PDF-документы. Aspose.Cells for C++ может самостоятельно преобразовать таблицу в PDF без необходимости использования Aspose.PDF для C++. Преобразование не требует создания или использования временных файлов, весь процесс выполняется в памяти.

{{% /alert %}} 

## **Сохранить каждый лист в отдельный файл PDF**
Если вам нужно сохранить каждый лист из вашего шаблонного файла Excel для генерации различных PDF-файлов, это легко реализовать. Можно установить индекс одного листа в [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/) за раз для преобразования в PDF.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Get the Excel file path
    U16String filePath = srcDir + u"input.xlsx";

    // Instantiate a new workbook and open the Excel file from its location
    Workbook workbook(filePath);

    // Get the count of the worksheets in the workbook
    int sheetCount = workbook.GetWorksheets().GetCount();

    // Define PdfSaveOptions
    PdfSaveOptions pdfSaveOptions;

    // Take PDFs of each sheet
    for (int j = 0; j < sheetCount; j++)
    {
        Worksheet ws = workbook.GetWorksheets().Get(j);

        // Set worksheet to output
        SheetSet sheetSet(Vector<int32_t>{ ws.GetIndex() });
        pdfSaveOptions.SetSheetSet(sheetSet);

        // Save the workbook with the current worksheet as PDF
        workbook.Save(srcDir + u"worksheet-" + ws.GetName() + u".out.pdf", pdfSaveOptions);
    }

    std::cout << "PDFs generated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

Если в вашей таблице есть формулы, лучше всего вызвать [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) перед преобразованием таблицы в PDF. Это обеспечит перерасчет значений, зависящих от формул, и правильное отображение значений в PDF.

{{% /alert %}}
