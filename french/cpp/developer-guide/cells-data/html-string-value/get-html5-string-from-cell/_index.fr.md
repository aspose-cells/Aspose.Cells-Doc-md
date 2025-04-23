---
title: Obtenir la chaîne HTML5 de la cellule avec C++
linktitle: Obtenir la chaîne HTML5 de la cellule
type: docs
weight: 90
url: /fr/cpp/get-html5-string-from-cell/
description: Apprenez comment obtenir la chaîne HTML5 d une cellule en utilisant l API Aspose.Cells for C++.
keywords: Obtenir une chaîne HTML5 de la cellule, Obtenir une chaîne HTML5 de la cellule, Gérer une chaîne HTML5 de cellule
---

## **Scénarios d'utilisation possibles**

Aspose.Cells retourne la chaîne HTML de la cellule en utilisant la méthode [**GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/) qui accepte un paramètre booléen. Si vous passez **false** en paramètre, il retournera le HTML Normal mais si vous passez **true**, il retournera la chaîne HTML5.

## **Obtenir la chaîne HTML5 de la cellule**

Le code d'exemple suivant crée un objet classeur et ajoute du texte dans la cellule A1 de la première feuille de calcul. Ensuite, il récupère la chaîne HTML normale et HTML5 de la cellule A1 à l'aide de la méthode [**GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/) et les imprime dans la console.

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

    // Access cell A1 and put some text inside it
    Cell cell = ws.GetCells().Get(u"A1");
    cell.PutValue(u"This is some text.");

    // Get the Normal and Html5 strings
    U16String strNormal = cell.GetHtmlString(false);
    U16String strHtml5 = cell.GetHtmlString(true);

    // Print the Normal and Html5 strings on console
    std::cout << "Normal:\r\n" << strNormal.ToUtf8() << std::endl;
    std::cout << std::endl;
    std::cout << "Html5:\r\n" << strHtml5.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sortie console**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
