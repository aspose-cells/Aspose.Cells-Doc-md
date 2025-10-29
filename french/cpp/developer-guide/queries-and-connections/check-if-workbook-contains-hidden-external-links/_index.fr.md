---
title: Vérifier si le classeur contient des liens externes cachés avec C++
linktitle: Vérifiez si le classeur contient des liens externes cachés
type: docs
weight: 230
url: /fr/cpp/check-if-workbook-contains-hidden-external-links/
description: Apprenez comment détecter les liens externes cachés dans les classeurs Excel en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**
Parfois, le classeur contient des liens externes qui sont cachés et ne peuvent pas être visualisés dans Microsoft Excel. Aspose.Cells récupère tous les liens externes, qu'ils soient visibles ou cachés. Cependant, vous pouvez vérifier la propriété [ExternalLink.IsVisible](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/isvisible/) pour voir si le lien externe est visible ou non.

## **Vérifiez si le classeur contient des liens externes cachés**
Le code d'exemple suivant charge le [fichier source Excel](5115413.xlsx) qui contient des liens externes cachés. Ces liens ne peuvent pas être visualisés dans Microsoft Excel mais ils sont présents dans le classeur. Après avoir affiché [ExternalLink.GetDataSource()](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/getdatasource/) et la propriété [ExternalLink.IsReferred](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/isreferred/), il affiche la propriété [ExternalLink.IsVisible](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/isvisible/). Dans la sortie de la console ci-dessous, vous voyez que tous ses liens externes ne sont pas visibles.

### **Code d'exemple**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Loads the workbook which contains hidden external links
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access the external link collection of the workbook
    ExternalLinkCollection links = workbook.GetWorksheets().GetExternalLinks();

    // Print all the external links and check their IsVisible property
    for (int i = 0; i < links.GetCount(); i++)
    {
        ExternalLink link = links.Get(i);
        std::cout << "Data Source: " << link.GetDataSource().ToUtf8() << std::endl;
        std::cout << "Is Visible: " << (link.IsVisible() ? "true" : "false") << std::endl;
        std::cout << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

### **Sortie console**
Voici la sortie console du code d'exemple ci-dessus lors de son exécution avec le [fichier Excel d'exemple](5115413.xlsx) donné.

{{< highlight java >}}

Data Source: C:\International\DDB\FAS 133\Swap Rates\GS_1M_3M_1_2_5_¥$_(B)IRSwaps_0400.xls

Is Referred: True

Is Visible: False

Data Source: C:\DIST DAY\MAY TEMPLATES\030601t.xls

Is Referred: True

Is Visible: False

Data Source: C:\AREVIEW\2002 Controllable\Autobrct.xls

Is Referred: True

Is Visible: False

Data Source: C:\CARDSFO\Main Files\Rate Forecast\FY 11\IFR 11 01 (New Model REPORTS 11.08.07).xls

Is Referred: True

Is Visible: False

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
