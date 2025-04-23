---
title: Используйте свойство Sheet.SheetId OpenXml с C++
linktitle: Используйте свойство Sheet.SheetId OpenXml
type: docs
weight: 200
url: /ru/cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/
description: В этой статье показано, как использовать свойство Sheet.SheetId OpenXml с помощью API или библиотеки для работы с Excel на C++ программным методом.
keywords: свойство id листа openxml c++, id листа рабочей книги Excel c++
---

## **Возможные сценарии использования**

Свойство *Sheet.SheetId* находится в пространстве имен *DocumentFormat.OpenXml.Spreadsheet* и является частью OpenXml. Вы можете увидеть это свойство и его значение внутри *workbook.xml*, как показано на следующем снимке экрана. Aspose.Cells предоставляет эквивалентное свойство как [**Worksheet.GetTabId()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettabid/).

![todo:image_alt_text](utilize-sheet-sheetid-property-of-openxml-using-aspose-cells_1.png)

## **Использование свойства Sheet.SheetId из OpenXml с помощью Aspose.Cells**

В следующем образце кода загружается [образцовый Excel-файл](51740716.xlsx), читается его идентификатор листа или вкладки, затем назначается новый идентификатор вкладки и сохраняется как [выходной файл Excel](51740717.xlsx). Также обратитесь к выводу консоли приведенного ниже кода для справки.

## **Образец кода**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load source Excel file
    Workbook wb(u"sampleSheetId.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Print its Sheet or Tab Id on console
    std::cout << "Sheet or Tab Id: " << ws.GetTabId() << std::endl;

    // Change Sheet or Tab Id
    ws.SetTabId(358);

    // Save the workbook
    wb.Save(u"outputSheetId.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Вывод в консоль**

{{< highlight java >}}

Sheet or Tab Id: 1297

{{< /highlight >}}
