---
title: Conserver le préfixe de guillemet simple du contenu ou de la plage de la cellule avec C++
linktitle: Préserver le préfixe de guillemet simple de la valeur de la cellule ou de la plage
type: docs
weight: 310
url: /fr/cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: Apprenez comment préserver le préfixe de guillemet simple du contenu ou de la plage via l’API Aspose.Cells for C++.
keywords: Préserver le préfixe de guillemet simple de la valeur de la cellule ou de la plage, Masquer le guillemet apostrophe ou le marqueur de guillemet simple en tête, Afficher le guillemet apostrophe ou le marqueur de guillemet simple en tête
---

## **Scénarios d'utilisation possibles**

Lorsque vous insérez une valeur dans la cellule qui commence par un apostrophe ou une marque de guillemet simple, alors Microsoft Excel la masque, mais lorsque vous sélectionnez la cellule, il affiche l’apostrophe ou le guillemet simple dans la barre de formule comme illustré dans la capture d'écran suivante.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells masque également l’apostrophe ou le guillemet simple comme Microsoft Excel, mais il définit [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) comme **true** pour cette cellule. Si vous définissez un style vide pour la cellule, alors [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) redevient **false**. Pour gérer ce problème, Aspose.Cells fournit la propriété [**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/getquoteprefix/). Lorsqu’elle est réglée sur **false**, [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) n’est pas du tout mis à jour et sa valeur ancienne est conservée. Cela signifie que si la valeur ancienne de la propriété [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) était **true**, elle restera **true**, et si elle était **false**, elle restera **false**.

## **Préserver le préfixe d'apostrophe unique de la valeur de la cellule ou de la plage**

Le code d’exemple ci-dessous explique l’utilisation de la propriété [**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/getquoteprefix/) comme décrit précédemment. Veuillez lire les commentaires dans le code et voir la sortie console ci-dessous pour plus d’aide.

## **Code d'exemple**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = ws.GetCells().Get(u"A1");

    // Put some text in cell, it does not have Single Quote at the beginning
    cell.PutValue(u"Text");

    // Access style of cell A1
    Style st = cell.GetStyle();

    // Print the value of Style.QuotePrefix of cell A1
    std::cout << "Quote Prefix of Cell A1: " << st.GetQuotePrefix() << std::endl;

    // Put some text in cell, it has Single Quote at the beginning
    cell.PutValue(u"'Text");

    // Access style of cell A1
    st = cell.GetStyle();

    // Print the value of Style.QuotePrefix of cell A1
    std::cout << "Quote Prefix of Cell A1: " << st.GetQuotePrefix() << std::endl;

    // Print information about StyleFlag.QuotePrefix property
    std::cout << std::endl;
    std::cout << "When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix." << std::endl;
    std::cout << "Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix." << std::endl;
    std::cout << std::endl;

    // Create an empty style
    st = wb.CreateStyle();

    // Create style flag - set StyleFlag.QuotePrefix as false
    // It means, we do not want to update the Style.QuotePrefix property of cell A1's style.
    StyleFlag flag;
    flag.SetQuotePrefix(false);

    // Create a range consisting of single cell A1
    Range rng = ws.GetCells().CreateRange(u"A1");

    // Apply the style to the range
    rng.ApplyStyle(st, flag);

    // Access the style of cell A1
    st = cell.GetStyle();

    // Print the value of Style.QuotePrefix of cell A1
    // It will print True, because we have not updated the Style.QuotePrefix property of cell A1's style.
    std::cout << "Quote Prefix of Cell A1: " << st.GetQuotePrefix() << std::endl;

    // Create an empty style
    st = wb.CreateStyle();

    // Create style flag - set StyleFlag.QuotePrefix as true
    // It means, we want to update the Style.QuotePrefix property of cell A1's style.
    flag.SetQuotePrefix(true);

    // Apply the style to the range
    rng.ApplyStyle(st, flag);

    // Access the style of cell A1
    st = cell.GetStyle();

    // Print the value of Style.QuotePrefix of cell A1
    // It will print False, because we have updated the Style.QuotePrefix property of cell A1's style.
    std::cout << "Quote Prefix of Cell A1: " << st.GetQuotePrefix() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sortie console**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
