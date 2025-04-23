---  
title: Сохранять указанные листы в PDF с помощью C++  
linktitle: Сохранить указанные листы в формат PDF  
type: docs  
weight: 140  
url: /ru/cpp/save-specified-worksheets-to-pdf/  
description: Экспортировать конкретные листы в PDF с помощью Aspose.Cells и C++.  
---  

По умолчанию Aspose.Cells сохраняет все **видимые** листы книги в PDF. С помощью опции [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/) можно сохранять указанные листы. Например, можно сохранить активный лист в PDF, все листы (как видимые, так и скрытые) или выбрать несколько листов для сохранения в PDF.

## **Сохранить активный лист в формат PDF**

Если нужно сохранить только активный лист, это можно сделать, передав [**SheetSet.GetActive()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetset/getactive/) в опцию [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/).

Лист `Sheet2` является активным листом исходного файла [sheetset-example.xlsx](sheetset-example.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open the template excel file
    Workbook workbook(u"sheetset-example.xlsx");

    // Set active sheet to output
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetSheetSet(SheetSet::GetActive());

    // Save the pdf file with PdfSaveOptions
    workbook.Save(u"output.pdf", pdfSaveOptions);

    std::cout << "PDF file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Сохранить все листы в PDF**

[**SheetSet.GetVisible()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetset/getvisible/) обозначает видимые листы в книге, а [**SheetSet.GetAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetset/getall/) — все листы, включая как видимые, так и скрытые/невидимые листы. Для экспорта всех листов в PDF передайте [**SheetSet.GetAll**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetset/getall/) в опцию [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/).

Исходный файл [sheetset-example.xlsx](sheetset-example.xlsx) содержит все четыре листа с скрытым листом `Sheet3`.

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"
#include "Aspose.Cells/SheetSet.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open the template Excel file
    Workbook workbook(u"sheetset-example.xlsx");

    // Set all sheets to output
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetSheetSet(SheetSet::GetAll());

    // Save the PDF file with PdfSaveOptions
    workbook.Save(u"output.pdf", pdfSaveOptions);

    std::cout << "PDF file generated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Сохранить указанные листы в формат PDF**

Для экспорта нужных/кастомных нескольких листов в PDF, передайте несколько индексов листов в опцию [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"
#include "Aspose.Cells/SheetSet.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open the template Excel file
    U16String inputFilePath(u"sheetset-example.xlsx");
    Workbook workbook(inputFilePath);

    // Set custom multiple sheets (Sheet1, Sheet3) to output
    Vector<int32_t> sheetIndexes = {0, 2};
    SheetSet sheetSet(sheetIndexes);

    // Initialize PDF save options
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetSheetSet(sheetSet);

    // Save the PDF file with PdfSaveOptions
    U16String outputFilePath(u"output.pdf");
    workbook.Save(outputFilePath, pdfSaveOptions);

    std::cout << "Excel file saved as PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Переупорядочить листы в PDF**

Для изменения порядка листов (например, в обратном порядке) при сохранении в PDF без изменения исходного файла, передайте переставленные индексы листов в опцию [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open the template excel file
    Workbook workbook(u"sheetset-example.xlsx");

    // Reorder sheets (Sheet1, Sheet2, Sheet3, Sheet4) to (Sheet4, Sheet3, Sheet2, Sheet1)
    Vector<int32_t> sheetIndexes = { 3, 2, 1, 0 };
    SheetSet sheetSet(sheetIndexes);

    // Create PdfSaveOptions and assign the sheet set
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetSheetSet(sheetSet);

    // Save the pdf file with PdfSaveOptions
    workbook.Save(u"output.pdf", pdfSaveOptions);

    std::cout << "PDF saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

Если ваш электронный таблицы содержит формулы, лучше всего вызвать [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) прямо перед преобразованием таблицы в формат PDF. Таким образом будет гарантирован пересчет значений, зависящих от формул, и в PDF файл будут выведены правильные значения.

{{% /alert %}}
