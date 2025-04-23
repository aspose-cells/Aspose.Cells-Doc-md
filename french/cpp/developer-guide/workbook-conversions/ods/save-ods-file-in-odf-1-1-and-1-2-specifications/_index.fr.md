---
title: Enregistrer un fichier ODS dans les spécifications ODF 1.1, 1.2 et 1.3 avec C++
linktitle: Enregistrer en tant que ODF 1.1, 1.2 et 1.3
description: Convertir Excel en spécifications ODF 1.1, 1.2 et 1.3 avec Aspose.Cells en C++.
type: docs
weight: 230
url: /fr/cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge la sauvegarde d'un fichier ODS (**OpenDocument Spreadsheet**) dans les spécifications ODF (**OpenDocument Format**) 1.1, 1.2 et 1.3. Aspose.Cells dispose de la propriété [**OdsSaveOptions.GetOdfStrictVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells/odssaveoptions/getodfstrictversion/) qui spécifie la version ODF pour la sauvegarde des fichiers ODS. La valeur par défaut de cette propriété est [**OpenDocumentFormatVersionType.Odf12**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/opendocumentformatversiontype/), donc le fichier ODS enregistré sans cette configuration utilise la spécification 1.2.

{{% /alert %}}

Le code d'exemple ci-dessous crée un objet classeur, ajoute une valeur dans la cellule A1 de la première feuille de calcul, puis enregistre le fichier ODS selon les spécifications ODF 1.1, 1.2 et 1.3. Par défaut, le fichier ODS est enregistré selon la spécification ODF 1.2.

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

    // Create workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put some value in cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");
    cell.PutValue(u"Welcome to Aspose!");

    // Save ODS in ODF 1.2 version which is default
    OdsSaveOptions options;
    workbook.Save(outDir + u"ODF1.2_out.ods", options);

    // Save ODS in ODF 1.1 version
    options.SetOdfStrictVersion(OpenDocumentFormatVersionType::Odf11);
    workbook.Save(outDir + u"ODF1.1_out.ods", options);

    // Save ODS in ODF 1.3 version
    options.SetOdfStrictVersion(OpenDocumentFormatVersionType::Odf13);
    workbook.Save(outDir + u"ODF1.3_out.ods", options);

    std::cout << "ODS files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
