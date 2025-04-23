---
title: Найти название корневого элемента XML карты с помощью C++
linktitle: Поиск имени корневого элемента XML схемы
type: docs
weight: 30
url: /ru/cpp/find-the-root-element-name-of-xml-map/
description: Узнайте, как определить название корневого элемента XML карты с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Вы можете найти *имя корневого элемента XML-карты* с помощью Aspose.Cells с помощью свойства [**XmlMap.GetRootElementName()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmap/getrootelementname/). На следующем скриншоте показано имя корневого элемента XML-карты в Microsoft Excel.

![todo:image_alt_text](find-the-root-element-name-of-xml-map_1.png)

## **Образец кода**

Следующий образец кода загружает [образец Excel-файла](55541789.xlsx), обращается к первой XML-карте и печатает ее свойство [**XmlMap.GetRootElementName()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmap/getrootelementname/). Пожалуйста, ознакомьтесь с консольным выводом образца кода, приведенным ниже.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleRootElementNameOfXmlMap.xlsx";

    // Load sample Excel file having Xml Map
    Workbook wb(inputFilePath);

    // Access first Xml Map inside the Workbook
    XmlMap xmap = wb.GetWorksheets().GetXmlMaps().Get(0);

    // Print Root Element Name of Xml Map on Console
    std::cout << "Root Element Name Of Xml Map: " << xmap.GetRootElementName().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Вывод в консоль**

{{< highlight java >}}

Root Element Name Of Xml Map: MiscData

{{< /highlight >}}
