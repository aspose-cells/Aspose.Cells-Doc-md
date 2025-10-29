---
title: Obtenir l adresse, le nombre de cellules, le décalage, la colonne entière et la ligne entière de la plage avec C++
linktitle: Obtenir l adresse, le nombre de cellules, le décalage, la colonne entière et la ligne entière de la plage
type: docs
weight: 330
url: /fr/cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
description: Apprenez comment obtenir l adresse, le nombre de cellules, le décalage, la colonne entière et la ligne entière d une plage en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**
Aspose.Cells fournit l'objet `Range`, qui possède diverses méthodes utilitaires facilitant le travail avec les plages Excel. Cet article illustre l'utilisation des méthodes ou propriétés suivantes de l'objet `Range` :

- **Adresse**

  Obtient l'adresse de la plage.

- **Nombre de cellules**

  Obtient le nombre total de cellules dans la plage.

- **Décalage**

  Obtient une plage par décalage.

- **Colonne entière**

  Obtient un objet `Range` qui représente la colonne entière (ou les colonnes) contenant la plage spécifiée.

- **Ligne entière**

  Obtient un objet `Range` qui représente la ligne entière (ou les lignes) contenant la plage spécifiée.

## **Obtenir l'adresse, le nombre de cellules, le décalage, la colonne entière et la ligne entière de la plage**
Le code d'exemple suivant explique l'utilisation des méthodes et propriétés évoquées ci-dessus. Veuillez voir la sortie de la console du code ci-dessous pour référence.

## **Code d'exemple**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Create range A1:B3
    cout << "Creating Range A1:B3" << endl;
    Range rng = ws.GetCells().CreateRange(u"A1:B3");

    // Print range address and cell count
    cout << "Range Address: " << rng.GetAddress().ToUtf8() << endl;
    cout << "Range row Count: " << rng.GetRowCount() << endl;
    cout << "Range column Count: " << rng.GetColumnCount() << endl;

    // Formatting console output
    cout << "----------------------" << endl;
    cout << endl;

    // Create range A1
    cout << "Creating Range A1" << endl;
    rng = ws.GetCells().CreateRange(u"A1");

    // Print range offset, entire column and entire row
    cout << "Offset: " << rng.GetOffset(2, 2).GetAddress().ToUtf8() << endl;
    cout << "Entire Column: " << rng.GetEntireColumn().GetAddress().ToUtf8() << endl;
    cout << "Entire Row: " << rng.GetEntireRow().GetAddress().ToUtf8() << endl;

    // Formatting console output
    cout << "----------------------" << endl;
    cout << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Sortie console**
{{< highlight java >}}

Creating Range A1:B3

Range Address: A1:B3

Cell Count: 6

\----------------------

Creating Range A1

Offset: C3

Entire Column: A:A

Entire Row: 1:1

\----------------------

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
