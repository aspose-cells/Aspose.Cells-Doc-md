---
title: Enregistrer un classeur au format de feuille de calcul XML strict avec C++
linktitle: Enregistrer le classeur au format de feuille de calcul strict Open XML
type: docs
weight: 150
url: /fr/cpp/save-workbook-to-strict-open-xml-spreadsheet-format/
description: Apprenez comment enregistrer un classeur au format XML strict en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Aspose.Cells permet d'enregistrer le classeur au format *Strict Open XML Spreadsheet*. À cette fin, il fournit la propriété [**GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcompliance/). Si vous définissez sa valeur à [**OoxmlCompliance::Iso29500_2008_Strict**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompliance/), le fichier Excel de sortie sera enregistré au format Strict Open XML Spreadsheet.

## **Enregistrer le classeur au format strict Open XML Spreadsheet**

Le code d'exemple suivant crée un classeur et définit la valeur de la propriété [**GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcompliance/) à [**OoxmlCompliance::Iso29500_2008_Strict**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompliance/), puis l'enregistre en tant que [fichier Excel de sortie](67338272.xlsx). Si vous ouvrez le fichier Excel de sortie dans Microsoft Excel et ouvrez la boîte de dialogue Enregistrer sous..., vous verrez son format comme *Strict Open XML Spreadsheet* comme indiqué dans cette capture d'écran.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Code d'exemple**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook wb;

    // Specify - Strict Open XML Spreadsheet - Format
    wb.GetSettings().SetCompliance(OoxmlCompliance::Iso29500_2008_Strict);

    // Add message in cell B4 of first worksheet
    Cell b4 = wb.GetWorksheets().Get(0).GetCells().Get(u"B4");
    b4.PutValue(u"This Excel file has Strict Open XML Spreadsheet format.");

    // Save to output Excel file
    wb.Save(u"outputSaveWorkbookToStrictOpenXMLSpreadsheetFormat.xlsx", SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully with Strict Open XML Spreadsheet format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
