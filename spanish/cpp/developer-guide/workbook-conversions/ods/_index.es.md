---
title: Convertir libro de Excel a Ods, Sxc y Fods (OpenOffice / LibreOffice calc) con C++
linktitle: Ods
type: docs
weight: 20
url: /es/cpp/convert-excel-to-ods/
description: Cómo convertir Excel a Ods (OpenOffice / LibreOffice Calc) o convertir Ods a Excel con Aspose.Cells con C++.
---

## **Acerca de OpenDocument**
El [formato de documento abierto (ODF)](https://es.wikipedia.org/wiki/OpenDocument) es un formato de archivo gratuito y abierto para documentos de oficina electrónicos desarrollado originalmente por Sun para la suite Open Office. OpenDocument Spreadsheet (ODS) es el formato de archivo para documentos de Excel. OpenDocument es actualmente un estándar OASIS e ISO.

## **Convertir Ods (OpenOffice / LibreOffice calc) a Excel**
Aspose.Cells soporta cargar Ods, Sxc y Fods, que son soportados por OpenOffice / LibreOffice Calc, y convertir [Ods](book1.ods), [Sxc](book1.sxc), y [Fods](book1.fods) a archivos de Excel.

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

## **Convertir Excel a Ods (OpenOffice / LibreOffice Calc)**
Aspose.Cells soporta convertir archivos de Excel a archivos Ods, Sxc y Fods. El ejemplo de código a continuación muestra cómo convertir el [modelo](book1.xlsx) en archivos Ods, Sxc y Fods.

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

## **Temas avanzados**
- [Guardar archivo ODS en las especificaciones de ODF 1.1 y 1.2](/cells/es/cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/)
- [Trabajar con fondo en archivos ODS](/cells/es/cpp/working-with-background-in-ods-files/)
{{< app/cells/assistant language="cpp" >}}
