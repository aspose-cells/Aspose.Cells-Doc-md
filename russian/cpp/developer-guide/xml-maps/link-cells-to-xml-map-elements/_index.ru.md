---
title: Связать ячейки с элементами XML карты с помощью C++
linktitle: Привязка ячеек к элементам XML отображения
type: docs
weight: 50
url: /ru/cpp/link-cells-to-xml-map-elements/
description: Узнайте, как связать ячейки с элементами XML карты с помощью Aspose.Cells и C++.
---

## **Возможные сценарии использования**

Вы можете связать ваши ячейки с элементами XML-карты, используя Aspose.Cells. Пожалуйста, используйте метод [**Cells.LinkToXmlMap()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/linktoxmlmap/) для этой цели.

## **Связать ячейки с элементами Xml-карты**

Следующий образец кода загружает [исходный Excel-файл](5115471.xlsx), который содержит XML-карту, затем связывает ячейки A1, B2, C3, D4, E5 и F6 с элементами XML-карты FIELD1, FIELD2, FIELD4, FIELD5, FIELD7 и FIELD8 соответственно, а затем сохраняет книгу Excel в [выходной Excel-файл](5115467.xlsx).

Если вы откроете [выходной Excel-файл](5115467.xlsx) и нажмете кнопку Developer > Source, вы увидите, что ячейки связаны с элементами XML-карты, и они также будут выделены Microsoft Excel, как показано на этом изображении.

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

    // Load sample workbook
    Workbook wb(srcDir + u"sample.xlsx");

    // Access the Xml Map inside it
    XmlMap map = wb.GetWorksheets().GetXmlMaps().Get(0);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Map FIELD1 and FIELD2 to cell A1 and B2
    ws.GetCells().LinkToXmlMap(map.GetName(), 0, 0, u"/root/row/FIELD1");
    ws.GetCells().LinkToXmlMap(map.GetName(), 1, 1, u"/root/row/FIELD2");

    // Map FIELD4 and FIELD5 to cell C3 and D4
    ws.GetCells().LinkToXmlMap(map.GetName(), 2, 2, u"/root/row/FIELD4");
    ws.GetCells().LinkToXmlMap(map.GetName(), 3, 3, u"/root/row/FIELD5");

    // Map FIELD7 and FIELD8 to cell E5 and F6
    ws.GetCells().LinkToXmlMap(map.GetName(), 4, 4, u"/root/row/FIELD7");
    ws.GetCells().LinkToXmlMap(map.GetName(), 5, 5, u"/root/row/FIELD8");

    // Save the workbook in xlsx format
    wb.Save(outDir + u"output.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
