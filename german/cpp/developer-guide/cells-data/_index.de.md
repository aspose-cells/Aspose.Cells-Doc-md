---
title: Verwalten von Daten in Excel Dateien mit C++
linktitle: Zellendaten
type: docs
weight: 110
url: /de/cpp/view-and-edit-excel-data/
description: Dieser Artikel beschreibt, wie man mit der Aspose.Cells Bibliothek in C++ Daten von Excel Dateien anzeigt und bearbeitet.
keywords: Aspose.Cells C++ Daten in Excel Dateien verwalten, Daten zu Excel hinzufügen, Daten aus Excel auslesen, Effizienz beim Hinzufügen von Daten verbessern, Zellen verwalten, Zellen aktualisieren, Zellen Daten abrufen, Zellen Daten einfügen
---

{{% alert color="primary" %}}

In [Zugriff auf Zellen eines Arbeitsblatts](/cells/de/cpp/accessing-cells-of-a-worksheet/) haben wir grundlegende Ansätze zum Zugriff auf Zellen in einem Arbeitsblatt besprochen. In diesem Artikel wird einer dieser Ansätze verwendet, um verschiedene Arten von Daten zu Zellen hinzuzufügen.

{{% /alert %}}

## **Wie man Daten zu Zellen hinzufügt**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), die eine Microsoft Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Klasse enthält eine [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-Sammlung, die Zugriff auf jede Arbeitsmappe in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-Klasse repräsentiert. Die [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-Klasse bietet eine [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung. Jedes Element in der [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung stellt ein Objekt der [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)-Klasse dar.

Mit Aspose.Cells können Entwickler Daten in Zellen von Arbeitsmappen hinzufügen, indem sie die [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)-Methode der [**PutValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)-Klasse aufrufen. Aspose.Cells bietet überladene Versionen der [**PutValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)-Methode, mit denen Entwickler verschiedene Arten von Daten zu Zellen hinzufügen können. Unter Verwendung dieser überladenen Versionen der [**PutValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)-Methode ist es möglich, Boolesche, Zeichenfolgen, Dezimalzahlen, Ganzzahlen oder Datum/Zeit usw. Werte der Zelle hinzuzufügen.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;

    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);


    worksheet.GetCells().Get(U16String(u"A1")).PutValue(U16String(u"Hello World"));
    worksheet.GetCells().Get(U16String(u"A2")).PutValue(20.5);
    worksheet.GetCells().Get(U16String(u"A3")).PutValue((int32_t)15);
    worksheet.GetCells().Get(U16String(u"A4")).PutValue(true);

    Cell cellA1 = worksheet.GetCells().Get(U16String(u"A4"));
    Style style = cellA1.GetStyle();
    style.SetNumber(15);
    cellA1.SetStyle(style);

    workbook.Save(outDir + u"output.out.xls");

    std::cout << "Data inserted and workbook saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Wie man die Effizienz verbessert**

Wenn Sie die Methode [**PutValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) verwenden, um eine große Menge an Daten in ein Arbeitsblatt einzufügen, sollten Sie zuerst Werte in die Zellen nach Zeilen und dann nach Spalten einfügen. Dieser Ansatz verbessert die Effizienz Ihrer Anwendungen erheblich.

## **Wie man Daten von Zellen abruft**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), die eine Microsoft Excel-Datei darstellt. Die [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)-Klasse enthält eine [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-Sammlung, die den Zugriff auf Arbeitsblätter in der Datei ermöglicht. Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-Klasse dargestellt. Die [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-Klasse bietet eine [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung. Jedes Element in der [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung stellt ein Objekt der [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)-Klasse dar.

Die Klasse [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) bietet mehrere Eigenschaften, die es Entwicklern ermöglichen, Werte aus den Zellen gemäß ihren Datentypen abzurufen. Diese Eigenschaften umfassen:

- [**StringValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/): gibt den String-Wert der Zelle zurück.
- [**DoubleValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/): gibt den Double-Wert der Zelle zurück.
- [**BoolValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getboolvalue/): gibt den Boolean-Wert der Zelle zurück.
- [**DateTimeValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdatetimevalue/): gibt den Datum/Uhrzeit-Wert der Zelle zurück.
- [**FloatValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/): gibt den Float-Wert der Zelle zurück.
- [**IntValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getintvalue/): gibt den Integer-Wert der Zelle zurück.

Wenn ein Feld nicht ausgefüllt ist, wirft die Zelle mit [**DoubleValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/) oder [**FloatValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/) eine Ausnahme.

Der Typ der in einer Zelle enthaltenen Daten kann auch über die Eigenschaft [**Type**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) der Klasse [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) überprüft werden. Tatsächlich basiert die Eigenschaft [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) der Klasse [**Type**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) auf der Enumeration [**CellValueType**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvaluetype/), deren vordefinierte Werte unten aufgeführt sind:

|**Zellwerttypen**|**Beschreibung**|
| :- | :- |
|IsBool| Gibt an, dass der Zellenwert Boolean ist.|
|IsDateTime| Gibt an, dass der Zellenwert Datum/Uhrzeit ist.|
|IsNull| Stellt eine leere Zelle dar.|
|IsNumeric| Gibt an, dass der Zellenwert numerisch ist.|
|IsString| Gibt an, dass der Zellenwert eine Zeichenfolge ist.|
|IsUnknown| Gibt an, dass der Zellenwert unbekannt ist.|

Sie können auch die oben vordefinierten Zellwerttypen verwenden, um sie mit dem Datentyp in jeder Zelle zu vergleichen.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = srcDir + u"book1.xls";

    Workbook workbook(inputFilePath);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    int maxRow = worksheet.GetCells().GetMaxDataRow();
    int maxCol = worksheet.GetCells().GetMaxDataColumn();

    for (int row = 0; row <= maxRow; row++)
    {
        for (int col = 0; col <= maxCol; col++)
        {
            Cell cell = worksheet.GetCells().Get(row, col);

            U16String stringValue;
            double doubleValue = 0.0;
            bool boolValue = false;

            switch (cell.GetType())
            {
                case CellValueType::IsString:
                    stringValue = cell.GetStringValue();
                    std::cout << "String Value: " << stringValue.ToUtf8() << std::endl;
                    break;

                case CellValueType::IsNumeric:
                    doubleValue = cell.GetDoubleValue();
                    std::cout << "Double Value: " << doubleValue << std::endl;
                    break;

                case CellValueType::IsBool:
                    boolValue = cell.GetBoolValue();
                    std::cout << "Bool Value: " << boolValue << std::endl;
                    break;

                case CellValueType::IsDateTime:
                    stringValue = cell.GetStringValue();
                    std::cout << "DateTime Value: " << stringValue.ToUtf8() << std::endl;
                    break;

                case CellValueType::IsUnknown:
                    stringValue = cell.GetStringValue();
                    std::cout << "Unknown Value: " << stringValue.ToUtf8() << std::endl;
                    break;

                case CellValueType::IsNull:
                    break;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Beim Arbeiten mit Arbeitsblättern können Benutzer verschiedene Arten von Daten in den Zellen hinzufügen. Diese Datentypen können Boolesche, Ganzzahlen, Gleitkommazahlen, Text- oder Datum-/Uhrzeitwerte umfassen. Mit Aspose.Cells können Sie die entsprechenden Werte basierend auf ihren Datentypen aus den Zellen abrufen.

{{% /alert %}}

## **Erweiterte Themen**
- [Zellen eines Arbeitsblatts zugreifen](/cells/de/cpp/accessing-cells-of-a-worksheet/)
- [Text numerische Daten in Nummer konvertieren](/cells/de/cpp/convert-text-numeric-data-to-number/)
- [Teilergebnisse erstellen](/cells/de/cpp/creating-subtotals/)
- [Daten filtern](/cells/de/cpp/data-filtering/)
- [Daten sortieren](/cells/de/cpp/sort-data-of-excel/)
- [Datenüberprüfung](/cells/de/cpp/data-validation/)
- [Daten suchen oder suchen](/cells/de/cpp/find-or-search-data/)
- [Zellzeichenfolgenwert mit und ohne Formatierung abrufen](/cells/de/cpp/get-cell-string-value-with-and-without-formatting/)
- [Hinzufügen von HTML-Rich-Text in die Zelle](/cells/de/cpp/adding-html-rich-text-inside-the-cell/)
- [Hyperlinks in Excel oder OpenOffice einfügen](/cells/de/cpp/insert-hyperlinks-to-excel/)
- [Verwendung und Platzierung von Enumeratoren](/cells/de/cpp/how-and-where-to-use-enumerators/)
- [Breite und Höhe des Zellenwerts in Pixeln messen](/cells/de/cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Lesen von Zellenwerten in mehreren Threads gleichzeitig](/cells/de/cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [Umwandlung zwischen Zellnamen und Zeilen-/Spaltenindex](/cells/de/cpp/names-and-indices/)
- [Daten erst nach Zeile und dann nach Spalte ausfüllen](/cells/de/cpp/populate-data-first-by-row-then-by-column/)
- [Einzelnes Anführungszeichen-Prefix des Zellenwerts oder -bereichs beibehalten](/cells/de/cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Teile des Rich-Texts der Zelle zugreifen und aktualisieren](/cells/de/cpp/access-and-update-the-portions-of-rich-text-of-cell/)
