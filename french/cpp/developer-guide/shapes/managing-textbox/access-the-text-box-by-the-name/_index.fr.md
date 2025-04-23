---
title: Accéder à la boîte de texte par le nom avec C++
linktitle: Accéder à la zone de texte par le nom
type: docs
weight: 230
url: /fr/cpp/access-the-text-box-by-the-name/
description: Apprenez comment accéder à une boîte de texte par son nom en utilisant Aspose.Cells for C++.
---

## Accéder à la zone de texte par le nom

Auparavant, les zones de texte étaient accessibles par index dans la collection [**Worksheet.GetTextBoxes()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettextboxes/), mais maintenant, vous pouvez également accéder à la zone de texte par son nom dans cette collection. C'est une méthode pratique et rapide pour accéder à votre zone de texte si vous connaissez déjà son nom.

Le code d'exemple suivant crée d'abord une boîte de texte, lui assigne un texte et un nom. Ensuite, dans les lignes suivantes, nous accédons à la même boîte de texte par son nom et affichons son contenu.

### Code C++ pour accéder à la boîte de texte par nom

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Create an object of the Workbook class
    Workbook workbook;

    // Access first worksheet from the collection
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add the TextBox to the worksheet
    int idx = sheet.GetTextBoxes().Add(10, 10, 10, 10);

    // Access newly created TextBox using its index & name it
    TextBox tb1 = sheet.GetTextBoxes().Get(idx);
    tb1.SetName(u"MyTextBox");

    // Set text for the TextBox
    tb1.SetText(u"This is MyTextBox");

    // Access the same TextBox via its name
    TextBox tb2 = sheet.GetTextBoxes().Get(u"MyTextBox");

    // Display the text of the TextBox accessed via name
    std::cout << tb2.GetText().ToUtf8() << std::endl;

    std::cout << "Press any key to continue..." << std::endl;
    std::cin.get();

    Aspose::Cells::Cleanup();
}
```

### Sortie de la console générée par le code d'exemple

Voici la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

This is MyTextBox

{{< /highlight >}}
