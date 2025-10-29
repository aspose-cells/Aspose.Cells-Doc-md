---
title: Преобразование рабочей книги Excel в Ods, Sxc и Fods (OpenOffice / LibreOffice Calc) с помощью C++
linktitle: Ods
type: docs
weight: 20
url: /ru/cpp/convert-excel-to-ods/
description: Как преобразовать Excel в Ods (OpenOffice / LibreOffice Calc) или преобразовать Ods (OpenOffice / LibreOffice Calc) в Excel с помощью Aspose.Cells и C++.
---

## **Об OpenDocument**
[Формат OpenDocument (ODF)](https://en.wikipedia.org/wiki/OpenDocument) - бесплатный и открытый формат файла для электронных офисных документов, изначально разработанный Sun для пакета Open Office. OpenDocument Spreadsheet (ODS) - это формат файла для документов Excel. OpenDocument в настоящее время является стандартом OASIS и ISO.

## **Преобразовать Ods (OpenOffice / LibreOffice Calc) в Excel**
Aspose.Cells поддерживает загрузку Ods, Sxc и Fods, поддерживаемых OpenOffice / LibreOffice Calc, и преобразование [Ods](book1.ods), [Sxc](book1.sxc) и [Fods](book1.fods) в файлы Excel.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source ods file
    U16String odsFilePath(u"book1.ods");
    std::shared_ptr<Workbook> workbook = std::make_shared<Workbook>(odsFilePath);

    // Save as xlsx file
    U16String xlsxOutputPath(u"ods_out.xlsx");
    workbook->Save(xlsxOutputPath);

    // Load your source sxc file
    U16String sxcFilePath(u"book1.sxc");
    workbook = std::make_shared<Workbook>(sxcFilePath);

    // Save as xls file
    U16String xlsOutputPath(u"sxc_out.xls");
    workbook->Save(xlsOutputPath);

    // Load your source fods file
    U16String fodsFilePath(u"book1.fods");
    workbook = std::make_shared<Workbook>(fodsFilePath);

    // Save as xlsb file
    U16String xlsbOutputPath(u"fods_out.xlsb");
    workbook->Save(xlsbOutputPath);

    std::cout << "Files converted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Конвертировать Excel в Ods (OpenOffice / LibreOffice Calc)**
Aspose.Cells поддерживает преобразование файлов Excel в файлы Ods, Sxc и Fods. Ниже приведен пример кода, показывающий, как преобразовать [шаблон](book1.xlsx) в файлы Ods, Sxc и Fods.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    Workbook workbook(u"book1.xlsx");

    // Save as ods file 
    workbook.Save(u"Out.ods");

    // Save as sxc file 
    workbook.Save(u"Out.sxc");

    // Save as fods file 
    workbook.Save(u"Out.fods");

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Продвинутые темы**
- [Сохранить файл ODS в спецификациях ODF 1.1 и 1.2](/cells/ru/cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/)
- [Работа с фоном в файлах ODS](/cells/ru/cpp/working-with-background-in-ods-files/)
{{< app/cells/assistant language="cpp" >}}
