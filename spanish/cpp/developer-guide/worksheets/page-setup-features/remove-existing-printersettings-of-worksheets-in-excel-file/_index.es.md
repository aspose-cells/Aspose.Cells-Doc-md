---
title: Eliminar la configuración de impresora existente de las hojas de trabajo en archivo Excel con C++
linktitle: Eliminar la configuración de impresora existente de las hojas de trabajo
type: docs
weight: 60
url: /es/cpp/remove-existing-printersettings-of-worksheets-in-excel-file/
description: Aprende cómo eliminar la configuración de impresora existente de una hoja de trabajo dentro del archivo Excel mediante el objeto Configuración de Página programáticamente usando Aspose.Cells con C++.
keywords: eliminar configuración de impresora de hoja de trabajo c++, eliminar configuración de impresora de hoja de Excel c++
---

## **Escenarios de uso posibles**
A veces, los desarrolladores desean evitar que Excel incluya archivos * .bin * de la configuración de impresora en los archivos XLSX guardados. Los archivos de configuración de impresora se encuentran en * "[file \"root\"] \xl \ printerSettings". *  Este documento explica cómo eliminar la configuración de impresora existente utilizando las API de Aspose.Cells.

## **Eliminar la configuración existente de PrinterSettings de las hojas de cálculo en el archivo de Excel**
Aspose.Cells te permite eliminar la configuración de impresora existente especificada para diferentes hojas en el archivo de Excel. El siguiente código de ejemplo ilustra cómo eliminar la configuración de impresora existente para todas las hojas de trabajo en el libro. Consulta su [archivo de Excel de muestra](45056020.xlsx), [archivo de Excel de salida](45056021.xlsx), salida de la consola y captura de pantalla como referencia.

## **Captura de pantalla**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **Código de muestra**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb(srcDir + u"sampleRemoveExistingPrinterSettingsOfWorksheets.xlsx");

    int sheetCount = wb.GetWorksheets().GetCount();

    for (int i = 0; i < sheetCount; i++)
    {
        Worksheet ws = wb.GetWorksheets().Get(i);
        PageSetup ps = ws.GetPageSetup();

        if (ps.GetPrinterSettings().GetLength() != 0)
        {
            std::cout << "PrinterSettings of this worksheet exist." << std::endl;
            std::cout << "Sheet Name: " << ws.GetName().ToUtf8() << std::endl;
            std::cout << "Paper Size: " << static_cast<int>(ps.GetPaperSize()) << std::endl;

            ps.SetPrinterSettings(Vector<uint8_t>());
            std::cout << "Printer settings of this worksheet are now removed by setting it null." << std::endl;
            std::cout << std::endl;
        }
    }

    wb.Save(outDir + u"outputRemoveExistingPrinterSettingsOfWorksheets.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Salida de la consola**
{{< highlight java >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: PaperLegal

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: PaperEnvelopeB5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: PaperA6

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: PaperA3

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
