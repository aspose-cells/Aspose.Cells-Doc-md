---
title: Éviter la notation exponentielle des grands nombres lors de l importation depuis HTML avec C++
linktitle: Éviter la notation exponentielle des grands nombres lors de l importation à partir d un fichier HTML
type: docs
weight: 10
url: /fr/cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: Apprenez comment éviter la notation exponentielle des grands nombres lors de l importation depuis HTML en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Parfois, votre HTML contient des nombres comme 1234567890123456 qui ont plus de 15 chiffres, et lorsque vous importez votre HTML dans un fichier Excel, ces nombres se convertissent en notation exponentielle comme 1.23457E+15. Si vous souhaitez que votre numéro soit importé tel quel et non converti en notation exponentielle, veuillez utiliser la propriété [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/cpp/aspose.cells/abstracttextloadoptions/getkeepprecision/) et la définir sur **true** lors du chargement de votre HTML.

{{% /alert %}}

Le code d'exemple suivant explique l'utilisation de la propriété [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/cpp/aspose.cells/abstracttextloadoptions/getkeepprecision/). L'API importera le nombre tel quel sans le convertir en notation exponentielle.

```c++
#include <iostream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Startup();

    U16String html = u"<html><body><p>1234567890123456</p></body></html>";

    std::vector<uint8_t> byteArray;
    for (int32_t i = 0; i < html.GetLength(); ++i)
    {
        char16_t c = html[i];
        if (c <= 0x7F)
            byteArray.push_back(static_cast<uint8_t>(c));
    }

    HtmlLoadOptions loadOptions = HtmlLoadOptions(LoadFormat::Html);
    loadOptions.SetKeepPrecision(true);

    Vector<uint8_t> data(byteArray.data(), static_cast<int32_t>(byteArray.size()));
    Workbook workbook(data, loadOptions);

    Worksheet sheet = workbook.GetWorksheets().Get(0);
    sheet.AutoFitColumns();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    workbook.Save(outDir + u"outputAvoidExponentialNotationWhileImportingFromHtml.xlsx", SaveFormat::Xlsx);

    std::cout << "File saved successfully." << std::endl;

    Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
