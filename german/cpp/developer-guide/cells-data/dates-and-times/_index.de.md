---
title: Wie man Daten und Zeiten mit C++ verwaltet
linktitle: Wie man Daten und Zeiten verwaltet
type: docs
weight: 600
url: /de/cpp/how-to-manage-dates-and-times/
description: Lernen Sie, wie Sie Daten und Zeiten über die Aspose.Cells for C++ API verwalten.
keywords: Wie man Daten und Zeiten verwaltet, das 1900 Datensystem, das 1904 Datensystem, Daten und Zeiten setzen, Daten und Zeiten abrufen, Daten und Zeiten verwalten, Daten und Zeiten in Excel speichern, Daten und Zeiten in Zellen anzeigen.
---

## **Wie man Daten und Zeiten in Excel speichert**
Daten und Zeiten werden in Zellen als Zahlen gespeichert. Daher sind die Werte von Zellen, die Daten und Zeiten enthalten, vom numerischen Typ. Eine Zahl, die Datum und Uhrzeit angibt, besteht aus den Komponenten Datum (Ganzzahlanteil) und Uhrzeit (Bruchteil). Die Methode `Cell::GetDoubleValue()` gibt diese Zahl zurück.

## **Wie man Daten und Zeiten in Aspose.Cells anzeigt**
Um eine Zahl als Datum und Uhrzeit anzuzeigen, wenden Sie das erforderliche Datum- und Uhrzeitformat auf eine Zelle über die Methoden `Style::SetNumber()` oder `Style::SetCustom()` an. Die Methode `Cell::GetDateTimeValue()` gibt das `DateTime`-Objekt zurück, das das Datum und die Uhrzeit angibt, die durch die in der Zelle enthaltene Zahl dargestellt werden.
<br>
<image src="1.png" width="70%" />

## **Wie man zwischen zwei Datumsystemen in Aspose.Cells wechselt**
MS-Excel speichert Daten als Zahlen, die als Serienwerte bezeichnet werden. Ein Serienwert ist eine Ganzzahl, die die Anzahl der vergangenen Tage seit dem ersten Tag im Datensystem angibt. Excel unterstützt die folgenden Datensysteme für Serienwerte:

1. Das 1900-Datensystem. Das erste Datum ist der 1. Januar 1900 und sein Serienwert ist 1. Das letzte Datum ist der 31. Dezember 9999 und sein Serienwert beträgt 2.958.465. Dieses Datensystem wird standardmäßig in der Arbeitsmappe verwendet.
1. Das 1904-Datensystem. Das erste Datum ist 1. Januar 1904 und sein Serienwert ist 0. Das letzte Datum ist der 31. Dezember 9999 und sein Serienwert ist 2.957.003. Um dieses Datensystem im Arbeitsbuch zu verwenden, setzen Sie die Eigenschaft `Workbook::GetSettings()->SetDate1904(true)`.

Dieses Beispiel zeigt, dass die in verschiedenen Datensystemen gespeicherten Serienwerte für dasselbe Datum unterschiedlich sind.
```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook workbook;
    workbook.GetSettings().SetDate1904(false);

    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell a1 = cells.Get(u"A1");
    a1.PutValue(45237.0);

    if (a1.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A1 is Numeric Value: " << a1.GetDoubleValue() << std::endl;
    }

    workbook.GetSettings().SetDate1904(true);
    std::cout << "use The 1904 date system====================" << std::endl;

    Cell a2 = cells.Get(u"A2");
    a2.PutValue(43775.0);

    if (a2.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A2 is Numeric Value: " << a2.GetDoubleValue() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
Ausgabenergebnis:
```
A1 is Numeric Value: 45253
use The 1904 date system====================
A2 is Numeric Value: 43791
```

## **So legen Sie den DateTime-Wert in Aspose.Cells fest**
Dieses Beispiel setzt einen `DateTime`-Wert in die Zellen A1 und A2, setzt das benutzerdefinierte Format für A1 und das Zahlenformat für A2 und gibt dann die Werttypen aus.

```c++
#include <iostream>
#include <ctime>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell a1 = cells.Get(u"A1");
    time_t now = time(nullptr);
    double oaDate1 = static_cast<double>(now) / (60 * 60 * 24) + 25569.0;
    a1.PutValue(oaDate1);

    if (a1.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A1 is Numeric Value: " << a1.IsNumericValue() << std::endl;
    }

    Style a1Style = a1.GetStyle();
    a1Style.SetCustom(u"mm-dd-yy hh:mm:ss", true);
    a1.SetStyle(a1Style);

    if (a1.GetType() == CellValueType::IsDateTime)
    {
        std::cout << "Cell A1 contains a DateTime value." << std::endl;
    }
    else
    {
        std::cout << "Cell A1 does not contain a DateTime value." << std::endl;
    }

    Cell a2 = cells.Get(u"A2");
    now = time(nullptr);
    double oaDate2 = static_cast<double>(now) / (60 * 60 * 24) + 25569.0;
    a2.SetValue(oaDate2);

    if (a2.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A2 is Numeric Value: " << a2.IsNumericValue() << std::endl;
    }

    Style a2Style = a2.GetStyle();
    a2Style.SetNumber(22);
    a2.SetStyle(a2Style);

    if (a2.GetType() == CellValueType::IsDateTime)
    {
        std::cout << "Cell A2 contains a DateTime value." << std::endl;
    }
    else
    {
        std::cout << "Cell A2 does not contain a DateTime value." << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

Ausgabenergebnis:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
```

## **So erhalten Sie den DateTime-Wert in Aspose.Cells**
Dieses Beispiel setzt einen `DateTime`-Wert in die Zellen A1 und A2, setzt das benutzerdefinierte Format für A1 und das Zahlenformat für A2, prüft die Werttypen beider Zellen und gibt anschließend den `DateTime`-Wert sowie die formatierte Zeichenkette aus.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell a1 = cells.Get(u"A1");
    a1.PutValue(Date{2023, 5, 15});

    if (a1.GetType() == CellValueType::IsNumeric) {
        std::cout << "A1 is Numeric Value: " << a1.IsNumericValue() << std::endl;
    }

    Style a1Style = a1.GetStyle();
    a1Style.SetCustom(u"mm-dd-yy hh:mm:ss", true);
    a1.SetStyle(a1Style);

    if (a1.GetType() == CellValueType::IsDateTime) {
        std::cout << "Cell A1 contains a DateTime value." << std::endl;
        Date dateTimeValue = a1.GetDateTimeValue();
        std::cout << "A1 DateTime String Value: " << a1.GetStringValue().ToUtf8() << std::endl;
    }
    else {
        std::cout << "Cell A1 does not contain a DateTime value." << std::endl;
    }

    Cell a2 = cells.Get(u"A2");
    a2.PutValue(Date{2023, 5, 16});

    if (a2.GetType() == CellValueType::IsNumeric) {
        std::cout << "A2 is Numeric Value: " << a2.IsNumericValue() << std::endl;
    }

    Style a2Style = a2.GetStyle();
    a2Style.SetNumber(22);
    a2.SetStyle(a2Style);

    if (a2.GetType() == CellValueType::IsDateTime) {
        std::cout << "Cell A2 contains a DateTime value." << std::endl;
        Date dateTimeValue = a2.GetDateTimeValue();
        std::cout << "A2 DateTime String Value: " << a2.GetStringValue().ToUtf8() << std::endl;
    }
    else {
        std::cout << "Cell A2 does not contain a DateTime value." << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

Ausgabenergebnis:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A1 DateTime Value: 11/23/2023 5:59:09 PM
A1 DateTime String Value: 11-23-23 17:59:09
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
A2 DateTime Value: 11/23/2023 5:59:09 PM
A2 DateTime String Value: 11/23/2023 17:59
```
{{< app/cells/assistant language="cpp" >}}
