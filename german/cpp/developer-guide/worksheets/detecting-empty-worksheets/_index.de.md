---
title: Leere Arbeitsblätter mit C++ erkennen
linktitle: Erkennen leerer Arbeitsblätter
type: docs
weight: 410
url: /de/cpp/detecting-empty-worksheets/
description: Dieser Artikel zeigt Ihnen Codebeispiele, die erklären, wie leere Arbeitsblätter von Excel Arbeitsmappen programmatisch mit C++ API und Aspose.Cells Library erkannt werden.
keywords: Leeres Arbeitsblatt mit C++ erkennen, leeres Excel Arbeitsblatt mit C++ finden
---

## **Überprüfung auf belegte Zellen**

Arbeitsblätter können mit Werten gefüllt sein, wobei die Werte einfach (Text, Nummern, Datum/Uhrzeit) oder eine Formel oder ein Formel-basierter Wert sein können. In einem solchen Fall ist es einfach zu erkennen, ob ein Arbeitsblatt leer ist oder nicht. Alles, was wir überprüfen müssen, sind die [**Cells.MaxDataRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/) oder [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/) Eigenschaften. Wenn die genannten Eigenschaften Null oder positive Werte zurückgeben, bedeutet dies, dass ein oder mehrere Zellen gefüllt wurden. Wenn jedoch eine dieser Eigenschaften -1 zurückgibt, deutet dies darauf hin, dass keine der Zellen im Arbeitsblatt gefüllt ist.

{{% alert color="primary" %}}

Die Zeilen- und Spalten-Sammlungen haben einen nullbasierten Index, daher bedeutet eine Zelle bei Zeile 0 & Spalte 0 die erste Zelle im Arbeitsblatt, also A1.

{{% /alert %}}

## **Überprüfung auf leere initialisierte Zellen**

Alle Zellen mit Werten werden automatisch initialisiert. Es besteht jedoch die Möglichkeit, dass ein Arbeitsblatt Zellen nur mit Formatierung enthält. In einem solchen Szenario geben die [**Cells.MaxDataRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/) oder [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/) Eigenschaften -1 zurück, was auf das Fehlen von gefüllten Werten hinweist. Initialisierte Zellen aufgrund der Zellformatierung können jedoch mit diesem Ansatz nicht erkannt werden. Um zu überprüfen, ob ein Arbeitsblatt leere initialisierte Zellen enthält, wird empfohlen, die `MoveNext`-Methode des Enumerationers, der aus der [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Sammlung gewonnen wurde, zu verwenden. Wenn die `MoveNext`-Methode **true** zurückgibt, bedeutet dies, dass mindestens eine initialisierte Zelle im Arbeitsblatt vorhanden ist.

## **Überprüfung auf Formen**

Es ist möglich, dass ein Arbeitsblatt keine gefüllten Zellen enthält, es jedoch Formen & Objekte wie Steuerelemente, Diagramme, Bilder usw. enthalten kann. Wenn wir überprüfen möchten, ob ein Arbeitsblatt eine Form enthält, können wir dies durch Inspektion der [**ShapeCollection.Count**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/getcount/) Eigenschaft tun. Ein positiver Wert zeigt die Anwesenheit von Formen im Arbeitsblatt an.

## **Programmierbeispiel**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create an instance of Workbook and load an existing spreadsheet
    Workbook book(srcDir + u"sample.xlsx");

    // Loop over all worksheets in the workbook
    WorksheetCollection sheets = book.GetWorksheets();
    for (int i = 0; i < sheets.GetCount(); i++)
    {
        Worksheet sheet = sheets.Get(i);

        // Check if worksheet has populated cells
        if (sheet.GetCells().GetMaxDataRow() != -1)
        {
            cout << sheet.GetName().ToUtf8() << " is not empty because one or more cells are populated" << endl;
        }
        // Check if worksheet has shapes
        else if (sheet.GetShapes().GetCount() > 0)
        {
            cout << sheet.GetName().ToUtf8() << " is not empty because there are one or more shapes" << endl;
        }
        // Check if worksheet has empty initialized cells
        else
        {
            Range range = sheet.GetCells().GetMaxDisplayRange();
            auto rangeIterator = range.GetEnumerator();
            if (rangeIterator.MoveNext())
            {
                cout << sheet.GetName().ToUtf8() << " is not empty because one or more cells are initialized" << endl;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
