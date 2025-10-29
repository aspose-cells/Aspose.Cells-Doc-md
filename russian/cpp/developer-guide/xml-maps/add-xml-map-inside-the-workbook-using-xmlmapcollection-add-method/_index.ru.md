---
title: Добавление XML карты внутри рабочей книги с помощью метода XmlMapCollection.Add в C++
linktitle: Добавить XML отображение внутри книги с использованием метода XmlMapCollection.Add
type: docs
weight: 10
url: /ru/cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/
description: Добавление XML карты внутри рабочей книги с помощью метода XmlMapCollection.Add в C++.
---

## **Возможные сценарии использования**

Aspose.Cells предоставляет метод [**XmlMapCollection.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmapcollection/add/), который вы можете использовать для импорта вашей XML-схемы внутри книги.

## **Добавить XML-отображение внутри книги с использованием метода XmlMapCollection.Add**

В следующем образце кода добавляется XML-схема внутри книги с помощью метода [**XmlMapCollection.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmapcollection/add/) и сохраняется как [файл Excel вывода](5115434.xlsx). На скриншоте показана XML-схема, которая была импортирована из [sample.xml](5115433.xml) в файл Excel вывода.

![add-xml-map](add-xml-map.png)

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

    // Path of input XML file
    U16String inputXmlMap = srcDir + u"sample.xml";

    // Create workbook object
    Workbook workbook;

    // Add XML map found inside the sample.xml inside the workbook
    workbook.GetWorksheets().GetXmlMaps().Add(inputXmlMap);

    // Save the workbook in xlsx format
    U16String outputFilePath = srcDir + u"output_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully as xlsx format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
