---
title: Lecture des valeurs de la cellule simultanément dans plusieurs threads avec C++
linktitle: Plusieurs threads
type: docs
weight: 1800
url: /fr/cpp/reading-cell-values-in-multiple-threads-simultaneously/
description: Apprenez comment lire les valeurs de la cellule simultanément dans plusieurs threads via l’API Aspose.Cells for C++.
keywords: Lecture simultanée des valeurs de la cellule dans plusieurs threads, Aspose.Cells C++, lecture de données en plusieurs threads
---

{{% alert color="primary" %}}

La nécessité de lire les valeurs de cellule dans plusieurs threads simultanément est une exigence courante. Cet article explique comment utiliser Aspose.Cells à cette fin.

{{% /alert %}}

Pour lire les valeurs de cellule dans plus d'un thread simultanément, définissez [**Worksheet.GetMultiThreadReading()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmultithreadreading/) sur **true**. Sinon, vous pourriez obtenir les mauvaises valeurs de cellule.

Le code suivant :

1. Crée un classeur.
1. Ajoute une feuille de calcul.
1. Remplit la feuille de calcul avec des valeurs de chaîne.
1. Crée ensuite deux threads qui lisent simultanément les valeurs de cellules aléatoires.
   Si les valeurs lues sont correctes, rien ne se passe. Si les valeurs lues sont incorrectes, un message est affiché.

Si vous commentez cette ligne :

{{< highlight cpp >}}

 testWorkbook->get_Worksheets()->Get(0)->get_Cells()->set_MultiThreadReading(true);

{{< /highlight >}}

alors le message suivant est affiché :

{{< highlight cpp >}}

 if (s != "R" + row + "C" + col)

{

    MessageBox::Show("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

Sinon, le programme s'exécute sans afficher de message, ce qui signifie que toutes les valeurs lues dans les cellules sont correctes.

```cpp
#include <iostream>
#include <thread>
#include <random>
#include <chrono>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

static Workbook testWorkbook;

U16String IntToU16String(int value) {
    wstring ws = to_wstring(value);
    return U16String(reinterpret_cast<const char16_t*>(ws.c_str()));
}

void ThreadLoop()
{
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> rowDist(0, 9999);
    uniform_int_distribution<> colDist(0, 99);

    while (true)
    {
        try
        {
            int row = rowDist(gen);
            int col = colDist(gen);
            U16String s = testWorkbook.GetWorksheets().Get(0).GetCells().Get(row, col).GetStringValue();
            U16String expected = U16String(u"R") + IntToU16String(row) + U16String(u"C") + IntToU16String(col);
            if (s != expected)
            {
                cout << "This message will show up when cells read values are incorrect." << endl;
            }
        }
        catch (...) {}
    }
}

void TestMultiThreadingRead()
{
    testWorkbook = Workbook();
    testWorkbook.GetWorksheets().Clear();
    testWorkbook.GetWorksheets().Add(u"Sheet1");

    for (int row = 0; row < 10000; row++)
    {
        for (int col = 0; col < 100; col++)
        {
            U16String value = U16String(u"R") + IntToU16String(row) + U16String(u"C") + IntToU16String(col);
            testWorkbook.GetWorksheets().Get(0).GetCells().Get(row, col).SetValue(value);
        }
    }

    // Commenting this line will show a pop-up message
    // testWorkbook.GetWorksheets().Get(0).GetCells().SetMultiThreadReading(true);

    thread myThread1(ThreadLoop);
    thread myThread2(ThreadLoop);

    this_thread::sleep_for(chrono::seconds(5));

    myThread1.detach();
    myThread2.detach();
}

int main()
{
    Aspose::Cells::Startup();
    TestMultiThreadingRead();
    Aspose::Cells::Cleanup();
    return 0;
}
```
