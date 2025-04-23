---
title: Convertir le classeur Excel en Ods, Sxc et Fods (OpenOffice / LibreOffice calc) avec C++
linktitle: Ods
type: docs
weight: 20
url: /fr/cpp/convert-excel-to-ods/
description: Comment convertir Excel en Ods (OpenOffice / LibreOffice Calc) ou convertir Ods (OpenOffice / LibreOffice Calc) en Excel avec Aspose.Cells en C++.
---

## **À propos du format OpenDocument**
Le [format OpenDocument (ODF)](https://en.wikipedia.org/wiki/OpenDocument) est un format de fichier gratuit et ouvert pour les documents de bureau électroniques initialement développé par Sun pour la suite Open Office. OpenDocument Spreadsheet (ODS) est le format de fichier pour les documents Excel. OpenDocument est actuellement une norme OASIS et ISO.

## **Convertir Ods (OpenOffice / LibreOffice calc) en Excel**
Aspose.Cells prend en charge le chargement d'Ods, Sxc et Fods, qui sont pris en charge par OpenOffice / LibreOffice Calc, et convertit [Ods](book1.ods), [Sxc](book1.sxc), et [Fods](book1.fods) en fichiers Excel.

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

## **Convertir Excel en Ods (OpenOffice / LibreOffice Calc)**
Aspose.Cells prend en charge la conversion des fichiers Excel en fichiers Ods, Sxc, et Fods. L'exemple de code ci-dessous montre comment convertir le [modèle](book1.xlsx) en fichiers Ods, Sxc, et Fods.

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

## **Sujets avancés**
- [Enregistrer un fichier ODS selon les spécifications ODF 1.1 et 1.2.](/cells/fr/cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/)
- [Travailler avec l'arrière-plan dans les fichiers ODS](/cells/fr/cpp/working-with-background-in-ods-files/)
