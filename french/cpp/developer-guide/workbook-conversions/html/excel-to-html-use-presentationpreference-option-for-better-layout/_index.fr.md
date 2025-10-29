---
title: Excel vers HTML  Utiliser l option PresentationPreference pour une meilleure mise en page avec C++
linktitle: Excel en HTML  Utiliser l option PresentationPreference pour une meilleure mise en page
type: docs
weight: 220
url: /fr/cpp/excel-to-html-use-presentationpreference-option-for-better-layout/
description: Apprenez à rendre une meilleure mise en page lors de l enregistrement de fichiers Excel en HTML avec C++.
---

{{% alert color="primary" %}} 

Aspose.Cells fournit une propriété HtmlSaveOptions.PresentationPreference utile pour les développeurs qui ont besoin d'obtenir une meilleure mise en page lors de la sauvegarde d'un fichier Microsoft Excel au format HTML ou MHT. La valeur par défaut de la propriété est false. Nous recommandons de définir cette propriété sur true pour obtenir une présentation plus attrayante des rapports Excel.

{{% /alert %}} 

Veuillez consulter le code d'exemple ci-dessous qui démontre comment rendre un fichier HTML à partir d'un rapport Excel avec une préférence de présentation activée.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/HtmlSaveOptions.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Instantiate the Workbook and load an Excel file
    Workbook workbook(inputFilePath);

    // Create HtmlSaveOptions object
    HtmlSaveOptions options;

    // Set the Presentation preference option
    options.SetPresentationPreference(true);

    // Save the Excel file to HTML with specified option
    U16String outputFilePath = srcDir + u"outPresentationlayout1.out.html";
    workbook.Save(outputFilePath, options);

    std::cout << "Excel file saved as HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{< app/cells/assistant language="cpp" >}}
