---
title: Spécifier un ensemble individuel ou privé de polices pour le rendu du classeur avec C++
linktitle: Spécifier un ensemble individuel ou privé de polices pour le rendu de classeur
type: docs
weight: 40
url: /fr/cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/
description: Apprenez comment spécifier un ensemble individuel ou privé de polices pour le rendu du classeur en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

En général, vous spécifiez le répertoire des polices ou une liste de polices pour tous les classeurs, mais parfois, vous devez spécifier un ensemble individuel ou privé de polices pour vos classeurs. Aspose.Cells fournit la classe [**IndividualFontConfigs**](https://reference.aspose.com/cells/cpp/aspose.cells/individualfontconfigs/) qui peut être utilisée pour spécifier l'ensemble individuel ou privé de polices pour votre classeur.

## **Spécifier un ensemble de polices individuelles ou privées pour le rendu du classeur**

Le code d'exemple ci-dessous charge le fichier Excel d'exemple (67338268.xlsx) avec son ensemble individuel ou privé de polices, qui sont spécifiées en utilisant la classe [**IndividualFontConfigs**](https://reference.aspose.com/cells/cpp/aspose.cells/individualfontconfigs/). Veuillez voir la police d'exemple (67338271.zip) utilisée dans le code ainsi que le PDF de sortie (67338269.pdf) généré. La capture d'écran suivante montre le rendu du PDF si la police est trouvée avec succès.

![todo:image_alt_text](specify-individual-or-private-set-of-fonts-for-workbook-rendering_1.png)

## **Code d'exemple**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path of your custom font directory
    U16String customFontsDir(u"C:\\TempDir\\CustomFonts");

    // Specify individual font configs custom font directory
    IndividualFontConfigs fontConfigs;

    // If you comment this line or if custom font directory is wrong or 
    // if it does not contain required font then output pdf will not be rendered correctly
    fontConfigs.SetFontFolder(customFontsDir, false);

    // Specify load options with font configs
    LoadOptions opts(LoadFormat::Xlsx);
    opts.SetFontConfigs(fontConfigs);

    // Load the sample Excel file with individual font configs
    Workbook wb(u"sampleSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.xlsx", opts);

    // Save to PDF format
    wb.Save(u"outputSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.pdf", SaveFormat::Pdf);

    std::cout << "Workbook saved to PDF with custom font configurations successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
