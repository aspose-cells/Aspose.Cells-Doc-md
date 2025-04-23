---
title: Convertir des dates en dates japonaises avec C++
linktitle: Convertir les dates en dates japonaises
type: docs
weight: 350
url: /fr/cpp/convert-dates-to-japanese-dates/
description: Apprenez comment convertir des dates grégoriennes en dates japonaises en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Dans le calendrier japonais, une nouvelle ère commence avec le règne d’un nouveau empereur. Le 1er mai 2019, un nouveau empereur est monté sur le trône, marquant la fin de l’ère Heisei et le début de l’ère Reiwa.

{{% /alert %}}

Aspose.Cells offre un moyen de convertir les dates grégoriennes en dates japonaises. Lors de cette conversion, les changements d'ère sont également pris en compte. Le fragment de code suivant convertit le fichier [Excel source](90112015.xlsx) contenant des dates grégoriennes en [PDF de sortie](90112016.pdf) avec des dates japonaises comme indiqué dans l'image ci-dessous.

![todo:image_alt_text](convert-dates-to-japanese-dates_1.jpg)

```c++
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

    // Create load options for XLSX format
    LoadOptions options(LoadFormat::Xlsx);

    // Set culture info to Japanese
    options.SetLanguageCode(CountryCode::Japan);

    // Load the workbook with Japanese dates
    Workbook workbook(srcDir + u"JapaneseDates.xlsx", options);

    // Save the workbook as PDF
    workbook.Save(outDir + u"JapaneseDates.pdf", SaveFormat::Pdf);

    std::cout << "Workbook saved successfully as PDF with Japanese dates!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
