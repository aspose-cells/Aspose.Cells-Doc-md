---
title: Сохранение рабочей книги в формате Strict Open XML Spreadsheet с помощью C++
linktitle: Сохранить книгу в формате строгой открытой электронной таблицы XML
type: docs
weight: 150
url: /ru/cpp/save-workbook-to-strict-open-xml-spreadsheet-format/
description: Узнайте, как сохранить рабочую книгу в формате Strict Open XML Spreadsheet с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Aspose.Cells позволяет сохранять рабочую книгу в формате *Strict Open XML Spreadsheet*. Для этого предоставляется свойство [**GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcompliance/). Если установить его значение в [**OoxmlCompliance::Iso29500_2008_Strict**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompliance/), то выходной файл Excel сохранится в формате Strict Open XML Spreadsheet.

## **Сохранить книгу в формате Strict Open XML Spreadsheet**

Следующий пример кода создает рабочую книгу и устанавливает значение свойства [**GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcompliance/) как [**OoxmlCompliance::Iso29500_2008_Strict**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompliance/), затем сохраняет ее как [выходной файл Excel](67338272.xlsx). Если открыть выходной файл Excel в Microsoft Excel и выбрать «Сохранить как…», вы увидите его формат как *Strict Open XML Spreadsheet*, что показано на этом скриншоте.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook wb;

    // Specify - Strict Open XML Spreadsheet - Format
    wb.GetSettings().SetCompliance(OoxmlCompliance::Iso29500_2008_Strict);

    // Add message in cell B4 of first worksheet
    Cell b4 = wb.GetWorksheets().Get(0).GetCells().Get(u"B4");
    b4.PutValue(u"This Excel file has Strict Open XML Spreadsheet format.");

    // Save to output Excel file
    wb.Save(u"outputSaveWorkbookToStrictOpenXMLSpreadsheetFormat.xlsx", SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully with Strict Open XML Spreadsheet format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
