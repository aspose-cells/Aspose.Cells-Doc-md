---
title: Supprimer les espaces redondants après un saut de ligne lors de l importation de HTML avec C++
linktitle: Supprimez les espaces redondants après un saut de ligne lors de l importation du HTML
type: docs
weight: 20
url: /fr/cpp/delete-redundant-spaces-after-line-break-while-importing/
description: Apprenez comment supprimer les espaces redondants après les sauts de ligne lors de l importation HTML en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Veuillez utiliser la propriété [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getdeleteredundantspaces/) et la définir sur **true** pour supprimer tous les espaces redondants après la balise de saut de ligne. Par défaut, cette propriété est **false** et les espaces redondants sont conservés dans les fichiers Excel en sortie.

{{% /alert %}}

## Effet de la définition de la propriété HTMLLoadOptions.DeleteRedundantSpaces à false et true

La capture d'écran suivante montre l'effet de définir cette propriété sur **false** et **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## Supprimer les espaces redondants après un saut de ligne lors de l'importation du HTML

### Exemple de programmation

Le code d'exemple suivant montre l'utilisation de la propriété [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getdeleteredundantspaces/). Veuillez le définir sur **true** ou **false** pour obtenir le résultat tel qu'indiqué dans la capture d'écran ci-dessus.

```c++
#include <iostream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String html = u8"<html> <body> <table> <tr> <td> <br>    This is sample data <br>    This is sample data<br>    This is sample data</td> </tr> </table> </body> </html>";

    std::vector<uint8_t> byteArray;
    for (int32_t i = 0; i < html.GetLength(); ++i)
    {
        char16_t c = html[i];
        if (c <= 0x7F)
            byteArray.push_back(static_cast<uint8_t>(c));
    }

    HtmlLoadOptions loadOptions(LoadFormat::Html);
    loadOptions.SetDeleteRedundantSpaces(true);

    Vector<uint8_t> data(byteArray.data(), static_cast<int32_t>(byteArray.size()));
    Workbook workbook(data, loadOptions);

    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);
    sheet.AutoFitColumns();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    workbook.Save(outDir + u"outputDeleteRedundantSpacesWhileImportingFromHtml.xlsx", SaveFormat::Xlsx);

    std::cout << "File saved successfully." << std::endl;

    Cleanup();

    Aspose::Cells::Cleanup();
    return 0;
}
```
