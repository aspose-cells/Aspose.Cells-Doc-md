---
title: Afficher des puces en définissant la valeur de la cellule en HTML avec C++
linktitle: Afficher des puces en définissant la valeur de la cellule à l aide d HTML
type: docs
weight: 130
url: /fr/cpp/display-bullets-by-setting-cell-value-using/
description: Ajouter des puces dans les cellules Excel en utilisant HTML et l API Aspose.Cells for C++ facile à utiliser.
keywords: ajouter des puces dans Excel, ajouter des puces dans Excel C++, afficher des puces dans Excel, afficher des puces dans Excel C++, ajouter des puces dans Excel avec HTML, ajouter des puces dans Excel avec HTML C++, afficher des puces dans Excel avec HTML, afficher des puces dans Excel avec HTML C++, afficher des puces dans Excel en utilisant HTML, ajouter des puces dans Excel en utilisant HTML
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge l'affichage des puces avec du code HTML. Cet article expliquera comment afficher des puces en définissant la valeur de la cellule à l'aide d'HTML. Nous utiliserons [**Cell.GetHtmlString()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/) la propriété pour définir la valeur de la cellule avec notre HTML.

{{% /alert %}}

## Code C++ pour afficher des puces en définissant la valeur de la cellule en HTML

Le code suivant utilise le code HTML pour définir la valeur de la cellule. Une fois que vous aurez exécuté ce code, vous obtiendrez la sortie comme indiqué dans l'image ci-dessous.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get("A1");

    // Set the HTML string
    cell.SetHtmlString(u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'>Text 1 </font>"
                       u"<font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font>"
                       u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 2 </font>"
                       u"<font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font>"
                       u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 3 </font>"
                       u"<font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font>"
                       u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 4 </font>");

    // Auto fit the Columns
    worksheet.AutoFitColumns();

    // Save the workbook
    U16String outputFilePath = u"BulletsInCells_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Sortie générée par le code d'exemple

La capture d'écran suivante montre la sortie du code d'exemple ci-dessus.

![todo:image_alt_text](display-bullets-by-setting-cell-value-using-html_1.png)
{{< app/cells/assistant language="cpp" >}}
