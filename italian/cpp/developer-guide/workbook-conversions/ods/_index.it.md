---
title: Converti cartella di lavoro Excel in Ods, Sxc e Fods (OpenOffice / LibreOffice calc) con C++
linktitle: Ods
type: docs
weight: 20
url: /it/cpp/convert-excel-to-ods/
description: Come convertire Excel in Ods (OpenOffice / LibreOffice Calc) o convertire Ods (OpenOffice / LibreOffice Calc) in Excel con Aspose.Cells con C++.
---

## **Informazioni su OpenDocument**
Il [formato OpenDocument (ODF)](https://it.wikipedia.org/wiki/OpenDocument) è un formato file libero e aperto per documenti elettronici originariamente sviluppato da Sun per la suite Open Office. Il formato file per i documenti Excel è OpenDocument Spreadsheet (ODS). OpenDocument è attualmente uno standard OASIS e ISO.

## **Converti Ods (OpenOffice / LibreOffice calc) in Excel**
Aspose.Cells supporta il caricamento di Ods, Sxc e Fods, supportati da OpenOffice / LibreOffice Calc, e converte [Ods](book1.ods), [Sxc](book1.sxc), e [Fods](book1.fods) in file Excel.

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

## **Converti Excel in Ods (OpenOffice / LibreOffice Calc)**
Aspose.Cells supporta la conversione di file Excel in file Ods, Sxc e Fods. L'esempio di codice di seguito mostra come convertire il [modello](book1.xlsx) in file Ods, Sxc e Fods.

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

## **Argomenti avanzati**
- [Salva il file ODS nelle specifiche ODF 1.1 e 1.2](/cells/it/cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/)
- [Lavorare con lo sfondo nei file ODS](/cells/it/cpp/working-with-background-in-ods-files/)
{{< app/cells/assistant language="cpp" >}}
