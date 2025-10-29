---
title: Trouver si la valeur de la cellule commence par une marque de citation simple avec C++
linktitle: Trouvez si la valeur de la cellule commence par un guillemet simple
type: docs
weight: 270
url: /fr/cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: Apprenez comment vérifier si la valeur d une cellule commence par une marque de citation simple via l API Aspose.Cells for C++.
keywords: Trouver si la valeur de la cellule commence par un guillemet simple, Rechercher si la valeur de la cellule commence par un guillemet simple
---

{{% alert color="primary" %}}

Aspose.Cells fournit maintenant la propriété [**Style::QuotePrefix**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) pour déterminer si la valeur de la cellule commence par un guillemet simple. Avant cette propriété, il n'y avait aucun moyen de distinguer entre les chaînes comme échantillon et 'échantillon etc.

{{% /alert %}}

Le code d'exemple suivant explique que les chaînes comme échantillon et 'échantillon ne peuvent pas être différenciées avec la propriété [**Cell::GetStringValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/). Nous devons donc utiliser la propriété [**Style::QuotePrefix**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/) pour les distinguer.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook wb;

    // Create worksheet
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Access cell A1 and A2
    Cell a1 = sheet.GetCells().Get(u"A1");
    Cell a2 = sheet.GetCells().Get(u"A2");

    // Add sample in A1 and sample with quote prefix in A2
    a1.PutValue(u"sample");
    a2.PutValue(u"'sample");

    // Print their string values, A1 and A2 both are same
    std::cout << "String value of A1: " << a1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "String value of A2: " << a2.GetStringValue().ToUtf8() << std::endl;

    // Access styles of A1 and A2
    Style s1 = a1.GetStyle();
    Style s2 = a2.GetStyle();

    std::cout << std::endl;

    // Check if A1 and A2 has a quote prefix
    std::cout << "A1 has a quote prefix: " << s1.GetQuotePrefix() << std::endl;
    std::cout << "A2 has a quote prefix: " << s2.GetQuotePrefix() << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
